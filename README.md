DAY 1 — AGENT FOUNDATIONS

Nodes = actions
Edges = transitions
State = shared memory


START
  ↓
Research Node
  ↓
Summarizer Node
  ↓
END


agent-system/
│
├── app/
│   ├── main.py
│   ├── graph.py
│   ├── state.py
│   ├── nodes/
│   │   ├── planner.py
│   │   ├── researcher.py
│   │   └── summarizer.py
│   ├── tools/
│   │   └── search_tool.py
│
├── requirements.txt
└── README.md

run:

python -m app.main
---

DAY 2 — REAL AGENT BEHAVIOR
Now we introduce:
LLM
+
Tools
+
Decision Making
---
We want:
User Question
↓
LLM thinks
↓
Uses Tool
↓
Gets Information
↓
Stores Research
↓
Continues Workflow

---
Agent Architecture V1

START
  ↓
Planner Node
  ↓
Research Node
  ↓
Summarizer Node
  ↓
END
---
A tool is simply:
input
↓
function
↓
output
---
Why Mock Tool First?

Because we want to understand:

Agent
↓
Tool
↓
Result

before introducing:

Tavily
Serper
Web APIs
---
Agent decides:
I need information
↓
Call tool
↓
Use output
---
Why Add Planner?

Because agents don't just answer.

They:

Goal
↓
Plan
↓
Execute
↓
Evaluate

This is the foundation of agentic systems.
---
This is the first TRUE agent pattern:

Goal
↓
Planner
↓
Tool Usage
↓
Result
↓
Summary
---
Agent V2

Replace mock tool with:

Tavily Search API

Then:

Planner
↓
Web Search Tool
↓
Research
↓
Summary

My first real internet-connected agent.
---

Flow becomes:

Planner
↓
Tavily Search
↓
Web Results
↓
Summary
---
But There's A Problem

Current summary node:

summary = f"Summary: {research}"

That worked with mock data.

Now you'll get:

20 pages of search results dumped back

Ugly.
---
Agent V2 Needs An LLM

This is the perfect point to integrate Groq.

New Flow
Planner
↓
Web Search Tool
↓
Research Results
↓
Groq LLM
↓
Summary

Now the LLM transforms raw search results into a useful answer.
---
Agent V2 Architecture
User Query
↓
Planner Node
↓
Research Node
(Tavily)
↓
Summarizer Node
(Groq LLM)
↓
Final Answer

This is the first time an LLM is becoming part of your graph execution.
---
Result:

"query": "Latest Nvidia AI initiatives"

LLM Output:
**Key Findings:**
1. Nvidia has introduced six new AI chips and expanded its World Foundation Model line with Cosmos Reason 2, Cosmos Transfer 2.5, and Cosmos Predict.
2. The company has released new open models, including Nemotron 3, for building and implementing multi-agent systems.
3. Nvidia's Rubin platform combines diverse AI chips to accelerate agentic AI, advanced reasoning, and mixture-of-experts models.

**Important Technologies:**
1. Nvidia's NVLink interconnect technology
2. Transformer technologies
3. GPU-accelerated AI perception, simulation, and software
4. Open-weight models (e.g., OpenAI's gpt-oss-20b and gpt-oss-120b)

**Business Impact:**
1. Nvidia's initiatives aim to inspire customers to look beyond GPUs and see the whole underlying infrastructure as an AI factory.
2. The company's focus on open models and diverse AI chips can help drive breakthrough performance in AI-enabled applications and services.
3. Nvidia's technologies have the potential to transform various industries, including autonomous vehicles, healthcare, and cybersecurity.
---

Next Evolution (Agent V3)

we'll introduce the thing that makes LangGraph powerful:

Conditional Routing

Instead of:

Planner
↓
Research
↓
Summary

we'll do:

Planner
↓
Decision
├── Research
├── Calculator
├── RAG Tool
└── Memory Lookup

The graph will dynamically choose which tool to use.

That is the moment the system becomes a true decision-making agent. 🚀
---
The Problem

Suppose user asks:

What is 25 * 42?

Should we:

Search Tavily
↓
Summarize

No.

Waste of tokens.

Suppose user asks:

What products are in invoice 1213?

Should we:

Search Internet

No.

We should use your:

RAG System

Suppose user asks:

Latest Nvidia AI initiatives

Then:

Research Agent

makes sense.
---
Agent V3 Goal

The agent should decide:

Which tool should I use?
---
New Architecture
                ┌────────────┐
                │   Planner  │
                └─────┬──────┘
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
      Research     Calculator     RAG
       Agent         Tool        Tool
          │           │           │
          └───────────┼───────────┘
                      ▼
                Summarizer
                      ▼
                     END

This is the first genuinely agentic graph.

---
First New Concept

Conditional Edges

builder.add_conditional_edges(...)

instead of builder.add_edge("planner", "researcher")
---
This Is Actually A Design Smell

Your graph currently looks like:

Planner
 ↓
Conditional Route
 ↓
Research / Calculator / RAG
 ↓
One Universal Summarizer

The problem is:

Different routes
Different output requirements
---

Agent V3.5

Instead of:

Research
Calculator
RAG
 ↓
Same Summarizer

they do:

Research
 ↓
Research Summarizer

Calculator
 ↓
Calculator Formatter

RAG
 ↓
RAG Formatter

Each path has its own response style.
---

Research Route
Planner
 ↓
Researcher
 ↓
Research Summarizer
 ↓
END
Calculator Route
Planner
 ↓
Calculator
 ↓
END

Calculator already knows the answer.

No LLM needed.

RAG Route
Planner
 ↓
RAG
 ↓
END

Your RAG system already generates a user-ready answer.

No reason to summarize again.
---

Better Graph
                    Planner
                       │
         ┌─────────────┼─────────────┐
         │             │             │
         ▼             ▼             ▼
      Research     Calculator       RAG
         │             │             │
         ▼             ▼             ▼
 ResearchSummary      END           END
         │
         ▼
        END

Not every node should use an LLM.
---

Expected Results
Query
Latest Nvidia AI initiatives

Flow:

Planner
↓
Research
↓
ResearchSummary
↓
END

Output:

Key Findings...
Important Technologies...
Business Impact...
Query
calculate 25 * 42

Flow:

Planner
↓
Calculator
↓
END

Output:

25 * 42 = 1050
Query
What products are in invoice 1213?

Flow:

Planner
↓
RAG
↓
END

Output:

Actual invoice answer

No fake business impact nonsense.

What You Just Learned

This is one of the biggest transitions in agent design:

From:

One giant LLM does everything

to:

Specialized workflows

That's exactly how real agent systems evolve.
        
