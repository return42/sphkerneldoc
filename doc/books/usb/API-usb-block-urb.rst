
.. _API-usb-block-urb:

=============
usb_block_urb
=============

*man usb_block_urb(9)*

*4.6.0-rc1*

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

After the routine has run, attempts to resubmit the URB will fail with error -EPERM. Thus even if the URB's completion handler always tries to resubmit, it will not succeed and the
URB will become idle.

The URB must not be deallocated while this routine is running. In particular, when a driver calls this routine, it must insure that the completion handler cannot deallocate the
URB.
