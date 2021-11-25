from logging import error
from flask import Flask,render_template,request
import requests

from json import JSONDecodeError

app = Flask(__name__)

base_url = "https://api.github.com/users/"

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        githubname = request.form.get("githubname")
        response = requests.get(base_url + githubname)
        user_info = response.json()

        if "message" in user_info:
            return render_template("index.html",error = "Kullanıcı bulanamadı...")
        else:
            return render_template("index.html", profile = user_info)
    else:
        return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)