pip install locust

You can control the following parameters:

--users: Number of concurrent users (threads)
--spawn-rate: Ramp-up speed (users spawned per second)
--run-time: Total test duration (e.g., 5m for 5 minutes)
--headless: Run in command-line mode without UI
--html: Generate a report

locust --host=https://example.com --users 50 --spawn-rate 5 --run-time 5m --headless --html report.html

Credit -
https://apipheny.io/free-api/