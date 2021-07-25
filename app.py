#!/usr/bin/env python3
import os
import cgi
import json
import requests
import html
from flask import Flask, request, render_template


url_back = os.environ.get('URL_BACK_ENV')


dict_people = {}
dict_planets = {}

def init_data():
    count_person  = 0
    count_planet  = 0
    

    people = requests.get("{}/api/people/".fopmat(url_back))
    for i  in range(len(people.json())):
        dict_people.update({people.json()[i].get('id'): people.json()[i].get('name')})
        count_person  += 1

    planets = requests.get("{}/api/planets/".fopmat(url_back))
    for i  in range(len(planets.json())):
        dict_planets.update({planets.json()[i].get('id'): planets.json()[i].get('name')})
        count_planet += 1
    return([count_person, count_planet])




app = Flask(__name__)
@app.route("/")
def header():
    count_items = []
    count_items = init_data()
    return render_template('index.html', items = dict_planets.items(), piple = dict_people.items(), db_empty = count_items)

@app.route('/all_people')
def all_people():
    characters = []
    people = requests.get("{}/api/people/".fopmat(url_back))
    for i  in range(len(people.json())):
        characters.append([people.json()[i].get('id'),
                           people.json()[i].get('name'),
                           people.json()[i].get('gender'),
                           people.json()[i].get('height'),
                           people.json()[i].get('homeworld')
                          ])
    return render_template('all_people.html', items = dict_planets.items(), piple = dict_people.items(), character = characters)





@app.route('/all_planets')
def all_planets():
    planets = []
    planet = requests.get("{}/api/planets/".fopmat(url_back))
    for i  in range(len(planet.json())):
        planets.append([planet.json()[i].get('id'),
                        planet.json()[i].get('name'),
                        planet.json()[i].get('gravity'),
                        planet.json()[i].get('climate'),
                        planet.json()[i].get('terrain')
                        ])
    return render_template('all_planets.html', items = dict_planets.items(), piple = dict_people.items(), planet_s = planets)


@app.route('/people', methods = ['POST', 'GET'])
def person():
    if request.method == 'POST':
        ids = list(request.form.values())
        id = ids[0]
        print(id)
    #    print(request.form.get(id))
        person = []
        people = requests.get("{}/api/people/{}/".format(url_back, id))
        person.append(people.json().get('name'))
        person.append(people.json().get('gender'))
        person.append(people.json().get('height'))
        person.append(people.json().get('mass'))
        person.append(people.json().get('hair_color'))
        person.append(people.json().get('eye_color'))
        person.append(people.json().get('birth_year'))
        person.append(dict_planets.get(people.json().get('homeworld')))
        return render_template('person.html', items = dict_planets.items(), piple = dict_people.items(), personal = person)

@app.route('/planet', methods = ['POST', 'GET'])
def planet():
    if request.method == 'POST':
        ids = list(request.form.values())
        id = ids[0]
        print(id)
        plan = []
        planet = requests.get("{}/api/planets/{}".format(url_back, id))
        plan.append(planet.json().get('name'))
        plan.append(planet.json().get('gravity'))
        plan.append(planet.json().get('climate'))
        plan.append(planet.json().get('terran'))
        characters = []
        people = requests.get("{}/api/population/{}/".format(url_back, id))
        for i  in range(len(people.json())):
            characters.append([people.json()[i].get('id'),
                           people.json()[i].get('name'),
                           people.json()[i].get('gender'),
                           people.json()[i].get('height'),
                           people.json()[i].get('homeworld')
                          ])
        return render_template('planet.html', items = dict_planets.items(), piple = dict_people.items(), planet = plan, population = characters)




if __name__=="__main__":
    app.debug = True
    app.run(host="0.0.0.0")
