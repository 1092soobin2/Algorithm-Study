from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    # html 스트링
    return "<h1> html test </h1> \
            <p> content </p>"

@app.route("/data")
def user():
    df = pd.DataFrame({"A":[1,4,7], "B":[2,5,8], "C":[3,6,9]})

    # json 형식의 데이터
    return df.to_json()

if __name__ == "__main__":
    app.run(debug=True)