.. -*- coding: utf-8; mode: rst -*-

.. _API-queue-delayed-work:

==================
queue_delayed_work
==================

*man queue_delayed_work(9)*

*4.6.0-rc5*

queue work on a workqueue after delay


Synopsis
========

.. c:function:: bool queue_delayed_work( struct workqueue_struct * wq, struct delayed_work * dwork, unsigned long delay )

Arguments
=========

``wq``
    workqueue to use

``dwork``
    delayable work to queue

``delay``
    number of jiffies to wait before queueing


Description
===========

Equivalent to ``queue_delayed_work_on`` but tries to use the local CPU.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
