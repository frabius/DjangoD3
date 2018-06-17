from Diablo3_review.models import *
from django.forms import ModelForm


class CommentaireForm(ModelForm):
    class Meta:
        model = Commentaire
        fields = ['description', ]
