from datetime import datetime

logs = []

def add_log(input_text, classification, agent, response):
    logs.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input": input_text,
        "classification": classification,
        "agent": agent,
        "response": response
    })

def get_logs():
    return logs
