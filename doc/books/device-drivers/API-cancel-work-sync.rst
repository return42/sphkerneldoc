.. -*- coding: utf-8; mode: rst -*-

.. _API-cancel-work-sync:

================
cancel_work_sync
================

*man cancel_work_sync(9)*

*4.6.0-rc5*

cancel a work and wait for it to finish


Synopsis
========

.. c:function:: bool cancel_work_sync( struct work_struct * work )

Arguments
=========

``work``
    the work to cancel


Description
===========

Cancel ``work`` and wait for its execution to finish. This function can
be used even if the work re-queues itself or migrates to another
workqueue. On return from this function, ``work`` is guaranteed to be
not pending or executing on any CPU.

cancel_work_sync( ``delayed_work``->work) must not be used for
delayed_work's. Use ``cancel_delayed_work_sync`` instead.

The caller must ensure that the workqueue on which ``work`` was last
queued can't be destroyed before this function returns.


Return
======

``true`` if ``work`` was pending, ``false`` otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
