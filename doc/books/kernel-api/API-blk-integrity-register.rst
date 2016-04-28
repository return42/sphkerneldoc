.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-integrity-register:

======================
blk_integrity_register
======================

*man blk_integrity_register(9)*

*4.6.0-rc5*

Register a gendisk as being integrity-capable


Synopsis
========

.. c:function:: void blk_integrity_register( struct gendisk * disk, struct blk_integrity * template )

Arguments
=========

``disk``
    struct gendisk pointer to make integrity-aware

``template``
    block integrity profile to register


Description
===========

When a device needs to advertise itself as being able to send/receive
integrity metadata it must use this function to register the capability
with the block layer. The template is a blk_integrity struct with
values appropriate for the underlying hardware. See
Documentation/block/data-integrity.txt.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
