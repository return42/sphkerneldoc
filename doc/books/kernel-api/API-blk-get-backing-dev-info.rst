.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-get-backing-dev-info:

========================
blk_get_backing_dev_info
========================

*man blk_get_backing_dev_info(9)*

*4.6.0-rc5*

get the address of a queue's backing_dev_info


Synopsis
========

.. c:function:: struct backing_dev_info * blk_get_backing_dev_info( struct block_device * bdev )

Arguments
=========

``bdev``
    device


Description
===========

Locates the passed device's request queue and returns the address of its
backing_dev_info. This function can only be called if ``bdev`` is
opened and the return value is never NULL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
