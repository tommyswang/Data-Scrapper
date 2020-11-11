from flask_sqlalchemy import SQLAlchemy
from db import db
from flask import current_app

from models.job_attr import JobStatus, JobType
from models.scrape_file import ScrapeFile
from lib.parsers.html_parser import HTMLParser
from lib.parsers.pdf_parser import PdfParser
from lib.parsers.api_parser import APIParser
import pathlib
import os
from tempfile import NamedTemporaryFile
import sys
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
            parser = None
            if self.jobType == JobType.HTML:
                parser = HTMLParser(self.jobInput)
            elif self.jobType == JobType.PDF:
                parser = self.__get_pdf_parser()
            elif self.jobType == JobType.API:
                parser = APIParser(self.jobInput, self.extra)

            outputs = parser.parse()

            if len(outputs) > 0:
                # TODO: save first output for now
                csv_content = outputs[0]
                temp_file = NamedTemporaryFile(delete=False)
                temp_file.write(bytes(csv_content, 'utf-8'))
                temp_file.close()

                temp_file = open(temp_file.name, "rb")

                self.file = ScrapeFile(temp_file)

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

        local_file_path = str(root_path) + input_file_obj.path
        return PdfParser(local_file_path)
