Nodes = actions
Edges = transitions
State = shared memory


START
  ↓
Planner Node
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