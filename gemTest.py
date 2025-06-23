import google.generativeai as genai

def summarize_text_with_gemini(api_key, text, model_name="gemini-2.0-flash"): #changed from gemini-pro to gemini-1.0-pro
    """
    Summarizes the given text using the Gemini model.

    Args:
        api_key: Your Google Generative AI API key.
        text: The text to summarize.
        model_name: The name of the Gemini model to use (e.g., "gemini-2.0-flash").

    Returns:
        The summarized text, or None if an error occurs.
    """
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)

        prompt = f"""
        Summarize the following text:

        {text}
        """
        generation_config = genai.types.GenerationConfig(
            max_output_tokens=2048,
            temperature=0.9,
            top_p=1
        )

        response = model.generate_content(prompt, generation_config=generation_config)
        return response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    # Replace with your actual API key and text
    api_key = "AIzaSyAsp5Aa8AYC3VyKNeTW450WlYZkxZ2QTCo" #replace with your api key.
    text_to_summarize = """
    The quick brown fox jumps over the lazy dog. This is a classic pangram, a sentence that uses all the letters of the alphabet.
    It is often used to test fonts and keyboards. The fox is a small, agile mammal known for its cunning.
    Dogs, on the other hand, are domesticated canines that have been loyal companions to humans for thousands of years.
    They come in various breeds, each with its own unique characteristics.
    The weather today is sunny and warm, perfect for a walk in the park.
    Many people are enjoying the sunshine, picnicking and playing games.
    """

    summary = summarize_text_with_gemini(api_key, text_to_summarize)

    if summary:
        print("Summary:")
        print(summary)
    else:
        print("Failed to generate summary.")
