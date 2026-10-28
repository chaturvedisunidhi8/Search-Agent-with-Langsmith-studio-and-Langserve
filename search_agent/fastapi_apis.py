from fastapi import FastAPI
from langserve import add_routes
from agents import agent

app=FastAPI(title="Google Search Agent", description="A FastAPI app for the Search Agent", version="1.0.0")
#now we have to connect the routes of this app with the routes of agent which we have created in agents.py file 
add_routes(app, agent,path="/search-agent")  # this will add the routes of agent to the app


##SO here along with APIs of fastapi ,API of langserve agent api will also run 

