.. -*- coding: utf-8; mode: rst -*-

.. _API---blk-queue-free-tags:

=====================
__blk_queue_free_tags
=====================

*man __blk_queue_free_tags(9)*

*4.6.0-rc5*

release tag maintenance info


Synopsis
========

.. c:function:: void __blk_queue_free_tags( struct request_queue * q )

Arguments
=========

``q``
    the request queue for the device


Notes
=====

``blk_cleanup_queue`` will take care of calling this function, if
tagging has been used. So there's no need to call this directly.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
