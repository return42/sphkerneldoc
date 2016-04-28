.. -*- coding: utf-8; mode: rst -*-

.. _API---shost-for-each-device:

=======================
__shost_for_each_device
=======================

*man __shost_for_each_device(9)*

*4.6.0-rc5*

iterate over all devices of a host (UNLOCKED)


Synopsis
========

.. c:function:: __shost_for_each_device( sdev, shost )

Arguments
=========

``sdev``
    the ``struct scsi_device`` to use as a cursor

``shost``
    the ``struct scsi_host`` to iterate over


Description
===========

Iterator that returns each device attached to ``shost``. It does _not_
take a reference on the scsi_device, so the whole loop must be
protected by shost->host_lock.


Note
====

The only reason to use this is because you need to access the device
list in interrupt context. Otherwise you really want to use
shost_for_each_device instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
