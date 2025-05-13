import random
import streamlit as st
from words import word_list
from string import ascii_uppercase

st.set_page_config(initial_sidebar_state="expanded")

#############################################################

def printtrying(answer, tryingList):
    for i in range(5):
        if answer[i] == "G":
            answers[i] = ":green-background[" + tryingList[i] + "]"
        elif answer[i] == "Y":
            answers[i] = ":orange-background[" + tryingList[i] + "]"
        elif answer[i] == "N":
            answers[i] = ":grey-background[" + tryingList[i] + "]"
    clearclearclear()


def clearclearclear():
    st.session_state['char1'] = ''
    st.session_state['char2'] = ''
    st.session_state['char3'] = ''
    st.session_state['char4'] = ''
    st.session_state['char5'] = ''


def double_letters(word):

    doubleletters = []
    lt = []

    for i in range(5):
        for n in range(5):
            if word[i] == word[n] and i < n and word[i] != '' and word[n] != '':
                doubleletters.append([i, n, word[n]])
                lt.append(word[n])

    return doubleletters,lt


def caseA(word, correct, results):

    letters = []
    crtletters = []

    for i in range(5):
        if (word[i] not in letters) or (word[i] in letters):
            letters.append(word[i])

    for i in range(5):
        if (correct[i] not in crtletters) or (correct[i] in crtletters):
            crtletters.append(correct[i])


    if word == correct:
        return 'correct'
    else:
        for i in range(5):

            if word[i] == correct[i]:

                results[i] = 'G'

                letters.remove(word[i])

                crtletters.remove(word[i])

                tempindx = ascii_uppercase.index(word[i].upper())

                letter[tempindx] = ":green-background[" + word[i].upper() + "]"



        for i in range(5):

            for n in range(5):

                if word[i] == correct[n]:

                    if (word[i] in letters) and (word[i] in crtletters) and (results[i] != 'G'):

                        #st.title(str(i) + str(word[i]))


                        letters.remove(word[i])
                        crtletters.remove(word[i])

                        results[i] = 'Y'

                        tempindx = ascii_uppercase.index(word[i].upper())

                        if word[i].upper() in letter:
                            letter[tempindx] = ":orange-background[" + word[i].upper() + "]"

                        elif (word[i].upper() not in letter) and (":grey-background[" + word[i].upper() + "]" in letter):
                            letter[tempindx] = ":orange-background[" + word[i].upper() + "]"

                        #st.write(letter)

                    elif word[i] not in letters and results[i] == '':

                        results[i] = 'N'

                        if word[i].upper() in letter:
                            tempindx = ascii_uppercase.index(word[i].upper())

                            letter[tempindx] = ":grey-background[" + word[i].upper() + "]"

                    break

                elif results[i] == '':

                    results[i] = 'N'

                    if word[i].upper() in letter:
                        tempindx = ascii_uppercase.index(word[i].upper())

                        letter[tempindx] = ":grey-background[" + word[i].upper() + "]"


        for i in range(5):
            if results[i] == '':

                results[i] = 'N'

                if word[i].upper() in letter:
                    tempindx = ascii_uppercase.index(word[i].upper())

                    letter[tempindx] = ":grey-background[" + word[i].upper() + "]"

    return results


def check_word(word, startcorrect):

    results = ['', '', '', '', '']

    correct = [char.lower() for char in startcorrect]

    word = [a.lower() for a in word]

    results = caseA(word, correct, results)

    # st.write(results)

    return results


def do_next():

    gameOver = False
    donea = False

    tryingList = [str(cols[1].inpt).upper(), str(cols[2].inpt).upper(),
                  str(cols[3].inpt).upper(), str(cols[4].inpt).upper(),
                  str(cols[5].inpt).upper()]

    if len(tryingList) != 5:
        return

    answer = check_word(tryingList, correct)

    answers = st.session_state['answers']


    if answer == 'correct':

        for i in range(24, -1, -1):
            answers[i + 5] = answers[i]

        for i in range(5):

            answers[i] = ':green-background[' + tryingList[i] + ']'
            clearclearclear()

        # Win

        st.session_state["finishedGame"] = True

        st.toast("You Win!", icon="🎉")
        st.balloons()

        donea = True

    else:
        for i in range(1, 6):
            if (st.session_state['char'+str(i)] != '') and (st.session_state['char' + str(i)] is not None):
                if answers[29] == '☐':
                    for i in range(24, -1, -1):
                        answers[i + 5] = answers[i]

                    printtrying(answer, tryingList)

                else:
                    gameOver = True
                    donea = True

    if answers[29] != '☐':
        gameOver = True
        donea = True

    if gameOver == True:
        st.session_state["finishedGame"] = True
        st.toast("You Lose")

    if donea == True:
        st.toast("Starting a new game")



def clear():
    for i in range(30):
        answers[i] = '☐'

#############################################################

colsTop = st.columns([2.5, 3, 2.5])
colsTop[1].title = colsTop[1].title(":rainbow[W O R D L E]")

st.text(' ')

colsMid = st.columns([0.9, 5, 1])
button_pressed = colsMid[1].button('SUBMIT', on_click=do_next,
                                      use_container_width=True)


with st.sidebar:
    reset_pressed = st.button("RESET", on_click=clear, use_container_width=True)


cols = st.columns(7, gap='medium')

a1 = st.container()
b1 = st.container()
b2 = st.container()
b3 = st.container()
b4 = st.container()
b5 = st.container()
b6 = st.container()

st.markdown("""
    <style>
    [data-testid=stVerticalBlock]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)

#############################################################

# del st.session_state['answers']

answers = []

if "answers" not in st.session_state:
    for i in range(30):
        answers.append('☐')
else:
    answers = st.session_state["answers"]

    for i in range(30):
        if answers[i] == '':
            answers[i] = '☐'


if "letter" not in st.session_state:
    letter = list(ascii_uppercase)

else:
    letter = st.session_state["letter"]

#if "letterD" not in st.session_state:
    #letterD = list(ascii_uppercase)

#else:
    #letterD = st.session_state["letterD"]


# st.write(answers)

if 'correct' not in st.session_state:
    correct = random.choice(word_list)
    correct = correct.upper()
    st.session_state['correct'] = correct
else:
    correct = st.session_state['correct']

print(correct)

#############################################################

if 'text' not in st.session_state:
    st.session_state.text = 0
else:
    nextwd = 0

#############################################################

with a1:
    cols[1].inpt = cols[1].text_input('', max_chars=1, key='char1')
    cols[2].inpt = cols[2].text_input('', max_chars=1, key='char2')
    cols[3].inpt = cols[3].text_input('', max_chars=1, key='char3')
    cols[4].inpt = cols[4].text_input('', max_chars=1, key='char4')
    cols[5].inpt = cols[5].text_input('', max_chars=1, key='char5')

with b1:
    cols[1].answr1 = cols[1].title(str(answers[0]))
    cols[2].answr1 = cols[2].title(str(answers[1]))
    cols[3].answr1 = cols[3].title(str(answers[2]))
    cols[4].answr1 = cols[4].title(str(answers[3]))
    cols[5].answr1 = cols[5].title(str(answers[4]))


with b2:
    cols[1].answr2 = cols[1].title(str(answers[5]))
    cols[2].answr2 = cols[2].title(str(answers[6]))
    cols[3].answr2 = cols[3].title(str(answers[7]))
    cols[4].answr2 = cols[4].title(str(answers[8]))
    cols[5].answr2 = cols[5].title(str(answers[9]))

with b3:
    cols[1].answr3 = cols[1].title(str(answers[10]))
    cols[2].answr3 = cols[2].title(str(answers[11]))
    cols[3].answr3 = cols[3].title(str(answers[12]))
    cols[4].answr3 = cols[4].title(str(answers[13]))
    cols[5].answr3 = cols[5].title(str(answers[14]))

with b4:
    cols[1].answr4 = cols[1].title(str(answers[15]))
    cols[2].answr4 = cols[2].title(str(answers[16]))
    cols[3].answr4 = cols[3].title(str(answers[17]))
    cols[4].answr4 = cols[4].title(str(answers[18]))
    cols[5].answr4 = cols[5].title(str(answers[19]))

with b5:
    cols[1].answr5 = cols[1].title(str(answers[20]))
    cols[2].answr5 = cols[2].title(str(answers[21]))
    cols[3].answr5 = cols[3].title(str(answers[22]))
    cols[4].answr5 = cols[4].title(str(answers[23]))
    cols[5].answr5 = cols[5].title(str(answers[24]))

with b6:
    cols[1].answr6 = cols[1].title(str(answers[25]))
    cols[2].answr6 = cols[2].title(str(answers[26]))
    cols[3].answr6 = cols[3].title(str(answers[27]))
    cols[4].answr6 = cols[4].title(str(answers[28]))
    cols[5].answr6 = cols[5].title(str(answers[29]))


colsAlpha = st.columns([0.6, 1, 1, 1, 1, 1, 1, 1, 0.6], gap='medium')

c1 = st.container()
c2 = st.container()
c3 = st.container()
c4 = st.container()
c5 = st.container()

st.markdown("""
    <style>
    [data-testid=stVerticalBlock]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)


with c1:
    colsAlpha[1].letA = colsAlpha[1].header(letter[0])
    colsAlpha[2].letB = colsAlpha[2].header(letter[1])
    colsAlpha[3].letC = colsAlpha[3].header(letter[2])
    colsAlpha[4].letD = colsAlpha[4].header(letter[3])
    colsAlpha[5].letE = colsAlpha[5].header(letter[4])
    colsAlpha[6].letF = colsAlpha[6].header(letter[5])
    colsAlpha[7].letG = colsAlpha[7].header(letter[6])


with c2:
    colsAlpha[1].letH = colsAlpha[1].header(letter[7])
    colsAlpha[2].letI = colsAlpha[2].header(letter[8])
    colsAlpha[3].letJ = colsAlpha[3].header(letter[9])
    colsAlpha[4].letK = colsAlpha[4].header(letter[10])
    colsAlpha[5].letL = colsAlpha[5].header(letter[11])
    colsAlpha[6].letM = colsAlpha[6].header(letter[12])
    colsAlpha[7].letN = colsAlpha[7].header(letter[13])

with c3:
    colsAlpha[1].letO = colsAlpha[1].header(letter[14])
    colsAlpha[2].letP = colsAlpha[2].header(letter[15])
    colsAlpha[3].letQ = colsAlpha[3].header(letter[16])
    colsAlpha[4].letR = colsAlpha[4].header(letter[17])
    colsAlpha[5].letS = colsAlpha[5].header(letter[18])
    colsAlpha[6].letT = colsAlpha[6].header(letter[19])
    colsAlpha[7].letU = colsAlpha[7].header(letter[20])

with c4:
    colsAlpha[2].letV = colsAlpha[2].header(letter[21])
    colsAlpha[3].letW = colsAlpha[3].header(letter[22])
    colsAlpha[4].letX = colsAlpha[4].header(letter[23])
    colsAlpha[5].letY = colsAlpha[5].header(letter[24])
    colsAlpha[6].letZ = colsAlpha[6].header(letter[25])


#############################################################

tryingList = [str(cols[1].inpt).upper(), str(cols[2].inpt).upper(),
              str(cols[3].inpt).upper(), str(cols[4].inpt).upper(),
              str(cols[5].inpt).upper()]

trying = ''.join(tryingList)

st.session_state.answers = answers
st.session_state.letter = letter
#st.session_state.letterD = letterD

if button_pressed:
    st.session_state["textList"] = tryingList

if reset_pressed:
    del st.session_state["letter"]
    del st.session_state["answers"]
    del st.session_state['correct']

st.divider()

st.markdown(
    """
    ## How To Play
    ##### You get 6 chances to guess a 5-letter word!
    ###### The highlight of the letter will change to show how close your guess was to the word:  
    :green-background[Green highlight means the letter is in the word and in the correct spot.]  
    :orange-background[Yellow highlight means the letter is in the word but in the wrong spot.]  
    :gray-background[Gray highlight means the letter is not in the word in any spot.]
    
    
    :small[:red[*Because of the way streamlit works and how this app is coded, after you finish a 
    game, whenever you try to press a button or type in a character, a new game will start.]]
    """
)

if "finishedGame" in st.session_state:
    if st.session_state["finishedGame"] == True:
        del st.session_state["letter"]
        del st.session_state["answers"]
        del st.session_state['correct']
        st.session_state["finishedGame"] = False
    else:
        st.session_state["finishedGame"] = False