<p>
	<img src="media/pong-logo.png">
</p>

![Python Badge](https://img.shields.io/badge/python-3.9.2-blue?logo=python) ![Pygame Badge](https://img.shields.io/badge/pygame-2.0.1-brightgreen)

## :pencil: ABout the project

Pong is one of the first computer games that ever created, this simple "tennis like" game features two paddles and a ball, the goal is to defeat your opponent by being the first one to gain 10 points, a player gets a point once the opponent misses a ball.

### Built with

- [Pygame](https://www.pygame.org/news)


## :book: Getting started

### Pre requisites

- [Python][python-download] - 3.9 or up


### Installation

#### Pipfile and Pipfile.Lock

Inside the Pipfile there's all the modules name needed for the project. 

1. Download Pipenv through the terminal window (make sure you have [Python][python-download] installed):

	```python
    pip install pipenv
    ```
    
2. After installing pipenv all you have to do is to download the files and in the terminal window, go to the folder with these files and run:

	```python
    pipenv install
    ```
    This will create a virtual environment with the module `pygame`.

3. We must have this virtual environment to run our program, through the terminal window:

	```python
    pipenv shell # To run the virtual environment
    exit        # To close the virtual environment
    ```

If any doubts here's a link to some more explanations: [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html)

## :runner: Run

- Download the project, open terminal window on folder with 'pong.py' and type:

```
python pong.py
```

Enjoy the game :smiley:


[python-download]: https://www.python.org/downloads/
