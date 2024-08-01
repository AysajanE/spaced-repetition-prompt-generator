# Spaced Repetition Prompt Generator

## Description

The Spaced Repetition Prompt Generator is a web application that leverages AI to create effective spaced repetition prompts for enhanced learning and memory retention. This tool uses either OpenAI's GPT or Anthropic's Claude models to generate customized prompts based on user-provided text and optional topics.

## Features

- Generate spaced repetition prompts from input text
- Optional topic specification for more focused prompts
- Choice between GPT (OpenAI) and Claude (Anthropic) AI models
- User-friendly interface built with Gradio
- Clear and submit functionality

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/spaced-repetition-prompt-generator.git
   cd spaced-repetition-prompt-generator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ANTHROPIC_API_KEY=your_anthropic_api_key
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to the local URL provided by Gradio (usually `http://127.0.0.1:7860`).

3. Enter your text in the input box, optionally specify topics, and choose an AI model.

4. Click "Submit" to generate prompts.

5. Use the "Clear" button to reset the input fields.

## Dependencies

Main dependencies include:
- gradio
- openai
- anthropic
- python-dotenv

For a full list of dependencies, see the `requirements.txt` file.

## Configuration

The application uses the following AI models:
- OpenAI: GPT-4
- Anthropic: Claude 3 Haiku

You can modify the model choices in the `app.py` file if needed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Acknowledgements

- This project uses the Gradio library for the web interface.
- AI capabilities are provided by OpenAI's GPT and Anthropic's Claude models.