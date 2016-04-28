.. -*- coding: utf-8; mode: rst -*-

.. _API-hcd-buffer-create:

=================
hcd_buffer_create
=================

*man hcd_buffer_create(9)*

*4.6.0-rc5*

initialize buffer pools


Synopsis
========

.. c:function:: int hcd_buffer_create( struct usb_hcd * hcd )

Arguments
=========

``hcd``
    the bus whose buffer pools are to be initialized


Context
=======

!\ ``in_interrupt``


Description
===========

Call this as part of initializing a host controller that uses the dma
memory allocators. It initializes some pools of dma-coherent memory that
will be shared by all drivers using that controller.

Call ``hcd_buffer_destroy`` to clean up after using those pools.


Return
======

0 if successful. A negative errno value otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
