from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View, generic


# Top screen
class IndexView(generic.TemplateView):
    template_name = 'task_management/index.html'


# List of Interest Category
class InterestCategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = 'task_management/interest_category_list.html'
    context_object_name = 'interest_categories'

    def get_queryset(self):
        return self.request.user.interest_categories.all()
    

# List of Learning Goal
class LearningGoalListView(LoginRequiredMixin, generic.ListView):
    template_name = 'task_management/learning_goal_list.html'
    