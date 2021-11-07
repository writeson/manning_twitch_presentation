# The Well-Grounded Python Developer Twitch Presentation

The code in this repository goes along with the Twitch presentation. Each example expands
on the previous one to illustrate ways to make your Flask web development work
easier and more maintainable.

## Installation

The examples in this repository were built and run against Python 3.9.6. I would recommend
using the [pyenv](https://github.com/pyenv/pyenv) utility to install and manage installing and using that version of Python to avoid conflicting with any system installed Python.

There is a port of pyenv for windows you can find [here](https://github.com/pyenv-win/pyenv-win). However, I haven't tried it, so your mileage may vary.

Once you have pyenv installed, install the 3.9.6 version of Python with this command in a terminal:

```console
pyenv install 3.9.6
```

To create a Python virtual environment in the directory where you've cloned this repo take the following steps once `pyenv` is installed:

1. cd <folder where you've cloned the repo>
1. pyenv local 3.9.6
1. python -m venv .venv
1. source .venv/bin/activate
1. python pip install --upgrade pip
1. pip install -r requirements.txt

These steps will create and activate a Python 3.9.6 virtual environment in the directory where you've cloned the repo. It will also install the necessary modules (Flask) to run the example applications.

To deactivate the Python virtual environment enter the command from the terminal:

```console
deactivate
```

## Running The Examples

To run the example applications you must activate the Python 3.9.6 virtual environment with this command from a terminal in Mac or Linux:

```console
source .venv/bin/activate
```

Then set some environment variables that are used by Flask:

```console
export FLASK_APP=myapp.py
export FLASK_ENV=development
```

To run a particular example application move to the folder in example folder that contains the `myapp.py` file and enter this command from a terminal:

```console
flask run
```

This will start the Flask development server. You can open a browser to `localhost:5000` to navigate to the web application. The `CTRL-C` key combination in the terminal window will exit the Flask server.

# Examples

1. Is similar to most of the "Hello World" Flask examples you might have seen
1. Demonstrates a better starting point from which to grow and expand your Flask applications
   1. The versatility of this starting point will be shown in later examples
1. Shows creating more complex web pages
1. Shows how to use Jinja2 templates and template inheritance to manage complex web pages
1. Makes use of Flask Blueprints to namespace and modularize your web applications features. Also added Blueprint specific styling and JavaScript.
