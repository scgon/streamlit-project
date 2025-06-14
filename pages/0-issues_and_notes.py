import streamlit as st

st.title(":rainbow[Issues and Notes]")

with st.container(border=True):
    st.page_link("pages/5-guess_the_number.py", label=":green[**Guess the Number**]")
    st.markdown("Fully Functional")

with st.container(border=True):
    st.page_link("pages/2-wordle.py", label=":green[**Wordle**]")
    st.markdown("""Mostly functional, but game end messages may not work and may glitch.   
                    :material/arrow_right_alt: Known issue that if you win on the last guess you will get both the game won and game lost messages.   
                    :material/arrow_right_alt: Issues will be fixed shortly.""")

with st.container(border=True):
    st.page_link("pages/4-rock_paper_scissors.py", label=":green[**Rock-Paper-Scissors**]")
    st.markdown("""Fully Functional   
                :material/arrow_right_alt: However, not fully tested yet, there may be bugs]""")

with st.container(border=True):
    st.page_link("pages/1-password_game.py", label=":orange[**Password Game**]")
    st.markdown("""Functional but unfinished, the rest of the rules aren't completed.  
                May remain unfinished for a while.""")

with st.container(border=True):
    st.page_link("pages/3-tic_tac_toe.py", label=":red[**Tic-Tac-Toe**]")
    st.markdown("""Unstarted, just an idea.  
                May never be started.""")

with st.container(border=True):
    st.page_link("pages/6-guess_the_number_reversed.py", label=":red[**Guess the Number REVERSED**]")
    st.markdown("Unstarted, will be started soon.")