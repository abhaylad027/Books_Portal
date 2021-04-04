from flask import Flask, redirect
import pandas as pd


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!"

@app.route("/all_books")
def read_csv():
    df = pd.read_csv(r"D:\abhay\Interview\ICAV\Books_Portal\data\books.csv")
    print(df.to_string())
    return df.to_string()



if __name__ == "__main__":
    app.run(debug=True,port=6000)
