"""Ädditional context processors for the rendering engine."""
import os


def export_vars(request):
    """Export environment variables to the Jinja templates.

    Parameters
    ----------
    request : WSGIRequest
        The request that was made.

    Returns
    -------
    dict
        A dictionary with the following additional variables:
        - GA_TRACKING_CODE: The Google Analytics tracking code.
    """
    assert request
    data = dict()
    data['GA_TRACKING_CODE'] = os.getenv('GA_TRACKING_CODE', '')
    return data
