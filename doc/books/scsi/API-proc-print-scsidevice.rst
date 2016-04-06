
.. _API-proc-print-scsidevice:

=====================
proc_print_scsidevice
=====================

*man proc_print_scsidevice(9)*

*4.6.0-rc1*

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
