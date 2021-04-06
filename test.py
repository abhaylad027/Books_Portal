import unittest
from Portal import app
import json


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, True)

    # check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    # check for status code 200 with valid innut data with rest call which int
    # for example given value is 3 as numbers in rest call
    def test_valid_status_code_get_books(self):
        tester = app.test_client(self)
        response = tester.get("/get_books/3")
        print(response.data)
        print(str(response.data))
        statuscode = response.status_code
        self.assertEqual(statuscode,2000)

        self.assertEqual(response.content_type, "application/json")

    # # check for content with valid input data with rest call which int
    # # for example given value is 3 as numbers in rest call
    # def test_valid_op_content_get_books(self):
    #     tester = app.test_client(self)
    #     response = tester.get("/get_books/3")
    #     self.assertEqual(response.content_type, "application/json")

    def test_valid_op_content_filer_rows(self):
        tester = app.test_client(self)
        filter_json_data = json.dumps({"author": "Bayo Ogunjimi"})
        response = tester.post('/filter_rows', headers={"Content-Type": "application/json"}, data=filter_json_data)
        print(response)
        print(response.data, "\n", response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")



if __name__ == '__main__':
    unittest.main()
