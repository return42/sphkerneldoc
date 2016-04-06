
.. _API-usb-ep-set-maxpacket-limit:

==========================
usb_ep_set_maxpacket_limit
==========================

*man usb_ep_set_maxpacket_limit(9)*

*4.6.0-rc1*

set maximum packet size limit for endpoint


Synopsis
========

.. c:function:: void usb_ep_set_maxpacket_limit( struct usb_ep * ep, unsigned maxpacket_limit )

Arguments
=========

``ep``
    the endpoint being configured

``maxpacket_limit``
    value of maximum packet size limit


Description
===========

This function should be used only in UDC drivers to initialize endpoint (usually in probe function).
