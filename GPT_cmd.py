from openai import OpenAI

def GPT_cmd_fcn(prompt, context, system_prompt):
    # The function sends commands to ChatGPT
    #   prompt - the user's prompt
    #   context - the user's past prompt and ChatGPT's reponses
    #   system_prompt - the system prompt

    # Initializtion to ChatGPT API
    client = OpenAI(api_key="PUT YOUR CHAT GPT'S API HERE")


    # Send a prompt to ChatGPT and receive a response
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "assistant",
                "content": context
            },
            {
                "role": "user",
                "content": prompt
            },
        ],
    )

    return completion.choices[0].message.content
