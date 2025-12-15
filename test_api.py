"""
Quick test script for the Email Decision API.
Run this AFTER starting the API server with: uvicorn api:app --reload --port 8000
"""
import requests
import json

API_URL = "http://127.0.0.1:8000"

def test_health():
    """Test the health endpoint."""
    response = requests.get(f"{API_URL}/health")
    print("Health check:", response.json())
    assert response.status_code == 200
    print("✅ Health endpoint works!\n")

def test_decide():
    """Test the decision endpoint."""
    payload = {
        "subject": "Production server is down",
        "body": "Users cannot log in since 10:20 AM and this affects multiple regions.",
        "intent": "urgent_issue",
        "urgency": "high"
    }
    
    response = requests.post(
        f"{API_URL}/decide",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    print("Decision endpoint response:")
    print(json.dumps(response.json(), indent=2))
    assert response.status_code == 200
    print("\n✅ Decision endpoint works!")

if __name__ == "__main__":
    print("Testing Email Decision API...\n")
    try:
        test_health()
        test_decide()
        print("\n🎉 All API tests passed!")
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API server.")
        print("Make sure you've started it with: uvicorn api:app --reload --port 8000")
    except Exception as e:
        print(f"❌ Error: {e}")

