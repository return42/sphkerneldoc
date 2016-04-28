.. -*- coding: utf-8; mode: rst -*-

.. _API-bdgrab:

======
bdgrab
======

*man bdgrab(9)*

*4.6.0-rc5*

- Grab a reference to an already referenced block device


Synopsis
========

.. c:function:: struct block_device * bdgrab( struct block_device * bdev )

Arguments
=========

``bdev``
    Block device to grab a reference to.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
