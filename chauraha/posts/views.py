from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from .models import Comment, Post, Subly
from rest_framework import serializers, viewsets, status
from .serializers import CommentSerializer, PostSerializer, SublySerializer, PostLikeSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions

# Create your views here.

# class MyPagination(PageNumberPagination):
#     page_size = 5



class PostView(viewsets.ViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    # pagination_class = MyPagination
    # ordering = ('post.id')
    def list(self, request):
        queryset = Post.objects.all().order_by('-id')
        serializer = PostSerializer(queryset, many=True)
        
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def create(self, request):
        mydata = request.data
        print(mydata)
        # dict['author'] = 'nik'
        # mydata['author'] = str(request.user.id)
        serializer = PostSerializer(data=mydata)
        if serializer.is_valid():
            serializer.save(author = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        # newdata = post.like.add(request.user)

        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        post = Post.objects.get(id = request.GET.get('id', 1))
        
        # in url fronted: http://127.0.0.1:8000/comments/comment/?id={post.id} eg.= http://127.0.0.1:8000/comments/comment/?id=1
        queryset = post.comments.all()
        serializer = CommentSerializer(queryset, many= True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def create(self, request):
        mydata = request.data
        print(mydata)
        # # dict['author'] = 'nik'
        # mydata['author'] = str(request.user.id)
        serializer = CommentSerializer(data = mydata)

        #post = Post.objects.get(mydata)
        #print(post)
        if serializer.is_valid():
            serializer.save(author = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk =None):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comment, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        comment = get_object_or_404(Comment, pk= pk)
        if comment.author != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SublyView(viewsets.ViewSet):

    def list(self, request):
        print(request)
        idint = int(request.GET.get('myid'))
        comment = Comment.objects.get(id = idint)
        print(comment)
        # print(type(request.GET.get('myid')))

        # in url fronted: http://127.0.0.1:8000/comments/comment/?id={post.id} eg.= http://127.0.0.1:8000/comments/comment/?id=1
        queryset = comment.subly.all().order_by('-id')
        serializer = SublySerializer(queryset, many= True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            subly = Subly.objects.get(pk=pk)
        except Subly.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SublySerializer(subly)
        return Response(serializer.data)

    def create(self, request):
        mydata = request.data
        print(mydata)
        # # dict['author'] = 'nik'
        # mydata['author'] = str(request.user.id)
        serializer = SublySerializer(data = mydata)
        if serializer.is_valid():
            serializer.save(author = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk =None):
        try:
            subly = Subly.objects.get(pk=pk)
        except Subly.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(subly, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        subly = get_object_or_404(Subly, pk= pk)
        if subly.author != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        subly.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class PostLikeAPI(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        # slug = self.kwargs.get("slug")
        print(request)
        obj = get_object_or_404(Post, id = request.GET.get('getid', 1) )
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated:
            if user in obj.like.all():
                liked = False
                obj.like.remove(user)
            else:
                liked = True
                obj.like.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        # serializer = SublySerializer(obj, many= True)
        return Response(data)


class AddLikeUnlikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request, pk =None):
        print(request)
        post = Post.objects.get(pk=pk)
        serializer = PostLikeSerializer(post, many=True)
        if post.likes.filter(pk=request.user.pk).exists():                                                              
            post.likes.remove(request.user)
        else:           
            post.likes.add(request.user)  
        return Response(serializer.data)

    



# @api_view(['POST'])
# def like_post(request):
#     post = Post.objects.get(request.postid)
#     serializer = PostLikeSerializer(request.data)
#     user = request.user
#     post.like.add(user)
#     return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world!"})


        




