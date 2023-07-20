# WhatsApp Contact List :)
contacts = [
    {
        "name": "Jonnathon",
        "phone": "98765 12345",
        "conversations": [
                            "hi",
                            "Hello",
                            "This is awesome day",
                            "Lets go and play"
                         ]
    },
    {
        "name": "Fionna",
        "phone": "99811 22112",
        "conversations": [
            "hola",
            "Whats up",
            "I am good",
            "How's your day"
        ]
    },
    {
        "name": "George",
        "phone": "77651 11221",
        "conversations": [
            "heya",
            "lets go for a WALK",
            "Wow. Lets catch up",
            "thanks"
        ]
    }
]

search_keyword = input("Enter Keyword to Search..")
print("search_keyword:", search_keyword)

# Assignment: Implement Search on Conversation as well
for contact in contacts:
    # if contact["name"].lower().startswith(search_keyword.lower()):
    # if contact["name"].lower().__contains__(search_keyword.lower()):
    if contact["name"].lower().find(search_keyword.lower()) >= 0 \
            or contact["phone"].find(search_keyword) >= 0:
        print(contact)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")