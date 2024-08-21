# SuperAGI Aider Toolkit

This toolkit integrates Aider, an AI-assisted coding tool, and command execution capabilities into SuperAGI.

## Features

1. **Aider Integration:** Run Aider sessions for AI-assisted coding directly from SuperAGI.
2. **Command Execution:** Execute shell commands as part of your SuperAGI workflows.
3. **Multi-Model Support:** Use OpenAI, Anthropic, or OpenRouter models with Aider.

## Setup

1. Ensure you have SuperAGI installed and set up.
2. Copy the contents of this directory into your SuperAGI installation under `superagi/tools/aider_toolkit/`.
3. Install Aider in your SuperAGI environment:
   ```
   pip install aider-chat
   ```
4. Add your API keys in the SuperAGI dashboard under the Aider Toolkit configuration:
   - OpenAI API key for GPT models
   - Anthropic API key for Claude models
   - OpenRouter API key for OpenRouter models

## Usage

In your SuperAGI agents, you can now use the Aider tool for AI-assisted coding and the Command Execution tool for running shell commands.

### Aider Tool

Use this tool to start an Aider session, provide coding instructions, and get AI-assisted code modifications. 
Example usage:
```python
aider_tool.execute(
    model="gpt-4",  # or "claude-2" or "openrouter/anthropic/claude-2"
    message="Create a Python function to calculate fibonacci numbers",
    files=["my_math.py"]
)
```

### Command Execution Tool

Use this tool to run shell commands as part of your SuperAGI workflows.
Example usage:
```python
command_tool.execute(
    commands=["git status", "npm install", "python test.py"]
)
```

## Configuration

In the SuperAGI dashboard, navigate to the Aider Toolkit configuration page to set up your API keys:
- OPENAI_API_KEY
- ANTHROPIC_API_KEY
- OPENROUTER_API_KEY

## Security Considerations

- Ensure that your API keys are kept secure and not exposed in logs or outputs.
- Be cautious when using the Command Execution tool, as it can run arbitrary shell commands.
- Review and test the code changes suggested by Aider before committing them to your project.

