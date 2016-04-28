.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-integrity-unregister:

========================
blk_integrity_unregister
========================

*man blk_integrity_unregister(9)*

*4.6.0-rc5*

Unregister block integrity profile


Synopsis
========

.. c:function:: void blk_integrity_unregister( struct gendisk * disk )

Arguments
=========

``disk``
    disk whose integrity profile to unregister


Description
===========

This function unregisters the integrity capability from a block device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
