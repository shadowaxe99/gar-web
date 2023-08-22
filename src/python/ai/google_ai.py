
import google.cloud.aiplatform as aiplatform

class GoogleAI:
    def __init__(self, project_id, location):
        self.project_id = project_id
        self.location = location
        self.client_options = {"api_endpoint": f"{location}-aiplatform.googleapis.com"}
        self.client = aiplatform.gapic.PredictionServiceClient(client_options=self.client_options)

    def predict(self, model_id, payload):
        endpoint = self.client.endpoint_path(
            project=self.project_id, location=self.location, endpoint=model_id
        )
        response = self.client.predict(endpoint=endpoint, instances=[payload])
        return response
