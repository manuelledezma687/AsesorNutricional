from flask import Flask, request, make_response, redirect, render_template
import LunchBuilder
import DinnerBuilder
import BreakfastBuilder
import SnackBuilder

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    Breakfast = BreakfastBuilder.menuGenerator()
    Lunch = LunchBuilder.menuGenerator()
    Snack = SnackBuilder.menuGenerator()
    Dinner = DinnerBuilder.menuGenerator()

    return render_template("index.html", Lunch=Lunch, Snack=Snack,Dinner=Dinner,Breakfast=Breakfast)


@app.route("/calculator", methods=['GET','POST'])
def calculator():
    response = make_response(redirect('/'))
    return response



if __name__ == "__main__":
    app.run(debug=True, port=5000)