
.. _API-usb-free-urb:

============
usb_free_urb
============

*man usb_free_urb(9)*

*4.6.0-rc1*

frees the memory used by a urb when all users of it are finished


Synopsis
========

.. c:function:: void usb_free_urb( struct urb * urb )

Arguments
=========

``urb``
    pointer to the urb to free, may be NULL


Description
===========

Must be called when a user of a urb is finished with it. When the last user of the urb calls this function, the memory of the urb is freed.


Note
====

The transfer buffer associated with the urb is not freed unless the URB_FREE_BUFFER transfer flag is set.
