# agent_logic/utils.py
def send_email(to: str, subject: str, body: str):
    # Pour une version de démonstration, nous nous contentons d'afficher dans la console.
    print(f"[EMAIL] À: {to} | Sujet: {subject}\nCorps: {body}")

def send_slack_message(channel: str, text: str):
    # Pour la démonstration, affichage dans la console.
    print(f"[SLACK] Canal: {channel}\nMessage: {text}")
