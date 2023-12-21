# 🐍 Automated robot for sending CVs 

## 👨‍💻 The project 
A program that automatically logs into the portal once a day, completes the appropriate data and sends job applications.

## 🤔 How it works in practice?
#### Pracuj.pl
https://user-images.githubusercontent.com/82182989/226676476-a32d867b-4b63-435e-a936-220e7ec605e0.mp4

## 💬 Installation instruction 
At the beginning, you must install the software that is mandatory to start the project, it is presented below.
 - [Python 3+ version](https://realpython.com/installing-python/#how-to-install-python-on-windows)
 - [Google Chrome](https://www.google.com/intl/pl_pl/chrome/) 
 - [Chrome driver to Chrome](https://chromedriver.chromium.org/getting-started)
 - [Install Poetry](https://github.com/piotek8/Poetry-windows-instruction)

You need to install the necessary libraries in the terminal in your environment (pycharm is recommended by me):

```bash
  poetry install
```


## 📜 Selenium Python Bindings Documentation

Use this documentations for learning and finding solutions to problems.

- [Selenium with Python Documentation](https://selenium-python.readthedocs.io/)
- [Stack Overflow](https://stackoverflow.com/)



## 🔗 Run Locally

Clone the project

```
git clone git@github.com:piotek8/auto-sender.git
```
Go to the project directory

```
cd auto-sender
```
Install dependencies

```
poetry install
```
Start the app

```
You can use Shift+f10 in Pycharm or run with command in terminal like: python main.py
```

 
## 📁 How to entering data into the program

    Create an .env file in the main folder and enter the necessary data in the login and password (your data to log in to the Pracuj.pl portal)
    There is an example in the .env.example file
