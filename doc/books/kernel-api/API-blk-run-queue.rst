.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-run-queue:

=============
blk_run_queue
=============

*man blk_run_queue(9)*

*4.6.0-rc5*

run a single device queue


Synopsis
========

.. c:function:: void blk_run_queue( struct request_queue * q )

Arguments
=========

``q``
    The queue to run


Description
===========

Invoke request handling on this queue, if it has pending work to do. May
be used to restart queueing when a request has completed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
