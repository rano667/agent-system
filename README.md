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