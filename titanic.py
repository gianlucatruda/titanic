# Python 3.4
# Gianluca Truda
# October 2016

import requests
from flask import Flask, render_template, send_from_directory, request
import matplotlib.pyplot as plt


def survivors_by_sex(x):
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
    fig1.savefig(fname)
    return fname


def survivors_by_class(x):
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
    fig2.savefig(fname)
    return fname


def survivors_by_age(x):
    fname = 'static/03_survivorsByAge.png'
    survAges = []
    ages = []
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for p in x:
        if p.age != '':
            ages.append(float(p.age))
            if p.survived == "1":
                survAges.append(float(p.age))

    plt.clf()
    plt.hist(ages, bins, histtype='bar', rwidth=0.8, alpha=0.4, facecolor='red', label="Embarked")
    plt.hist(survAges, bins, histtype='bar', rwidth=0.8, alpha=1, facecolor='blue', label="Survived")
    plt.legend(loc='best', numpoints=2, fancybox=True)
    plt.xlabel('Age Groups')
    plt.ylabel('Number of People')
    plt.title(r'Histogram of Survivorship by Age')

    fig3 = plt.gcf()
    fig3.savefig(fname)

    return fname


def configure(addr):
    # Importing the json data from the web using requests library.
    print("\nPlease be patient whilst retrieving data...")
    r = requests.get(addr)   # "https://titanic.businessoptics.biz/survival"
    data = r.json()
    print("Data retrieved successfully.\n")

    # Populating the objects with the json data
    passengers = []
    for p in data:
        passengers.append(Passenger(p['passenger_id'], p['survived'], p['class'], p['age'], p['sex'], p['name'],
                                    p['number_of_siblings_and_spouses_aboard'], p['number_of_parents_and_children_aboard'],
                                    p['Embarked']))

    # Configuring the output graphic parameters
    plt.clf()
    plt.style.use('fivethirtyeight')
    width = 16
    height = 10
    plt.rcParams['axes.facecolor']="#2a2f4a"
    plt.rcParams['savefig.facecolor']="#2a2f4a"
    plt.rcParams['lines.color']="#ffffff"
    plt.rcParams['text.color']="#ffffff"
    plt.rcParams['axes.labelcolor']="#ffffff"
    plt.rcParams['xtick.color']="#ffffff"
    plt.rcParams['ytick.color']="#ffffff"
    fig = plt.figure(figsize=(width, height), dpi=500)


    return passengers


class Passenger:
    def __init__(self, pid, surv, cls, age, sex, name, sibsSpouses, parentsChilds, embarked):
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
        print(self.survived + "\t" + self.sex + "\t" + self.passengerClass + "\t" + self.age + "\t" + self.name)


# Starting flask web-server.
app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def respond():
    return app.send_static_file('landing.html')

@app.route('/visual')
def visual():
    passengers = configure("https://titanic.businessoptics.biz/survival")
    survivors_by_sex(passengers)
    survivors_by_class(passengers)
    survivors_by_age(passengers)

    return app.send_static_file('vis.html')


if __name__ == "__main__":
    app.run('localhost', '8080')










