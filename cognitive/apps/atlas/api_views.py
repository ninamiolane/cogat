from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from .query import Concept, Contrast, Disorder, Task, do_query

Concept = Concept()
Contrast = Contrast()
Disorder = Disorder()
Task = Task()

class ConceptAPI(APIView):
    def get(self, request, format=None):
        fields = {}
        id = request.GET.get("id", "")
        name = request.GET.get("name", "")
        contrast_id = request.GET.get("contrast_id", "")
        if id:
            concept = Concept.get_full(id, 'id')
        elif name:
            concept = Concept.get_full(name, 'name')
        elif contrast_id:
            concept = Contrast.api_get_concepts(contrast_id)
        else:
            concept = Concept.api_all()
        
        if concept is None:
            raise NotFound('Concept not found')
        return Response(concept)

class TaskAPI(APIView):
    def get(self, request, format=None):
        id = request.GET.get("id", "")
        name = request.GET.get("name", "")
        
        if id:
            task = Task.get_full(id, 'id')
        elif name:
            task = Task.get_full(name, 'name')
        else:
            task = Task.api_all()

        if task is None:
            raise NotFound('Task not found')
        return Response(task)

class DisorderAPI(APIView):
    def get(self, request, format=None):
        id = request.GET.get("id", "")
        name = request.GET.get("name", "")
        
        if id:
            disorder = Disorder.get_full(id, 'id')
        elif name:
            disorder = Disorder.get_full(name, 'name')
        else:
            disorder = Disorder.api_all()
        
        if disorder is None:
            raise NotFound('Disorder not found')
        return Response(disorder)


class SearchAPI(APIView):
    def get(self, request, format=None):
        search_classes = [Concept, Contrast, Disorder, Task]
        queries = request.GET.get("q", "")
        results = []
        for sclass in search_classes:
            result = sclass.search_all_fields(queries)
            results += result
        if not results:
            raise NotFound('No results found')
        return Response(results)
