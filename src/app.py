import emoji
import random
import streamlit as st

from random_username.generate import generate_username

st.set_page_config(
    page_title="Python Username Generator",
    layout="wide")

emoji_list = [':smile:', ':flushed:', ':scream:', ':bowtie:', ':cold_sweat:', ':fire:', ':fist:', ':collision:', ':laughing:']

st.sidebar.text('Python Username Generator')

col1, col2 = st.beta_columns([2, 1])

with col1:
    st.subheader('How many usernames would you like to generate?')
    # user_number = st.number_input(label='Amount', min_value=1, max_value=5)
    button = st.button(label=emoji.emojize('Generate some usernames :rocket:'))

with col2:
    st.subheader('Your generated usernames')
    if button:
        user_name = generate_username(1)
        for i in user_name:
            st.write(i, emoji.emojize(random.choice(emoji_list)))
