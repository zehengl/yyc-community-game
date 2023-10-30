import streamlit as st


st.set_page_config(page_title="yyc-community-game", page_icon="random")
_, center, _ = st.columns([2, 1, 2])
with center:
    st.image(
        "https://cdn3.iconfinder.com/data/icons/brain-games/128/Quiz-Games-red.png",
        use_column_width=True,
    )
st.title("yyc-community-game")
st.caption("A Streamlit app for YYC community guessing game")
