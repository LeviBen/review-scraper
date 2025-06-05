from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import pandas as pd
from datetime import datetime, timedelta  # <-- Don't forget this

class ReviewScraper:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.sales_team = self.load_sales_team()

    def load_sales_team(self):
        return {
            "Sam Lallouz": [
        "Sam Lallouz"
    ],
    "Abe Burger": [
        "Abe Burger"
    ],
    "Mason Kashat": [
        "Mason Kashat"
    ],
    "Elie Golshan": [
        "Elie Golshan"
    ],
    "Adela Bejko": [
        "Adela Bejko"
    ],
    "Daniel Moore": [
        "Daniel Moore"
    ],
    "Anthony Victor": [
        "Anthony Victor"
    ],
    "Andrew Kennally": [
        "Andrew Kennally"
    ],
    "James Gieselmann": [
        "James Gieselmann"
    ],
    "Xashary Pimentel": [
        "Xashary Pimentel"
    ],
    "Liz Edery": [
        "Liz Edery"
    ],
    "Benjamin Arnold": [
        "Benjamin Arnold"
    ],
    "Jonathan Baker": [
        "Jonathan Baker"
    ],
    "Nash Fabregas": [
        "Nash Fabregas"
    ],
    "Or Florian": [
        "Or Florian"
    ],
    "David Chang": [
        "David Chang"
    ],
    "Sam Schonfeld": [
        "Sam Schonfeld"
    ],
    "Eva Ohana": [
        "Eva Ohana"
    ],
    "Shimon Wolk": [
        "Shimon Wolk"
    ],
    "Quincy Luzunaris": [
        "Quincy Luzunaris"
    ],
    "Jacob Goodman": [
        "Jacob Goodman"
    ],
    "Chris Mothershed": [
        "Chris Mothershed"
    ],
    "Evin Lopez": [
        "Evin Lopez"
    ],
    "Tanya Macchia": [
        "Tanya Macchia"
    ],
    "Anthony Sargenti": [
        "Anthony Sargenti"
    ],
    "Vladimir Duboriz": [
        "Vladimir Duboriz"
    ],
    "Ikey Jajati": [
        "Ikey Jajati"
    ],
    "Peter Feierman": [
        "Peter Feierman"
    ],
    "James Park": [
        "James Park"
    ],
    "Isaac Hanono": [
        "Isaac Hanono"
    ],
    "David Saadia": [
        "David Saadia"
    ],
    "Jacob Lapidus": [
        "Jacob Lapidus"
    ],
    "Thomas Elsmore": [
        "Thomas Elsmore"
    ],
    "Sam Hayyim": [
        "Sam Hayyim"
    ],
    "Asher Rafailov": [
        "Asher Rafailov"
    ],
    "Jeffrey Feit": [
        "Jeffrey Feit"
    ],
    "Scott Wellbrock": [
        "Scott Wellbrock"
    ],
    "Adam Maine": [
        "Adam Maine"
    ],
    "Huda Alyesh": [
        "Huda Alyesh"
    ],
    "Jonathan Davila": [
        "Jonathan Davila"
    ],
    "Dylan Bohn": [
        "Dylan Bohn"
    ],
    "Cole Gabel": [
        "Cole Gabel"
    ],
    "Ari Kay": [
        "Ari Kay"
    ],
    "Simon Chalouh": [
        "Simon Chalouh"
    ],
    "Dan Sebag": [
        "Dan Sebag"
    ],
    "Theo Rapoport": [
        "Theo Rapoport"
    ],
    "Terrence Cashe": [
        "Terrence Cashe"
    ],
    "Emmanuel Ishema": [
        "Emmanuel Ishema"
    ],
    "Ilan Benghozi": [
        "Ilan Benghozi"
    ],
    "Isaac Blane": [
        "Isaac Blane"
    ],
    "Philippe Augustin": [
        "Philippe Augustin"
    ],
    "Daniel Khodorkovsky": [
        "Daniel Khodorkovsky"
    ],
    "Aaron Haze": [
        "Aaron Haze"
    ],
    "Tracy Medina": [
        "Tracy Medina"
    ],
    "Darel Kimi": [
        "Darel Kimi"
    ],
    "Yosef Scheff": [
        "Yosef Scheff"
    ],
    "Dorin Griza": [
        "Dorin Griza"
    ],
    "Allen Armin": [
        "Allen Armin"
    ],
    "Jared Cole": [
        "Jared Cole"
    ],
    "Simon Halabi": [
        "Simon Halabi"
    ],
    "John Silva": [
        "John Silva"
    ],
    "Eli Versicherter": [
        "Eli Versicherter"
    ],
    "Dominic Ferranti": [
        "Dominic Ferranti"
    ],
    "Grace New": [
        "Grace New"
    ],
    "Lisa Davis": [
        "Lisa Davis"
    ],
    "Kari Auer": [
        "Kari Auer"
    ],
    "Michael Jabbour": [
        "Michael Jabbour"
    ],
    "Adam Belizzone": [
        "Adam Belizzone"
    ],
    "Mehdi Dahel": [
        "Mehdi Dahel"
    ],
    "Nicolas Lescalier": [
        "Nicolas Lescalier"
    ],
    "Joseph Hakakian": [
        "Joseph Hakakian"
    ],
    "Paul Housey": [
        "Paul Housey"
    ],
    "Joseph Heres": [
        "Joseph Heres"
    ],
    "Marcus Hoffman": [
        "Marcus Hoffman"
    ],
    "Nick Onwenu": [
        "Nick Onwenu"
    ],
    "Michael Mackey": [
        "Michael Mackey"
    ],
    "Olivia Esara": [
        "Olivia Esara"
    ],
    "Omer Fogel": [
        "Omer Fogel"
    ],
    "Brian Garcia": [
        "Brian Garcia"
    ],
    "Sebastiano Lamonato": [
        "Sebastiano Lamonato"
    ],
    "Josh Shamoil": [
        "Josh Shamoil"
    ],
    "Robert Pilat": [
        "Robert Pilat"
    ],
    "Nataly Gonzalez": [
        "Nataly Gonzalez"
    ],
    "Darien Ramirez": [
        "Darien Ramirez"
    ],
    "Jordan Josephs": [
        "Jordan Josephs"
    ],
    "Aaron Goldberg": [
        "Aaron Goldberg"
    ],
    "Max Gieselmann": [
        "Max Gieselmann"
    ],
    "Avi Tetrokalashvili": [
        "Avi Tetrokalashvili"
    ],
    "David Cohen": [
        "David Cohen"
    ],
    "Branden Walsh": [
        "Branden Walsh"
    ],
    "Robert Kestenbaum": [
        "Robert Kestenbaum"
    ],
    "Jared Biller": [
        "Jared Biller"
    ],
    "Samuel Hunter": [
        "Samuel Hunter"
    ],
    "Batsheva Zarchi": [
        "Batsheva Zarchi"
    ],
    "Jonathan Loring": [
        "Jonathan Loring"
    ],
    "Phil Andre Amiths": [
        "Phil Andre Amiths"
    ],
    "Hunny Khodorkovsky": [
        "Hunny Khodorkovsky"
    ],
    "Meir Leskin": [
        "Meir Leskin"
    ],
    "Shaya Fishman": [
        "Shaya Fishman"
    ],
    "Ryan Roach": [
        "Ryan Roach"
    ],
    "Roynees Murel": [
        "Roynees Murel"
    ],
    "Israel Lallouz": [
        "Israel Lallouz"
    ],
    "Cole Gem": [
        "Cole Gem"
    ],
    "Tameka Williams": [
        "Tameka Williams"
    ],
    "Slim Jim Admin": [
        "Slim Jim Admin"
    ],
    "David Alvarado": [
        "David Alvarado"
    ],
    "Luca Cremonini": [
        "Luca Cremonini"
    ],
    "Drew Gold": [
        "Drew Gold"
    ],
    "Esther Harooni": [
        "Esther Harooni"
    ],
    "Yeva Zakharchenko": [
        "Yeva Zakharchenko"
    ],
    "Riley Middendorf": [
        "Riley Middendorf", "Riley"
    ],
    "Tamar Harooni": [
        "Tamar Harooni"
    ],
    "Max Gualtieri": [
        "Max Gualtieri"
    ],
    "Christopher Pegues": [
        "Christopher Pegues"
    ],
    "Valeria Holub": [
        "Valeria Holub"
    ],
    "Alexander Watson": [
        "Alexander Watson"
    ],
    "Barry Dollman": [
        "Barry Dollman"
    ],
    "Marcos Cruz": [
        "Marcos Cruz"
    ],
    "Marco Bernardi": [
        "Marco Bernardi"
    ],
    "Jack Hoffman": [
        "Jack Hoffman"
    ],
    "Dillon Le'Blanc": [
        "Dillon Le'Blanc"
    ],
    "Michael Goldman": [
        "Michael Goldman"
    ],
    "Taylor Klavas": [
        "Taylor Klavas"
    ],
    "Yonah Stern": [
        "Yonah Stern"
    ],
    "Dave Salas": [
        "Dave Salas"
    ],
    "Nicole Heres": [
        "Nicole Heres"
    ],
    "Jeffrey Decator": [
        "Jeffrey Decator"
    ],
    "Gregory Blackmon": [
        "Gregory Blackmon"
    ],
    "Gabriel Muniz": [
        "Gabriel Muniz"
    ],
    "Everal Simon": [
        "Everal Simon"
    ],
    "Marco Duman": [
        "Marco Duman"
    ],
    "Daniel Kaplan": [
        "Daniel Kaplan"
    ],
    "Esther Rosenblum": [
        "Esther Rosenblum"
    ],
    "Yael Reingold": [
        "Yael Reingold"
    ],
    "Sam Cyr": [
        "Sam Cyr"
    ],
    "David Alhalabi": [
        "David Alhalabi"
    ],
    "Anthony Andrade": [
        "Anthony Andrade"
    ],
    "Beyoncee Onwenu": [
        "Beyoncee Onwenu"
    ],
    "Zack Obidov": [
        "Zack Obidov"
    ],
    "Antonios Kontos": [
        "Antonios Kontos"
    ],
    "Ricardo Bordas": [
        "Ricardo Bordas"
    ],
    "Louise Lallouz": [
        "Louise Lallouz"
    ],
    "Ben Shamus": [
        "Ben Shamus"
    ],
    "Thanny Wongmanee": [
        "Thanny Wongmanee"
    ],
    "Benjamin Eliav": [
        "Benjamin Eliav"
    ],
    "Raymon Sakal": [
        "Raymon Sakal"
    ],
    "Joe Kaplan": [
        "Joe Kaplan"
    ],
    "Nelind Dedolli": [
        "Nelind Dedolli"
    ],
    "Nikita Kalin": [
        "Nikita Kalin"
    ],
    "Eitan Miro": [
        "Eitan Miro"
    ],
    "Sam Nathan Levy": [
        "Sam Nathan Levy"
    ],
    "David Balanka": [
        "David Balanka"
    ],
    "Renada Hoxhallari": [
        "Renada Hoxhallari"
    ],
    "Santiago Vargas": [
        "Santiago Vargas"
    ],
    "Hannah Pinter": [
        "Hannah Pinter"
    ],
    "Elaine Peters": [
        "Elaine Peters"
    ],
    "Jessica Higgins": [
        "Jessica Higgins"
    ],
    "Hannah Fogel": [
        "Hannah Fogel"
    ],
    "Jesse Garcia": [
        "Jesse Garcia"
    ],
    "Freddy Parker": [
        "Freddy Parker"
    ],
    "Farah Hadi": [
        "Farah Hadi"
    ],
    "Haider Umar": [
        "Haider Umar"
    ],
    "Bo Straussberg": [
        "Bo Straussberg"
    ],
    "Justin Abdaal": [
        "Justin Abdaal"
    ],
    "Ricky Jezrawi": [
        "Ricky Jezrawi"
    ],
    "Lucca Biondo": [
        "Lucca Biondo"
    ],
    "Aryan Arora": [
        "Aryan Arora"
    ],
    "Diyorbek Alibekov": [
        "Diyorbek Alibekov"
    ],
    "Redi Bizhuta": [
        "Redi Bizhuta"
    ],
    "Harry Ohana": [
        "Harry Ohana"
    ],
    "Braydon Moore": [
        "Braydon Moore"
    ],
    "Michael Garcia": [
        "Michael Garcia"
    ],
    "Soukaina Qarnia": [
        "Soukaina Qarnia"
    ],
    "Morris Davidov": [
        "Morris Davidov"
    ],
    "Herta Cota": [
        "Herta Cota"
    ],
    "Erinda Lamaj": [
        "Erinda Lamaj"
    ],
    "Marvin Guerra": [
        "Marvin Guerra"
    ],
    "Miles Mitchell": [
        "Miles Mitchell"
    ],
    "Judah Zadeh": [
        "Judah Zadeh"
    ],
    "Maggie Atanasova": [
        "Maggie Atanasova"
    ],
    "Kyle Salley": [
        "Kyle Salley"
    ],
    "Daniela Donato": [
        "Daniela Donato"
    ],
    "Jop Abalos": [
        "Jop Abalos"
    ],
    "Keenan Gates": [
        "Keenan Gates"
    ],
    "Daniel Moro": [
        "Daniel Moro"
    ],
    "Joanna Ferreira": [
        "Joanna Ferreira"
    ],
    "Kaitlyn Vickers": [
        "Kaitlyn Vickers"
    ],
    "Jacob Macready": [
        "Jacob Macready"
    ],
    "Freddy Katz": [
        "Freddy Katz"
    ],
    "Alexsandre Devdariani": [
        "Alexsandre Devdariani"
    ],
    "Tara Weiss": [
        "Tara Weiss"
    ],
    "Jose Siman": [
        "Jose Siman"
    ],
    "Adi Athzva": [
        "Adi Athzva"
    ],
    "Anatoliy Kireyev": [
        "Anatoliy Kireyev"
    ],
    "Carlo Moreno": [
        "Carlo Moreno"
    ],
    "Dalton Short": [
        "Dalton Short"
    ],
    "Jose Mejia": [
        "Jose Mejia"
    ],
    "Forrest Sockwell": [
        "Forrest Sockwell"
    ],
    "Alina Miclea": [
        "Alina Miclea"
    ],
    "Clyde Wethers": [
        "Clyde Wethers", "Evin Lopez"
    ],
    "Maurice Allen": [
        "Maurice Allen"
    ],
    "Anna Clark": [
        "Anna Clark"
    ],
    "Eden Parker": [
        "Eden Parker"
    ],
    "Gerta Daci": [
        "Gerta Daci"
    ],
    "Xhenita Shera": [
        "Xhenita Shera"
    ],
    "Jackson Owens": [
        "Jackson Owens"
    ],
    "Rafael Ocariz Almirao": [
        "Rafael Ocariz Almirao"
    ],
    "Michael Duong": [
        "Michael Duong"
    ],
    "Raysa Morell": [
        "Raysa Morell"
    ],
    "Victoriano Hernandez": [
        "Victoriano Hernandez"
    ],
    "Moshe Katash": [
        "Moshe Katash"
    ],
    "Angel Arias": [
        "Angel Arias"
    ],
    "Liam Serebriakov": [
        "Liam Serebriakov"
    ],
    "Ramon Frias": [
        "Ramon Frias"
    ],
    "Cyrus Holder": [
        "Cyrus Holder"
    ],
    "Samuel Johnson": [
        "Samuel Johnson"
    ],
    "Ari Levin": [
        "Ari Levin"
    ],
    "Vanessa Castro": [
        "Vanessa Castro"
    ],
    "Michael Barker": [
        "Michael Barker"
    ],
    "Brian Ostapower": [
        "Brian Ostapower"
    ],
    "Alex Nunez": [
        "Alex Nunez"
    ],
    "Batel Benbenishti": [
        "Batel Benbenishti"
    ],
    "Noah Rabu": [
        "Noah Rabu"
    ],
    "Jessica Btesh": [
        "Jessica Btesh", "Jessica B"
    ],
    "Daniel Parada": [
        "Daniel Parada"
    ],
    "Christopher Moore": [
        "Christopher Moore"
    ],
    "Daniel Birger": [
        "Daniel Birger"
    ],
    "Mo Crowler": [
        "Mo Crowler"
    ],
    "Chase Brady": [
        "Chase Brady"
    ],
    "Galt Mikesell": [
        "Galt Mikesell"
    ],
    "Jhenceil Lozano": [
        "Jhenceil Lozano"
    ],
    "Hammad Bhatti": [
        "Hammad Bhatti"
    ],
    "Nate Broom": [
        "Nate Broom"
    ],
    "Aylin A": [
        "Aylin A"
    ],
    "Ari Sasson": [
        "Ari Sasson"
    ],
    "Sebastian Devia": [
        "Sebastian Devia"
    ],
    "Laurens Bell": [
        "Laurens Bell"
    ],
    "Abigail Marmol": [
        "Abigail Marmol"
    ],
    "Cameron McWilliams": [
        "Cameron McWilliams"
    ],
    "Justus Santiago": [
        "Justus Santiago"
    ],
    "Beri Spiro": [
        "Beri Spiro"
    ],
    "Bradley Yucht": [
        "Bradley Yucht"
    ],
    "Moshe Fishman": [
        "Moshe Fishman"
    ],
    "Chanel Caouette": [
        "Chanel Caouette"
    ],
    "Max Vernot": [
        "Max Vernot"
    ],
    "Gordon Carr": [
        "Gordon Carr"
    ],
    "Michael Lieber": [
        "Michael Lieber"
    ],
    "Rowan Kelly": [
        "Rowan Kelly"
    ],
    "Connor McCauley": [
        "Connor McCauley"
    ],
    "Tyrell Bell": [
        "Tyrell Bell"
    ],
    "Semina Bulic": [
        "Semina Bulic"
    ],
    "Braden Short": [
        "Braden Short"
    ],
    "Angelo Diaz": [
        "Angelo Diaz"
    ],
    "Alessi Martinez": [
        "Alessi Martinez"
    ],
    "Ander Ariztoy": [
        "Ander Ariztoy"
    ],
    "Kellen Philipp": [
        "Kellen Philipp"
    ],
    "Ernesto Morejon": [
        "Ernesto Morejon"
    ],
    "Fabrizzio Castelli": [
        "Fabrizzio Castelli"
    ],
    "Jonah Aaron": [
        "Jonah Aaron"
    ],
    "George Cripotos": [
        "George Cripotos"
    ],
    "Mario Petushi": [
        "Mario Petushi"
    ],
    "Sama Balayeva": [
        "Sama Balayeva"
    ],
    "Andrew Cohen": [
        "Andrew Cohen"
    ],
    "Savi Shal": [
        "Savi Shal"
    ],
    "Abraham Lancry": [
        "Abraham Lancry"
    ],
    "Wellington Da Silva": [
        "Wellington Da Silva"
    ],
    "Phoenix Daluz": [
        "Phoenix Daluz"
    ],
    "Joe Goldberg": [
        "Joe Goldberg"
    ],
    "Eve Ohana": [
        "Eve Ohana"
    ],
    "Brandon Graves": [
        "Brandon Graves"
    ],
    "Nick Tecocoatzi": [
        "Nick Tecocoatzi"
    ],
    "Orestes Denis": [
        "Orestes Denis"
    ],
    "Shad Amarouche": [
        "Shad Amarouche"
    ],
    "Kevin Moreno": [
        "Kevin Moreno"
    ],
    "Luis Lago": [
        "Luis Lago"
    ],
    "CCP Help Desk": [
        "CCP Help Desk"
    ],
    "Mani De Osu": [
        "Mani De Osu"
    ],
    "Othniel Samudra": [
        "Othniel Samudra"
    ],
    "Alexander Ferreira": [
        "Alexander Ferreira"
    ],
    "Courtney Swafford": [
        "Courtney Swafford"
    ],
    "Andres Elizalde": [
        "Andres Elizalde"
    ],
    "Joshua Celado": [
        "Joshua Celado"
    ],
    "Kristopher Galvan": [
        "Kristopher Galvan"
    ],
    "Alexa Sauer": [
        "Alexa Sauer"
    ],
    "Itai Katz": [
        "Itai Katz"
    ],
    "Herbert Sexton": [
        "Herbert Sexton"
    ],
    "Mahmoud Ahmed": [
        "Mahmoud Ahmed"
    ],
    "Matan Twersky": [
        "Matan Twersky"
    ],
    "Manuel Nunez": [
        "Manuel Nunez"
    ],
    "Giovanni Herrera": [
        "Giovanni Herrera"
    ],
    "David Adi": [
        "David Adi"
    ],
    "Marco Chahino": [
        "Marco Chahino"
    ],
    "Dias Dautov": [
        "Dias Dautov"
    ],
    "Sarah Yusufov": [
        "Sarah Yusufov"
    ],
    "Eduardo Fernandez": [
        "Eduardo Fernandez"
    ],
    "Christian Gonzalez": [
        "Christian Gonzalez"
    ],
    "Daniel Greenberg": [
        "Daniel Greenberg"
    ],
    "Ameda Tarr": [
        "Ameda Tarr"
    ],
    "Michael Cecchetto": [
        "Michael Cecchetto"
    ],
    "Jose Ferrer": [
        "Jose Ferrer"
    ],
    "Maria Ruiz": [
        "Maria Ruiz"
    ],
    "David Kamara": [
        "David Kamara"
    ],
    "Ethan Cherem": [
        "Ethan Cherem"
    ],
    "Yaakov Gros": [
        "Yaakov Gros"
    ],
    "Illia Derevianko": [
        "Illia Derevianko"
    ],
    "Chaim Boukai": [
        "Chaim Boukai"
    ],
    "Alesio Dosti": [
        "Alesio Dosti"
    ],
    "Lidor Sabag": [
        "Lidor Sabag"
    ],
    "Netali Bar": [
        "Netali Bar"
    ],
    "Jayson Guevara": [
        "Jayson Guevara"
    ],
    "Ali Ramos": [
        "Ali Ramos"
    ],
    "Jeremy Asheghian": [
        "Jeremy Asheghian"
    ],
    "Latif Nawab": [
        "Latif Nawab"
    ],
    "Danielle Harrington": [
        "Danielle Harrington"
    ],
    "William Cooke": [
        "William Cooke"
    ],
    "Maria Angulo": [
        "Maria Angulo"
    ],
    "Brendon Dragon": [
        "Brendon Dragon"
    ],
    "Dwain Kuffuor": [
        "Dwain Kuffuor"
    ],
    "James Beattie": [
        "James Beattie"
    ],
    "William Hawley": [
        "William Hawley"
    ],
    "Abdallah Meshal": [
        "Abdallah Meshal"
    ],
    "Roberto Tellez": [
        "Roberto Tellez"
    ],
    "Gabriel Sevilla": [
        "Gabriel Sevilla"
    ],
    "George Kloak": [
        "George Kloak"
    ],
    "Alexander Sherman": [
        "Alexander Sherman"
    ],
    "Harel Dahan": [
        "Harel Dahan"
    ],
    "Bryan Azzo": [
        "Bryan Azzo"
    ],
    "Dmitrii Samedinov": [
        "Dmitrii Samedinov"
    ],
    "Charlie Hara": [
        "Charlie Hara"
    ],
    "Vera Johnson": [
        "Vera Johnson"
    ],
    "Lucas Balderrama": [
        "Lucas Balderrama"
    ],
    "Jared Diaz": [
        "Jared Diaz"
    ],
    "Assem Moataz": [
        "Assem Moataz"
    ],
    "Suleman Ansar": [
        "Suleman Ansar"
    ],
    "Alex Temurov": [
        "Alex Temurov"
    ],
    "Kirt Bromley": [
        "Kirt Bromley"
    ],
    "Aryan Aurora": [
        "Aryan Aurora"
    ],
    "Ergi Strazimiri": [
        "Ergi Strazimiri"
    ],
    "Karah Tyson": [
        "Karah Tyson"
    ],
    "Gabriele Moretti": [
        "Gabriele Moretti"
    ],
    "Maguette Gueye": [
        "Maguette Gueye"
    ],
    "Sherilyn Khuu": [
        "Sherilyn Khuu"
    ],
    "Alicia Lucarelli": [
        "Alicia Lucarelli"
    ],
    "Victor Soulan": [
        "Victor Soulan"
    ],
    "Nataliia Honchar": [
        "Nataliia Honchar"
    ],
    "Alif Rahman": [
        "Alif Rahman"
    ],
    "Behlul Bibovic": [
        "Behlul Bibovic"
    ],
    "Gavriel Ellis": [
        "Gavriel Ellis"
    ],
    "Matias Wawro": [
        "Matias Wawro"
    ],
    "Ben Hazan": [
        "Ben Hazan"
    ],
    "Alvin Santiago": [
        "Alvin Santiago"
    ],
    "Jack Dehne": [
        "Jack Dehne"
    ],
    "Dante Desilvia": [
        "Dante Desilvia"
    ],
    "Olaoluwasubomi Aduloju": [
        "Olaoluwasubomi Aduloju"
    ],
    "Jacob Porter": [
        "Jacob Porter"
    ],
    "Samuel Isakov": [
        "Samuel Isakov"
    ],
    "Levi Benoliel": [
        "Levi Benoliel"
    ],
    "Janet Canepa": [
        "Janet Canepa"
    ],
    "Tohir Hodjakulov": [
        "Tohir Hodjakulov"
    ],
    "Fiorella Sturla": [
        "Fiorella Sturla"
    ],
    "Chris Bogias": [
        "Chris Bogias"
    ],
    "Samuel Branagan": [
        "Samuel Branagan"
    ],
    "Ariel Yusifov": [
        "Ariel Yusifov"
    ],
    "Kadeem Hylton": [
        "Kadeem Hylton"
    ],
    "Kila Ho'omana": [
        "Kila Ho'omana"
    ],
    "Nicholas Garcia": [
        "Nicholas Garcia"
    ],
    "Julien Durand": [
        "Julien Durand"
    ],
    "Michael Chang He He": [
        "Michael Chang He He"
    ],
    "Guy Twagiramungu": [
        "Guy Twagiramungu"
    ],
    "Javier Gutierrez": [
        "Javier Gutierrez"
    ],
    "Benjamin Smith": [
        "Benjamin Smith"
    ],
    "Kristine Igot": [
        "Kristine Igot"
    ],
    "Joseph Levy": [
        "Joseph Levy"
    ],
    "Mehdi El Bouzid": [
        "Mehdi El Bouzid"
    ],
    "Nathaniel Dery": [
        "Nathaniel Dery", "Nate"
    ],
    "Joseph Wieder": [
        "Joseph Wieder"
    ],
    "Andrew Tortoriello": [
        "Andrew Tortoriello"
    ],
    "David Toradze": [
        "David Toradze"
    ],
    "Kenneth Bobb": [
        "Kenneth Bobb"
    ],
    "Henrry Suazo": [
        "Henrry Suazo"
    ],
    "Jordan Madison": [
        "Jordan Madison"
    ],
    "Emilio Madeira": [
        "Emilio Madeira"
    ],
    "Jason Mullalli": [
        "Jason Mullalli"
    ],
    "Nicholas Fallick": [
        "Nicholas Fallick"
    ],
    "Elmir Sirar": [
        "Elmir Sirar"
    ],
    "Brice Gandhi": [
        "Brice Gandhi"
    ],
    "Thomas Good": [
        "Thomas Good"
    ],
    "Zeke Halfar": [
        "Zeke Halfar"
    ],
    "Chezkie Cohen": [
        "Chezkie Cohen"
    ],
    "Boris Gladstien": [
        "Boris Gladstien"
    ],
    "Matthew Fletcher": [
        "Matthew Fletcher"
    ],
    "Justin Boese": [
        "Justin Boese"
    ],
    "Jack Harary": [
        "Jack Harary"
    ],
    "William VInce": [
        "William VInce"
    ],
    "Kevin Valasquez": [
        "Kevin Valasquez"
    ],
    "Elias Rospigliosi": [
        "Elias Rospigliosi"
    ],
    "Simon Anbeh": [
        "Simon Anbeh"
    ],
    "Jessie Mazor": [
        "Jessie Mazor"
    ],
    "Isabela Carvajal Rios": [
        "Isabela Carvajal Rios"
    ],
    "Ludwig Bogdan Andrei": [
        "Ludwig Bogdan Andrei"
    ],
    "Jade Bota": [
        "Jade Bota"
    ],
    "Angela Jaume Martin": [
        "Angela Jaume Martin"
    ],
    "Beka Lezhava": [
        "Beka Lezhava"
    ],
    "Jose Hambra": [
        "Jose Hambra"
    ],
    "Charlie Jackman": [
        "Charlie Jackman"
    ],
    "Jessica Leslie": [
        "Jessica Leslie"
    ],
    "Gustavo Pazmino": [
        "Gustavo Pazmino"
    ],
    "John O'Day": [
        "John O'Day"
    ],
    "Benjamin Brasher": [
        "Benjamin Brasher"
    ],
    "Aidan Casey": [
        "Aidan Casey"
    ],
    "Mardell Young": [
        "Mardell Young"
    ],
    "Adrian Ferrer": [
        "Adrian Ferrer"
    ],
    "Nicholas DeDominicis": [
        "Nicholas DeDominicis"
    ],
    "Ellis Sorensen": [
        "Ellis Sorensen"
    ],
    "Reuven Dayan": [
        "Reuven Dayan"
    ],
    "Levi Grunblatt": [
        "Levi Grunblatt"
    ],
    "Amir Ardestany": [
        "Amir Ardestany"
    ],
    "Kimberli Ramirez": [
        "Kimberli Ramirez"
    ],
    "Cindy Shao": [
        "Cindy Shao"
    ],
    "Neir Taube": [
        "Neir Taube"
    ],
    "Galvin Jones": [
        "Galvin Jones"
    ],
    "Joshua Teich": [
        "Joshua Teich"
    ],
    "Elyssa Briggs": [
        "Elyssa Briggs"
    ],
    "Pierce Kinney": [
        "Pierce Kinney"
    ],
    "Samantha Ramirez": [
        "Samantha Ramirez"
    ],
    "Faton Sela": [
        "Faton Sela"
    ],
    "Jason Myers": [
        "Jason Myers"
    ],
    "Eli Vogel": [
        "Eli Vogel"
    ],
    "Pierre Cisar": [
        "Pierre Cisar"
    ],
    "Charles Stengel": [
        "Charles Stengel"
    ],
    "Till Brack": [
        "Till Brack"
    ],
    "Lukas Neufeldt": [
        "Lukas Neufeldt"
    ],
    "Christina Zajac": [
        "Christina Zajac"
    ],
    "Paul Darkow": [
        "Paul Darkow"
    ],
    "Jano Rathert": [
        "Jano Rathert"
    ],
    "Asher Swidler": [
        "Asher Swidler"
    ],
    "Carroll Rich": [
        "Carroll Rich"
    ],
    "Carlos Padilla": [
        "Carlos Padilla"
    ],
    "Mordechai Salem": [
        "Mordechai Salem", "Mordi", "Mordi Salem"
    ],
    "Roxana Chavarria": [
        "Roxana Chavarria"
    ],
    "Donne D'Arnall": [
        "Donne D'Arnall"
    ],
    "Alexis Belliveau": [
        "Alexis Belliveau"
    ],
    "Victor Mallakh": [
        "Victor Mallakh"
    ],
    "Katherine Decrescenzo": [
        "Katherine Decrescenzo"
    ],
    "Jeffrey Broome": [
        "Jeffrey Broome"
    ],
    "Jennifer Igualas": [
        "Jennifer Igualas"
    ],
    "Adam Jay Sher": [
        "Adam Jay Sher"
    ],
    "Valentin Nkoussou": [
        "Valentin Nkoussou"
    ],
    "Joseph Mitchell": [
        "Joseph Mitchell"
    ],
    "Mark Abinader": [
        "Mark Abinader"
    ],
    "Darren Adeobe": [
        "Darren Adeobe"
    ],
    "Manya Rubstein": [
        "Manya Rubstein"
    ],
    "Jeremy Gelber": [
        "Jeremy Gelber"
    ],
    "Jeremy Chiprin": [
        "Jeremy Chiprin"
    ],
    "Elie Alfaks": [
        "Elie Alfaks"
    ],
    "Motty Houli": [
        "Motty Houli"
    ],
    "Marcus Khademi": [
        "Marcus Khademi"
    ],
    "Mike Rahrooh": [
        "Mike Rahrooh"
    ],
    "Bruno Francesco": [
        "Bruno Francesco"
    ],
    "Mendel Vogel": [
        "Mendel Vogel"
    ],
    "Arjun Rawal": [
        "Arjun Rawal"
    ],
    "Shlomo Polishuk": [
        "Shlomo Polishuk"
    ],
    "Victor Rodriguez": [
        "Victor Rodriguez"
    ],
    "Yuri Badalyan": [
        "Yuri Badalyan"
    ],
    "Mikayla Duncan": [
        "Mikayla Duncan"
    ],
    "Cynthia Owaygen": [
        "Cynthia Owaygen"
    ],
    "Sevphen Eman": [
        "Sevphen Eman"
    ],
    "Julio Lopez": [
        "Julio Lopez"
    ],
    "Nate Melman": [
        "Nate Melman"
    ],
    "Akiva Jesmer": [
        "Akiva Jesmer"
    ],
    "Jacob Ben": [
        "Jacob Ben"
    ],
    "Nasir Kakar": [
        "Nasir Kakar"
    ],
    "Triston Eugenio": [
        "Triston Eugenio"
    ],
    "Gabriel Starr": [
        "Gabriel Starr"
    ],
    "Adrian Popa": [
        "Adrian Popa"
    ],
    "Ethan Butcher": [
        "Ethan Butcher"
    ],
    "Juan Alvarez": [
        "Juan Alvarez"
    ],
    "Adnan Bashir": [
        "Adnan Bashir"
    ],
    "Cher Alkrief": [
        "Cher Alkrief"
    ],
    "Taier Levy": [
        "Taier Levy"
    ],
    "Leor Tsadok": [
        "Leor Tsadok"
    ]
}

    def setup_driver(self):
        options = Options()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(service=Service(self.driver_path), options=options)

    def find_representative(self, text):
        matched_reps = []
        for name, aliases in self.sales_team.items():
            for alias in aliases:
                # Buscar palabra completa, no substring
                if re.search(rf'\b{re.escape(alias)}\b', text, re.IGNORECASE):
                    matched_reps.append(name)
                    break
        return matched_reps if matched_reps else None

    def parse_google_date(self, raw_text):
        try:
            text = raw_text.strip().lower()
            today = datetime.today()
            delta = None

            if "minute" in text:
                num = int(re.search(r'\d+', text).group())
                delta = timedelta(minutes=num)
            elif "hour" in text:
                num = int(re.search(r'\d+', text).group())
                delta = timedelta(hours=num)
            elif "day" in text:
                num = 1 if "a day" in text else int(re.search(r'\d+', text).group())
                delta = timedelta(days=num)
            elif "week" in text:
                num = 1 if "a week" in text else int(re.search(r'\d+', text).group())
                delta = timedelta(weeks=num)
            elif "month" in text:
                num = 1 if "a month" in text else int(re.search(r'\d+', text).group())
                delta = timedelta(days=num * 30)
            elif "year" in text:
                num = 1 if "a year" in text else int(re.search(r'\d+', text).group())
                delta = timedelta(days=num * 365)

            return (today - delta).strftime("%Y-%m-%d") if delta else "Unknown"
        except:
            return "Unknown"

    def scrape_google(self):
        driver = self.setup_driver()
        wait = WebDriverWait(driver, 15)
        driver.get("https://www.google.com/maps/search/Premium+Merchant+Funding")
        time.sleep(5)

        try:
            reviews_tab = wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(., "Reviews")]')))
            driver.execute_script("arguments[0].click();", reviews_tab)
            time.sleep(5)

            sort_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label*="Sort"]')))
            driver.execute_script("arguments[0].click();", sort_button)
            time.sleep(1)

            newest_option = wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Newest")]')))
            driver.execute_script("arguments[0].click();", newest_option)
            time.sleep(2)
        except:
            print("⚠️ Couldn't sort reviews")

        reviews = []
        try:
            scrollable_div = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "m6QErb.DxyBCb.kA9KIf.dS8AEf")))
            for _ in range(10):
                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
                time.sleep(2)

            review_elements = driver.find_elements(By.CLASS_NAME, "jftiEf")
            for el in review_elements:
                text = el.text
                reps = self.find_representative(text)
                if not reps or not isinstance(reps, list):
                    continue
                try:
                    stars_raw = el.find_element(By.CSS_SELECTOR, 'span[role="img"]').get_attribute("aria-label")
                    match = re.search(r'(\d+)', stars_raw)
                    stars = match.group(1) if match else "No rating"
                except:
                    stars = "No rating"

                try:
                    raw_date = el.find_element(By.CLASS_NAME, "DU9Pgb").text.strip()
                    date = self.parse_google_date(raw_date)
                except:
                    date = "Unknown"

                for rep in reps:
                    reviews.append({
                        "Representative": rep,
                        "Date": date,
                        "Stars": stars,
                        "Text": text.strip(),
                        "Platform": "Google"  # o "Trustpilot"
                    })
        except Exception as e:
            print(f"❌ Google scraping error: {e}")

        driver.quit()
        return reviews

    def scrape_trustpilot(self):
        driver = self.setup_driver()
        wait = WebDriverWait(driver, 15)
        driver.get("https://www.trustpilot.com/review/www.pmfus.com")
        time.sleep(5)

        try:
            cookie = wait.until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
            cookie.click()
        except:
            pass

        reviews = []

        while True:
            print("🔄 Scroll hasta cargar reseñas...")
            for _ in range(20):
                driver.execute_script("window.scrollBy(0, 600);")
                time.sleep(1.5)

            review_blocks = driver.find_elements(By.XPATH, '//section//article')
            print(f"🔍 Procesando {len(review_blocks)} reseñas en esta página...")

            for block in review_blocks:
                try:
                    text = " ".join([p.text for p in block.find_elements(By.CSS_SELECTOR, 'p') if p.text.strip()])
                    reps = self.find_representative(text)
                    if not reps or not isinstance(reps, list):
                        continue
                    try:
                        stars_text = re.search(r'Rated (\d) out of 5',
                                               block.find_element(By.CSS_SELECTOR, "img[alt*='Rated']").get_attribute(
                                                   "alt")).group(1)
                    except:
                        stars_text = "No rating"

                    try:
                        date_text = block.find_element(By.TAG_NAME, 'time').text.strip()
                    except:
                        date_text = "Unknown"

                    for rep in reps:
                        reviews.append({
                            "Representative": rep,
                            "Date": date_text,
                            "Stars": stars_text,
                            "Text": text.strip(),
                            "Platform": "Google"  # o "Trustpilot"
                        })
                except Exception as e:
                    print(f"⚠️ Error procesando una reseña: {e}")
                    continue

            # Intentar ir a la siguiente página
            try:
                next_button = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@aria-label="Next page"]')))
                driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                time.sleep(1)

                if next_button.get_attribute("aria-disabled") != "true":
                    print("➡️ Pasando a la siguiente página...")
                    driver.execute_script("arguments[0].click();", next_button)
                    time.sleep(4)
                else:
                    print("✅ Última página alcanzada.")
                    break
            except Exception as e:
                print("✅ No se encontró el botón de siguiente página o está deshabilitado. Fin.")
                break

        driver.quit()
        return reviews

    def run(self):
        print("🔍 Scraping Google Reviews...")
        google_reviews = self.scrape_google()
        print(f"✅ {len(google_reviews)} Google reviews found.")

        print("🔍 Scraping Trustpilot Reviews...")
        trustpilot_reviews = self.scrape_trustpilot()
        print(f"✅ {len(trustpilot_reviews)} Trustpilot reviews found.")

        all_reviews = google_reviews + trustpilot_reviews

        filtered_reviews = []
        cutoff = datetime(2024, 5, 1)

        for review in all_reviews:
            raw_date = review.get("Date", "")
            if raw_date == "Unknown":
                continue
            try:
                # Detectar formato
                if re.match(r'^[A-Za-z]{3} \d{1,2}, \d{4}$', raw_date):  # Trustpilot: May 13, 2024
                    date_obj = datetime.strptime(raw_date, "%b %d, %Y")
                else:  # Google: 2024-05-13
                    date_obj = datetime.strptime(raw_date, "%Y-%m-%d")

                if date_obj >= cutoff:
                    filtered_reviews.append(review)
            except Exception as e:
                print(f"⚠️ Error parseando fecha: {raw_date} -> {e}")

        df = pd.DataFrame(all_reviews)
        df.to_csv("Review Tracker 2025.csv", index=False)
        print("📁 CSV saved: combined_reviews_sales_mentions.csv")

if __name__ == "__main__":
        DRIVER_PATH = r"C:\\Users\\PMF Guest\\Documents\\Reviews Project\\chromedriver.exe"
        scraper = ReviewScraper(DRIVER_PATH)
        scraper.run()