def build_prompt(email_text, tone):
    return (
        f"You are an email assistant. Read the email below and write 3 "
        f"distinct reply options in a {tone} tone.\n\n"
        f"Original email:\n{email_text}\n\n"
        f"Format each reply clearly as Option 1, Option 2, Option 3."
    )