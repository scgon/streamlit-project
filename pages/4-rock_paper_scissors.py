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

def resetIt():
    score = 0
    comScore = 0
    rDone = 0
    del st.session_state['comScore']
    del st.session_state['score']
    del st.session_state['rDone']
    del st.session_state['done']


################################################

rpsSelect = ["Rock", "Paper", "Scissors"]

score = 0
comScore = 0
tied = 0
rDone = 0
rTotal = 0
resetQ = False

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
        rTotal = int(rTotal)

        if "rDone" in st.session_state:
            rDone = st.session_state["rDone"]

################################################

st.divider()

cols = st.columns(3)
slot1 = cols[0].empty()
slot2 = cols[1].empty()
slot3 = cols[2].empty()
slot4 = cols[0].empty()

st.text(" ")

rps = st.selectbox("Rock, Paper, Scissors", ("Rock", "Paper", "Scissors"),
                   index=None, key="rps")


submit = st.button("Submit", use_container_width=True, key="submit", on_click=clear)

with st.sidebar:
    reset = st.button("Reset", use_container_width=True)

################################################

if submit:
    if rDone < rTotal or rTotal == 0:
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


                if score >= rTotal // 2 + 1:
                    st.success("You win the game!")
                    st.balloons()
                    st.toast("Starting new game")

                    resetQ = True

                elif comScore >= rTotal // 2 + 1:
                    st.error("Computer wins the game, you lose!")
                    st.toast("Starting new game")

                    resetQ = True

            else:
                st.error("Please select rock, paper, or scissors.")

        else:
            st.error("Please select a gamemode")
    else:
        st.error("Game is finished, please reset.")

if reset:
    score = 0
    comScore = 0
    rDone = 0
    del st.session_state['comScore']
    del st.session_state['score']
    del st.session_state['rDone']
    del st.session_state['done']

################################################

slot1.markdown("#### :green[Your score: " + str(score) + "]")
slot2.markdown("#### :red[Computer score: " + str(comScore) + "]")
slot3.markdown("#### :blue[Tied: " + str(tied) + "]")

if "done" in st.session_state:
    if st.session_state["done"] != "Infinite":
        slot3.markdown("#### :orange[Round: " + str(rDone) + "/" + str(rTotal) + "]")
    else:
        slot4.markdown("#### :violet[Round: " + str(score) + "]")
        slot3.markdown("#### :blue[Tied: " + str(tied) + "]")
else:
    slot4.markdown("#### :violet[Round: " + str(score) + "]")
    slot3.markdown("#### :blue[Tied: " + str(tied) + "]")

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

aCols = st.columns([0.6, 0.4])

scoreA = score
comScoreA = comScore

if "done" in st.session_state:
    if st.session_state["done"] == "Infinite":
        scoreA = score - tied
        comScoreA = comScore - tied

data = {"Player": ["Player", "Computer", "Tie"], "Score": [scoreA, comScoreA, tied]}

st.divider()

df = pd.DataFrame(data)

st.session_state['df'] = df

aCols[0].bar_chart(data, x="Player", y="Score")

aCols[1].dataframe(df)


################################################

st.session_state['comScore'] = comScore
st.session_state['score'] = score
st.session_state['rDone'] = rDone

if "temp" in st.session_state:
    del st.session_state['temp']

if resetQ == True:
    resetIt()
    score = 0
    comScore = 0
    rDone = 0