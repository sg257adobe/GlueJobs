import SimpleLambda.lambda_function.lambda_function as lf

def test_process_event():
    # Unit test for process_event function
    # Mocking the HTTP request for testing purposes
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code

    def mock_get(url):
        return MockResponse(200)

    lf.requests.get = mock_get
    assert lf.process_event({}) == 200
