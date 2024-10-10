from django.urls import path
from .views import IndexView, PostDetailView, CommentCreateView, CastsView, SeasonsView, AboutView
urlpatterns = [
    path("", IndexView.as_view(), name="index_view"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail_view"),
    path("comment/<int:pk>", CommentCreateView.as_view(), name="comment_create"),
    path("extra/casts/", CastsView.as_view(), name="extra_casts"),
    path("extra/seasons/", SeasonsView.as_view(), name="season_view"),
    path("extra/abouts/", AboutView.as_view(), name="about_view"),

]