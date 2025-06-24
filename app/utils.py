def log_call_request(client):
    with open("call_logs.txt", "a") as log:
        log.write(
            f"{client.client_name} | {client.phone_number} | Qarz: {client.debt} | Muddat: {client.due_date}\n"
        )
