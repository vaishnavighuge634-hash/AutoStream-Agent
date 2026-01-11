from intent import detect_intent
from tools import mock_lead_capture

print("🤖 AutoStream AI Agent Started (type 'exit' to quit)\n")

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    intent = detect_intent(user_input)

    if intent == "greeting":
        print("Bot: Hi! How can I help you with AutoStream today?")

    elif intent == "product_query":
        print("""
Bot: Our Plans:

Basic – $29/month
• 10 videos
• 720p

Pro – $79/month
• Unlimited videos
• 4K
• AI captions
""")

    elif intent == "high_intent":
        print("Bot: Great! Please share your details.")

        name = input("Bot: Your Name: ")
        email = input("Bot: Your Email: ")
        platform = input("Bot: Creator Platform (YouTube/Instagram): ")

        mock_lead_capture(name, email, platform)

    else:
        print("Bot: Sorry, I didn’t understand that.")
