.. -*- coding: utf-8; mode: rst -*-

.. _API-proc-print-scsidevice:

=====================
proc_print_scsidevice
=====================

*man proc_print_scsidevice(9)*

*4.6.0-rc5*

return data about this host


Synopsis
========

.. c:function:: int proc_print_scsidevice( struct device * dev, void * data )

Arguments
=========

``dev``
    A scsi device

``data``
    ``struct seq_file`` to output to.


Description
===========

prints Host, Channel, Id, Lun, Vendor, Model, Rev, Type, and revision.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
