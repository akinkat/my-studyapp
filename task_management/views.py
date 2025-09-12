from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View, generic

from accounts.models import CustomUser
from .models import LearningGoal


# Top screen
class IndexView(generic.TemplateView):
    template_name = 'task_management/index.html'


# List of Interest Category
class InterestCategoryListView(LoginRequiredMixin, generic.ListView):
    model = CustomUser
    template_name = 'task_management/interest_categories.html'
    context_object_name = 'interest_categories'

    def get_queryset(self):
        return self.request.user.interest_categories.all()

  
class AddInterestCategoryView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'task_management/add_interest_category.html'
    

# List of Learning Goal
class LearningGoalListView(LoginRequiredMixin, generic.ListView):
    model = LearningGoal
    template_name = 'task_management/learning_goal_list.html'
    context_object_name = 'learning_goals'

    def get_queryset(self):
        cateogy_id = self.kwargs['category_id']
        return LearningGoal.objects.filter(
            user=self.request.user,
            category_id=cateogy_id,
        )
    