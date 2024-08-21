from typing import Type, Optional
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
import subprocess
import os

class AiderToolInput(BaseModel):
    model: str = Field(..., description="The model to use for Aider (e.g., 'gpt-4', 'claude-2', 'openrouter/anthropic/claude-2')")
    message: str = Field(..., description="The message to send to Aider")
    files: Optional[list] = Field(default=None, description="List of files to include in the Aider session")

class AiderTool(BaseTool):
    name: str = "Aider"
    args_schema: Type[BaseModel] = AiderToolInput
    description: str = "Run an Aider session for AI-assisted coding"

    def _execute(self, model: str, message: str, files: Optional[list] = None):
        if 'gpt' in model.lower():
            api_key = self.get_tool_config("OPENAI_API_KEY")
            os.environ["OPENAI_API_KEY"] = api_key
        elif 'claude' in model.lower() and 'openrouter' not in model.lower():
            api_key = self.get_tool_config("ANTHROPIC_API_KEY")
            os.environ["ANTHROPIC_API_KEY"] = api_key
        elif 'openrouter' in model.lower():
            api_key = self.get_tool_config("OPENROUTER_API_KEY")
            os.environ["OPENROUTER_API_KEY"] = api_key
        else:
            return f"Unsupported model: {model}. Please use a GPT, Claude, or OpenRouter model."

        command = ["aider", "--model", model]
        
        if files:
            command.extend(files)
        
        try:
            process = subprocess.Popen(
                command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            stdout, stderr = process.communicate(input=message)
            
            if process.returncode != 0:
                return f"Aider session failed with error: {stderr}"
            
            return stdout
        except Exception as e:
            return f"An error occurred while running Aider: {str(e)}"
