from flask import Flask, request
import pandas as pd
import json

import local_setting as config

# csv file path
csv_file = config.csv_file["file_path"]

# saving csf file data into dataframe
df = pd.read_csv(csv_file)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!!"


# getting books records as enetered number of books
@app.route("/get_books/<numbers>")
def read_csv(numbers):
    try:

        # selecting records from data frame
        result = df.head(int(numbers))

        # converting data dataframe rows into json object
        result = result.to_json(orient="records")

        # loading json object into dict as per required format of result
        final_result = {"books": json.loads(result)}

        return final_result
    except Exception as e:
        print(e)
        return "Got some exception please check input passed with following error\n{}".format(e)


# for getting filtered records as per column value
@app.route("/filter_rows", methods=['POST'])
def filter_rows():
    try:
        # getting input column and its value as json format
        request_data = request.get_json()

        # getting column name which have to filter
        column_name = list(request_data.keys())[0]

        # getting value of to be passed for filtered column
        value = request_data[str(column_name)]

        # list of columns present in dataframe
        col_list = df.columns.to_list()

        # if entered column is existing in list of columns
        if column_name in col_list:
            # if column exists
            # getting filtered records
            df_row = df[df[column_name] == value]
            result = df_row.to_json(orient="records")
            final_result = {"books": json.loads(result)}

            # if filtered record is empty
            if final_result["books"] == []:
                return "No Records found for given column data\n{}".format(final_result)

            # returning filtered records
            return final_result

        # if a column is not present then a graceful error message will return.
        else:
            return "Entered Column name:{} \nDoesnt exist in CSV file".format(column_name)

    except Exception as e:
        print(e)
        return "Got some exception please check input passed with following error\n{}".format(e)


if __name__ == "__main__":
    app.run(debug=True)
