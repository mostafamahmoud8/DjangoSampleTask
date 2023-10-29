from django_filters import FilterSet, rest_framework
from .models import Transaction

# write your filters here

class CardTemplateFilter(FilterSet):

    date = rest_framework.DateTimeFromToRangeFilter(field_name='created_at')
    currency = rest_framework.CharFilter(field_name='from_currency', method='filter_currency')

    
    class Meta:
        model = Transaction
        fields = ['date', 'currency']
    
   
    def filter_currency(self, queryset, name, value):
        # construct the full lookup expression.
        lookup = '__'.join([name, 'in'])
        return queryset.filter(**{lookup: value.split(',')})