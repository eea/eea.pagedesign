from zope.interface import Interface

class IPageDesignView(Interface):

    def getBackgroundURL(url):
        """ """

class IPageDesignEditView(Interface):

    def setBackgroundURL(url):
        """ """
