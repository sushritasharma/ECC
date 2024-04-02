import requests
import threading
import matplotlib.pyplot as plt
import time

# Target URL to flood with requests
target_url = "http://example.com"

# Function to send HTTP requests
def send_requests(num_requests):
    response_times = []
    for _ in range(num_requests):
        try:
            start_time = time.time()
            response = requests.get(target_url)
            end_time = time.time()
            response_time = end_time - start_time
            response_times.append(response_time)
            print("Request sent")
        except Exception as e:
            print("Exception:", e)
    return response_times


# Get the number of requests from the user
num_requests = 4

# Send requests
response_times = send_requests(num_requests)


# Plotting the response times
plt.plot(range(1, num_requests+1), response_times)
plt.xlabel('Number of Requests')
plt.ylabel('Response Time (s)')
plt.title('Server Response Time vs Number of Requests')
plt.show()

exit()