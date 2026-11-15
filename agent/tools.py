from langchain.tools import tool


@tool
def greetings(user:str)->str:
    """ This tool is used to greet the user"""
    return f"Welcome to the multiverse {user}"

