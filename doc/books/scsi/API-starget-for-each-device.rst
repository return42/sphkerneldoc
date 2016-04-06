
.. _API-starget-for-each-device:

=======================
starget_for_each_device
=======================

*man starget_for_each_device(9)*

*4.6.0-rc1*

helper to walk all devices of a target


Synopsis
========

.. c:function:: void starget_for_each_device( struct scsi_target * starget, void * data, void (*fn) struct scsi_device *, void * )

Arguments
=========

``starget``
    target whose devices we want to iterate over.

``data``
    Opaque passed to each function call.

``fn``
    Function to call on each device


Description
===========

This traverses over each device of ``starget``. The devices have a reference that must be released by scsi_host_put when breaking out of the loop.
