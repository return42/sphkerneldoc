.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-delay-queue:

===============
blk_delay_queue
===============

*man blk_delay_queue(9)*

*4.6.0-rc5*

restart queueing after defined interval


Synopsis
========

.. c:function:: void blk_delay_queue( struct request_queue * q, unsigned long msecs )

Arguments
=========

``q``
    The ``struct request_queue`` in question

``msecs``
    Delay in msecs


Description
===========

Sometimes queueing needs to be postponed for a little while, to allow
resources to come back. This function will make sure that queueing is
restarted around the specified time. Queue lock must be held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
