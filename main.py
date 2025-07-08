import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    
    args = sys.argv[1:]

    if not args:
        print("Usage: uv run main.py [your prompt here]")
        sys.exit(1)
    
    verbose_enabled = False

    if args[-1] == "--verbose":
        verbose_enabled = True
        args.pop()

    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = generate_content(client, messages)

    print("Response:")
    print(response.text)

    if verbose_enabled:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")



def generate_content(client, messages):
    response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages)
    return response

if __name__ == "__main__":
    main()
