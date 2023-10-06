import streamlit as st

# App information and setup
project_title = "re:tune Chatbot"
project_desc = """
A Chatbot Implementation using re:tune https://retune.so/docs/chatgpt-for-your-business"""

project_icon = "icon.png"
st.set_page_config(page_title=project_title, initial_sidebar_state='expanded', page_icon=project_icon)

def main():
    head_col = st.columns([1, 8])
    with head_col[0]:
        st.image(project_icon)
    with head_col[1]:
        st.title(project_title)
    st.markdown(project_desc)

    st.components.v1.html("""
    <script
      src="https://retune.so/api/script/chat.js?id=11ee6456-70b2-6a90-9a7b-ef781cf4e2cc"
      defer
    ></script>""")


if __name__ == "__main__":
    main()