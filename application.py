#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : application.py
# Author            : Yu Hsien Chiang <samy9ch@gmail.com>
# Date              : 17.09.19 Tue 15:47:47
# Last Modified Date: 17.09.19 Tue 15:48:23
# Last Modified By  : Yu Hsien Chiang <samy9ch@gmail.com>
#
from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def start():
    session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
    session["state"] = "X"
    session["winner"] = None
    
    return redirect(url_for("game"))

@app.route("/game")
def game():
    return render_template("game.html", game = session["board"], turn = session["state"], winner=session["winner"])



@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    
    if ("board" not in session or "state" not in session or "winner" not in session):
        return redirect(url_for("index"))
    
    session["board"][row][col] = session["state"]

    if (isOver(session["board"]) or isTie(session["board"])):
        if (isTie(session["board"])):
            session["winner"] = "Tie"
        else:
            session["winner"] = session["state"]
    else:
        if (session["state"] == "X"):
            session["state"] = "O"
        else:
            session["state"] = "X"
    return redirect(url_for("game"))

@app.route("/reset")
def reset():
    if ("board" in session):
        session.pop("board")
    return redirect(url_for("index"))


def isOver(board):
    # Row win
    for row in board:
        if row[0] is not None and (row[0] == row[1] == row[2]):
            return True

    # Col win
    for col in range(3):
        if board[0][col] is not None and (board[0][col] == board[1][col] == board[2][col]):
            return True

    # Cross win
    if (board[0][0] is not None and (board[0][0] == board[1][1] == board[2][2])):
        return True

    if (board[0][2] is not None and (board[0][2] == board[1][1] == board[2][0])):
        return True

    return False

def isTie(board):
    if (None not in board[0] and None not in board[1] and None not in board[2]) and (not isOver(board)):
        return True
    else:
        return False
