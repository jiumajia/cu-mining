#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import ConfigParser

def getConfig(section, key):
    config = ConfigParser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/cu_sql.ini'
    config.read(path)
    return config.get(section, key)




