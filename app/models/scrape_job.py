from flask_sqlalchemy import SQLAlchemy
from setup import db
from flask import current_app

from models.job_attr import JobStatus, JobType
from models.scrape_file import ScrapeFile, FILE_DIR
from lib.parsers.html_parser import HTMLParser
from lib.parsers.pdf_parser import PdfParser
import pathlib
import uuid
import os
from tempfile import NamedTemporaryFile
import sys
from zipfile import ZipFile
import traceback


class ScrapeJob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), unique=False)
    jobType = db.Column(db.String(20), unique=False)
    jobInput = db.Column(db.String(300), unique=False)
    fileId = db.Column(db.String(64), db.ForeignKey(
        'scrape_file.id'), unique=False)
    extra = db.Column(db.Text)
    file = db.relationship("ScrapeFile")
    inputFile = db.relationship("ScrapeFile")

    def __init__(self, jobType, jobInput, extra=None):
        """Constructor of ScrapeJob.

        Args:
            jobType: a value of JobType.
            jobInput: url for HTML/API job, ScrapeFile id for PDF/FORM job.
            extra: JSON string. Extra information about the job.

        """

        self.status = JobStatus.PENDING
        self.jobType = jobType
        self.jobInput = jobInput
        self.extra = extra

    def run(self):
        self.status = JobStatus.RUNNING
        db.session.add(self)
        db.session.commit()

        try:
            print(self.jobType)
            parser = None
            if self.jobType == JobType.HTML:
                parser = HTMLParser(self.jobInput)
            elif self.jobType == JobType.PDF:
                parser = self.__get_pdf_parser()

            outputs = parser.parse()

            if len(outputs) > 0:
                zip_name = uuid.uuid1().hex.upper()[:10] + '.zip'
                root_path = pathlib.Path(__file__).resolve().parents[1]
                filepath = os.path.join(root_path, FILE_DIR, zip_name)

                z = ZipFile(filepath, 'w')
                # keep a list of temp files and call close to delete them after zip
                temp_file_list = []

                # create temp CSVs and zip up
                for csv_content in outputs:
                    temp_file = NamedTemporaryFile(delete=True)
                    temp_file.write(bytes(csv_content, 'utf-8'))
                    temp_file.flush()
                    temp_file_list.append(temp_file)
                    z.write(temp_file.name, os.path.basename(temp_file.name + '.csv'))

                # close stream + delete temp CSVs (delete=True)
                for t in temp_file_list:
                    t.close()

                z.close()

                f = open(filepath, "rb")
                self.file = ScrapeFile(f)

            self.status = JobStatus.FINISHED

            db.session.add(self)
            db.session.commit()

            # TODO: logic not correct
        except Exception as e:
            traceback.print_exc()
            if hasattr(e, 'message'):
                current_app.logger.error(
                    "Parsing error [%]: %" % (self.id, e.message))
            else:
                current_app.logger.error(
                    "Parsing error [%]: %" % (self.id, e))

            self.status = JobStatus.FAILED

            db.session.add(self)
            db.session.commit()

    def __get_pdf_parser(self):
        root_path = pathlib.Path(
            __file__).resolve().parents[1]
        input_file_obj = ScrapeFile.query.filter_by(
            id=self.jobInput).first()

        print(input_file_obj)
        print(self.jobInput)
        local_file_path = str(root_path) + input_file_obj.path

        return PdfParser(local_file_path)
