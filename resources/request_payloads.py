def create_post_payload():
    return {
        "title": "Test Post",
        "body": "This is a test post.",
        "userId": 500
    }


def update_post_payload():
    return [{
        "title": "Updated Post",
        "body": "This post has been updated.",
        "userId": 28
    }, {
        "id": 1
    }]
