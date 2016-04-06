
.. _API-usb-put-dev:

===========
usb_put_dev
===========

*man usb_put_dev(9)*

*4.6.0-rc1*

release a use of the usb device structure


Synopsis
========

.. c:function:: void usb_put_dev( struct usb_device * dev )

Arguments
=========

``dev``
    device that's been disconnected


Description
===========

Must be called when a user of a device is finished with it. When the last user of the device calls this function, the memory of the device is freed.
