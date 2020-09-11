def customuser_info(request):
    context = {}
    print(request.resolver_match.kwargs.get("username", None))
    context.update(
        {'customuser': {'username': request.resolver_match.kwargs.get("username", None)}})
    return context
