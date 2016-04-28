.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-put-dev:

===========
usb_put_dev
===========

*man usb_put_dev(9)*

*4.6.0-rc5*

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

Must be called when a user of a device is finished with it. When the
last user of the device calls this function, the memory of the device is
freed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
