from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
responses = []

@app.get('/')
def get_homepage():
    """Returns the Survey Start Page"""
    return render_template("survey_start.html")

@app.post('/begin')
def start_survey():
    """clears responses, then redirects to question 1"""

    responses.clear()
    print(survey.questions)
    return redirect("/questions/0")

@app.get(f'/questions/<int:count>')
def show_next_question(count):

    return render_template("question.html", question=survey.questions[count])

@app.post("/answer")
def store_answer():
    answer = request.form.get("answer")
    # print(answer, responses, request.args.get("value"), request.args)
    responses.append(answer)
    # print(responses)
    if len(responses) != len(survey.questions):
        return redirect(f"/questions/{len(responses)}")
    else:
        return render_template("completion.html")
