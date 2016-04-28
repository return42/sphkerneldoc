.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-queue-work:

===============
scsi_queue_work
===============

*man scsi_queue_work(9)*

*4.6.0-rc5*

Queue work to the Scsi_Host workqueue.


Synopsis
========

.. c:function:: int scsi_queue_work( struct Scsi_Host * shost, struct work_struct * work )

Arguments
=========

``shost``
    Pointer to Scsi_Host.

``work``
    Work to queue for execution.


Return value
============

1 - work queued for execution 0 - work is already queued -EINVAL - work
queue doesn't exist


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
