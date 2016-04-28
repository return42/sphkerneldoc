.. -*- coding: utf-8; mode: rst -*-

.. _API-flush-workqueue:

===============
flush_workqueue
===============

*man flush_workqueue(9)*

*4.6.0-rc5*

ensure that any scheduled work has run to completion.


Synopsis
========

.. c:function:: void flush_workqueue( struct workqueue_struct * wq )

Arguments
=========

``wq``
    workqueue to flush


Description
===========

This function sleeps until all work items which were queued on entry
have finished execution, but it is not livelocked by new incoming ones.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
