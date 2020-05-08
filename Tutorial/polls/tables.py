from django_tables2 import tables, Table

from .models import Genre


class GenreTable(Table):
    class Meta:
        model = Genre
        template_name = 'django_tables/bootstrap.html'
        fields = ('id', 'genre')
