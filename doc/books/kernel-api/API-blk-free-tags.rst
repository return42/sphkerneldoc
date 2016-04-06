
.. _API-blk-free-tags:

=============
blk_free_tags
=============

*man blk_free_tags(9)*

*4.6.0-rc1*

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

Drop the reference count on ``bqt`` and frees it when the last reference is dropped.
