import streamlit as st
import random


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
    pass

################################################

rpsSelect = ["Rock", "Paper", "Scissors"]

score = 0
comScore = 0

if "score" not in st.session_state:
    score = 0

else:
    score = st.session_state["score"]

################################################

st.title(":red[Rock-Paper-Scissors!]")

place1 = st.empty()
place2 = st.empty()

gamemode = place1.selectbox("Gamemode", ("Best of 1", "Best of 3", "Best of 5", "Infinite"),
                            index=None, key="gamemode")
gamemodesubmit = place2.button("Submit Gamemode", use_container_width=True, key="gamemodesubmit")


if gamemodesubmit:
    pass


################################################

st.divider()

cols = st.columns(2)
slot1 = cols[0].empty()
slot2 = cols[1].empty()

rps = st.selectbox("Rock, Paper, Scissors", ("Rock", "Paper", "Scissors"),
                   index=None, key="rps")


submit = st.button("Submit", use_container_width=True, key="submit")

with st.sidebar:
    reset = st.button("Reset", use_container_width=True, on_click=clear)

if submit:

    if rps is not None:

        computerChoice = random.choice(rpsSelect)

        st.write("You selected: " + rps)
        st.write("The computer selected: " + computerChoice)

        wins = whoWins(rps, computerChoice)

        if wins == "You win!":
            st.success("You win!")
            score += 1

        elif wins == "You lose!":
            st.error("You lose!")
            comScore += 1

        else:
            st.info("It's a tie!")

    else:
        st.error("Please select rock, paper, or scissors.")

slot1.markdown("#### :blue[Your score: " + str(score) + "]")
slot2.markdown("#### :green[Computer score: " + str(comScore) + "]")

