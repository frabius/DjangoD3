from Diablo3_review.models import *
import django_filters


class articleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    class Meta:
        model = MyArticle
        fields =['name', ]
