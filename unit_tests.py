import unittest
from Portal import app
import json


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

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

        statuscode = response.status_code
        self.assertEqual(statuscode,200)

        self.assertEqual(response.content_type, "application/json")

    # invalid input with rest call , which is otherthan integer value
    # here used 'star' as input
    def test_invalid_status_code_get_books(self):
        tester = app.test_client(self)
        response = tester.get("/get_books/star")

        statuscode = response.status_code
        self.assertEqual(statuscode,200)
        self.assertEqual(response.data, b"Got  error: invalid literal for int() with base 10: 'star'")
        self.assertEqual(response.content_type,'text/html; charset=utf-8')


    def test_valid_op_content_filer_rows(self):
        tester = app.test_client(self)
        filter_json_data = json.dumps({"author": "Bayo Ogunjimi"})
        response = tester.post('/filter_rows', headers={"Content-Type": "application/json"}, data=filter_json_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")

    # passing value of column name which is not existing in csv file
    # passing jsondata as {"author": "Bayo Ogunjimi11"}
    def test_col_value_not_exists_filer_rows(self):
        tester = app.test_client(self)
        filter_json_data = json.dumps({"author": "Bayo Ogunjimi11"})
        response = tester.post('/filter_rows', headers={"Content-Type": "application/json"}, data=filter_json_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"No Records found for entered column data:\n{'books': []}")
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    # column name for pass json data is not exists in csv file
    # passing 'author1' as column name
    def test_col_not_exists_filer_rows(self):
        tester = app.test_client(self)
        filter_json_data = json.dumps({"author1": "Bayo Ogunjim"})
        response = tester.post('/filter_rows', headers={"Content-Type": "application/json"}, data=filter_json_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Entered Column name: author1 , doesnt exist in CSV file")
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')


if __name__ == '__main__':
    unittest.main()
