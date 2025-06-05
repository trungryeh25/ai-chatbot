# Getting started
## Understanding Key Concepts
### Intents
In the context of chatbots and Natural Language Understanding (NLU), an **intent** is the **goal or purpose behind a user’s message** — what the user wants to achieve by saying something.

**Intents matter in a chatbot system**:
1. Identify what the user wants.
2. Determine how the system should respond.
3. Trigger specific APIs or actions (e.g., calling a weather API for check_weather).
4. Guide the flow of conversation.

### Entities
In chatbot and NLU systems, **entities** are **pieces of information extracted from the user’s message that help fill in the details** of an intent.

**Purpose of Entities**
1. Understand details of the user's request.
2. Collect parameters needed to fulfill an action.
3. Pass data to APIs or databases (e.g., search flights to "Hanoi" on "Friday").

### Example
User says `Book a flight to Hanoi on Friday.`
- **Intent**: `book_flight`
- **Entities**:
    - `"location": "Hanoi"`
    - `"date": "Friday"`

## Admin Panel
The admin panel serves as the central hub for managing your chatbot. You can use it for following:
* Configure and manage intents
* Create and edit entities
* Train your chatbot
* Test conversations in real-time
* Monitor conversation logs
* Manage Channel integrations (being implemented)

Access the admin panel at http://localhost:8080 after starting the application.

## Next Steps
[Create your first intent](https://github.com/trungryeh25/ai-chatbot/blob/master/docs/03-creating-order-status-check.md)