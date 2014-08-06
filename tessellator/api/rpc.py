# from django.core.exceptions import NoReverseMatch
from django.core.urlresolvers import reverse
from mbtilesmap.models import MBTiles
from rpc4django import rpcmethod

@rpcmethod()
def dataset_list():
    """Return the list of available MBTiles data sets.
    """
    results = []
    for tile in MBTiles.objects.all():
        try:
            url = reverse('tile', kwargs={'name': tile.name.replace(" ", ''), 
                          'x': '111', 'y': '222', 'z': '333'})
            url = url.replace('111', '${x}')
            url = url.replace('222', '${y}')
            url = url.replace('333', '${z}')
            preview = reverse('preview', kwargs={'name': tile.name.replace(" ", '')})
            
        except Exception as e:
            print str(e), e.__class__
            continue
        print url
        print preview
        results.append({'name': tile.name, 'catalog': tile.catalog,
                        'minzoom': tile.minzoom, 'maxzoom': tile.maxzoom, 
                        'bounds': tile.bounds, 'url': url, 'preview': preview,
                        })
    return results

@rpcmethod()
def dataset_get(name):
    """Return information on the named dataset.
    """
    
    print "Getting dataset!", name
    tile = MBTiles(name)
    print tile
    url = reverse('tile', kwargs={'name': tile.name, 
                  'x': '111', 'y': '222', 'z': '333'})
    url = url.replace('111', '${x}')
    url = url.replace('222', '${y}')
    url = url.replace('333', '${z}')
    preview = reverse('preview', kwargs={'name': tile.name})
    
    return {
        'name': tile.name,
        'catalog': tile.catalog,
        'minzoom': tile.minzoom,
        'maxzoom': tile.maxzoom,
        'bounds': tile.bounds,
        'url': url,
        'preview': preview
    }
