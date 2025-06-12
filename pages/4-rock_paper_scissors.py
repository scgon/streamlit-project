import streamlit as st
import random
import pandas as pd
from time import sleep

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
    if "comScore" in st.session_state:
        del st.session_state['comScore']
    if "score" in st.session_state:
        del st.session_state['score']
    if "rDone" in st.session_state:
        del st.session_state['rDone']
    if "done" in st.session_state:
        del st.session_state['done']
    if "simamount" in st.session_state:
        del st.session_state['simamount']
    if "tied" in st.session_state:
        del st.session_state['tied']

################################################

rpsSelect = ["Rock", "Paper", "Scissors"]

score = 0
comScore = 0
tied = 0
rDone = 0
rTotal = 0
resetQ = False
hidden = False
runsimatbottom = False

if "score" not in st.session_state:
    score = 0

else:
    score = st.session_state["score"]

if "comScore" not in st.session_state:
    comScore = 0

else:
    comScore = st.session_state["comScore"]

if "tied" not in st.session_state:
    tied = 0

else:
    tied = st.session_state["tied"]

################################################

st.title(":rainbow[Rock-Paper-Scissors!]")

place1 = st.empty()
place2 = st.empty()
place3 = st.empty()

if "done" in st.session_state:
    if st.session_state["done"] != "Infinite" and st.session_state["done"] != "Random Simulation":
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

rpsSlot = st.empty()
rps = rpsSlot.selectbox("Rock, Paper, Scissors", ("Rock", "Paper", "Scissors"),
                   index=None, key="rps")

submitSlot = st.empty()
submit = submitSlot.button("Submit", use_container_width=True, key="submit", on_click=clear)

with st.sidebar:
    reset = st.button("Reset", use_container_width=True)
    if "done" in st.session_state:
        if st.session_state["done"] == "Random Simulation":
            progress_bar = st.sidebar.progress(0, text="Simulation Progress")
            status_text = st.sidebar.empty()

warningSlot1 = st.empty()
warningSlot2 = st.empty()
warningSlot3 = st.empty()

aCols = st.columns([0.6, 0.4])
aSlot = st.empty()

################################################

if submit:
    if rDone < rTotal or rTotal == 0:
        if "done" in st.session_state and st.session_state["done"] is not None:
            if st.session_state["done"] != "Random Simulation":
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
                            rDone += 1

                    st.markdown("##### You selected: " + colory + "[" + st.session_state["temp"] + "]")
                    st.markdown("##### The computer selected: " + colorc + "[" + computerChoice + "]")

                    st.text(" ")

                    if wins == "You win!":
                        warningSlot1.success("You win!")

                    elif wins == "You lose!":
                        warningSlot1.error("You lose!")

                    else:
                        warningSlot1.info("It's a tie!")

                    if st.session_state["done"] != "Infinite":
                        if score >= rTotal // 2 + 1:
                            warningSlot2.success("You win the game!")
                            st.balloons()
                            st.toast("Starting new game")

                            resetQ = True

                        elif comScore >= rTotal // 2 + 1:
                            warningSlot2.error("Computer wins the game, you lose!")
                            st.toast("Starting new game")

                            resetQ = True

                else:
                    warningSlot1.error("Please select rock, paper, or scissors.")
            else:
                runsimatbottom = True


        else:
            st.error("Please select a gamemode")
    else:
        st.error("Game is finished, please reset.")

if reset:
    score = 0
    comScore = 0
    rDone = 0
    tied = 0
    resetIt()
    resetQ = False

################################################

slot1.markdown("#### :green[Your score: " + str(score) + "]")
slot2.markdown("#### :red[Computer score: " + str(comScore) + "]")
slot3.markdown("#### :blue[Tied: " + str(tied) + "]")

if "done" in st.session_state:
    if st.session_state["done"] == "Infinite" or st.session_state["done"] == "Random Simulation":
        slot4.markdown("#### :violet[Round: " + str(rDone) + "]")
    else:
        slot3.markdown("#### :orange[Round: " + str(rDone) + "/" + str(rTotal) + "]")
else:
    slot4.markdown("#### :violet[Round: " + str(score) + "]")
    slot3.markdown("#### :blue[Tied: " + str(tied) + "]")

if "done" not in st.session_state:

    gamemode = place1.selectbox("Gamemode", ("Best of 1", "Best of 3", "Best of 5", "Infinite", "Random Simulation"),
                                index=None, key="gamemode")
    gamemodesubmit = place2.button("Submit Gamemode", use_container_width=True, key="gamemodesubmit")


    if gamemodesubmit:
        place1.markdown("### :red[Gamemode: " + gamemode + "]")
        place2.empty()
        st.session_state["done"] = gamemode

else:
    place1.markdown("### :red[Gamemode: " + st.session_state['done'] + "]")

if "done" in st.session_state:
    if st.session_state["done"] == "Random Simulation" and "simamount" not in st.session_state:
        simamount = place2.number_input("How many simulations should run?", 9, 799)
        simamountSubmit = place3.button("Submit Simulations Amount", use_container_width=True, key="simamountsubmit")
        hidden = True
    
        if simamountSubmit:
            place2.markdown("#### :blue[" + str(simamount) + " Simulations Will Run]")
            place3.empty()
            st.session_state["simamount"] = simamount
    
    elif st.session_state["done"] == "Random Simulation" and "simamount" in st.session_state:
        place2.markdown("#### :blue[" + str(st.session_state["simamount"]) + " Simulations Will Run]")
        place3.empty()
    
if hidden == True:
    #submitSlot.empty()
    rpsSlot.empty()


################################################

if "done" in st.session_state:
    if st.session_state["done"] != "Random Simulation":
        #aCols = st.columns([0.6, 0.4])

        scoreA = score
        comScoreA = comScore

        data = {"Player": ["Player", "Computer", "Tie"], "Score": [scoreA, comScoreA, tied]}

        st.divider()

        df = pd.DataFrame(data)

        st.session_state['df'] = df

        aCols[0].bar_chart(data, x="Player", y="Score")

        aCols[1].dataframe(df)

else:
    #aCols = st.columns([0.6, 0.4])

    scoreA = score
    comScoreA = comScore

    data = {"Player": ["Player", "Computer", "Tie"], "Score": [scoreA, comScoreA, tied]}

    st.divider()

    df = pd.DataFrame(data)

    st.session_state['df'] = df

    aCols[0].bar_chart(data, x="Player", y="Score")

    aCols[1].dataframe(df)


if runsimatbottom == True:
    
    data1 = {"Player": [score], "Computer": [comScore], "Tie": [tied]}

    df1 = pd.DataFrame(data1)

    st.session_state["df1"] = df1
    
    for i in range(st.session_state["simamount"]):
        playerChoice = random.choice(rpsSelect)
        computerChoice = random.choice(rpsSelect)

        wins = whoWins(playerChoice, computerChoice)

        if wins == "You win!":
            score += 1
            rDone += 1

        elif wins == "You lose!":
            comScore += 1
            rDone += 1

        else:
            tied += 1
            rDone += 1

        sleep(7.5 / st.session_state["simamount"])

        if st.session_state["simamount"] < 300:
            sleep(7.5 / st.session_state["simamount"])
        else:
            sleep(0.01)

        progress_bar.progress((round((i + 1) / st.session_state["simamount"] * 100)), text="Simulation Progress")
        status_text.text(str(round((i + 1) / st.session_state["simamount"] * 100, 1)) + "% complete")

        data = {"Player": ["Player", "Computer", "Tie"], "Score": [score, comScore, tied]}

        df = pd.DataFrame(data)

        st.session_state['df'] = df

        aCols[0] = aCols[0].bar_chart(data, x="Player", y="Score")

        
        #aCols[1] = aCols[1].dataframe(df)

        if st.session_state["simamount"] < 400:
            data1["Player"].append(score)
            data1["Computer"].append(comScore)
            data1["Tie"].append(tied)

            df1 = pd.DataFrame(data1)

            st.session_state["df1"] = df1

            aSlot = aSlot.line_chart(df1)

        if st.session_state["simamount"] >= 100:
            aCols[1] = aCols[1].dataframe(df)
        else:
            aCols[1] = aCols[1].dataframe(df1)

        #aSlot[1] = aSlot[1].dataframe(df1)

        slot1.markdown("#### :green[Your score: " + str(score) + "]")
        slot2.markdown("#### :red[Computer score: " + str(comScore) + "]")
        slot3.markdown("#### :blue[Tied: " + str(tied) + "]")
        slot4.markdown("#### :violet[Round: " + str(rDone) + "]")

        rpsSlot.empty()
        submitSlot.empty()

    warningSlot1.warning("Simulation finished!")
    sleep(1)

    while score == comScore:
        warningSlot2.warning("It's a tie! Running an extra round:")
        playerChoice = random.choice(rpsSelect)
        computerChoice = random.choice(rpsSelect)

        wins = whoWins(playerChoice, computerChoice)

        if wins == "You win!":
            score += 1
            rDone += 1

        elif wins == "You lose!":
            comScore += 1
            rDone += 1

        else:
            tied += 1
            rDone += 1

        if st.session_state["simamount"] < 400:
            data1["Player"].append(score)
            data1["Computer"].append(comScore)
            data1["Tie"].append(tied)

            df1 = pd.DataFrame(data1)

            st.session_state["df1"] = df1

            aSlot = aSlot.line_chart(df1)


        sleep(0.5)

    if score > comScore:
        warningSlot3.success("You win the simulation!")
        st.balloons()
        st.toast("Starting new game")
        st.toast("Check out the dataframe and chart below!")

        resetQ = True

    elif comScore > score:
        warningSlot3.error("Computer wins the simulation, you lose!")
        st.toast("Starting new game")
        st.toast("Check out the dataframe and chart below!")

        resetQ = True

    data = {"Player": ["Player", "Computer", "Tie"], "Score": [score, comScore, tied]}

    df = pd.DataFrame(data)

    st.session_state['df'] = df
    
    aCols[0] = aCols[0].bar_chart(data, x="Player", y="Score")

    if st.session_state["simamount"] >= 100:
        aCols[1] = aCols[1].dataframe(df)
    else:
        aCols[1] = aCols[1].dataframe(df1)

    slot1.markdown("#### :green[Your score: " + str(score) + "]")
    slot2.markdown("#### :red[Computer score: " + str(comScore) + "]")
    slot3.markdown("#### :blue[Tied: " + str(tied) + "]")
    slot4.markdown("#### :violet[Round: " + str(rDone) + "]")

    rpsSlot.empty()
    submitSlot.empty()

################################################

st.session_state['comScore'] = comScore
st.session_state['score'] = score
st.session_state['rDone'] = rDone
if "done" in st.session_state:
    if st.session_state["done"] == "Infinite":
        st.session_state['tied'] = tied

if "temp" in st.session_state:
    del st.session_state['temp']

if resetQ == True:
    resetIt()
    score = 0
    comScore = 0
    rDone = 0
    tied = 0
    resetQ = False
