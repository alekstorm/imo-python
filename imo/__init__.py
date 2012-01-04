# TODO escaping

import json
import socket
import struct
from xml.etree import ElementTree

class Endpoint(object):
    PRODUCTION = ''
    SANDBOX = 'sandbox.e-imo.com'

class Format(object):
    UNDEFINED = 0
    XML = 1
    JSON = 2

class Payload(object):
    SEARCH = 0
    FULL = 1

def parens(node):
    return '(%s)' % node

def prim(value):
    if isinstance(value, basestring):
        return '"'+value+'"'
    if isinstance(value, bool):
        return 'TRUE' if value else 'FALSE'
    return str(value)

class Symbol(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class UnaryOperator(Symbol):
    def __init__(self, name, param):
        Symbol.__init__(self, name)
        self.param = param

    def __str__(self):
        return self.name+prim(params[0])

class BinaryOperator(Symbol):
    def __init__(self, name, param_a, param_b):
        Symbol.__init__(self, name)
        self.param_a = param_a
        self.param_b = param_b

    def __str__(self):
        return parens(prim(self.param_a)+self.name+prim(self.param_b))

class ListOperator(Symbol):
    def __init__(self, name, var, elems):
        Symbol.__init__(self, name)
        self.var = var
        self.elems = elems

    def __str__(self):
        return self.var+' '+self.name+' '+parens(','.join([prim(elem) for elem in self.elems]))

class Function(Symbol):
    def __init__(self, name, *params):
        Symbol.__init__(self, name)
        self.params = params

    def __str__(self):
        return self.name+parens(','.join([prim(param) for param in self.params]))

class Portal(object):
    def __init__(self, org_id=None, host=Endpoint.PRODUCTION, port=1967):
        self.org_id = org_id
        self.host = host
        self.port = port

    def _send(self, method, params):
        params.append(('^', self.org_id))
        request = method+''.join([sep+str(param) for (sep, param) in params if param])+'\n'
        print request

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        sock.send(request)

        length = struct.unpack('>I', sock.recv(4))[0]
        response = ''
        while length > 0:
            chunk = sock.recv(length)
            length -= len(chunk)
            response += chunk
        sock.close()
        return response

    def _format(self, response, format):
        if format == Format.JSON:
            return json.loads(response)
        elif format == Format.XML:
            return ElementTree.fromstring(response)
        return response

    def search(self, query, result_size, dym_size=5, page=1, filter=None, format=Format.UNDEFINED):
        return self._format(self._send('search', [
            ('^', result_size),
            ('|', dym_size),
            ('|', format),
            ('|', page),
            ('^', query),
            ('|', filter)]), format)

    def count(self, query, filter=None, format=Format.UNDEFINED):
        return self._format(self._send('count', [
            ('^', format),
            ('^', query),
            ('|', filter)]), format)

    def detail(self, code, payload):
        response = self._send('detail', [
            ('^', code),
            ('^', payload)])
        if payload == Payload.FULL:
            return ElementTree.fromstring('<imo>'+response+'</imo>')
        return response

    def cross(self, segment_id, codes_a=None, codes_b=None, format=Format.UNDEFINED):
        return self._format(self._send('search', [
            ('^', format),
            ('^', segment_id),
            ('|', ','.join(codes_a or [])),
            ('|', ','.join(codes_b or []))]), format)
