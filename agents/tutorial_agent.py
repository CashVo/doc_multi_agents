from agents.base_agent import BaseAgent

class TutorialAgent(BaseAgent):
    def __init__(self, llm_manager):
        """
        Initialize this Agent's LLM details
        """
        super().__init__(llm_manager)
        print("Tutorial Agent initailized")

    def generate_response(self, prompt):
        """
        Given the user prompt and additional instructions in the prompt_template,
        query the LLM and return the response.
        """
        prompt_template = f"""Role: You are an expert coder
            Instruction: Provide step by step instructions for the following scenario 
            Prompt: {prompt}
        """
        return "Tutorial Agent was called"
        #return self.llm_manager.query_llm(prompt)
