import streamlit as st

from random_username.generate import generate_username

st.title('Python Username Generater')

st.markdown("![Alt Text](https://media.giphy.com/media/okLCopqw6ElCDnIhuS/giphy.gif)")

user_number = st.number_input(label='How many usernames would you like to generate?', min_value=1, max_value=5)

if user_number == 1:
    st.write(generate_username(1))
elif user_number == 2:
    st.write(generate_username(2))
elif user_number == 3:
    st.write(generate_username(3))
elif user_number == 4:
    st.write(generate_username(4))
elif user_number == 5:
    st.write(generate_username(5))
else:
    st.stop()
