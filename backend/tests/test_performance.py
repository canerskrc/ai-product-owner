from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def test_list_requirements(self):
        self.client.get("/requirements")

    @task(1)
    def test_add_requirement(self):
        requirement_data = {
            "title": "Performance Test",
            "description": "Testing system under load"
        }
        self.client.post("/requirements", json=requirement_data)
