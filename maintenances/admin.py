from django.contrib import admin
from .models import Mantenances, PiecesEchanges, InfosPieces
# Register your models here.

admin.site.register(Mantenances)
admin.site.register(PiecesEchanges)
admin.site.register(InfosPieces)