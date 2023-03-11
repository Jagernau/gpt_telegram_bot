from settings import openai



def get_message(prompt): 
    """
    Generates text completion based on given prompt using the OpenAI API.

    Args:
        prompt (str): Input text prompt for the API.

    Returns:
        str: Generated text completion.
    """
    completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt,temperature=0.5, max_tokens=1000)
    return completion.choices[0]['text']

def get_pic(prompt):
    """
    Generates image based on given prompt using the OpenAI API.

    Args:
        prompt (str): Input text prompt for the API.

    Returns:
        str: URL of the generated image.
    """
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")
    return response["data"][0]["url"]
