from imo import Endpoint, Portal, Symbol as sym
from imo.filter import *

portal = Portal(org_id='36b2cee0ad54b925', host=Endpoint.SANDBOX, port=42011)
print portal.search('chest', result_size=10)
print portal.count('chest', format=Format.JSON, filter=Eq(Lower(sym('title')), 'chest asymmetry'))
#print portal.cross(segment_id='48', codes_a=['003.1','003.20'], codes_b=['71010','71016'], format=Format.UNDEFINED)
