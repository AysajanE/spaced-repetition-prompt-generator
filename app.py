import gradio as gr
from openai import OpenAI
import anthropic
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI and Anthropic client
openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
claude_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Define system message
SYSTEM_MESSAGE = """You are an AI assistant specialized in creating effective spaced repetition prompts enhance learning and memory retention. Your task is to generate prompts based on the given text and optional topics. Follow these guidelines:

1. Understand the content before creating prompts. If the material is complex, provide a brief summary or explanation before creating prompts.
2. Identify and present an overview of the key concepts and main ideas before breaking down the information into detailed prompts.
3. Begin with fundamental concepts and definitions. Create prompts that cover basic information before moving on to more detailed or complex prompts.
4. Create simple, focused prompts for single facts or concepts. Simplify the material to the smallest, most easily digestible pieces of information. Each prompt should focus on a single fact or concept.
5. Use cloze deletions where appropriate. Create prompts by omitting key parts of sentences or concepts, requiring the learner to fill in the blanks. For example, "The capital of France is ___."
6. Where applicable, incorporate visual aids or describe visual elements related to the content to enhance retention.
7. Employ mnemonic techniques. Use mnemonic devices such as acronyms, rhymes, or associations to make memorization easier. Personalize these techniques to increase their effectiveness.
8. Avoid sets or enumerations. Break down sets and long lists into individual, simpler questions. Use overlapping cloze deletions if necessary to manage enumerations.
9. Use clear, concise language. Avoid unnecessary complexity to speed up learning and reduce errors.
10. Connect new information to previously learned concepts or commonly known facts to enhance contextual understanding.
11. Provide examples and context cues. Use personal or vivid examples to create stronger memory associations. Relate prompts to real-life experiences when possible.
12. Incorporate redundancy. Repeat important information in different ways to strengthen memory. Use both active and passive recall techniques.
13. Add dates to prompts for volatile information that changes over time. This helps track the currency and relevance of the knowledge.
14. Prioritize knowledge. Focus on the most important information first. Continuously improve and prioritize prompts based on their importance and the learner’s needs.

Generate a set of 5-20 prompts based on the input text and topics."""

OPENAI_MODEL = "gpt-4o"
ANTHROPIC_MODEL = "claude-3-haiku-20240307"
def generate_prompts(text, topics, model_choice):
    if not text:
        return "Please enter some text to generate prompts."
    
    if not model_choice:
        return "Please select an AI model."

    try:
        if model_choice == "GPT (OpenAI)":
            response = openai_client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_MESSAGE},
                    {"role": "user", "content": f"Text: {text}\nTopics: {topics}"}
                ],
                temperature=0,
            )
            return response.choices[0].message.content
        elif model_choice == "Claude (Anthropic)":
            response = claude_client.messages.create(
                model=ANTHROPIC_MODEL,
                max_tokens=1000,
                temperature=0,
                system=SYSTEM_MESSAGE,
                messages=[
                    {"role": "user", "content": f"Text: {text}\nTopics: {topics}"}
                ]
            )
            return response.completion
    except Exception as e:
        return f"An error occurred: {str(e)}"

def clear_inputs():
    return "", "", gr.Dropdown.update(value=None)

with gr.Blocks() as demo:
    gr.Markdown("# Spaced Repetition Prompt Generator")
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="Paste your text here", lines=10)
            topics = gr.Textbox(label="Enter topics (optional)")
            model_choice = gr.Dropdown(choices=["GPT (OpenAI)", "Claude (Anthropic)"], label="Select AI Model")
            
            with gr.Row():
                clear_btn = gr.Button("Clear")
                submit_btn = gr.Button("Submit")
        
        output = gr.Textbox(label="Generated Prompts", lines=10)
    
    submit_btn.click(generate_prompts, inputs=[input_text, topics, model_choice], outputs=output)
    clear_btn.click(clear_inputs, outputs=[input_text, topics])

demo.launch()