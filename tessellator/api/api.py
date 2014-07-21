from tastypie.resources import Resource
from tastypie import fields
from mbtilesmap.models import MBTiles

class TileResource(Resource):
    """Interact with the available map tiles. 
    """
    catalog = fields.CharField(attribute='catalog', null=True)
    name = fields.CharField(attribute='name')
    minzoom = fields.IntegerField(attribute='minzoom')
    maxzoom = fields.IntegerField(attribute='maxzoom')
    bounds = fields.CharField(attribute='bounds')
    
    class Meta: 
        allowed_methods = ('get',)
    
    def get_object_list(*args):
        return list(t for t in MBTiles.objects.all())
        
    def obj_get_list(self, bundle):
        results = []
        class bag:
            pass
        for t in MBTiles.objects.all():
            d = dict(name=t.name, catalog=t.catalog, minzoom=t.minzoom, 
                     maxzoom=t.maxzoom, bounds=t.bounds) 
            b = bag()
            b.catalog = t.catalog
            b.name = t.name
            b.minzoom = t.minzoom 
            b.maxzoom = t.maxzoom
            
            results.append(b)
        return results