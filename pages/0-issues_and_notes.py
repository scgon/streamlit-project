import streamlit as st

st.title(":rainbow[Issues and Notes]")

with st.container(border=True):
    st.page_link("pages/5-guess_the_number.py", label=":green[**Guess the Number**]")
    st.write("Issue with reseting score, the score will not be reset properly. Will be fixed the next time I update this.")
    st.write("Fix: reload the tab.")

with st.container(border=True):
    st.page_link("pages/2-wordle.py", label=":green[**Wordle**]")
    st.write("Mostly functional, but missing game end messages.")

with st.container(border=True):
    st.page_link("pages/1-password_game.py", label=":orange[**Password Game**]")
    st.write("Unfinished, need to finish the rest of the rules")

with st.container(border=True):
    st.page_link("pages/3-tic_tac_toe.py", label=":red[**Tic-Tac-Toe**]")
    st.write("Unstarted")

with st.container(border=True):
    st.page_link("pages/4-rock_paper_scissors.py", label=":red[**Rock-Paper-Scissors**]")
    st.write("Unstarted")

with st.container(border=True):
    st.page_link("pages/6-guess_the_number_reversed.py", label=":red[**Guess the Number REVERSED**]")
    st.write("Unstarted")
