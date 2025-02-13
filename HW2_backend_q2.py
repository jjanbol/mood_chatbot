import os
from langchain import hub
from langchain.agents import AgentExecutor, create_structured_chat_agent, Tool
from langchain_google_vertexai import ChatVertexAI
from langchain.utilities import SerpAPIWrapper
from langchain.memory import ConversationBufferMemory  

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./key.json"
os.environ["SERPAPI_API_KEY"] = "593aa475d9f1f0be79ccb2192415ec6747ffea22b92862c4a3f7365af9d6bb9b"


llm = ChatVertexAI(
        model_name="gemini-1.5-pro-001",
        temperature=0,
        allow_image_uploads=False
    )

serp_tool = Tool(
        name="Search",
        func=SerpAPIWrapper().run,
        description="Search for the latest news related to a specific mood."
    )

tools = [
        Tool(
            name="Intermediate Answer",
            func=SerpAPIWrapper().run,
            description="News search"
        )
    ]

prompt = hub.pull("hwchase17/structured-chat-agent")

    # **Initialize Memory**
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # **Create Agent with Memory**
agent = create_structured_chat_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        memory=memory  # Add memory here
    )


input = '''
You are a professional AI psychologist that can determine the mood of a person by asking three different questions from the user. After these three questions of your choice, you will assign the mood a person is experiencing. 

You must let the user now what you mood the user is experiencing.

once you determined this mood, search and gather latest live news that is related to the mood in the following categories: politics, technology, business, sports, or comedy using the internet search. 

Do not just make up news on your own and you must use the custom tool api to do this. Other methods are not allowed.

You will provide three article summaries and their corresponding categories in TOTAL. NEVER break this character and never return extra.

Follow this template for returning:
1. Category: Article name - Summary
2. Category: Article name - Summary
3. Category: Article name - Summary



'''


input2 = '''
"You are an AI psychologist. Determine my mood with three questions and then retrieve only three articles based on the mood in the field of politics, technology, business, sports, or comedy."
'''


def run_llm():

    output = agent_executor.invoke({
        "input": input
    })


    
    return output["output"]




def run_llm2(input):

    output = agent_executor.invoke({
        "input": input
    })
    
    return output["output"]
