.. -*- coding: utf-8; mode: rst -*-

.. _API-queue-work:

==========
queue_work
==========

*man queue_work(9)*

*4.6.0-rc5*

queue work on a workqueue


Synopsis
========

.. c:function:: bool queue_work( struct workqueue_struct * wq, struct work_struct * work )

Arguments
=========

``wq``
    workqueue to use

``work``
    work to queue


Description
===========

Returns ``false`` if ``work`` was already on a queue, ``true``
otherwise.

We queue the work to the CPU on which it was submitted, but if the CPU
dies it can be processed by another CPU.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
