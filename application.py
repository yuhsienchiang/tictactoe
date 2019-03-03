#-*- coding:utf-8 -*-
# AUTHOR:   samchiang
# FILE:     application.py
# ROLE:     TODO (some explanation)
# CREATED:  2019-02-27 11:25:03
# MODIFIED: 2019-02-27 20:47:11

from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def check(board, turn):
    return ((board[0][0] == turn and board[0][1] == turn and board[0][2] == turn) or
    (board[1][0] == turn and board[1][1] == turn and board[1][2] == turn) or
    (board[2][0] == turn and board[2][1] == turn and board[2][2] == turn) or
    (board[0][0] == turn and board[1][0] == turn and board[2][0] == turn) or
    (board[0][1] == turn and board[1][1] == turn and board[2][1] == turn) or
    (board[0][2] == turn and board[1][2] == turn and board[2][2] == turn) or
    (board[0][0] == turn and board[1][1] == turn and board[2][2] == turn) or
    (board[0][2] == turn and board[1][1] == turn and board[2][0] == turn))

def is_end(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return (False)
    return (True)

@app.route("/")
def index():

    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"

    return render_template("game.html", game = session["board"], turn = session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["turn"]
    if check(session["board"], session["turn"]):
        return render_template("result.html", game = session["board"], winner = session["turn"])
    elif (not (check(session["board"], session["turn"])) and is_end(session["board"])):
        return render_template("result.html", game = session["board"], winner = "Tie")
    else:
        if session["turn"] == "X":
            session["turn"] = "O"
        else:
            session["turn"] = "X"
        return redirect(url_for("index"))

@app.route("/reset")
def reset():
    del session["board"]
    return redirect(url_for("index"))
