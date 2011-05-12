""" Page design view module responsible for PagedesignView BrowserView
"""
from Products.Five import BrowserView

class PageDesignView(BrowserView):
    """ Page Design View class """

    def getBackgroundURL(self):
        """ Method that returns page_background url if present"""
        img = getattr(self.context, 'page_background', None)
        if img != None:
            return img.absolute_url()

    def getLogoURL(self):
        """ Method that returns page_logo url if present"""
        img = getattr(self.context, 'page_logo', None)
        if img != None:
            return img.absolute_url()
