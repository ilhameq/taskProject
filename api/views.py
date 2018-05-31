from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from candidate.models import Candidate
from api.serializers import CandidateSerializer


@api_view(['GET', 'POST'])
def candidate_list(request):

    if request.method == 'GET':
        tasks = Candidate.objects.all()
        serializer = CandidateSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def candidate_detail(request, pk):


    try:
        task = Candidate.objects.get(pk=pk)
    except Candidate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CandidateSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CandidateSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
