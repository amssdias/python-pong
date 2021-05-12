# Pong

Pong is one of the first computer games that ever created, this simple "tennis like" game features two paddles and a ball, the goal is to defeat your opponent by being the first one to gain 10 points, a player gets a point once the opponent misses a ball.

## Pre requisites

- [Python](https://www.python.org/downloads/) - 3.8.4 or up

### Pipfile and Pipfile.Lock

Inside the Pipfile there's all the modules name needed for the project.
Download Pipenv through the terminal window (make sure you have Python installed), just type `pip install pipenv`.

After installing pipenv all you have to do is to download the files and in the terminal window, got to the folder with these files and run `pipenv install` and automatically will install this modules.

This will create a virtual environment with the module `pygame`.

To run this virtual environment all you must do is run `pipenv shell` and to close the virtual environment `exit`.

If any doubts here's a link to some more explanations:

- [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html)

## Run

- Download the project, open terminal window on folder with 'pong.py' and type:

```
python pong.py
```