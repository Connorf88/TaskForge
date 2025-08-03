import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    task_id = context.get_input()
    task = yield context.call_activity("activity_get_task", task_id)
    result = yield context.call_activity("activity_complete_task", task)
    return result

main = df.Orchestrator.create(orchestrator_function)
