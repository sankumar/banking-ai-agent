from openai import OpenAI
from config import OPENAI_API_KEY
from database import create_ticket, get_ticket_status
import re

client = OpenAI(api_key=OPENAI_API_KEY)

def positive_feedback_agent(customer_name="Customer"):
    prompt = f"""
Generate a warm thank-you message for a banking customer.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

def negative_feedback_agent(issue):
    ticket_id = create_ticket(issue)
    prompt = f"""
Generate an empathetic response mentioning ticket #{ticket_id}.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

def query_handler_agent(message):
    match = re.search(r"(\d{6})", message)
    if not match:
        return "Please provide a valid 6-digit ticket number."

    ticket_id = int(match.group())
    status = get_ticket_status(ticket_id)

    prompt = f"""
Respond with the ticket status.
Ticket #{ticket_id}: {status}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()
