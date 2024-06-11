from bot import StoryBot


def main():
    story_bot = StoryBot(name="Storyteller")

    print("Greetings, curious adventurer. What tales do you seek today?")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Exiting...")
            break

        generated_story = story_bot.chat(user_input)
        print("Generated Story:")
        print(generated_story)

        save_story = input("Do you want to save the story to 'story.txt'? (y/n): ")
        if save_story.lower() == "y":
            story_bot.save_stories_to_file([generated_story], "story.txt")
            print("Story saved to 'story.txt'")


if __name__ == "__main__":
    main()
