.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-alloc-target:

=================
scsi_alloc_target
=================

*man scsi_alloc_target(9)*

*4.6.0-rc5*

allocate a new or find an existing target


Synopsis
========

.. c:function:: struct scsi_target * scsi_alloc_target( struct device * parent, int channel, uint id )

Arguments
=========

``parent``
    parent of the target (need not be a scsi host)

``channel``
    target channel number (zero if no channels)

``id``
    target id number


Description
===========

Return an existing target if one exists, provided it hasn't already gone
into STARGET_DEL state, otherwise allocate a new target.

The target is returned with an incremented reference, so the caller is
responsible for both reaping and doing a last put


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
