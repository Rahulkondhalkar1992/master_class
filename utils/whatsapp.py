"""WhatsApp contact helpers."""

WHATSAPP_CONTACTS = [
    {
        "label": "WhatsApp 1",
        "number": "8655448143",
        "display": "+91 86554 48143",
        "url": "https://wa.me/918655448143",
    },
    {
        "label": "WhatsApp 2",
        "number": "8692016111",
        "display": "+91 86920 16111",
        "url": "https://wa.me/918692016111",
    },
]


def get_whatsapp_url(index: int = 0) -> str:
    """Return WhatsApp click-to-chat URL by contact index."""
    if index < 0 or index >= len(WHATSAPP_CONTACTS):
        return WHATSAPP_CONTACTS[0]["url"]
    return WHATSAPP_CONTACTS[index]["url"]
