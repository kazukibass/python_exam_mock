from flask import Flask, render_template, request, redirect, url_for, session
import random
from python_mock_exam import python_mock_exam

app = Flask(__name__, template_folder="templates")
app.secret_key = "change_this_to_a_random_secret"

@app.route("/")
def index():
    return render_template("index.html", total=len(python_mock_exam))

@app.route("/start")
def start():
    order = list(python_mock_exam.keys())
    random.shuffle(order)
    session["order"] = order
    session["current"] = 0
    session["score"] = 0
    return redirect(url_for("quiz"))

@app.route("/quiz")
def quiz():
    order = session.get("order")
    current = session.get("current", 0)
    if not order or current >= len(order):
        return redirect(url_for("result"))
    qid = order[current]
    question = python_mock_exam[qid]
    return render_template(
        "question.html",
        question=question,
        qid=qid,
        current=current + 1,
        total=len(order),
    )

@app.route("/answer", methods=["POST"])
def answer():
    order = session.get("order")
    current = session.get("current", 0)
    if not order or current >= len(order):
        return redirect(url_for("index"))

    qid = int(request.form["qid"])
    selected = request.form.get("choice")
    question = python_mock_exam[qid]
    correct = question["choices"][question["answer"] - 1]
    is_correct = selected == correct

    if is_correct:
        session["score"] = session.get("score", 0) + 1

    session["current"] = current + 1
    next_label = "結果を見る" if session["current"] >= len(order) else "次の問題へ"
    next_url = url_for("result") if session["current"] >= len(order) else url_for("quiz")

    return render_template(
        "answer.html",
        selected=selected,
        correct=correct,
        is_correct=is_correct,
        score=session.get("score", 0),
        total=len(order),
        next_label=next_label,
        next_url=next_url,
    )

@app.route("/result")
def result():
    return render_template(
        "result.html",
        score=session.get("score", 0),
        total=len(session.get("order", [])),
    )

@app.route("/help")
def help_page():
    return render_template("help.html")

if __name__ == "__main__":
    app.run(debug=True)
