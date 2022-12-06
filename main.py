import streamlit as st
from datetime import date
from streamlit.components.v1 import iframe
import openai

openai.api_key = "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"

st.set_page_config(layout="centered",
                   page_title="Combinatorics Final Project")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}footer:after {
	content:''; 
    padding: 1500px;
	visibility: visible;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


@st.cache
def label_problem(problem, user_prompt):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_prompt,
        temperature=0.5,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    return solve_problem(

        'Solve the following problem by giving an answer followed by a brief explanation: ' + problem + '\n The problem can be solved using ' + response['choices'][0]['text'] + '.\n Answer:')


@st.cache
def solve_problem(user_prompt):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_prompt,
        temperature=0.3,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    return response['choices'][0]['text']


@st.cache
def generate_problem(user_prompt):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    return response['choices'][0]['text']


header = st.header('Combinatorics Final Project')
text = st.text_area('Enter a combinatorics word problem to solve')
if st.button('Solve a Problem'):
    if not text:
        st.text('Enter a problem to solve')
    else:
        ai_response = label_problem(text,
                                    'Problem:' + text + 'Identify which of the following six categories this problem falls under and output it as a response.\n1. Permutations of distinct objects\n2. Permutations of indistinct objects\n3. Combinations of distinct objects\n4. Bucketing with distinct objects\n5. Bucketing with indistinct objects\n6. Bucketing into fix sized containers\n7. None of the above\n\nResponse: ')
        st.write(ai_response)


option = st.selectbox(
    'Select a combinatorics topic to generate a problem',
    ('Permutations of distinct objects', 'Permutations of indistinct objects', 'Combinations of distinct objects', 'Bucketing with distinct objects', 'Bucketing with indistinct objects', 'Bucketing into fix sized containers'))

if st.button('Generate Problem'):

    if not option:
        st.text('Enter a capability')

    if option:
        ai_response = generate_problem(
            'Generate a combinatorics word problem based on the following category: ' + option + '\n Response:')
        st.write(ai_response)
