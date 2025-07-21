from flask import Flask, render_template
import json

app = Flask(__name__)

def load_json(file_name: str) -> list[dict]:
    route = "data/" + file_name + ".json"

    with open(route) as f:
        return json.load(f)
    

@app.route("/")
def home():
    projects = load_json("projects")

    return render_template("index.html", projects=projects)

if __name__=="__main__":
    app.run(debug=True)