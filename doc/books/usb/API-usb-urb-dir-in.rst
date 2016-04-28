.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-urb-dir-in:

==============
usb_urb_dir_in
==============

*man usb_urb_dir_in(9)*

*4.6.0-rc5*

check if an URB describes an IN transfer


Synopsis
========

.. c:function:: int usb_urb_dir_in( struct urb * urb )

Arguments
=========

``urb``
    URB to be checked


Return
======

1 if ``urb`` describes an IN transfer (device-to-host), otherwise 0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
