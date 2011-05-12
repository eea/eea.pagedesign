""" Intefaces browser package for eea.pagedesign
"""
from zope.interface import Interface


class IPageDesignView(Interface):
    """ Interface for Page Design View """

    def getBackgroundURL(url):
        """ Method to check if url has background url """

    def getLogoURL(url):
        """  Method to check if url has logo url """




