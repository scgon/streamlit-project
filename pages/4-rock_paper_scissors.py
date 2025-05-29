import streamlit as st
import random
import pandas as pd

def whoWins(player, computer):

    if player == computer:
        return "tie"

    elif player == "Rock":
        if computer == "Paper":
            return "You lose!"
        else:
            return "You win!"

    elif player == "Paper":
        if computer == "Scissors":
            return "You lose!"
        else:
            return "You win!"

    elif player == "Scissors":
        if computer == "Rock":
            return "You lose!"
        else:
            return "You win!"

    else:
        return "Invalid"

def clear():
    if 'rps' in st.session_state:
        st.session_state['temp'] = st.session_state['rps']
    st.session_state['rps'] = None


################################################

rpsSelect = ["Rock", "Paper", "Scissors"]

score = 0
comScore = 0
tied = 0
rDone = 0

data = [["Player", score], ["Computer", comScore], ["Tie", tied]]

if "score" not in st.session_state:
    score = 0

else:
    score = st.session_state["score"]

if "comScore" not in st.session_state:
    comScore = 0

else:
    comScore = st.session_state["comScore"]

################################################

st.title(":rainbow[Rock-Paper-Scissors!]")

place1 = st.empty()
place2 = st.empty()

if "done" in st.session_state:
    if st.session_state["done"] != "Infinite":
        rTotal = st.session_state["done"][8]

        if "rDone" in st.session_state:
            rDone = st.session_state["rDone"]

################################################

st.divider()

cols = st.columns(2)
slot1 = cols[0].empty()
slot2 = cols[1].empty()
slot3 = st.empty()

st.text(" ")

rps = st.selectbox("Rock, Paper, Scissors", ("Rock", "Paper", "Scissors"),
                   index=None, key="rps")


submit = st.button("Submit", use_container_width=True, key="submit", on_click=clear)

with st.sidebar:
    reset = st.button("Reset", use_container_width=True)

################################################

if submit:
    if "done" in st.session_state and st.session_state["done"] is not None:
        if "temp" in st.session_state and st.session_state["temp"] is not None:

            computerChoice = random.choice(rpsSelect)

            wins = whoWins(st.session_state["temp"], computerChoice)

            if wins == "You win!":
                score += 1
                rDone += 1
                colory = ":green"
                colorc = ":red"

            elif wins == "You lose!":
                comScore += 1
                rDone += 1
                colory = ":red"
                colorc = ":green"

            else:
                colory = ":blue"
                colorc = ":blue"
                tied += 1

                if st.session_state["done"] == "Infinite":
                    score += 1
                    comScore += 1
                    rDone += 1

            st.markdown("##### You selected: " + colory + "[" + st.session_state["temp"] + "]")
            st.markdown("##### The computer selected: " + colorc + "[" + computerChoice + "]")

            st.text(" ")

            if wins == "You win!":
                st.success("You win!")

            elif wins == "You lose!":
                st.error("You lose!")

            else:
                st.info("It's a tie!")

        else:
            st.error("Please select rock, paper, or scissors.")

    else:
        st.error("Please select a gamemode")

if reset:
    score = 0
    comScore = 0
    rDone = 0
    del st.session_state['comScore']
    del st.session_state['score']
    del st.session_state['rDone']
    del st.session_state['done']

################################################

slot1.markdown("#### :blue[Your score: " + str(score) + "]")
slot2.markdown("#### :green[Computer score: " + str(comScore) + "]")

if "done" in st.session_state:
    if st.session_state["done"] != "Infinite":
        slot3.markdown("#### :orange[Round: " + str(rDone) + "/" + str(rTotal) + "]")

if "done" not in st.session_state:

    gamemode = place1.selectbox("Gamemode", ("Best of 1", "Best of 3", "Best of 5", "Infinite"),
                                index=None, key="gamemode")
    gamemodesubmit = place2.button("Submit Gamemode", use_container_width=True, key="gamemodesubmit")


    if gamemodesubmit:
        place1.markdown("### :red[Gamemode: " + gamemode + "]")
        place2.empty()
        st.session_state["done"] = gamemode

else:
    place1.markdown("### :red[Gamemode: " + st.session_state['done'] + "]")
    place2.empty()

################################################

st.session_state['comScore'] = comScore
st.session_state['score'] = score
st.session_state['rDone'] = rDone

if "temp" in st.session_state:
    del st.session_state['temp']