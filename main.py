import streamlit as st
import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from RAG_Chatbot import show_rag_chatbot


def main():
    show_rag_chatbot()
    
if __name__ == "__main__":
    main()