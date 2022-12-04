# Student Storage App

This is group 20's python project. This project is a Python GUI application created with Tkinter. The major use of this application is to store and analyse student scores.

# Requirements

To run this application successfully, you need to make sure you are running python version 3. To check for your python version, run the following command:
```bash
python --version
```

If you get something like `Python 3.x.x` on as your output, then you are on the right track. If you get something like `Python 2.x.x`, you may need to run the following instead:
```bash
python3 --version
```

After running the command above, if you get `Python 3.x.x`, then there's no worry. It means you need to use `python3` instead of `python` to access python version 3. Example:
```bash
python3 StudentRecords.py

# instead of 
python StudentRecords.py
```

If you get an error running `python` or `python3`, or you don't get `Python 3.x.x` from either of them, then you need to install python on your system.

# Getting started

To get this application running the first thing you need to do is install `tkinter` on your system. Tkinter is a libary for building graphical user interfaces in 3. If you don't have it installed in your system, run the following command to install it:
```bash
pip install tk
```

When everything is set up, run the following command to start the application:
```bash
python StudentRecords.py
```

# How to compile

Compiling is the process of converting a high-level program (like this project) into machine code (an executable application). Once you compile, the project you'll be able to distrubute the application without the need for the users to have python installed in their system.

To compile this application, you need to first install `pyinstaller`:
```bash
pip install -U pyinstaller
```

Then, run this command to compile the project:
```bash
pyinstaller StudentRecords.py
```

Once you run the command above, `pyinstaller` creates a directory called *dist*. Inside the *dist* folder, there'll be a *main* project folder.
