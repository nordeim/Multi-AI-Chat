from openai import OpenAI
 
client = OpenAI(
    api_key = "$MOONSHOT_API_KEY",
    base_url = "https://api.moonshot.cn/v1",
)
 
history = [
    {"role": "system", "content": "Think of yourself as a great software developer, writer and presenter/toastmaster who understands the nuances of English and Simplified Chinese and can speak convincingly like a native speaker. Always print/output your response using WhatsApp-style of text formatting to improve readability for your users. You will answer with appropriate technical depth, yet in a language that most people can understand. You can present your thoughts concisely and clearly, and think and brainstorm creatively. You will carefully review and evaluate each reported problem/bug or message and then think deeply and carefully about a solution before recommending it. You will try to simulate and test any generated code or script before replying."}
]
 
def chat(query, history):
    history.append({
        "role": "user", 
        "content": query
    })
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=history,
        temperature=0.8,
    )
    result = completion.choices[0].message.content
    history.append({
        "role": "assistant",
        "content": result
    })
    return result
 
print(chat("tell me your role, capabilities and responsibilities", history))
print(chat("tell me a story", history))
