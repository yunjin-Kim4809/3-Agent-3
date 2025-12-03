!pip install -U langchain langchain-community
!pip install -U langgraph langchain-openai

import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
load_dotenv()

tavily_tool = TavilySearchResults(
    api_key=os.environ["TAVILY_API_KEY"],
    max_results=5
)

import datetime
today = datetime.datetime.now().strftime("%Y년 %m월 %d일")

query = "오늘은 {today}야. 내일 서울 비 와?"
response = agent_executor.invoke({"messages": [HumanMessage(content=query)]})
print(response["messages"][-1].content)

query = "신촌역 최신 맛집 3개 추천해줘"
response = agent_executor.invoke({"messages": [HumanMessage(content=query)]})
print(response["messages"][-1].content)

query = "NVIDIA 최근 뉴스를 한국어로 요약해줘"
response = agent_executor.invoke({"messages": [HumanMessage(content=query)]})
print(response["messages"][-1].content)