.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-host-lookup:

================
scsi_host_lookup
================

*man scsi_host_lookup(9)*

*4.6.0-rc5*

get a reference to a Scsi_Host by host no


Synopsis
========

.. c:function:: struct Scsi_Host * scsi_host_lookup( unsigned short hostnum )

Arguments
=========

``hostnum``
    host number to locate


Return value
============

A pointer to located Scsi_Host or NULL.

The caller must do a ``scsi_host_put`` to drop the reference that
``scsi_host_get`` took. The ``put_device`` below dropped the reference
from ``class_find_device``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
