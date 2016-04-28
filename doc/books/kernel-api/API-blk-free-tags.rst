.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-free-tags:

=============
blk_free_tags
=============

*man blk_free_tags(9)*

*4.6.0-rc5*

release a given set of tag maintenance info


Synopsis
========

.. c:function:: void blk_free_tags( struct blk_queue_tag * bqt )

Arguments
=========

``bqt``
    the tag map to free


Description
===========

Drop the reference count on ``bqt`` and frees it when the last reference
is dropped.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
