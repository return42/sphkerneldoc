
.. _API-blk-init-tags:

=============
blk_init_tags
=============

*man blk_init_tags(9)*

*4.6.0-rc1*

initialize the tag info for an external tag map


Synopsis
========

.. c:function:: struct blk_queue_tag ⋆ blk_init_tags( int depth, int alloc_policy )

Arguments
=========

``depth``
    the maximum queue depth supported

``alloc_policy``
    tag allocation policy
