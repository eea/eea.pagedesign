from Products.Five import BrowserView

class PageDesignView(BrowserView):

    def getBackgroundURL(self):
        img = getattr(self.context, 'page_background', None)
        if img != None:
            return img.absolute_url()
