.. -*- coding: utf-8; mode: rst -*-

.. _API-hcd-buffer-destroy:

==================
hcd_buffer_destroy
==================

*man hcd_buffer_destroy(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
