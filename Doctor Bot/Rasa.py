import rasa
from rasa.shared.core.domain import Session
from rasa.shared.core.events import ActionExecuted
from rasa.shared.core.trackers import DialogueTracker

def greet_user(sender_id: str):
    """Greets the user."""
    session = Session()
    tracker = DialogueTracker.from_dict({
        "sender_id": sender_id,
        "session": session,
    })
    tracker.update(ActionExecuted("utter_greet"))
    return tracker.latest_message.data

def main():
    """Runs the chatbot."""
    response = greet_user("user_1")
    print(response)

if __name__ == "__main__":
    main()
