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

st.title("Guess the number!")

st.markdown("The program will choose a number between 1 and 1000. It is your job to "
            "guess the number. The program will tell you if your guess is too large "
            "or too small.")

if "answer" not in st.session_state:
    answer = randint(0,1000)
    st.session_state["answer"] = answer

else:
    answer = st.session_state["answer"]


guess = st.number_input("Guess the number!", min_value=1, max_value=1000, format="%d", key="guess")

message = ''

submit = st.button("Submit", use_container_width=True)
                   #on_click=check_number(answer, guess, message))

with st.sidebar:
    reset = st.button("Reset", use_container_width=True, on_click=clear)

slot = st.empty()

if submit:
    message = check_number(answer, guess, message)

    if message == 'Correct!':
        slot = slot.success("You won!")
        del st.session_state["answer"]
        st.info("Starting new game")

    elif message == 'Too low!':
        slot = slot.error(message)
    elif message == 'Too high!':
        slot = slot.warning(message)

if reset:
    del st.session_state["answer"]