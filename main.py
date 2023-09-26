# Following https://python.langchain.com/docs/get_started/quickstart tutorial
import credentials

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI(openai_api_key=credentials.APIKEY)
chat_model = ChatOpenAI(openai_api_key=credentials.APIKEY)

text = "what would be a good name for a new kitten?"
response = llm.predict(text)
print (response)
response = chat_model.predict(text)
print (response)
