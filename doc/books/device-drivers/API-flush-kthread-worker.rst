.. -*- coding: utf-8; mode: rst -*-

.. _API-flush-kthread-worker:

====================
flush_kthread_worker
====================

*man flush_kthread_worker(9)*

*4.6.0-rc5*

flush all current works on a kthread_worker


Synopsis
========

.. c:function:: void flush_kthread_worker( struct kthread_worker * worker )

Arguments
=========

``worker``
    worker to flush


Description
===========

Wait until all currently executing or pending works on ``worker`` are
finished.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
