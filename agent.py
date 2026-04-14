from langgraph.graph import StateGraph

def planner(state):
    task = state["input"]
    return {"plan": f"Steps required to complete the task: {task}"}

def executor(state):
    return {"output": f"Completed execution based on plan: {state['plan']}"}

graph = StateGraph()
graph.add_node("planner", planner)
graph.add_node("executor", executor)
graph.add_edge("planner", "executor")
graph.set_entry_point("planner")

agent = graph.compile()
