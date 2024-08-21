from typing import Type, List
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
import subprocess

class CommandExecutionInput(BaseModel):
    commands: List[str] = Field(..., description="List of commands to execute")

class CommandExecutionTool(BaseTool):
    name: str = "Command Execution"
    args_schema: Type[BaseModel] = CommandExecutionInput
    description: str = "Execute a list of shell commands"

    def _execute(self, commands: List[str]):
        results = []
        for command in commands:
            try:
                result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
                results.append({"command": command, "output": result.stdout, "status": "success"})
            except subprocess.CalledProcessError as e:
                results.append({"command": command, "output": e.stderr, "status": "error"})
        return results
