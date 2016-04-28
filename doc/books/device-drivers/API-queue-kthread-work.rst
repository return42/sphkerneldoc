.. -*- coding: utf-8; mode: rst -*-

.. _API-queue-kthread-work:

==================
queue_kthread_work
==================

*man queue_kthread_work(9)*

*4.6.0-rc5*

queue a kthread_work


Synopsis
========

.. c:function:: bool queue_kthread_work( struct kthread_worker * worker, struct kthread_work * work )

Arguments
=========

``worker``
    target kthread_worker

``work``
    kthread_work to queue


Description
===========

Queue ``work`` to work processor ``task`` for async execution. ``task``
must have been created with ``kthread_worker_create``. Returns ``true``
if ``work`` was successfully queued, ``false`` if it was already
pending.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
