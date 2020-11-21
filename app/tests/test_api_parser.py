from json import JSONDecodeError

import pytest
from lib.parsers.api_parser import APIParser

from os import path


def test_parser():
    parser = APIParser(
        "http://hapi.fhir.org/baseR4/Patient/1215583", "structured")

    ret = parser.parse()

    assert ret == [',resourceType,id,identifier,name,gender,meta.versionId,meta.lastUpdated,meta.source,text.status,text.div\n0,Patient,1215583,"[{\'type\': {\'coding\': [{\'system\': \'http://terminology.hl7.org/CodeSystem/v2-0203\', \'code\': \'MR\', \'display\': \'Medical Record Number\'}], \'text\': \'Medical Record Number\'}, \'value\': \'CT9132\'}, {\'type\': {\'coding\': [{\'system\': \'http://terminology.hl7.org/CodeSystem/v2-0203\', \'code\': \'NIIP\', \'display\': \'National Insurance Payor Identifier\'}], \'text\': \'National Insurance Payor Identifier\'}, \'value\': \'9800004449\'}]","[{\'family\': \'Joseph\', \'given\': [\'Edmunds\']}]",male,1,2020-06-17T06:17:34.680+00:00,#Rfn12jeDCtleYAun,generated,"<div xmlns=""http://www.w3.org/1999/xhtml""><div class=""hapiHeaderText"">Edmunds <b>JOSEPH </b></div><table class=""hapiPropertyTable""><tbody><tr><td>Identifier</td><td>CT9132</td></tr></tbody></table></div>"\n']

    parser = APIParser(
        "http://hapi.fhir.org/baseR4/Patient/1215583", "flat")

    ret = parser.parse()

    assert ret == [',resourceType,id,meta_versionId,meta_lastUpdated,meta_source,text_status,text_div,identifier_0_type_coding_0_system,identifier_0_type_coding_0_code,identifier_0_type_coding_0_display,identifier_0_type_text,identifier_0_value,identifier_1_type_coding_0_system,identifier_1_type_coding_0_code,identifier_1_type_coding_0_display,identifier_1_type_text,identifier_1_value,name_0_family,name_0_given_0,gender\n0,Patient,1215583,1,2020-06-17T06:17:34.680+00:00,#Rfn12jeDCtleYAun,generated,"<div xmlns=""http://www.w3.org/1999/xhtml""><div class=""hapiHeaderText"">Edmunds <b>JOSEPH </b></div><table class=""hapiPropertyTable""><tbody><tr><td>Identifier</td><td>CT9132</td></tr></tbody></table></div>",http://terminology.hl7.org/CodeSystem/v2-0203,MR,Medical Record Number,Medical Record Number,CT9132,http://terminology.hl7.org/CodeSystem/v2-0203,NIIP,National Insurance Payor Identifier,National Insurance Payor Identifier,9800004449,Joseph,Edmunds,male\n']

    parser = APIParser(
        "http://www.google.com", "flat")

    with pytest.raises(Exception, match="Sorry, url didn't return json") as execinfo:
        ret = parser.parse()
