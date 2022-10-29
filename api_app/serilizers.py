from rest_framework.serializers import ModelSerializer
from .models import Advocate,Company


class CompanySerilizer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
        
class AdvocateSerilizer(ModelSerializer):
    company = CompanySerilizer()
    class Meta:
        model = Advocate
        fields = ['username','bio', 'company']
    