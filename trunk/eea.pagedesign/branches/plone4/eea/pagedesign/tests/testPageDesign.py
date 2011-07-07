""" test page design module
"""
from eea.pagedesign.tests.base import FunctionalTestCase 

class TestPageBackground(FunctionalTestCase):
    """Test-cases for class(es) Frontpage."""

    def afterSetUp(self):
        """ After setup test method """
        self.setRoles(['Manager'])
        self.testPage = self.portal[self.portal.invokeFactory(
                                            'Folder', id='test')]
        self.testSubPage = self.testPage[self.testPage.invokeFactory(
                                            'Folder', id='child')]
        self.testPage.invokeFactory('Image', id='page_background')
        self.testPage.invokeFactory('Image', id='page_logo')

    def test_rootPageBackground(self):
        """ tests if traversed view is equal to page_background """
        context = self.testPage
        view = context.restrictedTraverse('@@page_design')
        self.failUnless(view.getBackgroundURL() == \
                'http://nohost/plone/test/page_background')

    def test_rootPageLogo(self):
        """ test if traversed view is equal to for page_logo """
        context = self.testPage
        view = context.restrictedTraverse('@@page_design')
        self.failUnless(view.getLogoURL() == \
                'http://nohost/plone/test/page_logo')

    def test_subPageBackground(self):
        """ Acquisition should locate the parent folders image """
        context = self.testSubPage
        view = context.restrictedTraverse('@@page_design')
        self.failUnless(view.getBackgroundURL() == \
                'http://nohost/plone/test/page_background')

def test_suite():
    """ main test suite method """
    from unittest import TestSuite, makeSuite
    suite = makeSuite(TestPageBackground)
    return  TestSuite(suite)
