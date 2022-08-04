from import_export import resources
from mysite.models import Shelter

class ShelterResource(resources.ModelResource):
    class Meta:
        model = Shelter