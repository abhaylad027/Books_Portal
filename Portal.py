from flask import Flask, redirect
from random import random, sample
import pandas as pd
import json

import local_setting as config

#csv file path
csv_file = config.csv_file["file_path"]

# saving csf file data into dataframe
df = pd.read_csv(csv_file)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!!"


@app.route("/get_books/<numbers>")
def read_csv(numbers):
    try:

        # print(numbers,type(numbers))
        # df = pd.read_csv(r"D:\abhay\Interview\ICAV\Books_Portal\data\books.csv",nrows=int(numbers))
        # df = pd.read_csv(csv_file, nrows=int(numbers))

        # Cleaning data as empty into null in csv
        # cleaned_df = df.fillna("null")
        # result = cleaned_df.to_json(orient="records")
        result = df.head(int(numbers))

        result = result.to_json(orient="records")
        # df.to_json('books.json',orient="records",)
        final_result = {"books": json.loads(result)}

        # dj = json.loads(result)
        # print("dj",dj)
        # dc = {"books":dj}
        # print(dc)


        return final_result
    except Exception as e:
        print(e)
        return "Got some exception please check input passed"



if __name__ == "__main__":
    app.run(debug=True)
