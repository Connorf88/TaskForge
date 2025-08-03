import azure.functions as func
import azure.durable_functions as df

def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)
    task_id = req.route_params.get("id")
    instance_id = client.start_new("orchestrator", None, task_id)
    return client.create_check_status_response(req, instance_id)
