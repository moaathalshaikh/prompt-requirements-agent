# هذا السكربت يوضح كيف يمكن لوكيل ذكي اقتراح متطلبات من prompt

def extract_requirements(prompt: str):
    # مثال بسيط لمحاكاة توليد متطلبات من prompt
    # This script demonstrates how an intelligent agent can suggest requirements from a prompt.
    requirements = []
    if "chatbot" in prompt.lower():
        requirements.append("The system must respond to user inputs.")
        requirements.append("The chatbot should support Arabic and English.")
    if "login" in prompt.lower():
        requirements.append("The system must authenticate users securely.")
    return requirements

# تجربة
user_prompt = "I want to build a chatbot with login functionality"
reqs = extract_requirements(user_prompt)
for i, req in enumerate(reqs, 1):
    print(f"{i}. {req}")
