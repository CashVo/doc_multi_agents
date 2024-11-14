from flask import Flask, render_template, request
from load_data import load_data
from llm_manager import LLMManager
from llama_index.core.agent import ReActAgent

app = Flask(__name__)
llm_manager = LLMManager()

query_tools = load_data()
agent = ReActAgent.from_tools(
    query_tools,
    llm = llm_manager.llm,
    verbose = True,
    context = """ You are a PyTorch doc expert. You know everything there is to know about what it is, how to use it.
    You can provide concise answers about PyTorch. You can also provide step-by-step instructions for how to use it.
    However, you are not to answer any question outside of PyTorch. If you detech a question outside of PyTorch, kindly ask the
    user to rephrase their question. Be helpful and give them an example question that you could asnswer.
"""
)
print("ReAct agent initialized!!! Reay to chat...")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    print("Start chatting...")
    user_input = request.json.get("user_input")
    if not user_input:
        return {"error": "Prompt is required"}, 400

    # Generate response 
    response = agent.chat(user_input)

    html_response = f"<p> {response} </p>"

    return { "response": html_response }, 200

if __name__ == "__main__":
   app.run(debug=True)
