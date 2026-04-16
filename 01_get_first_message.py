from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


load_dotenv()
model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.1, # Yaratıcılık seviyesi. 1'e yaklaştıkça artar, 0'a yaklaştıkça daha kesin cevaplar verir.
)

messages = [
    SystemMessage(
        content="Translate the following from English to Turkish",
    ),
    HumanMessage(
        content="Hi!"
    )
]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response.content)
