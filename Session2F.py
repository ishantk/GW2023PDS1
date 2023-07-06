# WhatsApp
# Create MODEL

contact1 = {
    "name": "John",
    "phone": "+91 98765 12345"
}

conversation = [
    {
        "from": "+91 98765 11211",
        "to": "+91 98098 09809",
        "text": "Hello, How are You",
        "sent_time": "12:00",
        "status": 1
    },
    {
        "from": "+91 98098 09809",
        "to": "+91 98765 11211",
        "text": "I am fine",
        "sent_time": "12:02",
        "status": 1
    }
]

contact2 = {
    "name": "Fionna",
    "phone": "+91 98765 11211",
    "conversation": conversation
}

contact3 = {
    "name": "George",
    "phone": "+91 89898 11098"
}


whats_app = [ contact1, contact2, contact3 ]

# Assignment: Try To Model - PayTM, Amazon, Instagram :)