import requests

class DiscordNotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path == '/':  # Notify only on homepage visits
            self.send_discord_notification(request)
        return response

    def send_discord_notification(self, request):
        webhook_url = 'https://discord.com/api/webhooks/1381693946006212849/0bkKdB4x-xnksBsfvbJn9ZC9ZEeZ8YpJOeY66DAwr6AY4yOMjjaDJtELKn1GK1VBDpWx'
        ip = request.META.get('REMOTE_ADDR', 'unknown IP')
        message = f"@everyone New visit on michel.dev from {ip}"
        requests.post(webhook_url, json={"content": message})
