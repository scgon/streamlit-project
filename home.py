import streamlit as st

st.title(":rainbow[Streamlit Project]")

st.markdown(
    """
    ##### This is a project containing several smaller streamlit projects/games.  
    """
)

st.text(" ")

container1 = st.container(border=True)

with container1:
    st.write("Right now, the pages that are fully functional are:")
    st.page_link("pages/2-wordle.py", label=":green[**Wordle**]")
    st.page_link("pages/5-guess_the_number.py", label=":green[**Guess the Number**]")
    st.page_link("pages/4-rock_paper_scissors.py", label=":green[**Rock-Paper-Scissors**]")

    st.write("The pages that are mostly functional but unfinished are:")
    st.page_link("pages/1-password_game.py", label=":orange[**Password Game**]")

    st.write("The pages that are in progress or partially functional are:")
    st.markdown(":blue[***None!***]")

    st.write("The pages that are not functional or haven't been started are:")
    st.page_link("pages/3-tic_tac_toe.py", label=":red[**Tic-Tac-Toe**]")
    st.page_link("pages/6-guess_the_number_reversed.py", label=":red[**Guess the Number REVERSED**]")


with st.container(border=True):

    st.write("For more information, visit:")

    st.page_link("pages/0-issues_and_notes.py", label=":blue[**Issues and Notes**]")

st.text(" ")

with st.container(border=True):
    st.markdown(
        """
        #### General Instructions and Notes:
        :red[*If you want to reset in a game that can be reset, the reset button will 
        be on the sidebar.]  
        :red[**In most games, there will be in a submit button, but if there isn't,
        press enter to submit.]  
        :red[**If the title of a page is red, that means it isn't properly functional, 
        even if the rest of the page looks normal.]  
        """)

st.markdown("Github Repository: https://github.com/scgon/streamlit-project")
