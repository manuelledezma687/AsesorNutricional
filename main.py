from flask import Flask, make_response, redirect, render_template
from recipe_book.ideas import RecipeBook

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    Breakfast = RecipeBook.breakfast(self=print)
    Lunch = RecipeBook.lunch(self=print)
    Snack = RecipeBook.snack(self=print)
    Dinner = RecipeBook.dinner(self=print)

    return render_template("index.html", Lunch=Lunch, Snack=Snack,Dinner=Dinner,Breakfast=Breakfast)


@app.route("/calculator", methods=['GET','POST'])
def calculator():
    response = make_response(redirect('/'))
    return response


if __name__ == "__main__":
    app.run(debug=True, port=5000)
