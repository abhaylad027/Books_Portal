from flask import Flask, redirect
from random import random, sample
import pandas as pd
import json

import local_setting as config

csv_file = config.csv_file["file_path"]


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!!"


@app.route("/get_books/<numbers>")
def read_csv(numbers):
    # print(numbers,type(numbers))
    # df = pd.read_csv(r"D:\abhay\Interview\ICAV\Books_Portal\data\books.csv",nrows=int(numbers))
    df = pd.read_csv(csv_file, nrows=int(numbers))
    # df_book = pd.DataFrame[{'books':[1]}]

    # Cleaning data as empty into null in csv
    # cleaned_df = df.fillna("null")
    # result = cleaned_df.to_json(orient="records")

    result = df.to_json(orient="records")
    # df.to_json('books.json',orient="records",)
    final_result = {"books": json.loads(result)}

    # dj = json.loads(result)
    # print("dj",dj)
    # dc = {"books":dj}
    # print(dc)


    return final_result



if __name__ == "__main__":
    app.run(debug=True)
