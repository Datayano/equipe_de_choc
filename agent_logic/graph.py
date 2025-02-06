# agent_logic/graph.py
from langgraph.graph import StateGraph, START, END
from agents import web_search_agent, enrich_data_agent, compose_response_agent, notification_agent

def build_graph():
    # Utilisation d'un état sous forme de dictionnaire simple
    graph = StateGraph(dict)
    graph.add_node("compose_response", compose_response_agent)
    graph.add_node("web_search", web_search_agent)
    graph.add_node("enrich_data", enrich_data_agent)
    graph.add_node("notification", notification_agent)
    
    # Définition du flux :
    # Entrée -> compose_response -> web_search -> enrich_data -> compose_response -> notification
    graph.set_entry_point("compose_response")
    graph.add_edge("compose_response", "web_search")
    graph.add_edge("web_search", "enrich_data")
    graph.add_edge("enrich_data", "compose_response")
    graph.add_edge("compose_response", "notification")
    
    return graph

if __name__ == "__main__":
    state = {"query": "Quel est le dernier article sur l'intelligence artificielle ?"}
    graph = build_graph()
    result = graph.invoke({"state": state})
    print("Réponse finale :", result.get("final_response"))
