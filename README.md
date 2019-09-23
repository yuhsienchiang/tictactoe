# Tic-Tac-Toe Web App Game
This web application is a small project for learning to build a web application.

## Web APP URL
[http://samy9ch.pythonanywhere.com](http://samy9ch.pythonanywhere.com)

## Install
You can play this game at the URL shown above, or install it on your own device.

First, clone this repository to your working directory
```
$ git clone https://github.com/yuhsienchiang/tictactoe.git
```
Set up a virtual environment and activate it.
```
$ python3 -m venv tutorial-env
$ source tutorial-env/bin/activate
```
Next, change your directory to the project repository and install all the dependencies.
```
$ cd tictactoe
$ pip install -r requirements.txt
```

## Usage
Before running this web app, you'll have to activate the virtual environment first.
Then, set the environment variable.
```
export FLASK_APP=application.py
```
Finally, now you can launch the simple builtin server.
```
flask run
```
Head over to http://127.0.0.1:5000/ and enjoy the game!

## Credits
* [CS50 Beyond 2019](https://www.youtube.com/playlist?list=PLhQjrBD2T381Q6R1jRxgXknYO7VuTYPBI)
* [mnajib2018/Python-Flask-Tic-Tac-Toe](https://github.com/mnajib2018/Python-Flask-Tic-Tac-Toe/blob/master/application.py)
