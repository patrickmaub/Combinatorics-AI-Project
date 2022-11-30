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
def solve_problem(user_prompt):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_prompt,
        temperature=0.5,
        max_tokens=256,
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
text = st.text_area('Solve a combinatorics word problem')
if st.button('Solve a Problem'):
    if not text:
        st.text('Enter a problem to solve')
    else:
        ai_response = solve_problem(
            'Select the correct formula to solve the following combinatorics word problem. Then, calculate the answer and explain it in simple terms.\nProblem:' + text + '\nSolution:')
        st.write(ai_response)


option = st.selectbox(
    'Generate a combinatorics word problem',
    ('multiplication principle', 'probability', 'combinatorial number', 'variations', 'permutations', 'combinations with repitition', 'permutations with repitition'))

if st.button('Generate Combinatorics Word Problem'):

    if not option:
        st.text('Enter a capability')

    if option:
        ai_response = generate_problem(
            'Generate a combinatorics word problem based on the following category: ' + option + '\n Response:')
        st.write(ai_response)
