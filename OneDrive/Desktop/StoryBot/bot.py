import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


class StoryBot:
    def __init__(self):
        # Load pre-trained model and tokenizer
        self.model = GPT2LMHeadModel.from_pretrained("gpt2-medium")
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")

        # Set maximum length for generated stories
        self.max_length = 1000

    def __call__(self, user_prompt: str) -> str:
        # Tokenize user input
        input_ids = self.tokenizer.encode(user_prompt, return_tensors='pt')

        # Generate story based on user input
        with torch.no_grad():
            outputs = self.model.generate(
                input_ids,
                max_length=self.max_length,
                pad_token_id=self.tokenizer.eos_token_id,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                top_k=50,
                top_p=0.95,
                temperature=1.0,
                do_sample=True
            )

        # Decode and return the generated story
        story = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return story


# Instantiate the StoryBot
story_bot = StoryBot()

# Generate and print a story based on user input
user_prompt = "Once upon a time"
generated_story = story_bot(user_prompt)
print(generated_story)

# Save story to a txt file (Stretch Goal)
with open("story.txt", "a") as file:
    file.write(generated_story)
