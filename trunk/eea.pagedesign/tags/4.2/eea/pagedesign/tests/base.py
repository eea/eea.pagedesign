""" base test case module
"""
#from Products.PloneTestCase import PloneTestCase
#from Products.GenericSetup import EXTENSION, profile_registry
#from Products.CMFPlone.interfaces import ITestCasePloneSiteRoot
from Products.PloneTestCase.layer import onsetup
from Testing import ZopeTestCase as ztc
from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
ztc.installProduct('eea.pagedesign')

#PROFILES = ['eea.design:default']

#PloneTestCase.setupPloneSite(products="eea.pagedesign", 
#            extension_profiles=['eea.pagedesign:default'])
#profile_registry.registerProfile(
#                    'testfixture',
#                    'test:EEAContentTypes',
#                    'Extension profile for testing EEAContentTypes',
#                    'profile/testfixture',
#                    'EEAContentTypes',
#                    EXTENSION,
#                    for_=ITestCasePloneSiteRoot)
@onsetup
def setup_product():
    """Set up the package and its dependencies.
    """
    fiveconfigure.debug_mode = True
    import eea.pagedesign
    zcml.load_config('configure.zcml', eea.pagedesign)
    fiveconfigure.debug_mode = False
    ztc.installPackage('eea.pagedesign')


setup_product()
ptc.setupPloneSite(products=['eea.pagedesign'])

class FunctionalTestCase(ptc.PloneTestCase):
    """ base class for all the tests in this package. 
    """

