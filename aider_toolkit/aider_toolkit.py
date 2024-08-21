from typing import List
from superagi.tools.base_tool import BaseTool, BaseToolkit, ToolConfiguration
from .aider_tool import AiderTool
from .command_execution_tool import CommandExecutionTool
from superagi.types.key_type import ToolConfigKeyType

class AiderToolkit(BaseToolkit):
    name: str = "Aider Toolkit"
    description: str = "Toolkit for AI-assisted coding with Aider and command execution capabilities"

    def get_tools(self) -> List[BaseTool]:
        return [AiderTool(), CommandExecutionTool()]

    def get_env_keys(self) -> List[ToolConfiguration]:
        return [
            ToolConfiguration(key="OPENAI_API_KEY", key_type=ToolConfigKeyType.STRING, is_required=True, is_secret=True),
            ToolConfiguration(key="ANTHROPIC_API_KEY", key_type=ToolConfigKeyType.STRING, is_required=True, is_secret=True),
            ToolConfiguration(key="OPENROUTER_API_KEY", key_type=ToolConfigKeyType.STRING, is_required=True, is_secret=True)
        ]
