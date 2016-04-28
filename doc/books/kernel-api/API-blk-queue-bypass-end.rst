.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-bypass-end:

====================
blk_queue_bypass_end
====================

*man blk_queue_bypass_end(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
