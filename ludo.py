# Ludo game Integrated With AI #
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import tkinter as tk
from tkmacosx import Button
import pandas as pd
import traceback
import csv
import random
from itertools import zip_longest
import os




import time
from random import randint, choice

class Ludo:
    gameover =1  
    tmp_red = []
    tmp_blue = []
    tmp_yellow = []
    tmp_green = []    
    username_id=[]        

    df = pd.read_csv("gamestats_summary.csv")
    game= df["game_id"]
    game_id = int(df["game_id"].values[-1])
    game_id = game_id + 1
    game_id_single = game_id
    roll = 0
    usernames = []
    ages = []
    genders = []
    countries = []
    roll_id = []
    dice_face = []
    user_killed = 0
    user_killed_count = []
    game_username = []
    winner = ""
    first_runner_up = ""

    options = ["Aruba",
    "Afghanistan",
    "Angola",
    "Anguilla",
    "Albania",
    "Aland",
    "Andorra",
    "United Arab Emirates",
    "Argentina",
    "Armenia",
    "American Samoa",
    "Antarctica",
    "Ashmore and Cartier Islands",
    "French Southern and Antarctic Lands",
    "Antigua and Barbuda",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Burundi",
    "Belgium",
    "Benin",
    "Burkina Faso",
    "Bangladesh",
    "Bulgaria",
    "Bahrain",
    "The Bahamas",
    "Bosnia and Herzegovina",
    "Bajo Nuevo Bank (Petrel Is.)",
    "Saint Barthelemy",
    "Belarus",
    "Belize",
    "Bermuda",
    "Bolivia",
    "Brazil",
    "Barbados",
    "Brunei",
    "Bhutan",
    "Botswana",
    "Central African Republic",
    "Canada",
    "Switzerland",
    "Chile",
    "China",
    "Ivory Coast",
    "Clipperton Island",
    "Cameroon",
    "Cyprus No Mans Area",
    "Democratic Republic of the Congo",
    "Republic of Congo",
    "Cook Islands",
    "Colombia",
    "Comoros",
    "Cape Verde",
    "Costa Rica",
    "Coral Sea Islands",
    "Cuba",
    "Curaçao",
    "Cayman Islands",
    "Northern Cyprus",
    "Cyprus",
    "Czech Republic",
    "Germany",
    "Djibouti",
    "Dominica",
    "Denmark",
    "Dominican Republic",
    "Algeria",
    "Ecuador",
    "Egypt",
    "Eritrea",
    "Dhekelia Sovereign Base Area",
    "Spain",
    "Estonia",
    "Ethiopia",
    "Finland",
    "Fiji",
    "Falkland Islands",
    "France",
    "Faroe Islands",
    "Federated States of Micronesia",
    "Gabon",
    "United Kingdom",
    "Georgia",
    "Guernsey",
    "Ghana",
    "Gibraltar",
    "Guinea",
    "Gambia",
    "Guinea Bissau",
    "Equatorial Guinea",
    "Greece",
    "Grenada",
    "Greenland",
    "Guatemala",
    "Guam",
    "Guyana",
    "Hong Kong S.A.R.",
    "Heard Island and McDonald Islands",
    "Honduras",
    "Croatia",
    "Haiti",
    "Hungary",
    "Indonesia",
    "Isle of Man",
    "India",
    "Indian Ocean Territories",
    "British Indian Ocean Territory",
    "Ireland",
    "Iran",
    "Iraq",
    "Iceland",
    "Israel",
    "Italy",
    "Jamaica",
    "Jersey",
    "Jordan",
    "Japan",
    "Baykonur Cosmodrome",
    "Siachen Glacier",
    "Kazakhstan",
    "Kenya",
    "Kyrgyzstan",
    "Cambodia",
    "Kiribati",
    "Saint Kitts and Nevis",
    "South Korea",
    "Kosovo",
    "Kuwait",
    "Laos",
    "Lebanon",
    "Liberia",
    "Libya",
    "Saint Lucia",
    "Liechtenstein",
    "Sri Lanka",
    "Lesotho",
    "Lithuania",
    "Luxembourg",
    "Latvia",
    "Macao S.A.R",
    "Saint Martin",
    "Morocco",
    "Monaco",
    "Moldova",
    "Madagascar",
    "Maldives",
    "Mexico",
    "Marshall Islands",
    "Macedonia",
    "Mali",
    "Malta",
    "Myanmar",
    "Montenegro",
    "Mongolia",
    "Northern Mariana Islands",
    "Mozambique",
    "Mauritania",
    "Montserrat",
    "Mauritius",
    "Malawi",
    "Malaysia",
    "Namibia",
    "New Caledonia",
    "Niger",
    "Norfolk Island",
    "Nigeria",
    "Nicaragua",
    "Niue",
    "Netherlands",
    "Norway",
    "Nepal",
    "Nauru",
    "New Zealand",
    "Oman",
    "Pakistan",
    "Panama",
    "Pitcairn Islands",
    "Peru",
    "Spratly Islands",
    "Philippines",
    "Palau",
    "Papua New Guinea",
    "Poland",
    "Puerto Rico",
    "North Korea",
    "Portugal",
    "Paraguay",
    "Palestine",
    "French Polynesia",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Western Sahara",
    "Saudi Arabia",
    "Scarborough Reef",
    "Sudan",
    "South Sudan",
    "Senegal",
    "Serranilla Bank",
    "Singapore",
    "South Georgia and South Sandwich Islands",
    "Saint Helena",
    "Solomon Islands",
    "Sierra Leone",
    "El Salvador",
    "San Marino",
    "Somaliland",
    "Somalia",
    "Saint Pierre and Miquelon",
    "Republic of Serbia",
    "Sao Tome and Principe",
    "Suriname",
    "Slovakia",
    "Slovenia",
    "Sweden",
    "Swaziland",
    "Sint Maarten",
    "Seychelles",
    "Syria",
    "Turks and Caicos Islands",
    "Chad",
    "Togo",
    "Thailand",
    "Tajikistan",
    "Turkmenistan",
    "East Timor",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Tuvalu",
    "Taiwan",
    "United Republic of Tanzania",
    "Uganda",
    "Ukraine",
    "United States Minor Outlying Islands",
    "Uruguay",
    "United States of America",
    "US Naval Base Guantanamo Bay",
    "Uzbekistan",
    "Vatican",
    "Saint Vincent and the Grenadines",
    "Venezuela",
    "British Virgin Islands",
    "United States Virgin Islands",
    "Vietnam",
    "Vanuatu",
    "Wallis and Futuna",
    "Akrotiri Sovereign Base Area",
    "Samoa",
    "Yemen",
    "South Africa",
    "Zambia",
    "Zimbabwe"]

    # this function calculates the centre of the window
    def centerWindow(width, height, root):  
        screen_width = root.winfo_screenwidth() 
        screen_height = root.winfo_screenheight() 
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        return int(x), int(y) 

    # for drawing the ludo board 
    def __init__(self, root,six_side_block,five_side_block,four_side_block,three_side_block,two_side_block,one_side_block):
        self.window = root
        # Make canvas
        self.make_canvas = Canvas(self.window, bg="black", width=650, height=630)
        self.make_canvas.pack(fill=BOTH,expand=1)

        # Make some containers to store data
        self.made_red_coin = []
        self.made_green_coin = []
        self.made_yellow_coin = []
        self.made_sky_blue_coin = []

        self.red_number_label = []
        self.green_number_label = []
        self.yellow_number_label = []
        self.sky_blue_number_label = []

        self.block_value_predict = []
        self.total_people_play = []

        # Ludo block all side image store
        self.block_number_side = [one_side_block, two_side_block, three_side_block, four_side_block, five_side_block, six_side_block]

        # Use for store specific position of all coins
        self.red_coord_store = [-1, -1, -1, -1]
        self.green_coord_store = [-1, -1, -1, -1]
        self.yellow_coord_store = [-1, -1, -1, -1]
        self.sky_blue_coord_store = [-1, -1, -1, -1]

        self.red_coin_position = [0, 1, 2, 3]
        self.green_coin_position = [0, 1, 2, 3]
        self.yellow_coin_position = [0, 1, 2, 3]
        self.sky_blue_coin_position = [0, 1, 2, 3]

        for index in range(len(self.red_coin_position)):# Specific coin position set to -1 by default
            self.red_coin_position[index] = -1
            self.green_coin_position[index] = -1
            self.yellow_coin_position[index] = -1
            self.sky_blue_coin_position[index] = -1

        # Number to room to be traverse by specific color coin, store in that variable
        self.move_red_counter = 0
        self.move_green_counter = 0
        self.move_yellow_counter = 0
        self.move_sky_blue_counter = 0

        self.take_permission = 0
        self.six_with_overlap = 0

        self.red_store_active = 0
        self.sky_blue_store_active = 0
        self.yellow_store_active = 0
        self.green_store_active = 0

        self.six_counter = 0
        self.time_for = -1

        # Some variables initializes with None
        self.right_star = None
        self.down_star = None
        self.left_star = None
        self.up_star = None

        # for playng against computer
        self.robo_prem = 0
        self.count_robo_stage_from_start = 0
        self.robo_store = []

        # By default some function call
        self.board_set_up()

        self.instruction_btn_red()
        self.instruction_btn_sky_blue()
        self.instruction_btn_yellow()
        self.instruction_btn_green()

        self.take_initial_control()


    def board_set_up(self):
        # Cover Box made
        self.make_canvas.create_rectangle(100, 15, 100 + (40 * 15), 15 + (40 * 15), width=6, fill="white")

        # Square box
        self.make_canvas.create_rectangle(100, 15, 100+240, 15+240, width=3, fill="#fc4176")# left up large square
        self.make_canvas.create_rectangle(100, (15+240)+(40*3), 100+240, (15+240)+(40*3)+(40*6), width=3, fill="#74c0e3")# left down large square
        self.make_canvas.create_rectangle(340+(40*3), 15, 340+(40*3)+(40*6), 15+240, width=3, fill="#ade374")# right up large square
        self.make_canvas.create_rectangle(340+(40*3), (15+240)+(40*3), 340+(40*3)+(40*6), (15+240)+(40*3)+(40*6), width=3, fill="#fcb542")# right down large square

        # Left 3 box(In white region)
        self.make_canvas.create_rectangle(100, (15+240), 100+240, (15+240)+40, width=3)
        self.make_canvas.create_rectangle(100+40, (15 + 240)+40, 100 + 240, (15 + 240) + 40+40, width=3, fill="#fc4176")
        self.make_canvas.create_rectangle(100, (15 + 240)+80, 100 + 240, (15 + 240) + 80+40, width=3)

        # right 3 box(In white region)
        self.make_canvas.create_rectangle(100+240, 15, 100 + 240+40, 15 + (40*6), width=3)
        self.make_canvas.create_rectangle(100+240+40, 15+40, 100+240+80, 15 + (40*6), width=3, fill="#ade374")
        self.make_canvas.create_rectangle(100+240+80, 15, 100 + 240+80+40, 15 + (40*6), width=3)

        # up 3 box(In white region)
        self.make_canvas.create_rectangle(340+(40*3), 15+240, 340+(40*3)+(40*6), 15+240+40, width=3)
        self.make_canvas.create_rectangle(340+(40*3), 15+240+40, 340+(40*3)+(40*6)-40, 15+240+80, width=3, fill="#fcb542")
        self.make_canvas.create_rectangle(340+(40*3), 15+240+80, 340+(40*3)+(40*6), 15+240+120, width=3)

        # down 3 box(In white region)
        self.make_canvas.create_rectangle(100, (15 + 240)+(40*3), 100 + 240+40, (15 + 240)+(40*3)+(40*6), width=3)
        self.make_canvas.create_rectangle(100+240+40, (15 + 240)+(40*3), 100 + 240+40+40, (15 + 240)+(40*3)+(40*6)-40, width=3, fill="#74c0e3")
        self.make_canvas.create_rectangle(100 + 240+40+40, (15 + 240)+(40*3), 100 + 240+40+40+40, (15 + 240)+(40*3)+(40*6), width=3)

        # All left separation line
        start_x = 100 + 40
        start_y = 15 + 240
        end_x = 100 + 40
        end_y = 15 + 240 + (40 * 3)
        for _ in range(5):
            self.make_canvas.create_line(start_x, start_y, end_x, end_y, width=3)
            start_x+=40
            end_x+= 40

        # All right separation line
        start_x = 100+240+(40*3)+40
        start_y = 15 + 240
        end_x = 100+240+(40*3)+40
        end_y = 15 + 240 + (40 * 3)
        for _ in range(5):
            self.make_canvas.create_line(start_x, start_y, end_x, end_y, width=3)
            start_x += 40
            end_x += 40

        # All up separation done
        start_x = 100+240
        start_y = 15+40
        end_x = 100+240+(40*3)
        end_y = 15+40
        for _ in range(5):
            self.make_canvas.create_line(start_x, start_y, end_x, end_y, width=3)
            start_y += 40
            end_y += 40

        # All down separation done
        start_x = 100 + 240
        start_y = 15 + (40*6)+(40*3)+40
        end_x = 100 + 240 + (40 * 3)
        end_y = 15 + (40*6)+(40*3)+40
        for _ in range(5):
            self.make_canvas.create_line(start_x, start_y, end_x, end_y, width=3)
            start_y += 40
            end_y += 40

        # Square box(Coins containers) white region make
        self.make_canvas.create_rectangle(100+20, 15+40-20, 100 + 40 + 60 + 40 +60+20, 15+40+40+40+100-20, width=3, fill="white")
        self.make_canvas.create_rectangle(340+(40*3)+40 - 20, 15 + 40-20, 340+(40*3)+40 + 60 + 40 + 40+20+20, 15+40+40+40+100-20, width=3, fill="white")
        self.make_canvas.create_rectangle(100+20, 340+80-20+15, 100 + 40 + 60 + 40 +60+20, 340+80+60+40+40+20+15, width=3, fill="white")
        self.make_canvas.create_rectangle(340+(40*3)+40 - 20, 340 + 80 - 20+15, 340+(40*3)+40 + 60 + 40 + 40+20+20, 340 + 80 + 60 + 40 + 40 + 20+15, width=3, fill="white")


        # Left up square inside box made
        self.make_canvas.create_rectangle(100+40, 15+40, 100+40+40, 15+40+40, width=3, fill="#fc4176")
        self.make_canvas.create_rectangle(100+40+60+60, 15 + 40, 100+40+60+40+60, 15 + 40 + 40, width=3, fill="#fc4176")
        self.make_canvas.create_rectangle(100 + 40, 15 + 40+100, 100 + 40 + 40, 15 + 40 + 40+100, width=3, fill="#fc4176")
        self.make_canvas.create_rectangle(100 + 40 + 60 + 60, 15 + 40+100, 100 + 40 + 60 + 40 +60, 15 + 40 + 40+100, width=3, fill="#fc4176")


        # Right up square inside box made
        self.make_canvas.create_rectangle(340+(40*3)+40, 15 + 40, 340+(40*3)+40 + 40, 15 + 40 + 40, width=3, fill="#ade374")
        self.make_canvas.create_rectangle(340+(40*3)+40+ 60 + 40+20, 15 + 40, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40, width=3, fill="#ade374")
        self.make_canvas.create_rectangle(340+(40*3)+40, 15 + 40 + 100, 340+(40*3)+40 + 40, 15 + 40 + 40 + 100, width=3, fill="#ade374")
        self.make_canvas.create_rectangle(340+(40*3)+40+ 60 + 40+20, 15 + 40 + 100, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40 + 100, width=3, fill="#ade374")


        # Left down square inside box made
        self.make_canvas.create_rectangle(100 + 40, 340+80+15, 100 + 40 + 40, 340+80+40+15, width=3, fill="#74c0e3")
        self.make_canvas.create_rectangle(100 + 40 + 60 + 40+20, 340+80+15, 100 + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="#74c0e3")
        self.make_canvas.create_rectangle(100 + 40, 340+80+60+40+15, 100 + 40 + 40, 340+80+60+40+40+15, width=3, fill="#74c0e3")
        self.make_canvas.create_rectangle(100 + 40 + 60 + 40+20, 340+80+60+40+15, 100 + 40 + 60 + 40 + 40+20, 340+80+60+40+40+15, width=3, fill="#74c0e3")


        # Right down square inside box made
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40, 340+80+15, 340 + (40 * 3) + 40 + 40, 340+80+40+15, width=3, fill="#fcb542")
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40 + 60 + 40+20, 340+80+15, 340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="#fcb542")
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40, 340+80+60+40+15, 340 + (40 * 3) + 40 + 40,340+80+60+40+40+15, width=3, fill="#fcb542")
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40 + 60 + 40+20, 340+80+60+40+15,340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+60+40+40+15, width=3, fill="#fcb542")

        # sky_blue start position
        self.make_canvas.create_rectangle(100+240,340+(40*5)-5,100+240+40,340+(40*6)-5,fill="#74c0e3",width=3)
        # Red start position
        self.make_canvas.create_rectangle(100 + 40, 15+(40*6), 100 +40 + 40, 15+(40*6)+40, fill="#fc4176", width=3)
        # Green start position
        self.make_canvas.create_rectangle(100 + (40*8), 15 + 40, 100 +(40*9), 15 + 40+ 40, fill="#ade374", width=3)
        # Yellow start position
        self.make_canvas.create_rectangle(100 + (40 * 6)+(40*3)+(40*4), 15 + (40*8), 100 + (40 * 6)+(40*3)+(40*5), 15 + (40*9), fill="#fcb542", width=3)

        # Traingle in middle
        self.make_canvas.create_polygon(100+240, 15+240, 100+240+60, 15+240+60, 100+240, 15+240+(40*3), width=3,fill="#fc4176",outline="black")
        self.make_canvas.create_polygon(100 + 240+(40*3), 15 + 240, 100 + 240 + 60, 15 + 240 + 60, 100 + 240+(40*3), 15 + 240 + (40 * 3), width=3, fill="#fcb542",outline="black")
        self.make_canvas.create_polygon(100 + 240, 15 + 240, 100 + 240 + 60, 15 + 240 + 60, 100 + 240 + (40 * 3), 15 + 240, width=3, fill="#ade374",outline="black")
        self.make_canvas.create_polygon(100 + 240, 15 + 240+(40*3), 100 + 240 + 60, 15 + 240 + 60, 100 + 240 + (40 * 3), 15 + 240+(40*3), width=3, fill="#74c0e3",outline="black")

        # Make coin for red left up block
        red_1_coin = self.make_canvas.create_oval(100+40, 15+40, 100+40+40, 15+40+40, width=3, fill="#fc4176", outline="black")
        red_2_coin = self.make_canvas.create_oval(100+40+60+60, 15 + 40, 100+40+60+60+40, 15 + 40 + 40, width=3, fill="#fc4176", outline="black")
        red_3_coin = self.make_canvas.create_oval(100 + 40 + 60 + 60, 15 + 40 + 100, 100 + 40 + 60 + 60 + 40, 15 + 40 + 40 + 100, width=3, fill="#fc4176", outline="black")
        red_4_coin = self.make_canvas.create_oval(100 + 40, 15 + 40+100, 100 + 40 + 40, 15 + 40 + 40+100, width=3,fill="#fc4176", outline="black")
        self.made_red_coin.append(red_1_coin)
        self.made_red_coin.append(red_2_coin)
        self.made_red_coin.append(red_3_coin)
        self.made_red_coin.append(red_4_coin)

        # Make coin under number label for red left up block
        red_1_label = Label(self.make_canvas, text="1", font=("Papyrus", 15, "bold"), bg="#fc4176", fg="black")
        red_1_label.place(x=100 + 40+15, y=15 + 40 + 5)
        red_2_label = Label(self.make_canvas, text="2", font=("Papyrus", 15, "bold"), bg="#fc4176", fg="black")
        red_2_label.place(x=100 + 40 + 60 + 60 + 15, y=15 + 40 + 5)
        red_3_label = Label(self.make_canvas, text="3", font=("Papyrus", 15, "bold"), bg="#fc4176", fg="black")
        red_3_label.place(x=100 + 40 + 60 + 60 + 15, y=15 + 40 + 100 + 5)
        red_4_label = Label(self.make_canvas, text="4", font=("Papyrus", 15, "bold"), bg="#fc4176", fg="black")
        red_4_label.place(x=100 + 40 + 10, y=15 + 40 + 100 + 5)
        self.red_number_label.append(red_1_label)
        self.red_number_label.append(red_2_label)
        self.red_number_label.append(red_3_label)
        self.red_number_label.append(red_4_label)

        # Make coin for green right up block
        green_1_coin = self.make_canvas.create_oval(340+(40*3)+40, 15 + 40, 340+(40*3)+40 + 40, 15 + 40 + 40, width=3, fill="#ade374", outline="black")
        green_2_coin = self.make_canvas.create_oval(340+(40*3)+40+ 60 + 40+20, 15 + 40, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40, width=3, fill="#ade374", outline="black")
        green_3_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40 + 100, 340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 15 + 40 + 40 + 100, width=3, fill="#ade374", outline="black")
        green_4_coin = self.make_canvas.create_oval(340+(40*3)+40, 15 + 40 + 100, 340+(40*3)+40 + 40, 15 + 40 + 40 + 100, width=3, fill="#ade374", outline="black")
        self.made_green_coin.append(green_1_coin)
        self.made_green_coin.append(green_2_coin)
        self.made_green_coin.append(green_3_coin)
        self.made_green_coin.append(green_4_coin)

        # Make coin under number label for green right up block
        green_1_label = Label(self.make_canvas, text="1", font=("Papyrus", 15, "bold"), bg="#ade374", fg="black")
        green_1_label.place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 5)
        green_2_label = Label(self.make_canvas, text="2", font=("Papyrus", 15, "bold"), bg="#ade374", fg="black")
        green_2_label.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 5)
        green_3_label = Label(self.make_canvas, text="3", font=("Papyrus", 15, "bold"), bg="#ade374", fg="black")
        green_3_label.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 100 + 5)
        green_4_label = Label(self.make_canvas, text="4", font=("Papyrus", 15, "bold"), bg="#ade374", fg="black")
        green_4_label.place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 100 + 5)
        self.green_number_label.append(green_1_label)
        self.green_number_label.append(green_2_label)
        self.green_number_label.append(green_3_label)
        self.green_number_label.append(green_4_label)

        # Make coin for sky_blue left down block
        sky_blue_1_coin = self.make_canvas.create_oval(100 + 40, 340+80+15, 100 + 40 + 40, 340+80+40+15, width=3, fill="#74c0e3", outline="black")
        sky_blue_2_coin = self.make_canvas.create_oval(100 + 40 + 60 + 40+20, 340+80+15, 100 + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="#74c0e3", outline="black")
        sky_blue_3_coin = self.make_canvas.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15, 100 + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15, width=3, fill="#74c0e3", outline="black")
        sky_blue_4_coin = self.make_canvas.create_oval( 100 + 40, 340+80+60+40+15, 100 + 40 + 40, 340+80+60+40+40+15, width=3, fill="#74c0e3", outline="black")
        self.made_sky_blue_coin.append(sky_blue_1_coin)
        self.made_sky_blue_coin.append(sky_blue_2_coin)
        self.made_sky_blue_coin.append(sky_blue_3_coin)
        self.made_sky_blue_coin.append(sky_blue_4_coin)

        # Make coin under number label for sky_blue left down block
        sky_blue_1_label = Label(self.make_canvas, text="1", font=("Papyrus", 15, "bold"), bg="#74c0e3", fg="black")
        sky_blue_1_label.place(x=100 + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        sky_blue_2_label = Label(self.make_canvas, text="2", font=("Papyrus", 15, "bold"), bg="#74c0e3", fg="black")
        sky_blue_2_label.place(x=100 + 40 + 60 + 60 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        sky_blue_3_label = Label(self.make_canvas, text="3", font=("Papyrus", 15, "bold"), bg="#74c0e3", fg="black")
        sky_blue_3_label.place(x=100 + 40 + 60 + 60 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 60 + 40 + 10)
        sky_blue_4_label = Label(self.make_canvas, text="4", font=("Papyrus", 15, "bold"), bg="#74c0e3", fg="black")
        sky_blue_4_label.place(x=100 + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 60 + 40 + 10)
        self.sky_blue_number_label.append(sky_blue_1_label)
        self.sky_blue_number_label.append(sky_blue_2_label)
        self.sky_blue_number_label.append(sky_blue_3_label)
        self.sky_blue_number_label.append(sky_blue_4_label)

        # Make coin for yellow right down block
        yellow_1_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 340+80+15, 340 + (40 * 3) + 40 + 40, 340+80+40+15, width=3, fill="#fcb542", outline="black")
        yellow_2_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340+80+15, 340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="#fcb542", outline="black")
        yellow_3_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15, 340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15, width=3, fill="#fcb542", outline="black")
        yellow_4_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 340+80+60+40+15, 340 + (40 * 3) + 40 + 40,340+80+60+40+40+15, width=3, fill="#fcb542", outline="black")
        self.made_yellow_coin.append(yellow_1_coin)
        self.made_yellow_coin.append(yellow_2_coin)
        self.made_yellow_coin.append(yellow_3_coin)
        self.made_yellow_coin.append(yellow_4_coin)

        # Make coin under number label for yellow right down block
        yellow_1_label = Label(self.make_canvas, text="1", font=("Papyrus", 15, "bold"), bg="#fcb542", fg="black")
        yellow_1_label.place(x=340 + (40 * 3) + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        yellow_2_label = Label(self.make_canvas, text="2", font=("Papyrus", 15, "bold"), bg="#fcb542", fg="black")
        yellow_2_label.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        yellow_3_label = Label(self.make_canvas, text="3", font=("Papyrus", 15, "bold"), bg="#fcb542", fg="black")
        yellow_3_label.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)
        yellow_4_label = Label(self.make_canvas, text="4", font=("Papyrus", 15, "bold"), bg="#fcb542", fg="black")
        yellow_4_label.place(x=340 + (40 * 3) + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)
        self.yellow_number_label.append(yellow_1_label)
        self.yellow_number_label.append(yellow_2_label)
        self.yellow_number_label.append(yellow_3_label)
        self.yellow_number_label.append(yellow_4_label)

        # Make star safe zone
        """
                                              A
                                           L  *  B
                                   K *  *  *     *  *  * C
                                        *           *
                                        J *        * D
                                       *            *
                                  I*  *  *      *  *  * E
                                         H   *   F
                                             G
        """
        # Right star
        common_x = 340+(40*6)+20
        common_y = 15+240+2
        #              A                     B                        C                         D                        E                              F                    G                                  H                        I                            J                            K                         L
        coord = [common_x,common_y,  common_x+5,common_y+15,  common_x+15,common_y+15,  common_x+8,common_y+20,    common_x+15,common_y+25,    common_x+5,common_y+25,    common_x,common_y+25+10,   common_x-5,common_y+25,   common_x-16,common_y+25,   common_x-8,common_y+15+5,   common_x-15,common_y+15,   common_x-5,common_y+15]
        self.make_canvas.create_polygon(coord,width=3,fill="#74c0e3")

        # Up star
        common_x = 100+240+2+18
        common_y = 15 + (40*2) + 2
        #              A                              B                                   C                             D                                E                                        F                       G                                          H                               I                            J                                      K                                   L
        coord = [common_x, common_y,   common_x + 5,   common_y + 15,      common_x + 15, common_y + 15,      common_x + 8, common_y + 20,     common_x + 15, common_y + 25,       common_x + 5, common_y + 25,      common_x, common_y + 25 + 10,    common_x - 5, common_y + 25,     common_x - 16, common_y + 25,     common_x - 8,common_y + 15 + 5,     common_x - 15,common_y + 15,     common_x - 5,common_y + 15]
        self.make_canvas.create_polygon(coord, width=3, fill="#74c0e3")

        # Left star
        common_x = 100 + (40*2) + 2 +18
        common_y = 15 + 240+(40*2) + 2
        #                  A                     B                                   C                            D                                 E                                F                           G                                  H                                    I                                 J                                    K                                L
        coord = [common_x, common_y,   common_x + 5, common_y + 15,    common_x + 15, common_y + 15,    common_x + 8,common_y + 20,    common_x + 15, common_y + 25,    common_x + 5, common_y + 25,    common_x, common_y + 25 + 10,    common_x - 5, common_y + 25,      common_x - 16, common_y + 25,     common_x - 8, common_y + 15 + 5,     common_x - 15, common_y + 15,     common_x - 5, common_y + 15]
        self.make_canvas.create_polygon(coord, width=3, fill="#74c0e3")

        # Down star
        common_x = 100 + 240 + (40*2) + 2 + 18
        common_y = 15 + (40 * 6) + (40*3)+(40*3)+2
        #              A                         B                             C                                       D                        E                                       F                                   G                                     H                                  I                                  J                                  K                                  L
        coord = [common_x, common_y,   common_x + 5, common_y + 15,    common_x + 15, common_y + 15,    common_x + 8, common_y + 20,    common_x + 15, common_y + 25,      common_x + 5, common_y + 25,       common_x, common_y + 25 + 10,        common_x - 5, common_y + 25,       common_x - 16, common_y + 25,       common_x - 8, common_y + 15 + 5,      common_x - 15, common_y + 15,      common_x - 5, common_y + 15]
        self.make_canvas.create_polygon(coord, width=3, fill="#74c0e3")
   
    # Total number of players: Control take at first

    def take_initial_control(self):
        
        def simulation_aftercontrol():
            for player_index in range(int(numPlayersSim)):
                self.total_people_play.append(player_index)
                print(self.total_people_play)
                self.make_command()
                top.destroy()
            if numPlayersSim == 2:
                while Ludo.gameover:
                    # operate(1, top)
                    self.make_prediction_sim("#fc4176")
                    self.make_prediction_sim("#74c0e3")
            elif numPlayersSim == 3:
                while Ludo.gameover:
                # operate(1, top)
                    self.make_prediction_sim("#fc4176")
                    self.make_prediction_sim("#74c0e3")
                    self.make_prediction_sim("#fcb542")
            elif numPlayersSim == 4:
                while Ludo.gameover:
                    # operat e(1, top)
                    self.make_prediction_sim("#fc4176")
                    self.make_prediction_sim("#74c0e3")
                    self.make_prediction_sim("#fcb542")
                    self.make_prediction_sim("#ade374")

        def simulation():
            global numPlayersSim
            numPlayersSim = randint(2, 4)
            df = pd.read_csv("userdetails.csv")
            if numPlayersSim == 2:
                b1 = randint(1, len(df)//2)
                b2 = randint(len(df)//2, len(df))
                Ludo.usernames.append(df["username"].iloc[b1])
                Ludo.usernames.append(df["username"].iloc[b2])
            elif numPlayersSim == 3:
                b1 = randint(1, len(df)//6)
                b2 = randint(len(df)//6, len(df)//3)
                b3 = randint(len(df)//3, len(df))
                Ludo.usernames.append(df["username"].iloc[b1])
                Ludo.usernames.append(df["username"].iloc[b2])
                Ludo.usernames.append(df["username"].iloc[b3])
            elif numPlayersSim == 4:
                b1 = randint(1, len(df)//6)
                b2 = randint(len(df)//8, len(df)//6)
                b3 = randint(len(df)//6, len(df)//4)
                b4 = randint(len(df)//4, len(df)//2)
                b4 = randint(len(df)//2, len(df))
                Ludo.usernames.append(df["username"].iloc[b1])
                Ludo.usernames.append(df["username"].iloc[b2])
                Ludo.usernames.append(df["username"].iloc[b3])
                Ludo.usernames.append(df["username"].iloc[b4])
            top.destroy()

            simulation_aftercontrol()
        
        for i in range(1,4):
            self.block_value_predict[i][1]['state'] = DISABLED
        def on_enter(e):
            e.widget['background'] = '#F2F2F2'
        def on_leave_btn1(e):
            e.widget['background'] = '#ade374'
        def on_leave_btn2(e):
            e.widget['background'] = '#fcb542'
        def on_leave_btn3(e):
            e.widget['background'] = '#74c0e3'
        def on_leave_btn4(e):
            e.widget['background'] = '#fc4176'
        def on_exit():
            window.destroy()
        
        # this window is for single and multiplayer options
        top = Toplevel(background="black")
        x, y = Ludo.centerWindow(800, 650, top)
        top.geometry(f"800x650+{x}+{y}")
        top.title("Ludo Master")
        path="Images/screen3.png" 
        image = img= (Image.open(path))
        resized_image= image.resize((800,500), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)
        label = tk.Label(top, image = new_image, compound=tk.CENTER, bg="black", width=800, height=650).pack()
        # buttons for single, multilayer and simulation
        PLAY_BUTTON = Button(top, text="SINGLE PLAYER",font=("Papyrus",40,"italic"), fg="black", bg="#ade374",   borderwidth=0, command=lambda: user_input(top) )
        PLAY_BUTTON.place(x=220, y=100) 
        Multi_Button = Button(top, text="MULTI PLAYER",font=("Papyrus",40,"italic"), fg="black", bg="#fcb542",   borderwidth=0, command=lambda: multi_user_input())
        Multi_Button.place(x=220, y=200) 
        Simulation_Button = Button(top, text="SIMULATION",font=("Papyrus",40,"italic"), fg="black", bg="#74c0e3",   borderwidth=0, command=lambda: simulation())
        Simulation_Button.place(x=240, y=300) 
        Quit_Button = Button(top, text="QUIT",font=("Papyrus",40,"italic"), fg="black", bg="#fc4176",   borderwidth=0, command=on_exit)
        Quit_Button.place(x=300, y=400) 
        # to change colors over hovering
        PLAY_BUTTON.bind("<Enter>", on_enter)
        PLAY_BUTTON.bind("<Leave>", on_leave_btn1)
        Multi_Button.bind("<Enter>", on_enter)
        Multi_Button.bind("<Leave>", on_leave_btn2)
        Simulation_Button.bind("<Enter>", on_enter)
        Simulation_Button.bind("<Leave>", on_leave_btn3)
        Quit_Button.bind("<Enter>", on_enter)
        Quit_Button.bind("<Leave>", on_leave_btn4)
        # simulation()

        def go_back(top):
            top.destroy()
        def check_digit(input):
                    if input.isdigit():
                        if (int(input) > 2 and int(input) <= 100):
                            return True
                    else:
                        messagebox.showerror("Input Error", "Please enter age between 3 and 100")
                        return False
        def check_alphanumeric(input):
                    if input.isalnum():
                        return True
                    else:
                        messagebox.showerror("Input Error", "Please enter a valid username")
                        return False
        def check_string(input):
                    if input.isdigit():
                        return True
                    else:
                        messagebox.showerror("Input Error", "Please input number of players between 2 and 4")
                        return False
        
        def user_input(top):
        # top.destsroy()
            top2 = Toplevel(background="black")
            x, y = Ludo.centerWindow(800, 650, top2)
            top2.geometry(f"800x650+{x}+{y}")
            top2.title("Ludo Master")
            path="Images/screen3.png" 
            image = (Image.open(path))
            age_validation = top2.register(check_digit)
            username_validation = top2.register(check_alphanumeric)
            string_validation = top2.register(check_string)
            resized_image= image.resize((800,500), Image.ANTIALIAS)
            new_image= ImageTk.PhotoImage(resized_image)
            label = tk.Label(top2, image = new_image, compound=tk.CENTER, bg="black", width=800, height=650).pack()
            top2.update()
            usernameLabel = Label(top2, text="Username", font=("Papyrus", 20, "bold"), bg="#fc4176", fg="black").place(x=200, y=100)
            usernameEntry = Entry(top2 , validatecommand=(username_validation,'%P'), validate="focus")
            usernameEntry.place(x=350, y=100)
            ageLabel = Label(top2, text="Age", font=("Papyrus", 20, "bold"), bg="#fc4176", fg="black").place(x=200, y=170)
            ageEntry = Entry(top2, validatecommand=(age_validation,'%P'), validate="focus")
            ageEntry.place(x=350, y=170)
            country = StringVar(top2)
            countryLabel = Label(top2, text="Country", font=("Papyrus", 20, "bold"), bg="#fc4176", fg="black").place(x=200, y=240)
            country.set("None") # default value
            opt = Ludo.options
            w = OptionMenu(top2, country, *opt)
            w.place(x = 350, y = 240)
            PLAY_BUTTON = Button(top2, text="PLAY",font=("Papyrus",40,"italic"), fg="black", bg="#ade374",   borderwidth=0, command=lambda: operate(1, top2) )
            PLAY_BUTTON.place(x=320, y=500) 

                    
                    

        def multi_user_input():
                top.destroy()
                top3 = Toplevel(background="black")
                x, y = Ludo.centerWindow(800, 650, top3)
                top3.geometry(f"800x650+{x}+{y}")
                top3.title("Ludo Master")
                new_image= ImageTk.PhotoImage(resized_image)
                label = tk.Label(top3, compound=tk.CENTER, bg="black", width=800, height=650).pack()
                top3.update()
                age_validation = top3.register(check_digit)
                username_validation = top3.register(check_alphanumeric)
                string_validation = top3.register(check_string)
                numberPlayersLabel = Label(top3, text="Number of Players", font=("Papyrus", 20, "bold"), bg="#fc4176", fg="black").place(x=200, y=50)
                global numberPlayersText
                numberPlayersText = Entry(top3, width = 5)
                numberPlayersText.place(x=400, y=50)
                Submit_Button = Button(top3, text="SUBMIT",width = 200, height = 30, font=("Papyrus",15,"italic"), fg="black", bg="#ade374",   borderwidth=0, command=lambda: filtering())
                Submit_Button.place(x=500, y=50) 
                

                def sel(var):
                    selection = str(var.get())
                def player1():
                    usernameLabel1 = Label(top3, text="Username", font=("Papyrus", 20, "bold"), bg="#fc4176", fg="black")
                    usernameLabel1.place(x=50, y=150)
                    global usernameEntry1 
                    usernameEntry1 = Entry(top3, validatecommand=(username_validation,'%P'), validate="focus")
                    usernameEntry1.place(x=180, y=150)
                    ageLabel1 = Label(top3, text="Age", font=("Papyrus", 20, "bold"), bg="#fc4176", fg="black").place(x=50, y=200)
                    global ageEntry1
                    ageEntry1 = Entry(top3, validatecommand=(age_validation,'%P'), validate="focus")
                    ageEntry1.place(x=180, y=200)
                    global country1
                    country1 = StringVar(top3)
                    countryLabel1 = Label(top3, text="Country", font=("Papyrus", 20, "bold"), bg="#fc4176", fg="black").place(x=50, y=250)
                    country1.set("None") # default value
                    opt1 = Ludo.options
                    w1 = OptionMenu(top3, country1, *opt1)
                    w1.place(x = 180, y = 250)
                    global gender1
                    gender1 = StringVar(top3)
                    genderLabel1 = Label(top3, text="Gender", font=("Papyrus", 20, "bold"), bg="#fc4176", fg="black").place(x=50, y=300)
                    R11 = Radiobutton(top3, text="Female", font=("Papyrus", 13, "bold"), bg="#fc4176", fg="black", variable=gender1, value="female").place(x=180, y=300)
                    R21 = Radiobutton(top3, text="Male", font=("Papyrus", 13, "bold"), bg="#fc4176", fg="black", variable=gender1, value="male").place(x=260, y=300)
                    R31 = Radiobutton(top3, text="Other", font=("Papyrus", 13, "bold"), bg="#fc4176", fg="black", variable=gender1, value="other").place(x=340, y=300)
                    
                                        
                def player2():
                    # player 2 information
                    usernameLabel2 = Label(top3, text="Username", font=("Papyrus", 20, "bold"), bg="#74c0e3", fg="black").place(x=50, y=400)
                    global usernameEntry2
                    usernameEntry2 = Entry(top3, validatecommand=(username_validation,'%P'), validate="focus")
                    usernameEntry2.place(x=180, y=400)
                    ageLabel2 = Label(top3, text="Age", font=("Papyrus", 20, "bold"), bg="#74c0e3", fg="black").place(x=50, y=450)
                    global ageEntry2
                    ageEntry2 = Entry(top3, validatecommand=(age_validation,'%P'), validate="focus")
                    ageEntry2.place(x=180, y=450)
                    global country2
                    global gender2
                    country2 = StringVar(top3)
                    countryLabel2 = Label(top3, text="Country", font=("Papyrus", 20, "bold"), bg="#74c0e3", fg="black").place(x=50, y=500)
                    country2.set("None") # default value
                    opt = Ludo.options
                    w2 = OptionMenu(top3, country2, *opt)
                    w2.place(x = 180, y = 500)
                    gender2 = StringVar(top3)
                    genderLabel2 = Label(top3, text="Gender", font=("Papyrus", 20, "bold"), bg="#74c0e3", fg="black").place(x=50, y=550)
                    R12 = Radiobutton(top3, text="Female", font=("Papyrus", 13, "bold"), bg="#74c0e3", fg="black", variable=gender2, value="female").place(x=180, y=550)
                    R22 = Radiobutton(top3, text="Male", font=("Papyrus", 13, "bold"), bg="#74c0e3", fg="black", variable=gender2, value="male").place(x=260, y=550)
                    R32 = Radiobutton(top3, text="Other", font=("Papyrus", 13, "bold"), bg="#74c0e3", fg="black", variable=gender2, value="other").place(x=340, y=550)
                
                def player3():
                    # player 3 information
                    usernameLabel3 = Label(top3, text="Username", font=("Papyrus", 20, "bold"), bg="#fcb542", fg="black").place(x=430, y=150)
                    global usernameEntry3
                    usernameEntry3 = Entry(top3, validatecommand=(username_validation,'%P'), validate="focus")
                    usernameEntry3.place(x=560, y=150)
                    ageLabel3 = Label(top3, text="Age", font=("Papyrus", 20, "bold"), bg="#fcb542", fg="black").place(x=430, y=200)
                    global ageEntry3
                    global country3
                    global gender3
                    ageEntry3 = Entry(top3, validatecommand=(age_validation,'%P'), validate="focus")
                    ageEntry3.place(x=560, y=200)
                    country3 = StringVar(top3)
                    countryLabel3 = Label(top3, text="Country", font=("Papyrus", 20, "bold"), bg="#fcb542", fg="black").place(x=430, y=250)
                    country3.set("None") # default value
                    opt = Ludo.options
                    w3 = OptionMenu(top3,country3, *opt)
                    w3.place(x = 560, y = 250)
                    gender3 = StringVar(top3)
                    genderLabel3 = Label(top3, text="Gender", font=("Papyrus", 20, "bold"), bg="#fcb542", fg="black").place(x=430, y=300)
                    R13 = Radiobutton(top3, text="Female", font=("Papyrus", 13, "bold"), bg="#fcb542", fg="black", variable=gender3, value="female").place(x=550, y=300)
                    R23 = Radiobutton(top3, text="Male", font=("Papyrus", 13, "bold"), bg="#fcb542", fg="black", variable=gender3, value="male").place(x=630, y=300)
                    R33 = Radiobutton(top3, text="Other", font=("Papyrus", 13, "bold"), bg="#fcb542", fg="black", variable=gender3, value="other").place(x=700, y=300)

                def player4():
                    # player 4 information
                    usernameLabel4 = Label(top3, text="Username", font=("Papyrus", 20, "bold"), bg="#ade374", fg="black").place(x=430, y=400)
                    global usernameEntry4
                    usernameEntry4 = Entry(top3, validatecommand=(username_validation,'%P'), validate="focus")
                    usernameEntry4.place(x=560, y=400)
                    ageLabel4 = Label(top3, text="Age", font=("Papyrus", 20, "bold"), bg="#ade374", fg="black").place(x=430, y=450)
                    global ageEntry4
                    global country4
                    ageEntry4 = Entry(top3, validatecommand=(age_validation,'%P'), validate="focus")
                    ageEntry4.place(x=560, y=450)
                    country4 = StringVar(top3)
                    countryLabel4 = Label(top3, text="Country", font=("Papyrus", 20, "bold"), bg="#ade374", fg="black").place(x=430, y=500)
                    country4.set("None") # default value
                    global countryOption4   
                    countryOption4 = StringVar()
                    opt = Ludo.options
                    w4 = OptionMenu(top3, country4, *opt)
                    w4.place(x = 560, y = 500)
                    global gender4
                    gender4 = StringVar(top3)
                    genderLabel4 = Label(top3, text="Gender", font=("Papyrus", 20, "bold"), bg="#ade374", fg="black").place(x=430, y=550)
                    R14 = Radiobutton(top3, text="Female", font=("Papyrus", 13, "bold"), bg="#ade374", fg="black", variable=gender4, value="female").place(x=550, y=550)
                    R24 = Radiobutton(top3, text="Male", font=("Papyrus", 13, "bold"), bg="#ade374", fg="black", variable=gender4, value="male").place(x=630, y=550)
                    R34 = Radiobutton(top3, text="Other", font=("Papyrus", 13, "bold"), bg="#ade374", fg="black", variable=gender4, value="other").place(x=700, y=550)

                def filtering():# Total player input value filtering
                    def input_filtering(coin_number):# Input value Filtering
                        try:
                            return True if (4>=int(coin_number)>=2) or type(coin_number) == int else False
                        except:
                            return False
                    response_take_int = int(numberPlayersText.get())
                    response_take = input_filtering(numberPlayersText.get())
                    if (response_take_int == int(2)): 
                        player1()
                        player2()
                        Submit_Button['state'] = DISABLED
                        PLAY_BUTTON = Button(top3, text="PLAY",font=("Papyrus",40,"italic"), fg="black", bg="#ade374",   borderwidth=0, command=lambda: check_players(response_take_int, response_take) )
                        PLAY_BUTTON.place(x=320, y=600)
                    elif (response_take_int == 3):
                        player1()
                        player2()
                        player3()
                        Submit_Button['state'] = DISABLED
                        PLAY_BUTTON = Button(top3, text="PLAY",font=("Papyrus",40,"italic"), fg="black", bg="#ade374",   borderwidth=0, command=lambda: check_players(response_take_int, response_take) )
                        PLAY_BUTTON.place(x=320, y=600)
                    elif(response_take_int == 4):
                        player1()
                        player2()
                        player3()
                        player4()
                        Submit_Button['state'] = DISABLED
                        PLAY_BUTTON = Button(top3, text="PLAY",font=("Papyrus",40,"italic"), fg="black", bg="#ade374",   borderwidth=0, command=lambda: check_players(response_take_int, response_take) )
                        PLAY_BUTTON.place(x=320, y=600) 
                    else:
                        messagebox.showerror("Input Error", "Please input number of players between 2 and 4")
                        top3.destroy()
                        top.destroy()
                        self.take_initial_control()
                    
                def check_players(response_take_int, response_take):
                        if response_take_int == 2:
                            user1 = [str(usernameEntry1.get()), str(ageEntry1.get()), str(country1.get()), str(gender1.get())]
                            user2 = [str(usernameEntry2.get()), str(ageEntry2.get()), str(country2.get()), str(gender2.get())]
                            with open('userdetails.csv','a') as f:
                                writer = csv.writer(f)
                                writer.writerow(user1)
                                writer.writerow(user2)

                        elif response_take_int == 3:
                            user1 = [str(usernameEntry1.get()), str(ageEntry1.get()), str(country1.get()), str(gender1.get())]
                            user2 = [str(usernameEntry2.get()), str(ageEntry2.get()), str(country2.get()), str(gender2.get())]
                            user3 = [str(usernameEntry3.get()), str(ageEntry3.get()), str(country3.get()), str(gender3.get())]

                            with open('userdetails.csv','a') as f:
                                writer = csv.writer(f)
                                writer.writerow(user1)
                                writer.writerow(user2)
                                writer.writerow(user3)
                            
                        else:
                            user1 = [str(usernameEntry1.get()), str(ageEntry1.get()), str(country1.get()), str(gender1.get())]
                            user2 = [str(usernameEntry2.get()), str(ageEntry2.get()), str(country2.get()), str(gender2.get())]
                            user3 = [str(usernameEntry3.get()), str(ageEntry3.get()), str(country3.get()), str(gender3.get())]
                            user4 = [str(usernameEntry4.get()), str(ageEntry4.get()), str(country4.get()), str(gender4.get())]

                            with open('userdetails.csv','a') as f:
                                writer = csv.writer(f)
                                writer.writerow(user1)
                                writer.writerow(user2)
                                writer.writerow(user3)
                                writer.writerow(user4)
                        if response_take:
                            for player_index in range(0, int(numberPlayersText.get())):
                                self.total_people_play.append(player_index)
                            # print(self.total_people_play)
                            self.make_command()
                            top3.destroy()
                            top.destroy()
                        else:
                            messagebox.showerror("Input Error", "Please input number of players between 2 and 4")
                            # top3.destroy()
                            # top.destroy()
                            # self.take_initial_control()
                        top3.destroy()
                        top.destroy()
                        

                        Ludo.usernames.append(str(usernameEntry1.get()))
                        Ludo.usernames.append(str(usernameEntry2.get()))
                        Ludo.usernames.append(str(usernameEntry3.get()))
                        Ludo.usernames.append(str(usernameEntry4.get()))

                        Ludo.ages.append(str(ageEntry1.get()))
                        Ludo.ages.append(str(ageEntry2.get()))
                        Ludo.ages.append(str(ageEntry3.get()))
                        Ludo.ages.append(str(ageEntry4.get()))

                        Ludo.countries.append(str(country1.get()))
                        Ludo.countries.append(str(country2.get()))
                        Ludo.countries.append(str(country3.get()))
                        Ludo.countries.append(str(country4.get()))

                        Ludo.genders.append(str(gender1.get()))
                        Ludo.genders.append(str(gender2.get()))
                        Ludo.genders.append(str(gender3.get()))
                        Ludo.genders.append(str(gender4.get()))

            
             
                   
        def operate(ind, top2):
            top2.destroy()
            top1 = Toplevel(background="black")
            top1.grab_set()

            # top.overrideredirect(True)
            x, y = Ludo.centerWindow(800, 650, top1)
            top1.geometry(f"800x650+{x}+{y}")
            top1.title("LudoKing")
            path="Images/screen3.png" 
            image = img= (Image.open(path))
            resized_image= image.resize((800,650), Image.ANTIALIAS)
            new_image= ImageTk.PhotoImage(resized_image)
            label = tk.Label(top1, image = new_image, compound=tk.CENTER, bg="black", width=800, height=650).pack()
            BACK_BUTTON = Button(top1, text="BACK TO HOME",font=("Papyrus",30,"italic"), fg="black", bg="#ade374",   borderwidth=0, command=lambda: Ludo.go_back(top1) )
            BACK_BUTTON.place(x=250, y=100) 
            if ind:
                self.robo_prem = 1
                for player_index in range(2):
                    self.total_people_play.append(player_index)
                print(self.total_people_play)
                def delay_with_instrctions(time_is):
                    if place_ins['text'] != "":
                        place_ins.place_forget()
                    if command_play['text'] != "":
                        command_play.place_forget()
                
                    place_ins['text'] = f"Your game will start within {time_is} sec"
                    place_ins.place(x=150, y=200)

                    if time_is > 4:
                        command_play['text'] = f"Machine Play With Red and You Play With Sky Blue"
                    elif time_is> 1 and time_is<=4:
                        command_play['text'] = f"You Will Get the First Chance to play"
                    else: 
                        None
                        # command_play['text'] = f"Enjoy this Game"
                    command_play.place(x=150, y=400)

                time_is = 5
                place_ins = Label(top1, text="", font=("Papyrus", 30, "italic"), fg="#fc4176", bg="black")
                command_play = Label(top1, text="", font=("Papyrus", 20, "italic"), fg="#af7439", bg="black")

                try:
                    while time_is:
                        delay_with_instrctions(time_is)
                        time_is-=1
                        self.window.update()
                        time.sleep(1)
                    top.destroy()
                    top1.destroy()

                except:
                    print("Force Stop Error in Operate")
                self.block_value_predict[1][1]['state'] = NORMAL
            else:
                submit_btn['state'] = NORMAL
                take_entry['state'] = NORMAL

            top.mainloop()

    # Get block value after prediction based on probability
    def make_prediction(self,color_indicator):
        try:
            if color_indicator == "#fc4176":
                block_value_predict = self.block_value_predict[0]
                if self.robo_prem and self.count_robo_stage_from_start < 3:
                    self.count_robo_stage_from_start += 1
                if self.robo_prem and self.count_robo_stage_from_start == 3 and self.six_counter < 2:
                    permanent_block_number = self.move_red_counter = 6
                    self.count_robo_stage_from_start += 1
                else:    
                    permanent_block_number = self.move_red_counter = randint(1, 6)

            elif color_indicator == "#74c0e3":
                block_value_predict = self.block_value_predict[1]
                permanent_block_number = self.move_sky_blue_counter = randint(1, 6)
                if self.robo_prem and permanent_block_number == 6:
                    for coin_loc in self.red_coin_position:
                        if coin_loc>=40 and coin_loc<=46:
                            permanent_block_number = self.move_sky_blue_counter = randint(1, 5)
                            break
                            
            elif color_indicator == "#fcb542":
                block_value_predict = self.block_value_predict[2]
                permanent_block_number = self.move_yellow_counter = randint(1, 6)

            else:
                block_value_predict = self.block_value_predict[3]
                permanent_block_number = self.move_green_counter = randint(1, 6)

            block_value_predict[1]['state'] = DISABLED

            # Illusion of coin floating
            temp_counter = 12
            while temp_counter>0:
                move_temp_counter = randint(1, 6)
                block_value_predict[0]['image'] = self.block_number_side[move_temp_counter - 1]
                self.window.update()
                time.sleep(0.1)
                temp_counter-=1

            print("Prediction result: ", permanent_block_number)

            # Permanent predicted value containing image set
            block_value_predict[0]['image'] = self.block_number_side[permanent_block_number-1]
            if self.robo_prem == 1 and color_indicator == "#fc4176":
                self.window.update()
                time.sleep(0.4)
            self.instructional_btn_customization_based_on_current_situation(color_indicator,permanent_block_number,block_value_predict)
        except:
            print("Force Stop Error in Prediction")
        
    #     # print("face ids")
    #     print(Ludo.dice_face)
    #     # print("toll idds")
        

    #     print(Ludo.roll_id)
    #     try:
    #         if color_indicator == "#fc4176":                
    #             block_value_predict = self.block_value_predict[0]
    #             # print("ello"+str(block_value_predict))
    #             if self.robo_prem and self.count_robo_stage_from_start < 3:
    #                 self.count_robo_stage_from_start += 1
    #             if self.robo_prem and self.count_robo_stage_from_start == 3 and self.six_counter < 2:
    #                 permanent_block_number = self.move_red_counter = 6
    #                 self.count_robo_stage_from_start += 1
    #             else:    
    #                 permanent_block_number = self.move_red_counter = randint(1, 6)
    #             if permanent_block_number == 6:
                    
    #                 self.make_prediction("#fc4176")       
    #             # else:
    #             #     if Ludo.tmp_red:
    #             #             self.main_controller("#fc4176",'4')         
    #             if permanent_block_number == 6:
    #                 self.make_prediction("#fc4176")
    #                 # a = Ludo.roll_id[-1]
    #                 # if a == 6:
    #                 #     Ludo.roll = Ludo.roll
    #                 #     Ludo.roll_id.append(Ludo.roll)
    #                 #     # Ludo.username_id.append(str(Ludo.usernames[0]))
    #                 #     Ludo.dice_face.append(permanent_block_number)
    #                     # Ludo.roll = Ludo.roll
    #                     # Ludo.roll_id.append(Ludo.roll)
    #                     # # Ludo.username_id.append(str(Ludo.usernames[0]))
    #                     # Ludo.dice_face.append(permanent_block_number)
    #                     # Ludo.roll = Ludo.roll-1
    #             else:
    #                 Ludo.roll = Ludo.roll+1
    #                 Ludo.roll_id.append(Ludo.roll)
    #                 # Ludo.username_id.append(str(Ludo.usernames[0]))
    #                 Ludo.dice_face.append(permanent_block_number)
                    
    #                 # print(str(Ludo.roll) + "red")
    #         elif color_indicator == "#74c0e3":
    #             block_value_predict = self.block_value_predict[1]
    #             permanent_block_number = self.move_sky_blue_counter = randint(1, 6)
    #             if permanent_block_number == 6:
    #                 # a = randint(1,4)
    #                 # Ludo.tmp_blue.append(a)
    #                 # if a == 1:
    #                 #     self.main_controller("#74c0e3",'1')
    #                 # elif a == 2:
    #                 #     self.main_controller("#74c0e3",'2')
    #                 # elif a == 3:
    #                 #     self.main_controller("#74c0e3",'3')
    #                 # elif a == 4:
    #                 #     self.main_controller("#74c0e3",'4')  
    #                 self.make_prediction("#74c0e3")            
    #             # else:
    #                 # self.make_prediction("#74c0e3") 
    #                 # pass
    #                 #  if Ludo.tmp_blue:
    #                     # a = int(random.choice(Ludo.tmp_blue))
    #                     # if a == 1:
    #                     #     self.main_controller("#74c0e3",'1')
    #                     # elif a == 2:
    #                     #     self.main_controller("#74c0e3",'2')
    #                     # elif a == 3:
    #                     #     self.main_controller("#74c0e3",'3')
    #                     # elif a == 4:
    #                     #     self.main_controller("#74c0e3",'4')    
    #             # Ludo.roll_id.append(Ludo.roll)
    #             # Ludo.username_id.append(str(Ludo.usernames[1]))
    #             Ludo.dice_face.append(permanent_block_number)
    #             # print(*Ludo.roll_id, sep = "\n")
    #             if self.robo_prem and permanent_block_number == 6:
    #                 for coin_loc in self.red_coin_position:
    #                     if coin_loc>=40 and coin_loc<=46:
    #                         permanent_block_number = self.move_sky_blue_counter = randint(1, 5)                        
    #                         break
                            
    #         elif color_indicator == "#fcb542":
    #             block_value_predict = self.block_value_predict[2]
    #             permanent_block_number = self.move_yellow_counter = randint(1, 6)
    #             if permanent_block_number == 6:
    #                 # self.make_prediction("#fcb542")
    #                 # a = randint(1,4)
    #                 # Ludo.tmp_yellow.append(a)
    #                 # if a == 1:
    #                 #     self.main_controller("#fcb542",'1')
    #                 # elif a == 2:
    #                 #     self.main_controller("#fcb542",'2')
    #                 # elif a == 3:
    #                 #     self.main_controller("#fcb542",'3')
    #                 # elif a == 4:
    #                 #     self.main_controller("#fcb542",'4') 
    #                 self.make_prediction("#fcb542")             
    #             else:
    #                 pass
    #                 # if Ludo.tmp_yellow:
    #                     # a = int(random.choice(Ludo.tmp_yellow))
    #                     # if a == 1:
    #                     #     self.main_controller("#fcb542",'1')
    #                     # elif a == 2:
    #                     #     self.main_controller("#fcb542",'2')
    #                     # elif a == 3:
    #                     #     self.main_controller("#fcb542",'3')
    #                     # elif a == 4:
    #                 # self.main_controller("#fcb542",'4')    
    #             Ludo.roll_id.append(Ludo.roll)
    #             Ludo.username_id.append(str(Ludo.usernames[2]))
    #             Ludo.dice_face.append(permanent_block_number)

    #         elif color_indicator == "#ade374":
    #             block_value_predict = self.block_value_predict[3]
    #             permanent_block_number = self.move_green_counter = randint(1, 6)
    #             if permanent_block_number == 6:
    #                 # a = randint(1,4)
    #                 # Ludo.tmp_green.append(a)
    #                 # if a == 1:
    #                 #     self.main_controller("#ade374",'1')
    #                 # elif a == 2:
    #                 #     self.main_controller("#ade374",'2')
    #                 # elif a == 3:
    #                 #     self.main_controller("#ade374",'3')
    #                 # elif a == 4:
    #                 #     self.main_controller("#ade374",'4')  
    #                 self.make_prediction("#ade374")            
    #             else:
    #                 pass
    #                 # if Ludo.tmp_green:
    #                     # a = int(random.choice(Ludo.tmp_green))
    #                     # if a == 1:
    #                     #     self.main_controller("#ade374",'1')
    #                     # elif a == 2:
    #                     #     self.main_controller("#ade374",'2')
    #                     # elif a == 3:
    #                     #     self.main_controller("#ade374",'3')
    #                     # elif a == 4:
    #                     #     self.main_controller("#ade374",'4')    
    #             Ludo.roll_id.append(Ludo.roll)
    #             Ludo.username_id.append(str(Ludo.usernames[3]))
    #             Ludo.dice_face.append(permanent_block_number)

    #         block_value_predict[1]['state'] = DISABLED

    #         # Illusion of coin floating
    #         temp_counter = 12
    #         while temp_counter>0:
    #             move_temp_counter = randint(1, 6)
    #             block_value_predict[0]['image'] = self.block_number_side[move_temp_counter - 1]
    #             self.window.update()
    #             time.sleep(0.0001)
    #             temp_counter-=1

    #         # print("P / .rediction result: ", permanent_block_number)
    #         # Ludo.dice_face.append(permanent_block_number)
    #         # df['username']

    #         # Permanent predicted value containing image set
    #         block_value_predict[0]['image'] = self.block_number_side[permanent_block_number-1]
    #         if self.robo_prem == 1 and color_indicator == "#fc4176":
    #             self.window.update()
    #             time.sleep(0.4)
    #         self.instructional_btn_customization_based_on_current_situation(color_indicator,permanent_block_number,block_value_predict)
    #     except Exception:
    #             traceback.print_exc()
    #         # print("Force Stop Error in Prediction")
    # # Get block value after prediction based on probability
    def make_prediction_sim(self,color_indicator):
        # print("face ids")
        print(Ludo.dice_face)
        # print("toll idds")
        

        print(Ludo.roll_id)
        try:
            if color_indicator == "#fc4176":                
                block_value_predict = self.block_value_predict[0]
                # print("ello"+str(block_value_predict))
                if self.robo_prem and self.count_robo_stage_from_start < 3:
                    self.count_robo_stage_from_start += 1
                if self.robo_prem and self.count_robo_stage_from_start == 3 and self.six_counter < 2:
                    permanent_block_number = self.move_red_counter = 6
                    self.count_robo_stage_from_start += 1
                else:    
                    permanent_block_number = self.move_red_counter = randint(1, 6)
                if permanent_block_number == 6:
                    a = randint(1,4)
                    Ludo.tmp_red.append(a)
                    print(a)
                    if a == 1:
                        self.main_controller("#fc4176",'1')
                    elif a == 2:
                        self.main_controller("#fc4176",'2')
                    elif a == 3:
                        self.main_controller("#fc4176",'3')
                    elif a == 4:
                        self.main_controller("#fc4176",'4')  
                    self.make_prediction("#fc4176")       
                else:
                    if Ludo.tmp_red:
                        a = int(random.choice(Ludo.tmp_red))
                        if a == 1:
                            self.main_controller("#fc4176",'1')
                        elif a == 2:
                            self.main_controller("#fc4176",'2')
                        elif a == 3:
                            self.main_controller("#fc4176",'3')
                        elif a == 4:
                            self.main_controller("#fc4176",'4')         
                if permanent_block_number == 6:
                    # self.make_prediction("#fc4176")
                    a = Ludo.roll_id[-1]
                    if a == 6:
                        Ludo.roll = Ludo.roll
                        Ludo.roll_id.append(Ludo.roll)
                        # Ludo.username_id.append(str(Ludo.usernames[0]))
                        Ludo.dice_face.append(permanent_block_number)
                    else:
                        Ludo.roll = Ludo.roll
                        Ludo.roll_id.append(Ludo.roll)
                        # Ludo.username_id.append(str(Ludo.usernames[0]))
                        Ludo.dice_face.append(permanent_block_number)
                        # Ludo.roll = Ludo.roll-1
                else:
                    Ludo.roll = Ludo.roll+1
                    Ludo.roll_id.append(Ludo.roll)
                    # Ludo.username_id.append(str(Ludo.usernames[0]))
                    Ludo.dice_face.append(permanent_block_number)
                    
                    # print(str(Ludo.roll) + "red")
            elif color_indicator == "#74c0e3":
                block_value_predict = self.block_value_predict[1]
                permanent_block_number = self.move_sky_blue_counter = randint(1, 6)
                if permanent_block_number == 6:
                    a = randint(1,4)
                    Ludo.tmp_blue.append(a)
                    if a == 1:
                        self.main_controller("#74c0e3",'1')
                    elif a == 2:
                        self.main_controller("#74c0e3",'2')
                    elif a == 3:
                        self.main_controller("#74c0e3",'3')
                    elif a == 4:
                        self.main_controller("#74c0e3",'4')  
                    self.make_prediction("#74c0e3")            
                else:
                     if Ludo.tmp_blue:
                        a = int(random.choice(Ludo.tmp_blue))
                        if a == 1:
                            self.main_controller("#74c0e3",'1')
                        elif a == 2:
                            self.main_controller("#74c0e3",'2')
                        elif a == 3:
                            self.main_controller("#74c0e3",'3')
                        elif a == 4:
                            self.main_controller("#74c0e3",'4')    
                Ludo.roll_id.append(Ludo.roll)
                Ludo.username_id.append(str(Ludo.usernames[1]))
                Ludo.dice_face.append(permanent_block_number)
                # print(*Ludo.roll_id, sep = "\n")
                if self.robo_prem and permanent_block_number == 6:
                    for coin_loc in self.red_coin_position:
                        if coin_loc>=40 and coin_loc<=46:
                            permanent_block_number = self.move_sky_blue_counter = randint(1, 5)                        
                            break
                            
            elif color_indicator == "#fcb542":
                block_value_predict = self.block_value_predict[2]
                permanent_block_number = self.move_yellow_counter = randint(1, 6)
                if permanent_block_number == 6:
                    # self.make_prediction("#fcb542")
                    a = randint(1,4)
                    Ludo.tmp_yellow.append(a)
                    if a == 1:
                        self.main_controller("#fcb542",'1')
                    elif a == 2:
                        self.main_controller("#fcb542",'2')
                    elif a == 3:
                        self.main_controller("#fcb542",'3')
                    elif a == 4:
                        self.main_controller("#fcb542",'4') 
                    self.make_prediction("#fcb542")             
                else:
                     if Ludo.tmp_yellow:
                        a = int(random.choice(Ludo.tmp_yellow))
                        if a == 1:
                            self.main_controller("#fcb542",'1')
                        elif a == 2:
                            self.main_controller("#fcb542",'2')
                        elif a == 3:
                            self.main_controller("#fcb542",'3')
                        elif a == 4:
                            self.main_controller("#fcb542",'4')    
                Ludo.roll_id.append(Ludo.roll)
                Ludo.username_id.append(str(Ludo.usernames[2]))
                Ludo.dice_face.append(permanent_block_number)

            elif color_indicator == "#ade374":
                block_value_predict = self.block_value_predict[3]
                permanent_block_number = self.move_green_counter = randint(1, 6)
                if permanent_block_number == 6:
                    a = randint(1,4)
                    Ludo.tmp_green.append(a)
                    if a == 1:
                        self.main_controller("#ade374",'1')
                    elif a == 2:
                        self.main_controller("#ade374",'2')
                    elif a == 3:
                        self.main_controller("#ade374",'3')
                    elif a == 4:
                        self.main_controller("#ade374",'4')  
                    self.make_prediction("#ade374")            
                else:
                    if Ludo.tmp_green:
                        a = int(random.choice(Ludo.tmp_green))
                        if a == 1:
                            self.main_controller("#ade374",'1')
                        elif a == 2:
                            self.main_controller("#ade374",'2')
                        elif a == 3:
                            self.main_controller("#ade374",'3')
                        elif a == 4:
                            self.main_controller("#ade374",'4')    
                Ludo.roll_id.append(Ludo.roll)
                Ludo.username_id.append(str(Ludo.usernames[3]))
                Ludo.dice_face.append(permanent_block_number)

            block_value_predict[1]['state'] = DISABLED

            # Illusion of coin floating
            temp_counter = 12
            while temp_counter>0:
                move_temp_counter = randint(1, 6)
                block_value_predict[0]['image'] = self.block_number_side[move_temp_counter - 1]
                self.window.update()
                time.sleep(0.0001)
                temp_counter-=1

            # print("P / .rediction result: ", permanent_block_number)
            # Ludo.dice_face.append(permanent_block_number)
            # df['username']

            # Permanent predicted value containing image set
            block_value_predict[0]['image'] = self.block_number_side[permanent_block_number-1]
            if self.robo_prem == 1 and color_indicator == "#fc4176":
                self.window.update()
                time.sleep(0.4)
            self.instructional_btn_customization_based_on_current_situation(color_indicator,permanent_block_number,block_value_predict)
        except Exception:
                traceback.print_exc()
            # print("Force Stop Error in Prediction")
        
    def instructional_btn_customization_based_on_current_situation(self,color_indicator,permanent_block_number,block_value_predict):
        robo_operator = None
        if color_indicator == "#fc4176":
            temp_coin_position = self.red_coin_position
        elif color_indicator == "#ade374":
            temp_coin_position = self.green_coin_position
        elif color_indicator == "#fcb542":
            temp_coin_position = self.yellow_coin_position
        else:
            temp_coin_position = self.sky_blue_coin_position

        all_in = 1
        for i in range(4):
            if temp_coin_position[i] == -1:
                all_in = 1
            else:
                all_in = 0
                break

        if  permanent_block_number == 6:
            self.six_counter += 1
        else:
            self.six_counter = 0

        if ((all_in == 1 and permanent_block_number == 6) or (all_in==0)) and self.six_counter<3:
            permission = 1
            if color_indicator == "#fc4176":
                temp = self.red_coord_store
            elif color_indicator == "#ade374":
                temp = self.green_coord_store
            elif color_indicator == "#fcb542":
                temp = self.yellow_coord_store
            else:
                temp = self.sky_blue_coord_store

            if  permanent_block_number<6:
                if self.six_with_overlap == 1:
                    self.time_for-=1
                    self.six_with_overlap=0
                for i in range(4):
                    if  temp[i] == -1:
                        permission=0
                    elif temp[i]>100:
                        if  temp[i]+permanent_block_number<=106:
                            permission=1
                            break
                        else:
                            permission=0
                    else:
                        permission=1
                        break
            else:
                for i in range(4):
                    if  temp[i]>100:
                        if  temp[i] + permanent_block_number <= 106:
                            permission = 1
                            break
                        else:
                            permission = 0
                    else:
                        permission = 1
                        break
            if permission == 0:
                self.make_command(None)
            else:
                self.num_btns_state_controller(block_value_predict[2])

                if self.robo_prem == 1 and block_value_predict == self.block_value_predict[0]:
                    robo_operator = "give"
                block_value_predict[1]['state'] = DISABLED# Predict btn deactivation

        else:
            block_value_predict[1]['state'] = NORMAL# Predict btn activation
            if self.six_with_overlap == 1:
                self.time_for -= 1
                self.six_with_overlap = 0
            self.make_command()

        if  permanent_block_number == 6 and self.six_counter<3 and block_value_predict[2][0]['state'] == NORMAL:
            self.time_for-=1
        else:
            self.six_counter=0

        if self.robo_prem == 1 and robo_operator:
            self.robo_judge(robo_operator)
            
    # Player Scope controller
    def make_command(self, robo_operator=None):
        if  self.time_for == -1:
            pass
        else:
            self.block_value_predict[self.total_people_play[self.time_for]][1]['state'] = DISABLED
        if  self.time_for == len(self.total_people_play)-1:
            self.time_for = -1

        self.time_for+=1
        self.block_value_predict[self.total_people_play[self.time_for]][1]['state'] = NORMAL
        
        if self.robo_prem==1 and self.time_for == 0:
            robo_operator = "predict"
        if robo_operator:
            self.robo_judge(robo_operator)


    def instruction_btn_red(self):
        block_predict_red = Label(self.make_canvas,image=self.block_number_side[0])
        block_predict_red.place(x=30,y=15)
        predict_red = Button(self.make_canvas, height= 20, width=50, bg="#fc4176", fg="black", relief=RAISED, bd=1, text="Roll",font=("Papyrus", 10, "bold"), command=lambda: self.make_prediction("#fc4176"))
        predict_red.place(x=20, y=15 + 50)
        global red_btn_1
        global red_btn_2
        global red_btn_3
        global red_btn_4
        red_btn_1 = Button(self.make_canvas,height= 20, width=20, bg="#fc4176",fg="black",text="1",font=("Papyrus",13,"bold"), relief=RAISED, bd=1,command=lambda: self.main_controller("#fc4176",'1'), state=DISABLED, disabledforeground="black")
        red_btn_1.place(x=20,y=15+100)
        red_btn_2 = Button(self.make_canvas,height= 20, width=20, bg="#fc4176",fg="black",text="2",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#fc4176",'2'), state=DISABLED, disabledforeground="black")
        red_btn_2.place(x=50,y=15+100)
        red_btn_3 = Button(self.make_canvas,height= 20, width=20, bg="#fc4176",fg="black",text="3",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#fc4176",'3'), state=DISABLED, disabledforeground="black")
        red_btn_3.place(x=20,y=15+100+40)
        red_btn_4 = Button(self.make_canvas,height= 20, width=20, bg="#fc4176",fg="black",text="4",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#fc4176",'4'), state=DISABLED, disabledforeground="black")
        red_btn_4.place(x=50,y=15+100+40)

        Label(self.make_canvas,text=" Player 1",bg="black",fg="#fc4176",font=("Papyrus",15)).place(x=15,y=15+140+50)
        self.store_instructional_btn(block_predict_red,predict_red,[red_btn_1,red_btn_2,red_btn_3,red_btn_4])

    def instruction_btn_sky_blue(self):
        block_predict_sky_blue = Label(self.make_canvas, image=self.block_number_side[0])
        block_predict_sky_blue.place(x=30, y=15+(40*6+40*3)+10)
        predict_sky_blue = Button(self.make_canvas, height= 20, width=50, bg="#74c0e3", fg="black", relief=RAISED, bd=1, text="Roll",font=("Papyrus", 10, "bold"), command=lambda: self.make_prediction("#74c0e3"))
        predict_sky_blue.place(x=20, y=15+(40*6+40*3)+40 + 20)

        global blue_btn_1
        global blue_btn_2
        global blue_btn_3
        global blue_btn_4

        blue_btn_1 = Button(self.make_canvas,height= 20, width=20, bg="#74c0e3",fg="black",text="1",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#74c0e3",'1'), state=DISABLED, disabledforeground="black")
        blue_btn_1.place(x=20,y=15+(40*6+40*3)+40 + 70)
        blue_btn_2 = Button(self.make_canvas,height= 20, width=20, bg="#74c0e3",fg="black",text="2",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#74c0e3",'2'), state=DISABLED, disabledforeground="black")
        blue_btn_2.place(x=60,y=15+(40*6+40*3)+40 + 70)
        blue_btn_3 = Button(self.make_canvas,height= 20, width=20, bg="#74c0e3",fg="black",text="3",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#74c0e3",'3'), state=DISABLED, disabledforeground="black")
        blue_btn_3.place(x=20,y=15+(40*6+40*3)+40 + 70+ 40)
        blue_btn_4 = Button(self.make_canvas,height= 20, width=20, bg="#74c0e3",fg="black",text="4",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#74c0e3",'4'), state=DISABLED, disabledforeground="black")
        blue_btn_4.place(x=60,y=15+(40*6+40*3)+40 + 70+ 40)

        Label(self.make_canvas, text="Player 2", bg="black", fg="#74c0e3", font=("Papyrus", 15, "bold")).place(x=12,y=15+(40*6+40*3)+40 + 110+50)
        self.store_instructional_btn(block_predict_sky_blue, predict_sky_blue, [blue_btn_1,blue_btn_2,blue_btn_3,blue_btn_4])

    def instruction_btn_yellow(self):

        global yellow_btn_1
        global yellow_btn_2
        global yellow_btn_3
        global yellow_btn_4

        
        block_predict_yellow = Label(self.make_canvas, image=self.block_number_side[0])
        block_predict_yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 10)+20, y=15 + (40 * 6 + 40 * 3) + 10)
        predict_yellow = Button(self.make_canvas, height= 20, width=50, bg="#fcb542", fg="black", relief=RAISED, bd=1, text="Roll",font=("Papyrus", 10, "bold"), command=lambda: self.make_prediction("#fcb542"))
        predict_yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+20, y=15 + (40 * 6 + 40 * 3) + 40 + 20)
        
        yellow_btn_1 = Button(self.make_canvas,height= 20, width=20, bg="#fcb542",fg="black",text="1",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#fcb542",'1'), state=DISABLED, disabledforeground="black")
        yellow_btn_1.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15, y=15 + (40 * 6 + 40 * 3) + 40 + 70)
        yellow_btn_2 = Button(self.make_canvas,height= 20, width=20, bg="#fcb542",fg="black",text="2",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#fcb542",'2'), state=DISABLED, disabledforeground="black")
        yellow_btn_2.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15 + 40, y=15 + (40 * 6 + 40 * 3) + 40 + 70)
        yellow_btn_3 = Button(self.make_canvas,height= 20, width=20, bg="#fcb542",fg="black",text="3",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#fcb542",'3'), state=DISABLED, disabledforeground="black")
        yellow_btn_3.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15, y=15 + (40 * 6 + 40 * 3) + 40 + 70+ 40)
        yellow_btn_4 = Button(self.make_canvas,height= 20, width=20, bg="#fcb542",fg="black",text="4",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#fcb542",'4'), state=DISABLED, disabledforeground="black")
        yellow_btn_4.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15 + 40, y=15 + (40 * 6 + 40 * 3) + 40 + 70+ 40)
        
        Label(self.make_canvas, text="Player 3", bg="black", fg="#fcb542", font=("Papyrus", 15, "bold")).place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 +7),y=15+(40*6+40*3)+40 + 110+50)
        self.store_instructional_btn(block_predict_yellow, predict_yellow, [yellow_btn_1,yellow_btn_2,yellow_btn_3,yellow_btn_4])

    def instruction_btn_green(self):

        global green_btn_1
        global green_btn_2
        global green_btn_3
        global green_btn_4
        block_predict_green = Label(self.make_canvas, image=self.block_number_side[0])
        block_predict_green.place(x=100+(40*6+40*3+40*6+10)+20, y=15)
        predict_green = Button(self.make_canvas, height= 20, width=50, bg="#ade374", fg="black", relief=RAISED, bd=1, text="Roll", font=("Papyrus", 10, "bold"), command=lambda: self.make_prediction("#ade374"))
        predict_green.place(x=100+(40*6+40*3+40*6+2)+20, y=15 + 50)
        
        green_btn_1 = Button(self.make_canvas,height= 20, width=20, bg="#ade374",fg="black",text="1",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#ade374",'1'), state=DISABLED, disabledforeground="black")
        green_btn_1.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15,y=15+100)
        green_btn_2 = Button(self.make_canvas,height= 20, width=20, bg="#ade374",fg="black",text="2",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#ade374",'2'), state=DISABLED, disabledforeground="black")
        green_btn_2.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15 + 40,y=15+100)
        green_btn_3 = Button(self.make_canvas,height= 20, width=20, bg="#ade374",fg="black",text="3",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#ade374",'3'), state=DISABLED, disabledforeground="black")
        green_btn_3.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15,y=15+100+40)
        green_btn_4 = Button(self.make_canvas,height= 20, width=20, bg="#ade374",fg="black",text="4",font=("Papyrus",13,"bold"),relief=RAISED,bd=1,command=lambda: self.main_controller("#ade374",'4'), state=DISABLED, disabledforeground="black")
        green_btn_4.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15 + 40,y=15+100+40)
        
        Label(self.make_canvas, text="Player 4", bg="black", fg="#ade374", font=("Papyrus", 15, "bold")).place(x=100+(40*6+40*3+40*6+7), y=15+140+50)
        self.store_instructional_btn(block_predict_green, predict_green, [green_btn_1,green_btn_2,green_btn_3,green_btn_4])

    def store_instructional_btn(self, block_indicator, predictor, entry_controller):
        temp = []
        temp.append(block_indicator)
        temp.append(predictor)
        temp.append(entry_controller)
        self.block_value_predict.append(temp)

    def red_circle_start_position(self, coin_number):
        self.make_canvas.delete(self.made_red_coin[int(coin_number)-1])
        self.made_red_coin[int(coin_number)-1] = self.make_canvas.create_oval(100 + 40, 15+(40*6), 100 +40 + 40, 15+(40*6)+40, fill="#fc4176", width=3, outline="black")

        self.red_number_label[int(coin_number)-1].place_forget()
        red_start_label_x = 100 + 40 + 10
        red_start_label_y = 15 + (40 * 6) + 5
        self.red_number_label[int(coin_number)-1].place(x=red_start_label_x, y=red_start_label_y)

        self.red_coin_position[int(coin_number)-1] = 1
        self.window.update()
        time.sleep(0.2)

    def green_circle_start_position(self,coin_number):
        self.make_canvas.delete(self.made_green_coin[int(coin_number)-1])
        self.made_green_coin[int(coin_number)-1] = self.make_canvas.create_oval(100 + (40*8), 15 + 40, 100 +(40*9), 15 + 40+ 40, fill="#ade374", width=3)

        self.green_number_label[int(coin_number)-1].place_forget()
        green_start_label_x = 100 + (40*8) + 10
        green_start_label_y = 15 + 40 + 5
        self.green_number_label[int(coin_number)-1].place(x=green_start_label_x, y=green_start_label_y)

        self.green_coin_position[int(coin_number)-1] = 14
        self.window.update()
        time.sleep(0.2)

    def yellow_circle_start_position(self,coin_number):
        self.make_canvas.delete(self.made_yellow_coin[int(coin_number)-1])
        self.made_yellow_coin[int(coin_number)-1] = self.make_canvas.create_oval(100 + (40 * 6)+(40*3)+(40*4), 15 + (40*8), 100 + (40 * 6)+(40*3)+(40*5), 15 + (40*9), fill="#fcb542", width=3)

        self.yellow_number_label[int(coin_number)-1].place_forget()
        yellow_start_label_x = 100 + (40 * 6)+(40*3)+(40*4) + 10
        yellow_start_label_y = 15 + (40*8) + 5
        self.yellow_number_label[int(coin_number) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

        self.yellow_coin_position[int(coin_number) - 1] = 27
        self.window.update()
        time.sleep(0.2)

    def sky_blue_circle_start_position(self,coin_number):
        self.make_canvas.delete(self.made_sky_blue_coin[int(coin_number)-1])
        self.made_sky_blue_coin[int(coin_number)-1] = self.make_canvas.create_oval(100+240,340+(40*5)-5,100+240+40,340+(40*6)-5,fill="#74c0e3",width=3)

        self.sky_blue_number_label[int(coin_number)-1].place_forget()
        sky_blue_start_label_x = 100+240 + 10
        sky_blue_start_label_y = 340+(40*5)-5 + 5
        self.sky_blue_number_label[int(coin_number) - 1].place(x=sky_blue_start_label_x, y=sky_blue_start_label_y)

        self.sky_blue_coin_position[int(coin_number) - 1] = 40
        self.window.update()
        time.sleep(0.2)

    def num_btns_state_controller(self, take_nums_btns_list, state_control = 1):
        if state_control:
            for num_btn in take_nums_btns_list:
                num_btn['state'] = NORMAL
        else:
            for num_btn in take_nums_btns_list:
                num_btn['state'] = DISABLED

    def main_controller(self, color_coin, coin_number):
        robo_operator = None

        if  color_coin == "#fc4176":
            print("user killed")
            print(Ludo.user_killed_count)

            self.num_btns_state_controller(self.block_value_predict[0][2], 0)

            if self.move_red_counter == 106:
                messagebox.showwarning("Destination reached","Reached at the destination")

            elif self.red_coin_position[int(coin_number)-1] == -1 and self.move_red_counter == 6:
                self.red_circle_start_position(coin_number)
                self.red_coord_store[int(coin_number) - 1] = 1

            elif self.red_coin_position[int(coin_number)-1] > -1:
                take_coord = self.make_canvas.coords(self.made_red_coin[int(coin_number)-1])
                red_start_label_x = take_coord[0] + 10
                red_start_label_y = take_coord[1] + 5
                self.red_number_label[int(coin_number) - 1].place(x=red_start_label_x, y=red_start_label_y)

                if self.red_coin_position[int(coin_number)-1]+self.move_red_counter<=106:
                    self.red_coin_position[int(coin_number)-1] = self.motion_of_coin(self.red_coin_position[int(coin_number) - 1],self.made_red_coin[int(coin_number)-1],self.red_number_label[int(coin_number)-1],red_start_label_x,red_start_label_y,"#fc4176",self.move_red_counter) 
                    if self.robo_prem and self.red_coin_position[int(coin_number)-1] == 106 and color_coin == "#fc4176":
                        self.robo_store.remove(int(coin_number))
                        print("After removing: ", self.robo_store)

                else:
                    if not self.robo_prem: 
                        pass
                            # messagebox.showerror("Not possible","Sorry, not permitted")
                    self.num_btns_state_controller(self.block_value_predict[0][2])

                    if self.robo_prem:
                        robo_operator = "give"
                        self.robo_judge(robo_operator)
                    return

                if  self.red_coin_position[int(coin_number)-1]==22 or self.red_coin_position[int(coin_number)-1]==9 or self.red_coin_position[int(coin_number)-1]==48 or self.red_coin_position[int(coin_number)-1]==35 or self.red_coin_position[int(coin_number)-1]==14 or self.red_coin_position[int(coin_number)-1]==27 or self.red_coin_position[int(coin_number)-1]==40 or self.red_coin_position[int(coin_number)-1]==1:
                    pass
                else:
                    if self.red_coin_position[int(coin_number) - 1] < 100:
                        self.coord_overlap(self.red_coin_position[int(coin_number)-1],color_coin, self.move_red_counter)
                        

                self.red_coord_store[int(coin_number)-1] = self.red_coin_position[int(coin_number)-1]

            else:
                # messagebox.showerror("Wrong choice","Sorry, Your coin in not permitted to travel")
                self.num_btns_state_controller(self.block_value_predict[0][2])

                if self.robo_prem == 1:
                    robo_operator = "give"
                    self.robo_judge(robo_operator)
                return

            self.block_value_predict[0][1]['state'] = NORMAL


        elif color_coin == "#ade374":
            self.num_btns_state_controller(self.block_value_predict[3][2], 0)

            if self.move_green_counter == 106:
                pass
                # messagebox.showwarning("Destination reached","Reached at the destination")

            elif self.green_coin_position[int(coin_number) - 1] == -1 and self.move_green_counter == 6:
                self.green_circle_start_position(coin_number)
                self.green_coord_store[int(coin_number) - 1] = 14

            elif self.green_coin_position[int(coin_number) - 1] > -1:
                take_coord = self.make_canvas.coords(self.made_green_coin[int(coin_number) - 1])
                green_start_label_x = take_coord[0] + 10
                green_start_label_y = take_coord[1] + 5
                self.green_number_label[int(coin_number) - 1].place(x=green_start_label_x, y=green_start_label_y)


                if  self.green_coin_position[int(coin_number) - 1] + self.move_green_counter <= 106:
                    self.green_coin_position[int(coin_number) - 1] = self.motion_of_coin(self.green_coin_position[int(coin_number) - 1], self.made_green_coin[int(coin_number) - 1], self.green_number_label[int(coin_number) - 1], green_start_label_x, green_start_label_y, "green", self.move_green_counter)
                else:
                #    messagebox.showerror("Not possible","No path available")
                   self.num_btns_state_controller(self.block_value_predict[3][2])
                   return


                if  self.green_coin_position[int(coin_number)-1]==22 or self.green_coin_position[int(coin_number)-1]==9 or self.green_coin_position[int(coin_number)-1]==48 or self.green_coin_position[int(coin_number)-1]==35 or self.green_coin_position[int(coin_number)-1]==1 or self.green_coin_position[int(coin_number)-1]==27 or self.green_coin_position[int(coin_number)-1]==40 or self.green_coin_position[int(coin_number)-1]==14:
                    pass
                else:
                    if self.green_coin_position[int(coin_number) - 1] < 100:
                        self.coord_overlap(self.green_coin_position[int(coin_number) - 1],color_coin, self.move_green_counter)

                self.green_coord_store[int(coin_number) - 1] = self.green_coin_position[int(coin_number) - 1]

            else:
                # messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                self.num_btns_state_controller(self.block_value_predict[3][2])
                return

            self.block_value_predict[3][1]['state'] = NORMAL

        elif color_coin == "#fcb542":
            
            self.num_btns_state_controller(self.block_value_predict[2][2], 0)

            if self.move_yellow_counter == 106:
                pass
                # messagebox.showwarning("Destination reached","Reached at the destination")

            elif self.yellow_coin_position[int(coin_number) - 1] == -1 and self.move_yellow_counter == 6:
                self.yellow_circle_start_position(coin_number)
                self.yellow_coord_store[int(coin_number) - 1] = 27

            elif self.yellow_coin_position[int(coin_number) - 1] > -1:
                take_coord = self.make_canvas.coords(self.made_yellow_coin[int(coin_number) - 1])
                yellow_start_label_x = take_coord[0] + 10
                yellow_start_label_y = take_coord[1] + 5
                self.yellow_number_label[int(coin_number) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

                if  self.yellow_coin_position[int(coin_number) - 1] + self.move_yellow_counter <= 106:
                    self.yellow_coin_position[int(coin_number) - 1] = self.motion_of_coin(self.yellow_coin_position[int(coin_number) - 1], self.made_yellow_coin[int(coin_number) - 1], self.yellow_number_label[int(coin_number) - 1], yellow_start_label_x, yellow_start_label_y, "#fcb542", self.move_yellow_counter)
                else:
                #    messagebox.showerror("Not possible","No path available")
                   
                   self.num_btns_state_controller(self.block_value_predict[2][2])
                   return

                if  self.yellow_coin_position[int(coin_number)-1]==22 or self.yellow_coin_position[int(coin_number)-1]==9 or self.yellow_coin_position[int(coin_number)-1]==48 or self.yellow_coin_position[int(coin_number)-1]==35 or self.yellow_coin_position[int(coin_number)-1]==1 or self.yellow_coin_position[int(coin_number)-1]==14 or self.yellow_coin_position[int(coin_number)-1]==40 or self.yellow_coin_position[int(coin_number)-1]==27:
                    pass
                else:
                    if self.yellow_coin_position[int(coin_number) - 1] < 100:
                        self.coord_overlap(self.yellow_coin_position[int(coin_number) - 1],color_coin, self.move_yellow_counter)

                self.yellow_coord_store[int(coin_number) - 1] = self.yellow_coin_position[int(coin_number) - 1]

            else:
                # messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                self.num_btns_state_controller(self.block_value_predict[2][2])
                return

            self.block_value_predict[2][1]['state'] = NORMAL

 
        elif color_coin == "#74c0e3":
            self.num_btns_state_controller(self.block_value_predict[1][2], 0)   

            if self.move_red_counter == 106:
                pass
                # messagebox.showwarning("Destination reached","Reached at the destination")

            elif self.sky_blue_coin_position[int(coin_number) - 1] == -1 and self.move_sky_blue_counter == 6:
                self.sky_blue_circle_start_position(coin_number)
                self.sky_blue_coord_store[int(coin_number) - 1] = 40

            elif self.sky_blue_coin_position[int(coin_number) - 1] > -1:
                take_coord = self.make_canvas.coords(self.made_sky_blue_coin[int(coin_number) - 1])
                sky_blue_start_label_x = take_coord[0] + 10
                sky_blue_start_label_y = take_coord[1] + 5
                self.sky_blue_number_label[int(coin_number) - 1].place(x=sky_blue_start_label_x, y=sky_blue_start_label_y)

                if  self.sky_blue_coin_position[int(coin_number) - 1] + self.move_sky_blue_counter <= 106:
                    self.sky_blue_coin_position[int(coin_number) - 1] = self.motion_of_coin(self.sky_blue_coin_position[int(coin_number) - 1], self.made_sky_blue_coin[int(coin_number) - 1], self.sky_blue_number_label[int(coin_number) - 1], sky_blue_start_label_x, sky_blue_start_label_y, "#74c0e3", self.move_sky_blue_counter)
                else:
                #    messagebox.showerror("Not possible","No path available")
                   
                   self.num_btns_state_controller(self.block_value_predict[1][2])
                   return

                if  self.sky_blue_coin_position[int(coin_number)-1]==22 or self.sky_blue_coin_position[int(coin_number)-1]==9 or self.sky_blue_coin_position[int(coin_number)-1]==48 or self.sky_blue_coin_position[int(coin_number)-1]==35 or self.sky_blue_coin_position[int(coin_number)-1]==1 or self.sky_blue_coin_position[int(coin_number)-1]==14 or self.sky_blue_coin_position[int(coin_number)-1]==27 or self.sky_blue_coin_position[int(coin_number)-1]==40:
                    pass
                else:
                    if self.sky_blue_coin_position[int(coin_number) - 1] < 100:
                        self.coord_overlap(self.sky_blue_coin_position[int(coin_number) - 1],color_coin, self.move_sky_blue_counter)

                self.sky_blue_coord_store[int(coin_number) - 1] = self.sky_blue_coin_position[int(coin_number) - 1]

            else:
                # messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                self.num_btns_state_controller(self.block_value_predict[1][2])
                return

            self.block_value_predict[1][1]['state'] = NORMAL

        print(self.red_coord_store)
        print(self.green_coord_store)
        print(self.yellow_coord_store)
        print(self.sky_blue_coord_store)
        if self.robo_prem == 1:
            print("Robo Store is: ", self.robo_store)
        
        permission_granted_to_proceed = True

        if  color_coin == "#fc4176" and self.red_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif  color_coin == "#ade374" and self.green_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif  color_coin == "#fcb542" and self.yellow_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif  color_coin == "#74c0e3" and self.sky_blue_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)

        if permission_granted_to_proceed:# if that is False, Game is over and not proceed more
            self.make_command(robo_operator)

    def motion_of_coin(self,counter_coin,specific_coin,number_label,number_label_x ,number_label_y,color_coin,path_counter):
        try:
            number_label.place(x=number_label_x,y=number_label_y)
            while True:
                if path_counter == 0:
                    break
                elif (counter_coin == 51 and color_coin == "#fc4176") or (counter_coin==12 and color_coin == "#ade374") or (counter_coin == 25 and color_coin == "#fcb542") or (counter_coin == 38 and color_coin == "#74c0e3") or counter_coin>=100:
                    if counter_coin<100:
                        counter_coin=100

                    counter_coin = self.under_room_traversal_control(specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin, color_coin)

                    if  counter_coin == 106:
                        
                        if self.robo_prem == 1 and color_coin == "#fc4176":
                            pass
                            # messagebox.showinfo("Destination reached","Hey! I am at the destination")
                        else:
                            pass
                            # messagebox.showinfo("Destination reached","Congrats! You now at the destination")
                        if path_counter == 6:
                            self.six_with_overlap = 1
                        else:
                            self.time_for -= 1
                    break

                counter_coin += 1
                path_counter -=1
                number_label.place_forget()

                # print(counter_coin)

                if counter_coin<=5:
                    self.make_canvas.move(specific_coin, 40, 0)
                    number_label_x+=40
                elif counter_coin == 6:
                    self.make_canvas.move(specific_coin, 40, -40)
                    number_label_x += 40
                    number_label_y-=40
                elif 6< counter_coin <=11:
                    self.make_canvas.move(specific_coin, 0, -40)
                    number_label_y -= 40
                elif counter_coin <=13:
                    self.make_canvas.move(specific_coin, 40, 0)
                    number_label_x += 40
                elif counter_coin <=18:
                    self.make_canvas.move(specific_coin, 0, 40)
                    number_label_y += 40
                elif counter_coin == 19:
                    self.make_canvas.move(specific_coin, 40, 40)
                    number_label_x += 40
                    number_label_y += 40
                elif counter_coin <=24:
                    self.make_canvas.move(specific_coin, 40, 0)
                    number_label_x += 40
                elif counter_coin <=26:
                    self.make_canvas.move(specific_coin, 0, 40)
                    number_label_y += 40
                elif counter_coin <=31:
                    self.make_canvas.move(specific_coin, -40, 0)
                    number_label_x -= 40
                elif counter_coin == 32:
                    self.make_canvas.move(specific_coin, -40, 40)
                    number_label_x -= 40
                    number_label_y += 40
                elif counter_coin <= 37:
                    self.make_canvas.move(specific_coin, 0, 40)
                    number_label_y += 40
                elif counter_coin <= 39:
                    self.make_canvas.move(specific_coin, -40, 0)
                    number_label_x -= 40
                elif counter_coin <= 44:
                    self.make_canvas.move(specific_coin, 0, -40)
                    number_label_y -= 40
                elif counter_coin == 45:
                    self.make_canvas.move(specific_coin, -40, -40)
                    number_label_x -= 40
                    number_label_y -= 40
                elif counter_coin <= 50:
                    self.make_canvas.move(specific_coin, -40, 0)
                    number_label_x -= 40
                elif 50< counter_coin <=52:
                    self.make_canvas.move(specific_coin, 0, -40)
                    number_label_y -= 40
                elif counter_coin == 53:
                    self.make_canvas.move(specific_coin, 40, 0)
                    number_label_x += 40
                    counter_coin = 1

                number_label.place_forget()
                number_label.place(x=number_label_x, y=number_label_y)

                self.window.update()
                time.sleep(0.2)

            return counter_coin
        except:
            print("Force Stop Error Came in motion of coin")

    # For same position, previous coin deleted and set to the room
    def coord_overlap(self, counter_coin, color_coin, path_to_traverse_before_overlap):
        if  color_coin!="#fc4176":
            Ludo.user_killed = 0 
            
            for take_coin_number in range(len(self.red_coord_store)):
                if  self.red_coord_store[take_coin_number] == counter_coin:
                    Ludo.user_killed = Ludo.user_killed+1
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap=1
                    else:
                        self.time_for-=1

                    self.make_canvas.delete(self.made_red_coin[take_coin_number])
                    self.red_number_label[take_coin_number].place_forget()
                    self.red_coin_position[take_coin_number] = -1
                    self.red_coord_store[take_coin_number] = -1
                    if self.robo_prem == 1:
                        self.robo_store.remove(take_coin_number+1)
                        if self.red_coin_position.count(-1)>=1:
                            self.count_robo_stage_from_start = 2

                    if take_coin_number == 0:
                       remade_coin = self.make_canvas.create_oval(100+40, 15+40, 100+40+40, 15+40+40, width=3, fill="#fc4176", outline="black")
                       self.red_number_label[take_coin_number].place(x=100 + 40 + 10, y=15 + 40 + 5)
                    elif take_coin_number == 1:
                        remade_coin = self.make_canvas.create_oval(100+40+60+60, 15 + 40, 100+40+60+60+40, 15 + 40 + 40, width=3, fill="#fc4176", outline="black")
                        self.red_number_label[take_coin_number].place(x=100 + 40 + 60 +60 + 10, y=15 + 40 + 5)
                    elif take_coin_number == 2:
                        remade_coin = self.make_canvas.create_oval(100 + 40 + 60 + 60, 15 + 40 + 100, 100 + 40 + 60 + 60 + 40, 15 + 40 + 40 + 100, width=3, fill="#fc4176", outline="black")
                        self.red_number_label[take_coin_number].place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 100 + 5)
                    else:
                        remade_coin = self.make_canvas.create_oval(100 + 40, 15 + 40+100, 100 + 40 + 40, 15 + 40 + 40+100, width=3,fill="#fc4176", outline="black")
                        self.red_number_label[take_coin_number].place(x=100 + 40 + 10, y=15 + 40 + 100 + 5)

                    self.made_red_coin[take_coin_number]=remade_coin
        Ludo.user_killed_count.append(Ludo.user_killed)

        if  color_coin != "#ade374":
            Ludo.user_killed = 0 
            for take_coin_number in range(len(self.green_coord_store)):
                if  self.green_coord_store[take_coin_number] == counter_coin:
                    Ludo.user_killed = Ludo.user_killed+1
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap = 1
                    else:
                        self.time_for-=1

                    self.make_canvas.delete(self.made_green_coin[take_coin_number])
                    self.green_number_label[take_coin_number].place_forget()
                    self.green_coin_position[take_coin_number] = -1
                    self.green_coord_store[take_coin_number] = -1


                    if take_coin_number == 0:
                        remade_coin = self.make_canvas.create_oval(340+(40*3)+40, 15 + 40, 340+(40*3)+40 + 40, 15 + 40 + 40, width=3, fill="#ade374", outline="black")
                        self.green_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 5)
                    elif take_coin_number == 1:
                        remade_coin = self.make_canvas.create_oval(340+(40*3)+40+ 60 + 40+20, 15 + 40, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40, width=3, fill="#ade374", outline="black")
                        self.green_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 5)
                    elif take_coin_number == 2:
                        remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40 + 100, 340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 15 + 40 + 40 + 100, width=3, fill="#ade374", outline="black")
                        self.green_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 100 + 5)
                    else:
                        remade_coin = self.make_canvas.create_oval(340+(40*3)+40, 15 + 40 + 100, 340+(40*3)+40 + 40, 15 + 40 + 40 + 100, width=3, fill="#ade374", outline="black")
                        self.green_number_label[take_coin_number].place(x=340+(40*3) + 40 + 10, y=15 + 40 + 100 + 5)

                    self.made_green_coin[take_coin_number] = remade_coin
        Ludo.user_killed_count.append(Ludo.user_killed)


        if  color_coin != "#fcb542":
            Ludo.user_killed = 0 
            for take_coin_number in range(len(self.yellow_coord_store)):
                if  self.yellow_coord_store[take_coin_number] == counter_coin:
                    Ludo.user_killed = Ludo.user_killed+1
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap = 1
                    else:
                        self.time_for -= 1

                    self.make_canvas.delete(self.made_yellow_coin[take_coin_number])
                    self.yellow_number_label[take_coin_number].place_forget()
                    self.yellow_coin_position[take_coin_number] = -1
                    self.yellow_coord_store[take_coin_number] = -1

                    if take_coin_number == 0:
                        remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 340+80+15, 340 + (40 * 3) + 40 + 40, 340+80+40+15, width=3, fill="#fcb542", outline="black")
                        self.yellow_number_label[take_coin_number].place(x=340+(40*3) + 40 + 10, y=30 + (40*6)+(40*3)+40+10)
                    elif take_coin_number == 1:
                        remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340+80+15, 340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="#fcb542", outline="black")
                        self.yellow_number_label[take_coin_number].place(x=340+(40*3)+ 40 + 40+ 60 + 30, y=30 + (40*6)+(40*3)+40+10)
                    elif take_coin_number == 2:
                        remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15, 340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15, width=3, fill="#fcb542", outline="black")
                        self.yellow_number_label[take_coin_number].place(x=340+(40*3)+ 40 + 40+ 60 + 30, y=30 + (40*6)+(40*3)+40+100+10)
                    else:
                        remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 340+80+60+40+15, 340 + (40 * 3) + 40 + 40,340+80+60+40+40+15, width=3, fill="#fcb542", outline="black")
                        self.yellow_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)

                    self.made_yellow_coin[take_coin_number] = remade_coin
        Ludo.user_killed_count.append(Ludo.user_killed)

        if  color_coin != "#74c0e3":
            Ludo.user_killed = 0 
            for take_coin_number in range(len(self.sky_blue_coord_store)):
                if  self.sky_blue_coord_store[take_coin_number] == counter_coin:
                    Ludo.user_killed = Ludo.user_killed+1
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap = 1
                    else:
                        self.time_for -= 1

                    self.make_canvas.delete(self.made_sky_blue_coin[take_coin_number])
                    self.sky_blue_number_label[take_coin_number].place_forget()
                    self.sky_blue_coin_position[take_coin_number] = -1
                    self.sky_blue_coord_store[take_coin_number]=-1

                    if take_coin_number == 0:
                        remade_coin = self.make_canvas.create_oval(100 + 40, 340+80+15, 100 + 40 + 40, 340+80+40+15, width=3, fill="#74c0e3", outline="black")
                        self.sky_blue_number_label[take_coin_number].place(x=100+40+10, y=30 + (40*6)+(40*3)+40+10)
                    elif take_coin_number == 1:
                        remade_coin = self.make_canvas.create_oval(100 + 40 + 60 + 40+20, 340+80+15, 100 + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="#74c0e3", outline="black")
                        self.sky_blue_number_label[take_coin_number].place(x=100 + 40 + 60 +60 + 10, y=30 + (40*6)+(40*3)+40+10)
                    elif take_coin_number == 2:
                        remade_coin = self.make_canvas.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15, 100 + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15, width=3, fill="#74c0e3", outline="black")
                        self.sky_blue_number_label[take_coin_number].place(x=100 + 40 + 60 + 60 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 60 + 40 + 10)
                    else:
                        remade_coin = self.make_canvas.create_oval( 100 + 40, 340+80+60+40+15, 100 + 40 + 40, 340+80+60+40+40+15, width=3, fill="#74c0e3", outline="black")
                        self.sky_blue_number_label[take_coin_number].place(x=100+40+10, y=30 + (40*6)+(40*3)+40+60+40+10)

                    self.made_sky_blue_coin[take_coin_number] = remade_coin
        Ludo.user_killed_count.append(Ludo.user_killed)

    def under_room_traversal_control(self,specific_coin,number_label,number_label_x,number_label_y,path_counter,counter_coin,color_coin):
        if color_coin == "#fc4176" and counter_coin >= 100:
            if int(counter_coin)+int(path_counter)<=106:
               counter_coin = self.room_red_traversal(specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin)

        elif color_coin == "#ade374" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.room_green_traversal(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        elif color_coin == "#fcb542" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.room_yellow_traversal(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        elif color_coin == "#74c0e3" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.room_sky_blue_traversal(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        return counter_coin


    def room_red_traversal(self, specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin):
        while path_counter>0:
            counter_coin += 1
            path_counter -= 1
            self.make_canvas.move(specific_coin, 40, 0)
            number_label_x+=40
            number_label.place(x=number_label_x,y=number_label_y)
            self.window.update()
            time.sleep(0.2)
        return counter_coin

    def room_green_traversal(self, specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.make_canvas.move(specific_coin, 0, 40)
            number_label_y += 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.window.update()
            time.sleep(0.2)
        return counter_coin

    def room_yellow_traversal(self, specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.make_canvas.move(specific_coin, -40, 0)
            number_label_x -= 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.window.update()
            time.sleep(0.2)
        return counter_coin

    def room_sky_blue_traversal(self, specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.make_canvas.move(specific_coin, 0, -40)
            number_label_y -= 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.window.update()
            time.sleep(0.2)
        return counter_coin

    def check_winner_and_runner(self,color_coin):
        global destination_reached
        destination_reached = 0 # Check for all specific color coins
        if color_coin == "#fc4176":
            temp_store = self.red_coord_store
            temp_delete = 0# Player index
        elif color_coin == "#ade374":
            temp_store = self.green_coord_store
            temp_delete = 3# Player index
        elif color_coin == "#fcb542":
            temp_store = self.yellow_coord_store
            temp_delete = 2# Player index
        else:
            temp_store = self.sky_blue_coord_store
            temp_delete = 1# Player index

        for take in temp_store:
            if take == 106:
                destination_reached = 1
            else:
                destination_reached = 0
                break

        if  destination_reached == 1:# If all coins in block reach to the destination, winner and runner check
            Ludo.gameover = 0
            self.take_permission += 1
            if self.take_permission == 1:# Winner check
                if color_coin == "#fc4176":
                    Ludo.winner = Ludo.usernames[0]
                elif color_coin == "#ade374":
                    Ludo.winner = Ludo.usernames[3]
                elif color_coin == "#fcb542":
                    Ludo.winner = Ludo.usernames[2]
                elif color_coin == "#74c0e3":
                    Ludo.winner = Ludo.usernames[1]
                
                Ludo.game_id = [Ludo.game_id] * len(Ludo.roll_id)
                df = pd.read_csv("stats1.csv")
                os.remove("stats1.csv")
                username = list(df['username'])
                roll_id = list(df['roll_id'])
                dice_face = list(df['dice_face'])
                game_id = list(df['game_id'])
                killed = list(df['killed'])
                a = list(Ludo.username_id)
                b = list(Ludo.roll_id)
                c = list(Ludo.dice_face)
                d = list(Ludo.game_id)
                e = list(Ludo.user_killed_count)
                username.append(a)
                roll_id.append(b)
                dice_face.append(c)
                game_id.append(d)
                killed.append(e)
                data = {'username': username,
                        'roll_id': roll_id,
                        'dice_face': dice_face,
                        'game_id': game_id,
                        'killed': killed}
                
                df1 = pd.DataFrame(data)
                # df1['username'] = username
                # df1['roll_id'] = roll_id
                # df1['dice_face'] = dice_face
                # df1['game_id'] = game_id
                # df1['killed'] = killed
                df1.to_csv("stats1.csv")
            

                if self.robo_prem == 1 and color_coin == "#fc4176":
                    messagebox.showinfo("Winner", "Hurrah! I am the winner")
                else:
                    # messagebox.showinfo("Winner","Congrats! You are the winner")
                    Ludo.gameover = 0
                    window.destroy()
            elif self.take_permission == 2:# 1st runner check
                if color_coin == "#fc4176":
                    Ludo.first_runner_up = Ludo.usernames[0]
                elif color_coin == "#ade374":
                    Ludo.first_runner_up = Ludo.usernames[3]
                elif color_coin == "#fcb542":
                    Ludo.first_runner_up = Ludo.usernames[2]
                elif color_coin == "#74c0e3":
                    Ludo.first_runner_up = Ludo.usernames[1]

                
                if self.robo_prem == 1 and color_coin == "#fc4176":
                    messagebox.showinfo("Winner", "Hurrah! I am 1st runner")
                else:
                    pass
                    # messagebox.showinfo("Winner", "Wow! You are 1st runner")
            elif self.take_permission == 3:# 2nd runner check
                if self.robo_prem == 1 and color_coin == "#fc4176":
                    messagebox.showinfo("Result", "I am 2nd runner....Not bad at all")
                else:
                    messagebox.showinfo("Result", "You are 2nd runner....Better Luck next time")

            self.block_value_predict[temp_delete][1]['state'] = DISABLED
            self.total_people_play.remove(temp_delete)

            if len(self.total_people_play) == 1:
                Ludo.gameover = 0
                messagebox.showinfo("Game Over","Good bye!!!!")
                window.destroy()

                self.block_value_predict[0][1]['state'] = DISABLED
                return False
            else:
                self.time_for-=1
            
        else:
            print("Winner not decided")

        return True

    def robo_judge(self, ind="give"):
        if ind == "give":# For give the value
            all_in = 1# Denoting all the coins are present in the room
            for i in range(4):
                if self.red_coin_position[i] == -1:
                    all_in = 1
                else:
                    all_in = 0# Denoting all the coins not present in the room
                    break
            
            if all_in == 1:# All coins are present in room
                if self.move_red_counter == 6:
                    predicted_coin = choice([1,2,3,4])
                    self.robo_store.append(predicted_coin)
                    self.main_controller("#fc4176", predicted_coin)
                else:
                    pass
            else:# All coins not present in room
                temp = self.red_coin_position# Take red coin position reference
                take_ref = self.sky_blue_coin_position# Take sky_blue coin position reference
                
                if len(self.robo_store) == 1:# When only one coin is outside of the room
                    if self.move_red_counter<6:# When prediction less than 6
                        if (self.count_robo_stage_from_start>3) and (temp[self.robo_store[0]-1] >=33 and temp[self.robo_store[0]-1]<=38):
                            self.count_robo_stage_from_start = 2
                        self.main_controller("#fc4176", self.robo_store[0]) 
                    else:# When prediction is 6
                        forward_perm = 0# Controlling process to be forward or not
                        for coin in take_ref:# coin is sky_blue individual coin distance
                            if coin>-1 and coin<101:
                                if (coin != 40 or coin != 35 or coin != 27 or coin != 22 or coin != 14 or coin != 9 or coin !=1 or coin !=48) and coin-temp[self.robo_store[0]-1] >= 6 and coin-temp[self.robo_store[0]-1] <= 12:
                                    forward_perm = 1
                                    break
                                else:
                                    forward_perm = 0
                            else:
                                forward_perm = 0

                        if forward_perm == 0:# Not forward the process
                            store = [1,2,3,4]
                            store.remove(self.robo_store[0])
                            predicted_coin = choice(store)
                            self.robo_store.append(predicted_coin)
                            self.main_controller("#fc4176", predicted_coin)
                        else:# Forward the entire process
                            self.main_controller("#fc4176", self.robo_store[0])
                else:
                    def normal_movement_according_condition():
                        # This portion is for checking if current location + predicted value <= 106 or not.....Coin Filtering
                        normal_movement = 1# Normal Movement of the entite coin
                        
                        for coin in self.robo_store:# coin is coin number
                            if temp[coin-1]+self.move_red_counter <= 106:# For all coins having predicted location <=106
                                pass
                            else:
                                normal_movement = 0
                                break

                        if normal_movement:
                            temp_robo_store = [coin for coin in self.robo_store]
                        else:
                            temp_robo_store = [coin for coin in self.robo_store if temp[coin-1]+self.move_red_counter <= 106]

                        # This portion is for coin filtering under some constrains
                        for coin in temp_robo_store:# coin is coin number
                            if len(temp_robo_store)>1 and temp[coin-1]<101: # See Diagram under help to unserstand to understand the location                            
                                if (temp[coin-1] in take_ref) and (temp[coin-1] != 1 or temp[coin-1] != 9 or temp[coin-1] != 14 or temp[coin-1] != 22 or temp[coin-1] != 27 or temp[coin-1] != 35 or temp[coin-1] != 40 or temp[coin-1] != 48):
                                    temp_robo_store.remove(coin)
                                elif temp[coin-1]<=39 and temp[coin-1]+self.move_red_counter>39:                                    
                                    for loc_coin_other in take_ref:
                                        if (loc_coin_other>=40 and loc_coin_other<=46) and (temp[coin-1]+self.move_red_counter>loc_coin_other):
                                            temp_robo_store.remove(coin)
                                            break

                        # Overlapp checking with predicted value to eliminate other coin
                        process_forward = 1
                        for coin in temp_robo_store:
                            if temp[coin-1]+self.move_red_counter in take_ref:
                                process_forward = 0
                                self.main_controller("#fc4176", coin)
                                break
                        
                        # Not a single overlapp found so now self rescue or safe forward
                        if process_forward:
                            take_len = len(temp_robo_store)
                            store = {}
                            if take_ref:
                                for robo in temp_robo_store:#  robo is coin number
                                    for coin_other in take_ref:# coin_other is sky_blue coin location
                                        if coin_other>-1 and coin_other<100:
                                            if take_len>1 and (temp[robo-1]>38 and coin_other<=38) or ((temp[robo-1] == 9 or temp[robo-1] == 14 or temp[robo-1] == 27 or temp[robo-1] == 35 or temp[robo-1] == 40 or temp[robo-1] == 48 or temp[robo-1] == 22) and (coin_other<=temp[robo-1] or (coin_other>temp[robo-1] and coin_other<=temp[robo-1]+3))):  # avoid case to store
                                                take_len-=1
                                            else:
                                                store[temp[robo-1]-coin_other] = (robo, take_ref.index(coin_other)+1)# Store coin number
                            
                            # positive_distance = robo front          negative_distance = robo_behind
                            if store:
                                store_positive_dis = {}
                                store_negative_dis = {}
                                take_max = 0
                                take_min = 0
                                
                                try:
                                    store_positive_dis = dict((k,v) for k,v in store.items() if k>0)
                                    take_min = min(store_positive_dis.items())
                                except:
                                    pass
                                try:
                                    store_negative_dis = dict((k,v) for k,v in store.items() if k<0)
                                    take_max = max(store_negative_dis.items())
                                except:
                                    pass
                                
                                # Positive forward checking
                                work_comp_in_pos = 0
                                take_len = len(store_positive_dis)
                                index_from_last = -1

                                while take_len:
                                    if take_min and take_min[0] <= 6:
                        
                                        work_comp_in_pos = 1
                                        self.main_controller("#fc4176", take_min[1][0])
                                        break
                                    else:
                                        index_from_last -= 1
                                        try:
                                            take_min = min(sorted(store_positive_dis.items())[index_from_last])
                                        except:
                                            break
                                    take_len -= 1


                                # Negative forward checking
                                work_comp_in_neg = 0
                                if not work_comp_in_pos:
                                    take_len = len(store_negative_dis)
                                    index_from_last = len(store_negative_dis)-1
                                    while take_len:
                                        if take_max and temp[take_max[1][0]-1] + self.move_red_counter <= take_ref[take_max[1][1]-1]:
                                            work_comp_in_neg = 1
                                            self.main_controller("#fc4176", take_max[1][0])
                                            break
                                        else:
                                            index_from_last -= 1
                                            try:
                                                take_max = max(sorted(store_negative_dis.items())[index_from_last])
                                            except:
                                                break
                                        take_len -= 1
                        
                                # Not operate in positive and negative distance method...So now cover it by closest distance to the destination
                                if not work_comp_in_neg and not work_comp_in_pos:
                                    close_to_dest = temp_robo_store[0]
                                    for coin_index in range(1,len(temp_robo_store)):
                                        if temp[temp_robo_store[coin_index]-1] > temp[close_to_dest-1]:
                                            close_to_dest = temp_robo_store[coin_index]
                        
                                    self.main_controller("#fc4176", close_to_dest)
                            else:# If store(Not find the location difference) is empty
                                close_to_dest = temp_robo_store[0]
                                for coin_index in range(1,len(temp_robo_store)):
                                    if temp[temp_robo_store[coin_index]-1] > temp[close_to_dest-1]:
                                        close_to_dest = temp_robo_store[coin_index]
                                self.main_controller("#fc4176", close_to_dest)
                        else:
                            pass
                        
                    # For multiple Coin control Giving
                    if self.move_red_counter<6:
                        normal_movement_according_condition()
                    else:
                        coin_proceed = 0
                        
                        for coin in self.robo_store:
                            if temp[coin-1] + self.move_red_counter in self.sky_blue_coin_position:
                                coin_proceed = coin
                                break

                        if not coin_proceed:
                            if -1 in self.red_coin_position:
                                # Coin out
                                temp_store = [1,2,3,4]
                                for coin in self.robo_store:
                                    temp_store.remove(coin)
                                take_pred = choice(temp_store)
                                self.robo_store.append(take_pred)
                                self.main_controller("#fc4176", take_pred)
                            else:
                                # coin proceed
                                normal_movement_according_condition()
                        else:
                            self.main_controller("#fc4176", coin_proceed)
        else:
            self.make_prediction("#fc4176")# Prediction Function Call


if __name__ == '__main__':
    start = time.time()
    window = Tk()
    window.geometry("800x650")
    window.maxsize(800,650)
    window.minsize(800,650)
    window.title("Master Ludo")
    x, y = Ludo.centerWindow(800, 650, window)
    window.geometry(f"800x650+{x}+{y}")
    window.iconbitmap("Images/ludo_icon.ico")
    window.withdraw()
 
    # SPLASH SCREEN CODE
    splash_screen = tk.Toplevel(background="white")
    splash_screen.overrideredirect(True)
    splash_screen.title("LudoKing")
    x, y = Ludo.centerWindow(1200, 800, window)
    splash_screen.geometry(f"1200x800+{x}+{y}")
    path="Images/ludo.jpg" 
    image = ImageTk.PhotoImage(file=path)
    label = tk.Label(splash_screen, image = image)
    label.pack()
    splash_screen.update()
    # MAIN WINDOW CODE + Other Processing
    time.sleep(0.1)
    
    # Start the event loop
    window.deiconify()
    splash_screen.destroy()
    block_six_side = ImageTk.PhotoImage(Image.open("Images/6_block.png").resize((33, 33), Image.ANTIALIAS))
    block_five_side = ImageTk.PhotoImage(Image.open("Images/5_block.png").resize((33, 33), Image.ANTIALIAS))
    block_four_side = ImageTk.PhotoImage(Image.open("Images/4_block.png").resize((33, 33), Image.ANTIALIAS))
    block_three_side = ImageTk.PhotoImage(Image.open("Images/3_block.png").resize((33, 33), Image.ANTIALIAS))
    block_two_side = ImageTk.PhotoImage(Image.open("Images/2_block.png").resize((33, 33), Image.ANTIALIAS))
    block_one_side = ImageTk.PhotoImage(Image.open("Images/1_block.png").resize((33, 33), Image.ANTIALIAS))
    Ludo(window,block_six_side,block_five_side,block_four_side,block_three_side,block_two_side,block_one_side)
    window.mainloop()
    stop = time.time()
    # numberPlayersText = numberPlayersText
    numberPlayersText = numPlayersSim
    fields = [str(Ludo.game_id_single),str(numberPlayersText), str(Ludo.winner), str(stop-start)]
    with open("gamestats_summary.csv", "a", newline='') as f:
        writer = csv.writer(f)
        f.write("\n")
        writer.writerow(fields)

    print("Time" + str(stop-start))