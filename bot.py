from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv
import getpass

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

model = ChatGroq(model='llama-3.3-70b-versatile', )

message = [
    HumanMessage("Olá, tudo bem?"),
    SystemMessage("traduza para o portugues para o japones ?")
]

model.invoke(message)


# system_template = "traduza para do portugues para o {idioma} ?"

# prompt_template = ChatPromptTemplate.from_messages(
#    [
#        ("system", system_template),
#        ("user", "{input}"),
#    ]
#     )
# prompt = prompt_template.invoke({"idioma": "japones", "input": "Ola tudo bem?"})

# response = model.invoke(prompt)

# print(response.content)
