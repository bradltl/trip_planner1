from crewai import Agent
from textwrap import dedent
#from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from langchain_community.llms import OpenAI
from langchain.tools import tool

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools


"""
Goal = Create a 7 day itinerary for a trip

Boss = Expert travel agent

Employee = City selection agent
Employee = Local tour guide agent

Notes:
- Agents should be results driven and have a clear goal
- Role is their job title
- Goals should be actionable
- Backstory should be a their resume


"""



# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        #self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        #self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics. I have decades of experience 
                             in the travel industry. I have planned trips for thousands of clients and 
                             have a deep understanding of the best destinations, accommodations, 
                             and activities. I am passionate about creating unforgettable 
                             travel experiences for my clients and ensuring that every detail is 
                             taken care of. I have a keen eye for detail and a knack for finding 
                             hidden gems that most travelers miss. I am dedicated to providing the 
                             highest level of service and making sure that every trip is a 
                             once-in-a-lifetime experience."""),
            goal=dedent(f"""Create a 7 day itinerary with detailed per-day plans,
                        include budget, packing suggetions, and travel tips."""),
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analyizing and selecting the best cities for travel."""),
            goal=dedent(f"""Select the best cities based on weather, season, prices, and 
                        traveler preferences."""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    
    def local_tour_guide(self):
        return Agent(
            role="Define agent 2 role here",
            backstory=dedent(f"""Knowledgeable local tour guide with years of experience and extensive
                             information about the city, its history, culture, and attractions."""),
            goal=dedent(f"""Provide the BEST insights and recommendations about the selected cities."""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )