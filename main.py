from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
#from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool, python_repl_tool

# Load environment variables from .env file
load_dotenv()

# Define a Pydantic model for structured response
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Initialize the LLM and tools
llm = ChatOpenAI(model="gpt-5.5")
#llm2 = ChatAnthropic(model="claude-sonnet-4-6")

# Test the LLM
# response = llm.invoke("What is the meaning of life?")
# print(response)

# # Initialize the output parser and agent
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# # Define the prompt template with system instructions, placeholders for chat history and agent scratchpad, and human input
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate reasearch.
            Answer the user query and use necessary tools.
            Wrap the output in this frormat and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

# # Test with empty tools
# tools = []
# agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)

# # Test with tools
# # tools = [search_tool]
# tools = [search_tool, wiki_tool]
# # tools = [search_tool, wiki_tool, save_tool]
tools = [search_tool, wiki_tool, save_tool, python_repl_tool]
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)

# # Test with tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Test with runtime user input
query = input("What do you want to research? ")
raw_response = agent_executor.invoke({"query": query})

# # Test with hardcoded input
# # raw_response = agent_executor.invoke({"query": "Who is the President of India?"})

# # Test the LLM and agent
# # print(raw_response)

# # Test the LLM and agent & get structured response
structured_response = parser.parse(raw_response.get("output"))
# print(structured_response)
print("Topic: ",structured_response.topic)
print("Summary: ",structured_response.summary)
print("Sources: ",structured_response.sources)
print("Tools_used: ",structured_response.tools_used)

# # Error handling while passing the structured response to the agent
# try:
#     structured_response = parser.parse(raw_response.get("output"))
# except Exception as e:
#     print("Error parsing response:", e, "Raw response:", raw_response)