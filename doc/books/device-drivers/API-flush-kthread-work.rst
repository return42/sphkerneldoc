.. -*- coding: utf-8; mode: rst -*-

.. _API-flush-kthread-work:

==================
flush_kthread_work
==================

*man flush_kthread_work(9)*

*4.6.0-rc5*

flush a kthread_work


Synopsis
========

.. c:function:: void flush_kthread_work( struct kthread_work * work )

Arguments
=========

``work``
    work to flush


Description
===========

If ``work`` is queued or executing, wait for it to finish execution.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
