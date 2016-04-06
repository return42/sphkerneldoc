
.. _API-blk-queue-bypass-end:

====================
blk_queue_bypass_end
====================

*man blk_queue_bypass_end(9)*

*4.6.0-rc1*

leave queue bypass mode


Synopsis
========

.. c:function:: void blk_queue_bypass_end( struct request_queue * q )

Arguments
=========

``q``
    queue of interest


Description
===========

Leave bypass mode and restore the normal queueing behavior.
