# AI Research Assistant with LangChain

An intelligent research assistant powered by LangChain and OpenAI's GPT models. This application can perform comprehensive research on any topic by leveraging multiple tools including web search, Wikipedia queries, Python code execution, and result saving capabilities.

## Features

- **Intelligent Research**: Uses advanced AI to understand and research complex topics
- **Multi-Tool Integration**:
  - DuckDuckGo web search for current information
  - Wikipedia queries for encyclopedic knowledge
  - Python REPL for calculations and data processing
  - File saving for research output persistence
- **Structured Output**: Provides organized research results with topics, summaries, sources, and tools used
- **Interactive Interface**: Command-line interface for user queries
- **Extensible Architecture**: Easy to add new research tools and capabilities

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Internet connection for web searches and Wikipedia queries

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd AI_LangChain
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

Run the research assistant:

```bash
python main.py
```

When prompted, enter your research query. For example:
- "What are the latest developments in quantum computing?"
- "Explain the theory of relativity"
- "Calculate the fibonacci sequence up to 100"

The assistant will:
1. Analyze your query
2. Use appropriate tools to gather information
3. Process and synthesize the data
4. Provide a structured response with topic, summary, sources, and tools used
5. Save the research output to `research_output.txt`

## Project Structure

- `main.py` - Main application file containing the LangChain agent setup and execution logic
- `tools.py` - Custom tool definitions for search, Wikipedia, Python REPL, and file saving
- `requirements.txt` - Python dependencies
- `research_output.txt` - Saved research results with timestamps
- `README.md` - This documentation file

## Dependencies

- `langchain` - Core LangChain framework
- `langchain-openai` - OpenAI integration
- `langchain-community` - Community tools and utilities
- `langchain-experimental` - Experimental tools including Python REPL
- `wikipedia` - Wikipedia API wrapper
- `duckduckgo_search` - DuckDuckGo search integration
- `python-dotenv` - Environment variable management
- `pydantic` - Data validation and serialization

## Configuration

The application uses the following models:
- Primary: GPT-5.5 (OpenAI)
- Alternative: Claude Sonnet 4-6 (Anthropic) - commented out in code

You can modify the model selection in `main.py` by uncommenting the appropriate LLM initialization.

## Output Format

Research results are structured as:
- **Topic**: The main subject of research
- **Summary**: Comprehensive summary of findings
- **Sources**: List of information sources used
- **Tools Used**: Tools leveraged during research

All outputs are automatically saved to `research_output.txt` with timestamps for record-keeping.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Disclaimer

This tool uses AI language models and web scraping. Results should be verified for accuracy and may not reflect the most current information. Always cross-reference important research findings.
