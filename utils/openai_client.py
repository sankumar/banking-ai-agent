import os
from openai import OpenAI

def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        try:
            import streamlit as st
            api_key = st.secrets["OPENAI_API_KEY"]
        except Exception:
            pass

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is missing. "
            "Set it as an environment variable or Streamlit secret."
        )

    return OpenAI(api_key=api_key)
