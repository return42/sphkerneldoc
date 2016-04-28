.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-block-urb:

=============
usb_block_urb
=============

*man usb_block_urb(9)*

*4.6.0-rc5*

reliably prevent further use of an URB


Synopsis
========

.. c:function:: void usb_block_urb( struct urb * urb )

Arguments
=========

``urb``
    pointer to URB to be blocked, may be NULL


Description
===========

After the routine has run, attempts to resubmit the URB will fail with
error -EPERM. Thus even if the URB's completion handler always tries to
resubmit, it will not succeed and the URB will become idle.

The URB must not be deallocated while this routine is running. In
particular, when a driver calls this routine, it must insure that the
completion handler cannot deallocate the URB.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
