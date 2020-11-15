import re
import pandas as pd
import pdfplumber

class FormParser:
    def __init__(self, path):
        self.path = path

    def parse(self):
        """Parse the file at given path and returns the generated csv file path

        Returns:
            a list of strings. Each string is the output of CSV file content
        """
        pdf = pdfplumber.open(self.path)

        # Extract complete text in the form
        all_page =''
        for page in pdf.pages:
          all_page += page.extract_text()

        # define all the fields
        fields = {"CDC 2019-nCoV ID" : "CDC 2019-nCoV ID:(.*) \n",
          'Patient first name' : 'Patient first name(.*) P',
          "Patient last name": "Patient last name(.*) Date",
          'Patient Date of birth':'Date of birth \(MM/DD/YYYY\):(.*)',
          'Reporting Jurisdiction': 'Reporting Jurisdiction(.*)Case',
          'Case state or local ID' : 'Case state/local ID(.*) \n',
          'Reporting Health Department' : 'Reporting Health Department  (.*) CDC 2019-nCoV ID',
          'Contact ID' : 'Contact IDa(.*)NNDSS',
          'NNDSS loc. rec. ID or Case ID' : 'NNDSS loc. rec. ID/Case IDb(.*)',
          'Interviewer Last Name': 'Name of Interviewer: Last:(.*) First',
          'Interviewer First Name': 'Name of Interviewer: Last:.* First:(.*)Telephone:',
          'Interviewer Telephone': 'Name of Interviewer: Last:.*Telephone:(.*) Email:',
          'Interviewer Email': 'Name of Interviewer: Last:.*Email:(.*)\n',
          'Interviewer Affiliation/Organization' : 'Affiliation/Organization:(.*)\n',
          'Case Status' : '',
          'Reason of Probable Status' : '',
          'Process of Case Identification':'Other, specify:(.*) Meets clinical',
          'DGMQID':'DGMQID:(.*)\n',
          'Report date of case to CDC' : 'Detection of SARS-CoV-2 RNA.*test (.*)',
          'Date of first positive specimen collection' : 'plasma, .*recent infection(.*)Unknown',
          'Hospital admission date' : 'discharge date 1 .*\n(.*) \(MM/DD/YYYY\).*\(MM/DD/YYYY\)',
          'Hospital discharge date' : 'discharge date 1 .*\n.* \(MM/DD/YYYY\)(.*/.*/.*)\D.*/.*/.*\(MM/DD/YYYY\)',
          'ICU discharge date' : 'discharge date 1 .*\n.* \(MM/DD/YYYY\).*\(MM/DD/YYYY\)(.*)',
          'ICU admission date' : 'discharge date 1 .*\n.* \(MM/DD/YYYY\).*/.*/.*(\d+/.*/.*)\(MM/DD/YYYY\)',
          'Translator Language' : 'discharge date 1 .*\n.* \(MM/DD/YYYY\).*/.*/.*\D(.*)\D.*/.*/.*\(MM/DD/YYYY\)',
          'Date of Death' : 'date of death (MM/DD/YYYY):(.*)Unknown',
          'Patient Age' : 'Age:(.*)Age',
          'Patient Age Unit' : 'Age units (yr/mo/day):(.*) Male',
          'Patient State of Residence' : 'State of residence:(.*)County of residence',
          'Patient County of Residence' : 'County of residence(.*)Female',
          'Patient Tribal Affiliation' : 'Tribe name(s):(.*)Enrolled',
          'Symptoms':'',
          'Patient Sex' : '',
          'Patient Ethnicity'  : '',
          'Onsetdate' : '',
          'Patient Healthcare Worker Status': '',
          'Patient Residence at Case' : '',
          'Specimen for Covid Testing' : '[1|2|3]\)(.*)',
          'Chronic Disease' : 'yes, specify:(.*)\n.*Other',
          'Disability':'',
          'Type of Disability': 'Other chronic diseases  If yes, specify:(.*)',
          'Comments or Notes':'Additional Comments or Notes\n \n \n(.*)'
          }

        # create a filled valued dictionary in order to convert it to pd.DataFrame.to_csv
        updated_fields = {}
        for key, val in fields.items():
            item = re.findall(val, first_page)
            if len(item) != 0:
                updated_fields[key] = [item[0].replace('_', '').strip()]
            else:
                updated_fields[key] = ['']
        return [pd.DataFrame.from_dict(updated_fields).to_csv()]
