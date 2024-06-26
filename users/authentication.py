from users.models import User


def create_profile(backend, username, *args, **kwargs):
    print(backend)
    User.objects.get_or_create(username=username)
