import random
from flask import Flask, request, render_template
from dices import roll_the_dices


app = Flask(__name__)


def add_points(points):
    dice = request.form["dices"]
    move = roll_the_dices(dice)
    if move == 7:
        points //= 7
    if move == 11:
        points *= 11
    else:
        points += move
    return points


@app.route("/", methods=['GET', 'POST'])
def game_2001():
    if request.method == "GET":
        user_points = 0
        computer_points = 0
        return render_template("2001.html", user_points=user_points, computer_points=computer_points)
    if request.method == "POST":
        dice = request.form["dices"]
        move = roll_the_dices(dice)
        user_points = 0
        computer_points = 0

        user_points += move
        computer_points += move

        while computer_points < 2001 and user_points < 2001:
            roll_the_dices(dice)
            user_points = add_points(user_points)
            computer_points = add_points(computer_points)

        return render_template("2001.html", user_points=user_points, computer_points=computer_points)


if __name__ == "__main__":
    app.run(debug = True, port = 5555)
