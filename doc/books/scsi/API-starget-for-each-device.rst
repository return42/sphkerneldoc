.. -*- coding: utf-8; mode: rst -*-

.. _API-starget-for-each-device:

=======================
starget_for_each_device
=======================

*man starget_for_each_device(9)*

*4.6.0-rc5*

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

This traverses over each device of ``starget``. The devices have a
reference that must be released by scsi_host_put when breaking out of
the loop.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
