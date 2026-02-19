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
    skills = load_json("skills")
    certificates = load_json("certificates")

    return render_template("index.html", 
                           projects=projects, skills=skills, certificates=certificates)

# project details routes
# project id must match the function names
@app.route("/projects/cinemadd")
def cinemadd():
    return render_template("projects/cinemadd.html")

@app.route("/projects/school-system")
def schoolSystem():
    return render_template("projects/school-system.html")

@app.route("/projects/robot")
def robot():
    return render_template("projects/robot.html")

if __name__=="__main__":
    app.run(debug=False)