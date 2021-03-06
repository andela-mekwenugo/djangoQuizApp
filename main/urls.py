from django.conf.urls import url
from main import views


urlpatterns = [

    url(r'^admin/create/quiz/$',
        views.AdminView.as_view(),
        name='adminquestion'
        ),
    url(r'^quiz/(?P<quizname>\w+)/$',
        views.TakeQuizView.as_view(),
        name='quiz_name'
        ),
    url(r'^users/$',
        views.ViewUsers.as_view(),
        name='all_users'
        ),
    url(r'^user/profile$',
        views.UserProfileView.as_view(),
        name='user_profile'
        ),
    url(r'^result/(?P<score>[0-9].+)/$',
        views.ResultView.as_view(),
        name='result'
        ),
]
