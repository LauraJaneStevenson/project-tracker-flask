"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get("github")

    first, last, github = hackbright.get_student_by_github(github)

    return render_template("student-info.html",github=github,first=first,last=last)

@app.route("/add-test")
def show_search_form():

    return render_template("student-add.html")

@app.route("/student-add", methods=['POST'])
def student_add():

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    github = request.form.get("github")

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("confirmation.html",first_name=first_name,
                                               last_name=last_name, 
                                               github=github)

@app.route("/student-search")
def get_student_form():
    
    return render_template("student-search.html")

@app.route("/confirmation")
def redirect_to_info():

    return render_template("student-info.html")


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
