""" eea.pagedesign
"""
from os.path import dirname
from Products.CMFCore.DirectoryView import registerDirectory
from Products.CMFCore import utils
from App.Common import package_home

GLOBALS = globals()

ppath = utils.ProductsPath
utils.ProductsPath.append(dirname(package_home(GLOBALS)))
registerDirectory('skins', GLOBALS)
utils.ProductsPath = ppath
