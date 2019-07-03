def can_create(request, model):
    """Limited page creation to admins"""
    if request.user.is_staff or request.user.is_superuser:
        return True
    return not getattr(model, 'creation_limited', False)
