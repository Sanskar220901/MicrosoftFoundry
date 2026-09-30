# Microsoft Foundry + OpenAI: Mental Model for Beginners

This notebook is a small example of one thing:

> It connects to a Microsoft Foundry project, logs in securely, asks a model a question, and prints the answer.

If you only remember one sentence, remember this:

> Load settings -> sign in -> connect to project -> send prompt -> show response

---

## The big idea

Think of this notebook like ordering food at a restaurant.

- The `.env` file is your menu and order details.
- `DefaultAzureCredential()` is the waiter who proves who you are.
- `AIProjectClient` is the kitchen connection that knows where your restaurant is.
- `openai_client.responses.create(...)` is you actually placing the order.
- `response.output_text` is the food that arrives back from the kitchen.

The model is not magic. It is just a service that receives a prompt and returns text.

---

## Mermaid mental model

```mermaid
flowchart LR
    A[".env file<br/>FOUNDRY_PROJECT_ENDPOINT<br/>MODEL_DEPLOYMENT_NAME"] --> B[load_dotenv()]
    B --> C[os.getenv()]
    C --> D[foundry_project_endpoint]
    C --> E[model_deployment_name]

    D --> F["AIProjectClient<br/>endpoint + DefaultAzureCredential()"]
    E --> G["openai_client = project_client.get_openai_client()"]
    F --> G

    G --> H["responses.create<br/>model + instructions + input"]
    H --> I[AI model returns response]
    I --> J[response.output_text]
    J --> K[print(...)]

    K --> L[Answer shown in notebook]
```

---

## Step-by-step explanation, cell by cell

### 1) Install the required libraries

```python
%pip install azure-ai-projects==2.0.0b2 openai==1.109.1 python-dotenv azure-identity
```

This installs the Python tools needed for the notebook.

Simple explanation:

- `azure-ai-projects` lets Python talk to Azure AI Foundry
- `openai` gives us the OpenAI-style client
- `python-dotenv` lets us read values from a `.env` file
- `azure-identity` helps us log in to Azure without hardcoding secrets

Analogy:

This is like getting the right tools and ingredients before cooking.

---

### 2) Import the libraries

```python
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
```

This brings in the functions/classes we will use.

Simple explanation:

- `import os` gives access to environment variables
- `load_dotenv` reads values from the `.env` file
- `DefaultAzureCredential` helps us authenticate to Azure
- `AIProjectClient` is the connection object for the Foundry project

Analogy:

This is like unpacking your tools on the workbench before starting the task.

---

### 3) Load environment variables

```python
load_dotenv()
```

This tells Python: "look for a `.env` file and load its values into the program."

Simple explanation:

The `.env` file usually contains things like:

```text
FOUNDRY_PROJECT_ENDPOINT=https://your-project-url
MODEL_DEPLOYMENT_NAME=gpt-4o-mini
```

This keeps important settings separate from the code.

Analogy:

Instead of writing the address and order details directly on the table, you keep them in a note card you can read anytime.

---

### 4) Get the endpoint and model name

```python
foundry_project_endpoint = os.getenv("FOUNDRY_PROJECT_ENDPOINT")
model_deployment_name = os.getenv("MODEL_DEPLOYMENT_NAME")
```

This reads the values from the environment.

Simple explanation:

- `os.getenv("FOUNDRY_PROJECT_ENDPOINT")` gets the project URL
- `os.getenv("MODEL_DEPLOYMENT_NAME")` gets the model name to use

If the variable does not exist, Python returns `None`.

Analogy:

This is like grabbing the address and the name of the dish from your notes before you order.

---

### 5) Create the AI Foundry project client

```python
project_client = AIProjectClient(
    endpoint=foundry_project_endpoint,
    credential=DefaultAzureCredential()
)
```

This creates the object that points to your Azure AI Foundry project.

Simple explanation:

- `endpoint` tells it where the project is located
- `DefaultAzureCredential()` tells it how to log in to Azure

This does not send any prompt yet. It simply creates a connection object.

Analogy:

This is like opening the restaurant connection and telling the system where the kitchen is and who you are.

---

### 6) Get the OpenAI-compatible client

```python
openai_client = project_client.get_openai_client()
```

This converts the Azure project client into a client that works like the OpenAI client you are used to.

Simple explanation:

The Foundry project is the Azure-side wrapper. This method gives you the model-calling interface.

Analogy:

This is like getting the specific ordering system the restaurant uses so you can place your order.

---

### 7) Send a prompt to the model

```python
response = openai_client.responses.create(
    model=model_deployment_name,
    instructions="You are a helpful AI assistant.",
    input="Can you tell me about Microsoft Foundry?"
)
```

This is the main action of the notebook.

Simple explanation:

- `model` = which model should answer
- `instructions` = how the assistant should behave
- `input` = the actual user question

This is the moment where the model is asked to respond.

Analogy:

This is like handing a waiter your order: the dish name is the model, the instructions are extra cooking preferences, and the input is the exact request.

---

### 8) Print the response

```python
print(f"Response output: {response.output_text}")
```

This displays the returned answer in the notebook.

Simple explanation:

- `response.output_text` is the text produced by the model
- `print(...)` shows it in the output area

Analogy:

This is like receiving the dish from the kitchen and showing it to the customer.

---

## Why this pattern matters

This pattern is used in almost every AI app:

1. Configure the project
2. Authenticate securely
3. Create a client
4. Send prompt/instructions
5. Read the model output

It is the basic building block of AI workflows.

Once you understand this, you can reuse it for:

- chat apps
- document analysis
- AI agents
- summarization tools
- Q&A systems

---

## Easy memory sentence

Use this as your internal cheat sheet:

> "Load values, log in, connect, ask, print."

Or even shorter:

> "Config -> Auth -> Client -> Prompt -> Output"

That is the real mental model behind this notebook.

---

## Beginner-friendly summary

This notebook is basically a "hello world" for Azure AI Foundry + OpenAI.

It is doing less than it looks like:

- it is not doing anything complicated
- it is just connecting to a model service and asking a question
- the tough-looking code is mostly just setup boilerplate

Once you know the pattern, you can swap in different questions, different models, and different workflows without memorizing every line.

---

## The one thing to remember

The key to understanding this code is not the syntax alone.
The key is the flow:

```text
.env file  ->  Python reads values  ->  Azure login  ->  project connection  ->  model call  ->  answer shown
```

That flow is the real lesson.
