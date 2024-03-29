from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comment
from .serializers import CommentSerializer
from django.shortcuts import get_list_or_404


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def employee_comments(request):
    if request.method == 'GET':
        comments= Comment.objects.all()
        serializer= CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        print('User ', f"{request.user.id} {request.user.email} {request.user.username}")
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
