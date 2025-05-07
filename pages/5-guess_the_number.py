import streamlit as st
from random import randint

def check_number(answer, guess, message):

    if guess == answer:
        message = 'Correct!'
        return message

    if guess > answer:
        message = 'Too high!'
        return message

    if guess < answer:
        message = 'Too low!'
        return message

def clear():
    st.session_state["guess"] = 1



if "score" not in st.session_state:
    score = 0

else:
    score = st.session_state["score"]

if "hiscore" not in st.session_state:
    st.session_state["hiscore"] = 0

if "answer" not in st.session_state:
    answer = randint(0,1000)
    st.session_state["answer"] = answer

else:
    answer = st.session_state["answer"]

st.title(":rainbow[Guess the number!]")

st.markdown("The program will choose a number between 1 and 1000. It is your job to "
            "guess the number. The program will tell you if your guess is too large "
            "or too small.")


st.divider()

cols = st.columns(2)
slot1 = cols[0].empty()
slot2 = cols[1].empty()

gues = st.number_input("Guess the number!", min_value=1, max_value=1000, format="%d", key="guess")

message = ''

submit = st.button("Submit", use_container_width=True)
                   #on_click=check_number(answer, guess, message))


with st.sidebar:
    reset = st.button("Reset", use_container_width=True, on_click=clear)

slot = st.empty()

if submit:
    message = check_number(answer, gues, message)

    if message == 'Correct!':
        slot = slot.success("You won!")

        del st.session_state["answer"]
        del st.session_state["score"]

        st.info("Starting new game")
        st.balloons()

        if (score < st.session_state["hiscore"]) or (st.session_state["hiscore"] == 0):
            st.session_state["hiscore"] = score
            st.toast("New highscore: " + str(score), icon="🔥")


        score = 0


    elif message == 'Too low!':
        slot = slot.error(message)
        score += 1

    elif message == 'Too high!':
        slot = slot.warning(message)
        score += 1


if reset:
    del st.session_state["answer"]
    del st.session_state["score"]
    score = 0

st.session_state["score"] = score
slot1.markdown("#### :blue[Your score: " + str(score) + "]")

if st.session_state["hiscore"] == 0:
    slot2.markdown("#### :green[Best score this session: " + "None" + "]")
else:
    slot2.markdown("#### :green[Best score this session: " + str(st.session_state["hiscore"]) + "]")
