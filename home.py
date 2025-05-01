import streamlit as st

st.title(":rainbow[Streamlit Project]")

st.markdown(
    """
    ##### This is a app of several streamlit projects/games.  
    """
)

st.text(" ")

container1 = st.container(border=True)

with container1:
    st.write("Right now, the pages that are fully functional are:")
    st.page_link("pages/2-wordle.py", label=":green[**Wordle**]")
    st.page_link("pages/5-guess_the_number.py", label=":green[**Guess the Number**]")

    st.write("The pages that are mostly functional but unfinished are:")
    st.page_link("pages/1-password_game.py", label=":orange[**Password Game**]")

    st.write("The pages that are not functional or haven't been started are:")
    st.page_link("pages/3-tic_tac_toe.py", label=":red[**Tic-Tac-Toe**]")
    st.page_link("pages/4-rock_paper_scissors.py", label=":red[**Rock-Paper-Scissors**]")
    st.page_link("pages/6-guess_the_number_reversed.py", label=":red[**Guess the Number REVERSED**]")

    st.text(" ")

    st.write("For more information, visit:")
    st.page_link("pages/0-issues_and_notes.py", label=":blue[**Issues and Notes**]")

st.text(" ")


st.markdown(
    """
    :small[:red[*If you want to reset in any game, reset button will be on the sidebar.]]  
    :small[:red[**In most games, there will be in a submit button, but if there isn't,
    press enter to submit.]]  
    """
)

st.markdown("Github Repository: https://github.com/scgon/streamlit-project")
