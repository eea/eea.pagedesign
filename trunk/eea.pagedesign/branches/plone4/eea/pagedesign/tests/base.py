""" base test case module
"""
from Products.PloneTestCase import PloneTestCase
#from Products.GenericSetup import EXTENSION, profile_registry
#from Products.CMFPlone.interfaces import ITestCasePloneSiteRoot


#PROFILES = ['eea.design:default']

PloneTestCase.setupPloneSite(extension_profiles=('eea.pagedesign:default',))
#profile_registry.registerProfile(
#                    'testfixture',
#                    'test:EEAContentTypes',
#                    'Extension profile for testing EEAContentTypes',
#                    'profile/testfixture',
#                    'EEAContentTypes',
#                    EXTENSION,
#                    for_=ITestCasePloneSiteRoot)

class FunctionalTestCase(PloneTestCase.FunctionalTestCase):
    """ Functional test case base class """
    pass


