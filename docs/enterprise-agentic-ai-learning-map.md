# Enterprise Agentic AI learning map

This map is the learning compass for the Cloud Spend + Procurement multi-agent capstone. It deliberately identifies concepts and readiness questions—not a complete implementation procedure.

[Open the interactive learning map](../.archify/workflow-enterprise-agent-learning-map-20261007-231357/enterprise-agent-learning-map.html)

## Destination

Build one conversational experience that can understand a request, route it to a Cloud Spend agent, a Procurement agent, or both, and return a consolidated response whose sources and decisions remain understandable.

## Progression

| Stage | Focus | Core libraries | Readiness questions |
|---|---|---|---|
| Days 1–2 | Practical Python for agent code | Standard library, `asyncio` | Can I explain functions, classes, exceptions, context managers, and why agent calls are asynchronous? |
| Day 3 | Foundry mental model | `azure-identity`, `azure-ai-projects` | Can I trace identity → project client → agent → conversation → response? |
| Day 4 | One code-based agent | `agent-framework-foundry` | What belongs in instructions, Python code, or a tool? Can I preserve a session across turns? |
| Days 5–6 | Safe tool boundaries | `pydantic`, `pydantic-settings`, `httpx` | Can I validate inputs and outputs? What should happen when an API is slow, invalid, or unavailable? |
| Days 7–9 | Multi-agent coordination | `agent-framework-orchestrations` | When should I route, hand off, run concurrently, or ask for clarification? How will I measure routing accuracy? |
| Days 10–12 | Enterprise reliability | `pytest`, `pytest-asyncio`, `tenacity`, OpenTelemetry | Which failures are safe to retry? Which actions require approval? Can I trace which specialist produced each claim? |

## Priority order

1. Understand ordinary Python control flow before adding autonomous behavior.
2. Build one dependable agent before creating a multi-agent system.
3. Treat Pydantic models as contracts between conversations, agents, and tools.
4. Prefer an explicit, testable router before an open-ended manager agent.
5. Add retries, authorization, approvals, evaluation, and observability before calling the design enterprise-ready.

## How we will use the Socratic method

For each stage, I will first ask you to predict or explain the behavior. You will make a small change or investigate a notebook. We will then compare the result with your mental model and use the mismatch—if any—to choose the next question.

The objective is not to memorize APIs. It is to become able to answer:

- What component owns this decision?
- What data crosses this boundary?
- What could fail here?
- How would I test that claim?
- Why is an agent needed instead of ordinary Python?
- What evidence would make me trust the result?

## Capstone checkpoint

You are ready to start integrating the capstone when you can sketch and defend this flow without copying it:

```text
User request
    ↓
Structured routing decision
    ├── Cloud Spend specialist
    ├── Procurement specialist
    └── Both specialists concurrently
    ↓
Validated specialist results
    ↓
Consolidated, attributable response
```

The capstone remains the destination. The immediate goal is mastering the next concept—not rushing to assemble every component at once.
