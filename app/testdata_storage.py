# Test Data Storage

# Sample image URLs for testing
TEST_IMAGES = {
    'sample1': 'https://example.com/sample1.jpg',
    'sample2': 'https://example.com/sample2.png'
}

# Sample API responses for testing
TEST_API_RESPONSES = {
    'success': {
        'status': 'success',
        'data': {'result': 'enhanced_image_url'}
    },
    'error': {
        'status': 'error',
        'message': 'Invalid API key'
    }
}

# Utility function to get test data
def get_test_data(data_type, key):
    """
    Retrieve test data based on type and key.
    :param data_type: Type of test data ('images' or 'api_responses')
    :param key: Key for the specific test data
    :return: Requested test data or None if not found
    """
    if data_type == 'images':
        return TEST_IMAGES.get(key)
    elif data_type == 'api_responses':
        return TEST_API_RESPONSES.get(key)
    return None
