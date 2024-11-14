class BaseAgent:
    def __init__(self, llm_manager):
        self.llm_manager = llm_manager

    # Each agent will need to define their own model information
    # e.g.: index specific content and choose appropriate chat_mode
    def init_model(self):
        raise NotImplementedError
    
    def generate_response(self, prompt):
        raise NotImplementedError

    def breakdown_and_respond(self, prompt):
        # Use LlamaIndex's agent and worker to handle complex queries
        tasks = prompt.split(" and ")
        responses = []
        for task in tasks:
            responses.append(self.generate_response(task.strip()))
        return " ".join(responses)

    def query_llm(self, prompt):
        ''' Direct query to the LLM '''

        print(f"Querying LLM: {prompt}")
        return self.chat_engine.chat(prompt)
