.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-init-tags:

=============
blk_init_tags
=============

*man blk_init_tags(9)*

*4.6.0-rc5*

initialize the tag info for an external tag map


Synopsis
========

.. c:function:: struct blk_queue_tag * blk_init_tags( int depth, int alloc_policy )

Arguments
=========

``depth``
    the maximum queue depth supported

``alloc_policy``
    tag allocation policy


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
