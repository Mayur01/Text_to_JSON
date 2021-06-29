import unittest
import textJson as funCode

class testfile(unittest.TestCase):
    def test_texttojson(self):
        NotExpectedlist = []
        expectedlist = [{'eventTime': '2000-01-01T17:25:49Z', 'email': 'dedric_strosin@adams.co.uk', 'sessionid': 'dfad33e7-f734-4f70-af29-c42f2b467142'}, {'eventTime': '2000-01-01T23:59:04Z', 'email': 'abner@bartolettihills.com', 'sessionid': 'b3daf720-6112-4a49-9895-62dda13a2932'}, {'eventTime': '2000-01-02T20:59:05Z', 'email': 'janis_nienow@johnson.name', 'sessionid': '1f90471c-adc3-4daa-9a6d-ff9d184b7a61'}]
        self.assertEqual(funCode.textToJson(filename="sampletest.txt", fromdate="2000-01-01T17:25:49Z", todate="2000-01-02T20:59:05Z"), expectedlist)
        self.assertNotEqual(funCode.textToJson(filename="sampletest.txt", fromdate="2000-01-01T17:25:49Z", todate="2000-02-02T20:59:05Z"), NotExpectedlist)

    def test_checkdateformat(self):
        self.assertEqual(funCode.checkDateFormat(dateformat="2000-01-12T02:04:09Z"),True)    #Date format is correct, It should written True
        self.assertEqual(funCode.checkDateFormat(dateformat="2000-01-12T02:04"),False)       #Date format is Incorrect, It should written False

    def test_tojsonformat(self):
        ExpectedInput1=['2000-01-01T17:25:49Z', 'dedric_strosin@adams.co.uk', 'dfad33e7-f734-4f70-af29-c42f2b467142']
        Expectedjson = {'eventTime': '2000-01-01T17:25:49Z', 'email': 'dedric_strosin@adams.co.uk', 'sessionid': 'dfad33e7-f734-4f70-af29-c42f2b467142'}
        self.assertDictEqual(funCode.toJsonFormat(currentRecord=ExpectedInput1),Expectedjson)
        self.assertNotEqual(funCode.toJsonFormat(currentRecord=['2000-01-01T17', 'dedric_strosin@adams.co.uk', 'dfad33e7-f734-4f70-af29-c42f2b467142']),Expectedjson)


if __name__ == '__main__':
    unittest.main()