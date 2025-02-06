# agent_logic/agents.py
from langchain import PromptTemplate

# Outil fictif pour la démonstration (par exemple, un générateur de nom à partir d'un entier)
def dummy_tool(x: int) -> str:
    return f"NomGénéré_{x}"

def web_search_agent(state: dict) -> dict:
    query = state.get('query', '')
    # Simulation d'une recherche web
    result = f"Résultat de recherche web pour: {query}"
    state.setdefault('search_results', []).append(result)
    return state

def enrich_data_agent(state: dict) -> dict:
    query = state.get('query', '')
    # Simulation d'enrichissement via Qdrant (données fictives)
    enriched = f"Données enrichies pour: {query}"
    state['enriched_data'] = enriched
    return state

def compose_response_agent(state: dict) -> dict:
    template = PromptTemplate(
        input_variables=["query", "search_results", "enriched_data"],
        template="""Vous êtes un assistant intelligent.

Requête utilisateur: {query}

Résultats web:
{search_results}

Données contextuelles:
{enriched_data}

Rédigez une réponse finale:"""
    )
    prompt = template.format(
        query=state.get('query', ''),
        search_results="\n".join(state.get('search_results', [])),
        enriched_data=state.get('enriched_data', 'Aucune donnée')
    )
    
    # Instanciation du client LLM avec DeepSeek R1 en mode "json"
    from deepseek_llm import DeepSeekLLM
    llm_client = DeepSeekLLM(model="deepseek-r1:14b", format="json")
    # Pour activer le workaround, nous lions un outil fictif dummy_tool
    llm_client.bind_tools([dummy_tool])
    
    response = llm_client.generate(prompt)
    state['final_response'] = response
    return state

def notification_agent(state: dict) -> dict:
    final_response = state.get('final_response', '')
    # Simulation : affichage en console des notifications
    print("=== Notification ===")
    print("Envoi par email :")
    print(final_response)
    print("Envoi sur Slack :")
    print(final_response)
    return state
