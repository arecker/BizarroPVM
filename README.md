BizarroPVM
==========

This is my project for Geek Day.  It's a thrown-together patient registration web app built in Django.
The HTML / CSS (and basically everything else) is a skin of the built in admin interface called "Grappelli" - that
is the only dependency needed (along with Django, of course).

### Building the Virtualenv

I used PyCharm (http://www.jetbrains.com/pycharm/), the community version to do this.  It's a free IDE.

After python is installed on your machine, go into Setttings --> Python Interpreters and create a virtual interpreter
based on the python.exe you downloaded.  If you go into the advanced settings for the interpreter you just created,
you will find a screen where you can download packages.  Search for and install "Django" and "grappelli".

Once the environment is built, you can open the repo.  Choose the environment you just created.

### Debugging Web Server

Near the top, there should be a "play" button.  Select it, and choose "Edit Configurations".  Add a python configuration,
name it "Django Server", and select the "manage.py" script in the project.  Add the parameter "runserver".

Now, you should be able to "play" this script.

Open a browser to http://localhost:8000/admin .  Log in as admin (password = bronyflow).
