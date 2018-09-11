import urllib2
import json


class BajarDatos():
    def html(self):
        url = 'https://oja.la'
        response = urllib2.urlopen(url)
        print "La respuesta es: %s" % response.getcode()
        data = response.read()
        print data
        pass

    def json(self):
        url = 'https://jsonplaceholder.typicode.com/users'
        response = urllib2.urlopen(url)
        print "La respuesta es: %s" % response.getcode()
        data = response.read()
        Json = json.loads(data)
        for x in Json:
            print x['id']
        pass


Object = BajarDatos()
# Object.html()
Object.json()
