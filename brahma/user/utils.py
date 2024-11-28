from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    """
    Generate authentication tokens for a given user.
    """
    refresh_token = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh_token),
        'access': str(refresh_token.access_token),
    }