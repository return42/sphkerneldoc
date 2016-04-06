
.. _API-usb-ep-enable:

=============
usb_ep_enable
=============

*man usb_ep_enable(9)*

*4.6.0-rc1*

configure endpoint, making it usable


Synopsis
========

.. c:function:: int usb_ep_enable( struct usb_ep * ep )

Arguments
=========

``ep``
    the endpoint being configured. may not be the endpoint named “ep0”. drivers discover endpoints through the ep_list of a usb_gadget.


Description
===========

When configurations are set, or when interface settings change, the driver will enable or disable the relevant endpoints. while it is enabled, an endpoint may be used for i/o until
the driver receives a ``disconnect`` from the host or until the endpoint is disabled.

the ep0 implementation (which calls this routine) must ensure that the hardware capabilities of each endpoint match the descriptor provided for it. for example, an endpoint named
“ep2in-bulk” would be usable for interrupt transfers as well as bulk, but it likely couldn't be used for iso transfers or for endpoint 14. some endpoints are fully configurable,
with more generic names like “ep-a”. (remember that for USB, “in” means “towards the USB master”.)

returns zero, or a negative error code.
