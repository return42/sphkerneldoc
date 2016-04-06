
.. _API-hcd-buffer-destroy:

==================
hcd_buffer_destroy
==================

*man hcd_buffer_destroy(9)*

*4.6.0-rc1*

deallocate buffer pools


Synopsis
========

.. c:function:: void hcd_buffer_destroy( struct usb_hcd * hcd )

Arguments
=========

``hcd``
    the bus whose buffer pools are to be destroyed


Context
=======

!\ ``in_interrupt``


Description
===========

This frees the buffer pools created by ``hcd_buffer_create``.
