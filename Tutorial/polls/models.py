import datetime
import xml.etree.ElementTree as et
from django.utils import timezone

from django.db import models


class XMLHandler:
    def get_servers():
        tree = et.parse('polls/xml/servers.xml')
        root = tree.getroot()
        servers = []

        for server in root.findall('Server'):
            name = server.find('Name').text
            url = server.find('Ip').text
            port = server.find('Port').text

            servers.append((name, url, port))

        return servers

    servers = get_servers()


class Log(models.Model):
    xml_handler = XMLHandler()

    time_stamp = models.TextField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    function = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Log'
