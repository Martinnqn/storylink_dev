def customuser_info(request):
    context = {}
    context.update(
        {'customuser': {'username': request.resolver_match.kwargs.get("username", None)}})
    return context
