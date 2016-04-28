.. -*- coding: utf-8; mode: rst -*-

.. _API---blk-run-queue:

===============
__blk_run_queue
===============

*man __blk_run_queue(9)*

*4.6.0-rc5*

run a single device queue


Synopsis
========

.. c:function:: void __blk_run_queue( struct request_queue * q )

Arguments
=========

``q``
    The queue to run


Description
===========

See ``blk_run_queue``. This variant must be called with the queue lock
held and interrupts disabled.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
