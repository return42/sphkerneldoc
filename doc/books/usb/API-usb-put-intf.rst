
.. _API-usb-put-intf:

============
usb_put_intf
============

*man usb_put_intf(9)*

*4.6.0-rc1*

release a use of the usb interface structure


Synopsis
========

.. c:function:: void usb_put_intf( struct usb_interface * intf )

Arguments
=========

``intf``
    interface that's been decremented


Description
===========

Must be called when a user of an interface is finished with it. When the last user of the interface calls this function, the memory of the interface is freed.
