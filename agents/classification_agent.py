
class ClassificationAgent:
    def __init__(self, llm_manager):
        self.llm_manager = llm_manager
        self.chat_engine = llm_manager.init_index(chat_mode="simple")
        print("Classification Agent initailized")

    def classify(self, prompt):
        """
        Given the user prompt, classify what content type it is.
        Returns:
            One of these key terms: [conceptual, tutorial, glossary, api, other]
        """
        # Define prompt engineering for classification
        prompt_template = (
            f"""
            Context: You software developer seeking technical content information.
            Instruction: Classify the following prompt as one of the following content types: 
            [conceptual, tutorial, glossary, api, other] 
            Return only the classification keyword
            Prompt: {prompt}
            """
            # Author note: was thinking providing this would help but LLM seems to be more confused
            # Type definition: Use these definitions to help you classify
            # - Conceptual: Questions that primarily seeking understanding and facts
            # - Tutorial: Questions that primarily seeking instructions for how to do something with code
            # - Glossary: Questions primarily seeking definition of terms or concepts
            # - API: Questions primarily seeking code snippet, code sample, or API references
            # - Other: Any questions that does not fall into any of content types in this list
        )
        response = self.query_llm(prompt_template).response.strip().lower()
        
        # Ensure the response is one of the expected classifications
        print(f"Classify query as: {response}")
        if response in {"conceptual", "tutorial", "glossary", "api", "other"}:
            return response
        return "other"

    def suggest_prompt(self, prompt):
        """
        Given the user input, suggest a question the user can ask about it.
        Returns:
            A response containing the suggested question.
        """
        prompt_template = (
            f"""
            Context: You are a software developer.
            Instruction: Rewrite the following prompt as a question so that it can be classify as one of the following content types: 
            [conceptual, tutorial, glossary, api] 
            Prompt: {prompt}
            """
        )
        response = self.query_llm(prompt_template)
        print(f"Prompt suggestion: \n- Original: {prompt} \n- Suggestion: {response}")
        return response
    