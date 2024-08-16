# RANDOM PASSWORD GENERATOR 
# SUVAJIT KARMAKAR 

# IMPORTING THE REQUIRED MODULES IN THE WORK DIRECTORY 
import os
import random
import string
import streamlit as st
import time
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError
from dotenv import load_dotenv

# LOADING THE .env FILE
load_dotenv()

# CONFIGURATION
st.set_page_config(
    page_title="PyGuard", 
    page_icon="🔒", 
)

# MESSAGE TIMER 
message_timer = st.empty()


# PyGuard DEFINITION FOR PASSWORD GENERATION
def PyGuard(minimum_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_characters_set = string.punctuation

    character = letters
    if numbers:
        character += digits

    if special_characters:
        character += special_characters_set

    # GENERATED PASSWORD
    password = ""

    # VALIDATIONS FOR PASSWORD 
    criteria = False
    contains_numbers = False
    contains_special_characters = False

    # 
    while not criteria or len(password) < minimum_length:
        new_generation = random.choice(character)
        password += new_generation

        # VALIDATIONS RECHECK
        if new_generation in digits:
            contains_numbers = True
        elif new_generation in special_characters_set:
            contains_special_characters = True

        criteria = True
        if numbers:
            criteria = contains_numbers
        if special_characters:
            criteria = criteria and contains_special_characters

    return password

# INITIALING THE STREAMLIT APPLICATION
st.title("PyGuard")

# PASSWORD CONFIGURATION USER INPUTS
minimum_length = st.number_input("MINIMUM LENGTH : ", min_value=3, value=8)
need_digits = st.selectbox("INCLUDE DIGITS ? ", ["Yes", "No"])
need_special_characters = st.selectbox("INCLUDE SPECIAL CHARACTERS ?", ["Yes", "No"])
app_name = st.text_input("APPLICATION/WEBSITE NAME : ")

# USER INPUTS BOOLEAN CONVERSION 
include_digits = need_digits == "Yes"
include_special_characters = need_special_characters == "Yes"

# GENERATED PASSWORD VARIABLE
generated_password = None

# BUTTON TO GENERATE PASSWORD
if st.button("GET YOUR PASSWORD"):

    generated_password = PyGuard(minimum_length, include_digits, include_special_characters)
    st.write("WHAT TO DO NEXT ?")
    st.code(generated_password)

    # DATABASE CONNECTION USING ENVIRONMENT VARIABLES
    mongo_uri = os.getenv("MONGODB_URI")
    db_name = os.getenv("MONGODB_DB_NAME")
    collection_name = os.getenv("MONGODB_COLLECTION_NAME")

    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # STORING DATA 
    password_data = {
        "password": generated_password,
        "application": app_name,
    }

    collection.insert_one(password_data)

    message_timer.success(f"YOUR PASSWORD HAS BEEN GENERATED SUCCESSFULLY")
    # TIMER
    time.sleep(1)
    message_timer.empty()

    message_timer.info("PASSWORD SAVED TO DATABASE SUCCESSFULLY !")

    # TIMER
    time.sleep(2)
    message_timer.empty()

