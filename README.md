## Graducation Tracker

This is a stupid project, You may ask why because people ask me a lot how many semesters do you have to complete my graduation or my friends ask "Ay, How many credits did you complete?", I ended up like "I don't know `¯\_(ツ)_/¯`" because I don't track my records and can't remember at the time.

So, this stupid idea pops up in my mind, It's a pretty simple application if you can request features or can create an Issue](https://github.com/rudSarkar/graducation_tracker/issues)/[Pull Request](https://github.com/rudSarkar/graducation_tracker/pulls)Request to improve it.

Long story short this only works for [Green Univeristy of Bangladesh](https://green.edu.bd/).

#### How to use in your local machine

```bash
$ python3 -m pip install virtualenv

$ virtualenv venv

$ pip install -r requirements.txt

$ python3 app.py
```

Make sure you have [Chrome](https://chromedriver.chromium.org/downloads) is installed in your system wheather it's Mac/Linux/Win and set the Environment variable so the `chromedriver` binary easily accessible from the system.

#### If you have Docker

```
$ chmod +x build.sh
$ sudo ./build.sh
```

It will expose to [http://localhost:8000/](http://localhost:8000/)