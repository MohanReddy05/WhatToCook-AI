from agent.agent import agent
from agent.image_decoder import choose_image_file,image_to_data_url,build_image_message
from dotenv import load_dotenv
from agent.system_prompt import chef_prompt
import langchain

load_dotenv()
langchain.debug = True

path = choose_image_file()
message = build_image_message(path,chef_prompt)


response = agent.invoke(
    {"messages":[message]}
)

print(response["messages"][-1].content)

# for msg in response["messages"]:
#     print("\n-------------------")
#     print("TYPE:", msg.type)
#     print("CONTENT:", repr(msg.content))
#     print("TOOL CALLS:", getattr(msg, "tool_calls", None))