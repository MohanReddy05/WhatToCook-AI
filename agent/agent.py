from langchain.agents import create_agent
from tools import greetings
from models import model
from system_prompt import system_prompt
from langchain.messages import HumanMessage


agent = create_agent(
    model=model,
    tools=[greetings],
    system_prompt=system_prompt
)

response = agent.invoke(
    {"messages":[HumanMessage(content="Hello, my name is mohan")]}
)

print(response["messages"][-1].content)

print("------------------------------------------")

print(response["messages"])