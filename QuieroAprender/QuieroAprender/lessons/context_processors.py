from ..events.views import is_super_admin
from .views import is_teacher

def teacher_context(request):
    if request.user.is_authenticated:
        can_see_api = is_super_admin(request.user) or is_teacher(request.user)
    else:
        can_see_api = False
    return {"can_see_api": can_see_api}