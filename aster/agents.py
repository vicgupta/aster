from .models import GroqModel, OllamaModel, OpenAIModel
from .utils import create_prompt


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
        self._system_prompt = custom_system_prompt
        self._temperature = temperature
        self._format = format.lower()
        self._max_tokens = max_tokens
        self._history = []

    def ask(self, prompt):
        message_prompt = []
        message_prompt.append(create_prompt("system", self._system_prompt))
        message_prompt.append(create_prompt("user", prompt))

        if isinstance(self._llm, OllamaModel):
            response = self._llm.ask(
                message_prompt,
                temperature=self._temperature,
                format=self._format,
            )
        if isinstance(self._llm, GroqModel):
            response = self._llm.ask(
                message_prompt,
                temperature=self._temperature,
                max_tokens=self._max_tokens,
                format=self._format,
            )
        if isinstance(self._llm, OpenAIModel):
            response = self._llm.ask(
                message_prompt,
            )

        self._history.append(message_prompt)
        self._history.append(create_prompt("agent-reply", response))
        return response
