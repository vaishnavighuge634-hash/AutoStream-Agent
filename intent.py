def detect_intent(user_input):
    text = user_input.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    if any(word in text for word in ["price", "pricing", "plan", "cost"]):
        return "product_query"

    if any(word in text for word in ["buy", "sign up", "subscribe", "want", "pro"]):
        return "high_intent"

    return "unknown"
