from .models import GroqModel, OllamaModel, OpenAIModel
from .utils import create_prompt

# Display mode enables printing of API requests and responses
display_requests = True
display_responses = True

# Debug mode enables comprehensive logging for detailed diagnostics
debug_mode = False

# Define color codes
COLORS = {
    'cyan': '\033[96m',
    'blue': '\033[94m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'reset': '\033[0m'
}

def print_color(message, color):
    print(f"{COLORS.get(color, '')}{message}{COLORS['reset']}")

def print_api_request(message):
    if not display_requests:
        return
    print_color(message, 'cyan')

def print_api_response(message):
    if not display_responses:
        return
    print_color(message, 'blue')

def print_debug(message):
    if not debug_mode:
        return
    print_color(message, 'yellow')

def print_error(message):
    print_color(message, 'red')

class Agent:
    def __init__(
        self,
        llm: object,
        custom_system_prompt: str = "You are an AI Assistant.",
        format: str = "",
        temperature: float = 0.5,
        max_tokens: int = 1024,
    ):

        self._llm = llm
        self._temperature = temperature
        self._format = format.lower()
        self._max_tokens = max_tokens
        self.message_prompt = []
        self.message_prompt.append(create_prompt("system", custom_system_prompt))

    def ask(self, prompt):
        self.message_prompt.append(create_prompt("user", prompt))

        if isinstance(self._llm, OllamaModel):
            response = self._llm.ask(
                self.message_prompt,
                temperature=self._temperature,
                format=self._format,
            )
        if isinstance(self._llm, GroqModel):
            response = self._llm.ask(
                self.message_prompt,
                temperature=self._temperature,
                max_tokens=self._max_tokens,
                format=self._format,
            )
        if isinstance(self._llm, OpenAIModel):
            response = self._llm.ask(
                self.message_prompt,
            )

        # self._chat_history.append(message_prompt)
        self.message_prompt.append(create_prompt("assistant", response))
        return response

class ReasoningAgent(Agent):

    def __init__(
        self,
        llm: object,
        custom_system_prompt: str = "You are an intelligent AI Assistant focused on clear reasoning and step-by-step analysis.  You break down complex problems methodically and explain your thought process transparently.  You aim to be precise, logical and thorough in your responses while maintaining a helpful and professional tone.",
        format: str = "",
        temperature: float = 0.5,
        max_tokens: int = 1024,
    ):

        self._llm = llm
        self._temperature = temperature
        self._format = format.lower()
        self._max_tokens = max_tokens
        self.message_prompt = []
        self.message_prompt.append(create_prompt("system", custom_system_prompt))

