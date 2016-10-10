"""
Python 3.4
Gianluca Truda
trdgia001@myuct.ac.za
October 2016
"""

import requests
from flask import Flask
import matplotlib.pyplot as plt


def survivors_by_sex(x):
    """
    Takes in a list of Passenger objects,
    generates a bar chart of survival rates,
    and returns the .png file name.
    """
    fname = 'static/01_survivorsBySex.png'
    surv = []
    em = []
    for p in x:
        em.append(p.sex)
        if p.survived == '1':
            surv.append(p.sex)
    menSurv = surv.count("male")
    womenSurv = surv.count("female")
    menEm = em.count("male")
    womenEm = em.count("female")

    # Formatting the graphic styles and layout
    plt.clf()
    plt.bar(0, menEm, label="Men Embarked", color='blue', alpha=0.3)
    plt.bar(1, womenEm, label="Women Embarked", color='red', alpha=0.3)
    plt.bar(0, menSurv, label="Men Survived", color='blue', alpha=0.9)
    plt.bar(1, womenSurv, label="Women Survived", color='red', alpha=0.9)
    plt.xticks([0.0, 0.5, 1.0, 1.5, 2.0], ["", "Male", "", "Female", ""])
    plt.gca().xaxis.grid(False)
    plt.xlabel('Sex')
    plt.ylabel('Number of People')
    plt.title(r'Bar chart of Survivorship by Sex')
    fig1 = plt.gcf()

    # Saving the image as .png file
    fig1.savefig(fname)
    return fname


def survivors_by_class(x):
    """
    Takes in a list of Passenger objects,
    generates a bar chart of survival rates,
    and returns the .png file name.
    """
    fname = 'static/02_survivorsByClass.png'
    surv = []
    em = []
    for p in x:
        em.append(p.passengerClass)
        if p.survived == '1':
            surv.append(p.passengerClass)
    firstSurv = surv.count("1")
    secondSurv = surv.count("2")
    thirdSurv = surv.count("3")
    firstEm = em.count("1")
    secondEm = em.count("2")
    thirdEm = em.count("3")

    # Formatting the graphic styles and layout
    plt.clf()
    plt.bar(0, firstEm, label="Embarked", color='red', alpha=0.4)
    plt.bar(0, firstSurv, label="Survived", color='blue')
    plt.bar(1, secondEm, label="Embarked", color='red', alpha=0.4)
    plt.bar(1, secondSurv, label="Survived", color='blue')
    plt.bar(2, thirdEm, label="Embarked", color='red', alpha=0.4)
    plt.bar(2, thirdSurv, label="Survived", color='blue')
    plt.xticks([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0], ["", "First", "", "Second", "", "Third", ""])
    plt.gca().xaxis.grid(False)
    plt.xlabel('Class')
    plt.ylabel('Number of People')
    plt.title(r'Bar chart of Survivorship by Class')
    fig2 = plt.gcf()

    # Saving the image as .png file
    fig2.savefig(fname)
    return fname


def survivors_by_age(x):
    """
    Takes in a list of Passenger objects,
    generates a histogram of survival rates,
    and returns the .png file name.
    """
    fname = 'static/03_survivorsByAge.png'
    survAges = []
    ages = []
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for p in x:
        if p.age != '':
            ages.append(float(p.age))
            if p.survived == "1":
                survAges.append(float(p.age))

    # Formatting the graphic styles and layout
    plt.clf()
    plt.hist(ages, bins, histtype='bar', rwidth=0.8, alpha=0.4, facecolor='red', label="Embarked")
    plt.hist(survAges, bins, histtype='bar', rwidth=0.8, alpha=1, facecolor='blue', label="Survived")
    plt.legend(loc='best', numpoints=2, fancybox=True)
    plt.xlabel('Age Groups')
    plt.ylabel('Number of People')
    plt.title(r'Histogram of Survivorship by Age')
    fig3 = plt.gcf()

    # Saving the image as .png file
    fig3.savefig(fname)
    return fname


def configure(addr):
    """
    Takes in a URL as a string and does a request for json data
    at the address.
    Uses the data to generate an array of passenger objects and returns this array.
    """
    # Importing the json data from the web using requests library.
    print("\nPlease be patient whilst retrieving data...")
    r = requests.get(addr)
    data = r.json()
    print("Data retrieved successfully.\n")

    # Populating the objects with the json data
    passengers = []
    for p in data:
        passengers.append(Passenger(p['passenger_id'], p['survived'], p['class'], p['age'], p['sex'], p['name'],
                                p['number_of_siblings_and_spouses_aboard'], p['number_of_parents_and_children_aboard'],
                                p['Embarked']))

    return passengers


class Passenger:
    """
    A class that describes passengers on the Titanic
    and their attributes.
    """
    def __init__(self, pid, surv, cls, age, sex, name, sibsSpouses, parentsChilds, embarked):
        """
        Simple constructor.
        """
        self.pid = pid
        self.survived = surv
        self.passengerClass = cls
        self.age = age
        self.sex = sex
        self.name = name
        self.siblingsOrSpouses = sibsSpouses
        self.parentsOrChildren = parentsChilds
        self.embarked = embarked

    def display_details(self):
        """
        A function to give some output details for the purpose of debugging.
        Essentially a ToString.
        """
        print(self.survived + "\t" + self.sex + "\t" + self.passengerClass + "\t" + self.age + "\t" + self.name)


# Starting flask web-server and serving relevant content.
app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def respond():
    return app.send_static_file('landing.html')

@app.route('/visual')
def visual():
    passengers = configure("https://titanic.businessoptics.biz/survival")
    # Calling functions to generate graphics
    survivors_by_sex(passengers)
    survivors_by_class(passengers)
    survivors_by_age(passengers)

    # Giving the browser a static page populated with the newly generated images.
    return app.send_static_file('vis.html')

# The main body of the script

# Configuring the output graphic parameters
plt.clf()
plt.style.use('fivethirtyeight')
plt.rcParams['axes.facecolor']="#2a2f4a"
plt.rcParams['savefig.facecolor']="#2a2f4a"
plt.rcParams['lines.color']="#ffffff"
plt.rcParams['text.color']="#ffffff"
plt.rcParams['axes.labelcolor']="#ffffff"
plt.rcParams['xtick.color']="#ffffff"
plt.rcParams['ytick.color']="#ffffff"
width = 16
height = 10
fig = plt.figure(figsize=(width, height), dpi=500)

if __name__ == "__main__":
    app.run('localhost', '8080')










