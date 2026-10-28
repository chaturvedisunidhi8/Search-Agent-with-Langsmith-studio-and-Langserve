from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_groq import ChatGroq
#from langgraph.checkpoint.memory import InMemorySaver
import os

###Tools    ----> Here we defined what this tool exactly do

@tool
def google_search(query:str) -> str:
    """
    Search Google for Up to date information on the web
    args:query:What so search on google
    Returns: Top Search results as plain texts


    """

    ## To create tool
    search=GoogleSerperAPIWrapper(serper_api_key=os.getenv("SERPER_API_KEY"))
    return search.run(query)  ## pass upcoming user query

##LLm =Groq

llm=ChatGroq(model="openai/gpt-oss-120b",api_key=os.getenv("GROQ_API_KEY"))   # no need to pass API key here but if you want the U can 

## Now we need Prompt

SYSTEM_PROMPT="""
 You are a helpful research assistant with access to google

"""

#Agent 
agent=create_agent(
    model=llm,
    tools=[google_search],
    system_prompt=SYSTEM_PROMPT ,  # import memory  using langGraph
)

#result = agent.invoke(
#    {"messages": [{"role": "user", "content": "Hello, father of computer science?"}]},
#    config={"configurable": {"thread_id": "1"}}
#)
#print(result["messages"][-1].content)


##[-1]	Selects the last item from the list.
