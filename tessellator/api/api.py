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
    
    def obj_get(self, bundle, **kwargs):
        pk = kwargs.get('pk', '')
        return self._build_resultset([MBTiles(name=pk)])
        return None
    
    def obj_get_list(self, bundle):
        return self._build_resultset(MBTiles.objects.all())
    
    def _build_resultset(self, objects):
        # class that exists only to hold fields defined above 
        # (I'm missing something here)
        class bag:
            pass
        
        results = []
        for t in objects:
            b = bag()
            b.catalog = t.catalog
            b.name = t.name
            b.minzoom = t.minzoom 
            b.maxzoom = t.maxzoom
            b.bounds = t.bounds
            
            results.append(b)
        return results
        