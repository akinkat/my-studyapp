from django.urls import path
from task_management import views

app_name = 'task_management'
urlpatterns = [
    # Top page
    path('', views.IndexView.as_view(), name='index'),
    # Interest Category
    path('interest_categories/', views.InterestCategoryListView.as_view(), name='interest_categories'),
    # Learning Goal
    path('learning_goals/<int:category_id>', views.LearningGoalListView.as_view(), name='learning_goals'),
]
