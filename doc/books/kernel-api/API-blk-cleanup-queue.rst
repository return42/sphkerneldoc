.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-cleanup-queue:

=================
blk_cleanup_queue
=================

*man blk_cleanup_queue(9)*

*4.6.0-rc5*

shutdown a request queue


Synopsis
========

.. c:function:: void blk_cleanup_queue( struct request_queue * q )

Arguments
=========

``q``
    request queue to shutdown


Description
===========

Mark ``q`` DYING, drain all pending requests, mark ``q`` DEAD, destroy
and put it. All future requests will be failed immediately with -ENODEV.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
