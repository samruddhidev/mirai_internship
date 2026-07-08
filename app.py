import streamlit as st

st.set_page_config(page_title="Echo Chamber")

st.title("Echo Chamber")
st.write("Enter your name and message below, then click Transmit.")

user_name = st.text_input("Name")
user_message = st.text_input("Message")

if st.button("Transmit"):

    if not user_name.strip():
        st.error("Please provide your name.")

    elif not user_message.strip():
        st.warning("Please type a message to transmit.")

    else:
        token_count = round(len(user_message) / 4, 2)

        st.success(
            f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}"
        )

        st.info(
            f"System Check: Your message will consume approximately {token_count} tokens from our context window."
        )
