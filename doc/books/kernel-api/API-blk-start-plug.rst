
.. _API-blk-start-plug:

==============
blk_start_plug
==============

*man blk_start_plug(9)*

*4.6.0-rc1*

initialize blk_plug and track it inside the task_struct


Synopsis
========

.. c:function:: void blk_start_plug( struct blk_plug * plug )

Arguments
=========

``plug``
    The ``struct blk_plug`` that needs to be initialized


Description
===========

Tracking blk_plug inside the task_struct will help with auto-flushing the pending I/O should the task end up blocking between ``blk_start_plug`` and ``blk_finish_plug``. This is
important from a performance perspective, but also ensures that we don't deadlock. For instance, if the task is blocking for a memory allocation, memory reclaim could end up
wanting to free a page belonging to that request that is currently residing in our private plug. By flushing the pending I/O when the process goes to sleep, we avoid this kind of
deadlock.
