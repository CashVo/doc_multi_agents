from agents.base_agent import BaseAgent

class GlossaryAgent(BaseAgent):
    def __init__(self, llm_manager):
        """
        Initialize this Agent's LLM details
        """
        super().__init__(llm_manager)
        print("Glossary Agent initailized")

    def generate_response(self, prompt):
        """
        Given the user prompt and additional instructions in the prompt_template,
        query the LLM and return the response.
        """
        prompt_template = f"""Actor: You are an expert coder
            Instruction: Define the following term or concept 
            Prompt: {prompt}
        """
        return "Glossary Agent was called"
        #return self.llm_manager.query_llm(prompt)
