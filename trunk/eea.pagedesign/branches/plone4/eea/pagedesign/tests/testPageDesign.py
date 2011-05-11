from eea.pagedesign.tests.base import EEAMegaTestCase

class TestPageBackground(EEAMegaTestCase):
    """Test-cases for class(es) Frontpage."""

    def afterSetUp(self):
        self.setRoles(['Manager'])
        self.testPage = self.portal[self.portal.invokeFactory('Folder', id='test')]
        self.testSubPage = self.testPage[self.testPage.invokeFactory('Folder', id='child')]
        self.testPage.invokeFactory('Image', id='page_background')
        self.testPage.invokeFactory('Image', id='page_logo')

    def test_rootPageBackground(self):
        context = self.testPage
        view = context.restrictedTraverse('@@page_design')
        self.failUnless(view.getBackgroundURL() == 'http://nohost/plone/test/page_background')

    def test_rootPageLogo(self):
        context = self.testPage
        view = context.restrictedTraverse('@@page_design')
        self.failUnless(view.getLogoURL() == 'http://nohost/plone/test/page_logo')

    def test_subPageBackground(self):
        """ Acquisition should locate the parent folders image """
        context = self.testSubPage
        view = context.restrictedTraverse('@@page_design')
        self.failUnless(view.getBackgroundURL() == 'http://nohost/plone/test/page_background')

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = makeSuite(TestPageBackground)
    return  TestSuite(suite)
