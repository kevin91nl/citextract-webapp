"""Sitemap definitions."""
from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    """A static sitemap for the CMS app."""

    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        """Get sitemap items.

        Returns
        -------
        list
            List of sitemap items.
        """
        return ['landing', 'contact']

    def location(self, item):
        """Get the sitemap URL given an item.

        Parameters
        ----------
        item : str
            Item to get the URL for.

        Returns
        -------
        str
            The URL of the item.
        """
        return reverse(item)
