# pip install ollama
from ollama import Client


class OllamaModel:

    def __init__(self, host: str = "http://localhost:11434", model: str = "llama3"):
        self._host: str = host
        self._model: str = model
        self._ollama = Client(host)

    def ask(
        self,
        prompt: str,
        format: str = "",
        temperature: float = 0.5,
        context_window: int = 2048,
    ):
        res = self._ollama.chat(
            model=self._model,
            messages=prompt,
            format=format,
            options={
                "temperature": temperature,
                "num_ctx": context_window,
            },
        )
        return res["message"]["content"]

# pip install groq
# api keys at: https://console.groq.com/keys
# groq models = llama3-8b-8192, llama3-70b-8192, mixtral-8x7b-32768
from groq import Groq


class GroqModel:

    def __init__(
        self,
        model: str = "llama3-8b-8192",
        api_key: str = "",
    ):
        self._model = model
        self._api_key = api_key
        self._groq = Groq(api_key=self._api_key)

    def ask(
        self,
        prompt: str,
        temperature: float = 0.5,
        max_tokens: int = 2048,
        format: str = "",
    ):
        if format == "json":
            return (
                self._groq.chat.completions.create(
                    messages=prompt,
                    model=self._model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    response_format={"type": "json_object"},
                )
                .choices[0]
                .message.content
            )
        else:
            return (
                self._groq.chat.completions.create(
                    messages=prompt,
                    model=self._model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                .choices[0]
                .message.content
            )


# openai models = gpt-4o-mini, gpt-4o, gpt-3.5-turbo, dall-e-3
from openai import OpenAI


class OpenAIModel:

    def __init__(
        self,
        model: str = "gpt-4o-mini",
        api_key: str = "",
    ):
        self._model = model
        self._api_key = api_key
        self._openai = OpenAI(api_key=self._api_key)

    def ask(
        self,
        prompt: str,
        temperature: float = 0.5,
        max_tokens: int = 2048,
        format: str = "",
    ):
        return (
            self._openai.chat.completions.create(
                messages=prompt,
                model=self._model,
                temperature=temperature,
                max_tokens=max_tokens,
                format=format,
            )
            .choices[0]
            .message.content
        )
