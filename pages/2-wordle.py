import streamlit as st

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


def next_step(word, correct):

    wdbl,wlt = (double_letters(word))
    cdbl,clt = (double_letters(correct))

    wltstr = ''.join(wlt)
    cltstr = ''.join(clt)

    a = []

    # check if doubles are in the word
    if (len(wdbl) == 0 or len(cdbl) == 0):

        # if word has none:
        if len(wdbl) <= len(cdbl):
            return 'Normal'

        # if word has some but correct has none, we want to send to
        else:

            # only will happen if wdbl has 1, 2, or a 3 pair and the letter
            # IS IN CORRECT

            return 'CaseA'

    if len(wlt) != 2:
        if wlt[0] not in correct:
            a.append('good')
        else:
            if wlt[0] in cltstr:
                a.append('not good')
            else:
                a.append('bad')

    else:
        for i in range(2):
            if wlt[i] not in correct:
                a.append('good')
            else:
                if wlt[i] in cltstr:
                    a.append('not good')
                else:
                    a.append('bad')



    if ('bad' not in a) and ('not good' not in a):
        print('works!')
        return 'Normal'

    # combos: 1, 2; 2, 2; 1, 3; 2, 3;
    # total: 1, 2; 2, 2; 1, 3; 2, 3;
           # 2, 1; 3, 1; 3, 2

    # covers all containing 0:

    if len(wdbl) != 2 and len(cdbl) != 2:
        if wlt[0] == clt[0]:
            return 'Normal'

        # if it is the 11 or 33 combo but the letters aren't the same and
        # are both in the other group
        else:
            return 'CaseA'

    # covers all containing copies outside of the 00 and 11 copies:
    elif len(wdbl) == len(cdbl):

        # covers 1 and 3 copies:
        if (len(wdbl) == 1 or len(cdbl) == 3):

            # covers all with same letters:
            if wlt[0] == clt[0]:
                return 'CaseA'

            # covers with different letters not in opposite

            elif ((wdbl[0])[2] not in correct) or ((cdbl[0])[2] not in word):
                return 'Normal'

            # covers
    else:
        print("CAUGHT IN LAST -- UNSURE SITUATION")
        return 'CaseA'

    #covers all others:
    if len(cdbl) == 1:
        return 'Normal'


def logicNormal(word, correct, results):

    if word == correct:
        return 'correct'
    else:
        for i in range(5):
            if word[i] == correct[i]:
                results[i] = 'G'
            else:
                for n in range(5):
                    if word[i] == correct[n]:
                        results[i] = 'Y'
                        break
                    results[i] = 'N'

    return results


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


        for i in range(5):

            for n in range(5):

                if word[i] == correct[n]:

                    if (word[i] in letters) and (word[i] in crtletters) and (results[i] != 'G'):

                        #st.title(str(i) + str(word[i]))


                        letters.remove(word[i])
                        crtletters.remove(word[i])

                        results[i] = 'Y'

                    elif word[i] not in letters and results[i] == '':

                        results[i] = 'N'

                    break

                elif results[i] == '':
                    results[i] = 'N'

        for i in range(5):
            if results[i] == '':
                results[i] = 'N'


    return results


def check_word(word, startcorrect):

    results = ['', '', '', '', '']

    correct = [char.lower() for char in startcorrect]

    word = [a.lower() for a in word]

    nExt = next_step(word, correct)

    if nExt == 'Normal':
        results = logicNormal(word, correct, results)

    else:
        results = caseA(word, correct, results)

    # st.write(results)

    return results


def do_next():

    tryingList = [str(cols[1].inpt).upper(), str(cols[2].inpt).upper(),
                  str(cols[3].inpt).upper(), str(cols[4].inpt).upper(),
                  str(cols[5].inpt).upper()]


    answer = check_word(tryingList, correct)

    answers = st.session_state['answers']

    if answer == 'correct':

        for i in range(24, -1, -1):
            answers[i + 5] = answers[i]

        for i in range(5):

            answers[i] = ':green-background[' + tryingList[i] + ']'
            clearclearclear()

        # Win

    else:
        for i in range(1, 6):
            if (st.session_state['char'+str(i)] != '') and (st.session_state['char'+str(i)] != None):
                if answers[29] == '☐':
                    for i in range(24, -1, -1):
                        answers[i + 5] = answers[i]

                    printtrying(answer, tryingList)

                else:
                    # Loss
                    pass


def clear():
    for i in range(30):
        answers[i] = '☐'

#############################################################


colsTop = st.columns([2.6, 3, 2.5])
colsTop[1].title = colsTop[1].title(":rainbow[W O R D L E]")

st.text(' ')

colsMid = st.columns([0.9, 5, 1])
colsMid[1].button = colsMid[1].button('SUBMIT', on_click=do_next,
                                      use_container_width=True)

cols = st.columns(7, gap='medium')

a1 = st.container()
b1 = st.container()
b2 = st.container()
b3 = st.container()
b4 = st.container()
b5 = st.container()
b6 = st.container()


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



# st.write(answers)

if 'correct' not in st.session_state:
    correct = 'reels'
    correct = correct.upper()
    st.session_state['correct'] = correct
else:
    correct = st.session_state['correct']

#############################################################

if 'text' not in st.session_state:
    st.session_state.text = 0
else:
    nextwd = 0

if colsMid[1].button:
    password = ""
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

st.text(' ')

colsBottom = st.columns([0.9, 5, 1])
colsBottom[1].reset = colsBottom[1].button("RESET", on_click=clear,
                                           use_container_width=True)

#############################################################

tryingList = [str(cols[1].inpt).upper(), str(cols[2].inpt).upper(),
              str(cols[3].inpt).upper(), str(cols[4].inpt).upper(),
              str(cols[5].inpt).upper()]

trying = ''.join(tryingList)

st.session_state.answers = answers

if colsMid[1].button:
    st.session_state["textList"] = tryingList

if colsBottom[1].reset:
    del st.session_state["answers"]
    del st.session_state['correct']
