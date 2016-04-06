
.. _API-blk-integrity-unregister:

========================
blk_integrity_unregister
========================

*man blk_integrity_unregister(9)*

*4.6.0-rc1*

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
