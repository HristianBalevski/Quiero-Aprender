from .views import is_super_admin, is_staff_admin

def base_context(request):

    if request.user.is_authenticated:
        is_admin = is_super_admin(request.user) or is_staff_admin(request.user)
    else:
        is_admin = False
    return {'is_admin': is_admin}
