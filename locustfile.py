from locust import HttpUser, task, between
class APIUser(HttpUser):
    wait_time = between(1, 3)  # Simulates user think time

    @task
    def get_request(self):
        #Perform a GET request.
        self.client.get("/api/items")

    @task
    def post_request(self):
        #Perform a POST request.
        payload = {"name": "New Item", "price": 100}
        headers = {"Content-Type": "application/json"}
        self.client.post("/api/items", json=payload, headers=headers)

    @task
    def put_request(self):
        #Perform a PUT request (Updating an existing resource).
        payload = {"name": "Updated Item", "price": 150}
        headers = {"Content-Type": "application/json"}
        self.client.put("/api/items/1", json=payload, headers=headers)

    @task
    def patch_request(self):
        #Perform a PATCH request (Partially updating a resource).
        payload = {"price": 200}
        headers = {"Content-Type": "application/json"}
        self.client.patch("/api/items/1", json=payload, headers=headers)

    @task
    def delete_request(self):
        #Perform a DELETE request.
        self.client.delete("/api/items/1")
