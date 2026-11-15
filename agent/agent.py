from langchain.agents import create_agent
from .tools import web_search
from .models import model
from .system_prompt import system_prompt,chef_prompt
from langchain.messages import HumanMessage


agent = create_agent(
    model=model,
    tools=[web_search],
    system_prompt=system_prompt
)

# response = agent.invoke(
#     {"messages":[HumanMessage(content=chef_prompt)]}
# )

# print(response["messages"][-1].content)

