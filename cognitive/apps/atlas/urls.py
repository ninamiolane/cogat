from django.conf.urls import url,patterns
from django.conf.urls.static import static

from . import api_views, views


urlpatterns = [
    url(r'^concepts$', views.all_concepts, name="all_concepts"),
    url(r'^disorders$', views.all_disorders, name="all_disorders"),
    url(r'^batteries$', views.all_batteries, name="all_batteries"),
    url(r'^theories$', views.all_theories, name="all_theories"),
    url(r'^tasks$', views.all_tasks, name="all_tasks"),

    url(r'^concepts/(?P<letter>[a-z]|[A-Z]{1})/$', views.concepts_by_letter, name="concepts_by_letter"),
    url(r'^tasks/(?P<letter>[a-z]|[A-Z]{1})/$', views.tasks_by_letter, name="tasks_by_letter"),

    url(r'^disorders/id/(?P<uid>[a-z]|[A-Z])/$', views.view_disorder, name="disorder"),
    url(r'^batteries/id/(?P<uid>[a-z]|[A-Z])/$', views.view_battery, name="battery"),
    url(r'^theories/id/(?P<uid>[a-z]|[A-Z])/$', views.view_theory, name="theory"),
    url(r'^concepts/id/(?P<uid>[a-z]|[A-Z])/$', views.view_concept, name="concept"),
    url(r'^tasks/id/(?P<uid>[a-z]|[A-Z])/$', views.view_task, name="task"),
    url(r'^contrasts/id/(?P<uid>[a-z]|[A-Z])/$', views.view_contrast, name="contrast"),

] 

api_urls = [
    url(r'^api/search$', api_views.SearchAPI.as_view(), name='task_api_list'),
    url(r'^api/concept$',api_views.ConceptAPI.as_view(), name='task_api_list'),
    url(r'^api/task$', api_views.TaskAPI.as_view(), name='task_api_list'),
    url(r'^api/disorder', api_views.DisorderAPI.as_view(), name='task_api_list'),
]

urlpatterns += api_urls
