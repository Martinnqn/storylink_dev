def customuser_info(request):
    '''Add username if exists in the url parameters.'''

    context = {}
    context.update(
        {'customuser': {'username': request.resolver_match.kwargs.get("username", None)}})
    return context
