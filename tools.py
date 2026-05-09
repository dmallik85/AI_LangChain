from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool
from datetime import datetime


# Utility function to save research output to a text file
def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"

# Tool definition for saving text to a file
save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file."
)

# DuckDuckGo Search Tool
python_repl_func = PythonREPLTool()

# Tool definition for Python REPL
python_repl_tool = Tool(
    name="python_repl",
    func=python_repl_func.run,
    description=(
        "Execute Python code in a Python REPL. "
        "Use this for calculations, data processing, file operations, "
        "or testing small Python snippets. Input must be valid Python code."
    ),
)


# # DuckDuckGo Search Tool
# search = DuckDuckGoSearchRun()
# search_tool = Tool(
#     name="search",
#     func=search.run,
#     description="Search the web for information."
# )

# # Wikipedia Query Tool
# api_wrapper = WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=1000)
# wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)



# DuckDuckGo Search Tool
search = DuckDuckGoSearchRun()

# Define a safe wrapper function for DuckDuckGo search to handle exceptions and clean the query
def safe_duckduckgo_search(query: str) -> str:
    try:
        cleaned_query = query.replace("from duckduckgo", "").replace("DuckDuckGo", "").strip()

        if not cleaned_query:
            cleaned_query = query

        result = search.run(cleaned_query)

        if not result:
            return "No DuckDuckGo search results found."

        return result

    except Exception as e:
        return f"DuckDuckGo search failed: {type(e).__name__}: {str(e)}"

# Define the search tool using the safe wrapper function
search_tool = Tool(
    name="search",
    func=safe_duckduckgo_search,
    description="Search the web using DuckDuckGo. Use this for current or general web information."
)

# Wikipedia Query Tool with error handling
api_wrapper = WikipediaAPIWrapper(
    top_k_results=5,
    doc_content_chars_max=1000
)

# Define a safe wrapper function for Wikipedia search to handle exceptions and clean the query
def safe_wikipedia_search(query: str) -> str:
    try:
        result = api_wrapper.run(query)

        if not result:
            return "No Wikipedia result found."

        return result

    except Exception as e:
        return f"Wikipedia search failed: {type(e).__name__}: {str(e)}"

# Define the Wikipedia tool using the safe wrapper function
wiki_tool = Tool(
    name="wikipedia",
    func=safe_wikipedia_search,
    description="Search Wikipedia for encyclopedic information."
)


