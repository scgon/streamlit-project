import streamlit as st
import random
import math
from datetime import datetime
import ephem

##############################

def clear_text():
    st.session_state["password"] = ""

def rule2(password):
    for i in password:
        if i.isdigit():
            return True
    return False

def rule3(password):
    for i in password:
        if i.isupper():
            return True
    return False

def rule4(password):
    for i in password:
        if not i.isalnum() and not i.isspace():
            return True
    return False

def rule5(password):
    total = 0
    for i in password:
        if i.isdigit():
            total += int(i)
    if total == 25:
        return True
    else:
        return False

def rule6(password):
    months = ["january", "february", "march", "april", "may", "june", "july",
              "august", "september", "october", "november", "december"]
    password_lower = password.lower()

    for i in months:
        if i in password_lower:
            return True
    return False

def rule7(password):
    roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    for i in password:
        if i.isupper():
            if i in roman_numerals:
                return True
    return False

def rule8(password):
    roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    roman_numerals_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 1

    for i in password:
        if i.isupper():
            if i in roman_numerals:
                total *= roman_numerals_dict[i]

    if total == 5000:
        return True
    else:
        return False

def rule9(password):
    list1 = ['banana', 'Banana', 'bananas', 'Bananas']

    for item in list1:
        if item in password:
            return True
    return False

def rule10(password, a, b):
    c = math.gcd(a, b)
    if str(c) in password:
        return True
    return False

def rule11(password):
    date = ephem.Date(datetime.today())
    moon = ephem.Moon()
    nnm = ephem.next_new_moon(date)
    pnm = ephem.previous_new_moon(date)
    lunation = (date - pnm) / (nnm - pnm)

    st.write(lunation)

    if lunation >= 0.05 and lunation < 0.22:
        actual_phase = ('waxing crescent')
    elif lunation >= 0.22 and lunation < 0.28:
        actual_phase = ('first quarter')
    elif lunation >= 0.28 and lunation < 0.47:
        actual_phase = ('waxing gibbous')
    elif lunation >= 0.47 and lunation < 0.53:
        actual_phase = ('full moon')
    elif lunation >= 0.53 and lunation < 0.72:
        actual_phase = ('waning gibbous')
    elif lunation >= 0.72 and lunation < 0.78:
        actual_phase = ('last quarter')
    elif lunation >= 0.78 and lunation < 0.97:
        actual_phase = ('waning crescent')
    else:
        actual_phase = ('new moon')

    moon_phases_emojis = {'new moon': '🌑', 'waxing crescent': '🌒', 'first quarter': '🌓', 'waxing gibbous': '🌔',
                          'full moon': '🌕', 'waning gibbous': ' 🌖', 'third quarter': '🌗', 'waning crescent': '🌘'}

    if moon_phases_emojis[actual_phase] in password:
        return True
    else:
        return False

def rule12(password):
    pass

def rule13(password):
    pass

def rule14(password):
    pass

def rule15(password):
    pass

def rule16(password):
    pass

def rule17(password):
    pass

def rule18(password):
    pass

def rule19(password):
    pass

def rule20(password):
    pass

##############################

st.title("The Password Game!")

password = st.text_input("Please choose a password!", key="password")

##############################

if 'rando' not in st.session_state:
    possible_numbers = [60, 72, 84, 90, 96, 99, 63]
    choice = random.randrange(0, 2)
    a = random.choice(possible_numbers)

    if choice == 0:
        b = random.randrange(10, 500, 2)
    else:
        b = random.randrange(12, 500, 3)
    st.session_state.rando = [a, b, str(a), str(b)]

if 'successes' not in st.session_state:
    st.session_state.successes = 0
    max = 0
else:
    max = st.session_state.successes

successes = 1

##############################

if st.sidebar.button('Reset', use_container_width=True, on_click=clear_text):
    password = ""
    del st.session_state.rando
    del st.session_state.successes
    max = 0

topSlot = st.empty()
slot35 = st.empty()
slot34 = st.empty()
slot33 = st.empty()
slot32 = st.empty()
slot31 = st.empty()
slot30 = st.empty()
slot29 = st.empty()
slot28 = st.empty()
slot27 = st.empty()
slot26 = st.empty()
slot25 = st.empty()
slot24 = st.empty()
slot23 = st.empty()
slot22 = st.empty()
slot21 = st.empty()
slot20 = st.empty()
slot19 = st.empty()
slot18 = st.empty()
slot17 = st.empty()
slot16 = st.empty()
slot15 = st.empty()
slot14 = st.empty()
slot13 = st.empty()
slot12 = st.empty()
slot11 = st.empty()
slot10 = st.empty()
slot9 = st.empty()
slot8 = st.empty()
slot7 = st.empty()
slot6 = st.empty()
slot5 = st.empty()
slot4 = st.empty()
slot3 = st.empty()
slot2 = st.empty()
slot1 = st.empty()

##############################

if len(password) >= 5:
    slot1.success("**Rule 1:**" + "  \n  " + "Your password contains at least 5 characters.")
    successes += 1
else:
    slot1.error("**Rule 1:** " + "  \n  " + "Your password must contain at least 5 characters.")
    successes = 0

if successes >= 2 or max >= 2:
    if rule2(password) == True:
        slot2.success("**Rule 2:** " + "  \n  " + "Your password contains a number.")
        successes += 1
    else:
        slot2.error("**Rule 2:** " + "  \n  " + "Your password must contain a number.")

if successes >= 3 or max >= 3:
    if rule3(password) == True:
        slot3.success("**Rule 3:** " + "  \n  " + "Your password contains an uppercase letter.")
        successes += 1
    else:
        slot3.error("**Rule 3:** " + "  \n  " + "Your password must contain an uppercase letter.")

if successes >= 4 or max >= 4:
    if rule4(password) == True:
        slot4.success("**Rule 4:** " + "  \n  " + "Your password contains a special character.")
        successes += 1
    else:
        slot4.error("**Rule 4:** " + "  \n  " + "Your password must contain a special character.")

if successes >= 5 or max >= 5:
    if rule5(password) == True:
        slot5.success("**Rule 5:** " + "  \n  " + "The digits in your password add up to 25.")
        successes += 1
    else:
        slot5.error("**Rule 5:** " + "  \n  " + "The digits in your password must add up to 25.")

if successes >= 6 or max >= 6:
    if rule6(password) == True:
        slot6.success("**Rule 6:** " + "  \n  " + "Your password contains a month of the year.")
        successes += 1
    else:
        slot6.error("**Rule 6:** " + "  \n  " + "Your password must contain a month of the year.")

if successes >= 7 or max >= 7:
    if rule7(password) == True:
        slot7.success("**Rule 7:** " + "  \n  " + "Your password contains a roman numeral.")
        successes += 1
    else:
        slot7.error("**Rule 7:** " + "  \n  " + "Your password must contain a roman numeral.")

if successes >= 8 or max >= 8:
    if rule8(password) == True:
        slot8.success("**Rule 8:** " + "  \n  " + "The roman numerals in your password multiply to 5000.")
        successes += 1
    else:
        slot8.error("**Rule 8:** " + "  \n  " + "The roman numerals in your password must multiply to 5000.")

if successes >= 9 or max >= 9:
    if rule9(password) == True:
        slot9.success("**Rule 9:** " + "  \n  " + "Your password contains the most popular fruit in the world.")
        successes += 1
    else:
        slot9.error("**Rule 9:** " + "  \n  " + "Your password must contain the most popular fruit in the world.")

if successes >= 10 or max >= 10:
    d = st.session_state.rando[2]
    e = st.session_state.rando[3]
    ax = st.session_state.rando[0]
    bx = st.session_state.rando[1]

    if rule10(password, ax, bx) == True:
        slot10.success("**Rule 10:** " + "  \n  " + "Your password contains the greatest "
                                                    "common factor of " + d + " and " + e + ".")
        successes += 1
    else:
        slot10.error("**Rule 10:** " + "  \n  " + "Your password must contain the greatest "
                                                  "common factor of " + d + " and " + e + ".")
if successes >= 11 or max >= 11:
    if rule11(password) == True:
        slot11.success("**Rule 11:** " + "  \n  " + "Your password contains the most popular fruit in the world.")
        successes += 1
    else:
        topSlot.warning("**The rest of the rules are a work-in-progress.**")
        # slot12.error("**Rule 11:** " + "  \n  " + "Your password must contain the most popular fruit in the world.")

if successes >= 12 or max >= 12:
    if rule12(password) == True:
        slot12.success("**Rule 12:** " + "  \n  " + "Your password contains the current phase of the moon as an emoji.")
        successes += 1
    else:
        slot12.error("**Rule 12:** " + "  \n  " + "Your password must contain the the current phase of the moon as an emoji.")



if successes >= 13 or max >= 13:
    if rule13(password) == True:
        slot13.success("**Rule 13:** " + "  \n  " + "Your password contains the most popular fruit in the world.")
        successes += 1
    else:
        slot13.error("**Rule 13:** " + "  \n  " + "Your password must contain the most popular fruit in the world.")

if successes >= 14 or max >= 14:
    if rule14(password) == True:
        slot9.success("**Rule 14:** " + "  \n  " + "Your password contains the most popular fruit in the world.")
        successes += 1
    else:
        slot9.error("**Rule 14:** " + "  \n  " + "Your password must contain the most popular fruit in the world.")

if successes >= 15 or max >= 15:
    if rule15(password) == True:
        slot15.success("**Rule 15:** " + "  \n  " + "Your password contains the most popular fruit in the world.")
        successes += 1
    else:
        slot15.error("**Rule 15:** " + "  \n  " + "Your password must contain the most popular fruit in the world.")

if successes >= 16 or max >= 16:
    if rule16(password) == True:
        slot16.success("**Rule 16:** " + "  \n  " + "Your password contains the most popular fruit in the world.")
        successes += 1
    else:
        slot16.error("**Rule 16:** " + "  \n  " + "Your password must contain the most popular fruit in the world.")

if successes >= 17 or max >= 17:
    if rule17(password) == True:
        slot17.success("**Rule 17:** " + "  \n  " + "Your password contains the most popular fruit in the world.")
        successes += 1
    else:
        slot17.error("**Rule 17:** " + "  \n  " + "Your password must contain the most popular fruit in the world.")

if successes >= 18 or max >= 18:
    if rule18(password) == True:
        slot18.success("**Rule 18:** " + "  \n  " + "Your password contains the most popular fruit in the world.")
        successes += 1
    else:
        slot18.error("**Rule 18:** " + "  \n  " + "Your password must contain the most popular fruit in the world.")

if successes >= 19 or max >= 19:
    if rule19(password) == True:
        slot19.success("**Rule 19:** " + "  \n  " + "Your password contains the most popular fruit in the world.")
        successes += 1
    else:
        slot19.error("**Rule 19:** " + "  \n  " + "Your password must contain the most popular fruit in the world.")

if successes >= 20 or max >= 20:
    if rule20(password) == True:
        slot20.success("**Rule 20:** " + "  \n  " + "Your password contains the most popular fruit in the world.")
        successes += 1
    else:
        slot20.error("**Rule 20:** " + "  \n  " + "Your password must contain the most popular fruit in the world.")

if 'successes' in st.session_state:
    if st.session_state.successes < successes:
        st.session_state.successes = successes