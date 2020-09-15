
# import viewsets 
from rest_framework import viewsets 
  
# import local data 
from .serializers import UserSerializer 
from apps.users.models import CustomUser
  
# create a viewset 
class UserViewSet(viewsets.ModelViewSet): 
    # define queryset 
    queryset = CustomUser.objects.all() 
      
    # specify serializer to be used 
    serializer_class = UserSerializer 
