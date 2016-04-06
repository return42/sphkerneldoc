
.. _API-proc-scsi-write:

===============
proc_scsi_write
===============

*man proc_scsi_write(9)*

*4.6.0-rc1*

handle writes to /proc/scsi/scsi


Synopsis
========

.. c:function:: ssize_t proc_scsi_write( struct file * file, const char __user * buf, size_t length, loff_t * ppos )

Arguments
=========

``file``
    not used

``buf``
    buffer to write

``length``
    length of buf, at most PAGE_SIZE

``ppos``
    not used


Description
===========

this provides a legacy mechanism to add or remove devices by Host, Channel, ID, and Lun. To use, “echo 'scsi add-single-device 0 1 2 3' > /proc/scsi/scsi” or “echo 'scsi
remove-single-device 0 1 2 3' > /proc/scsi/scsi” with “0 1 2 3” replaced by the Host, Channel, Id, and Lun.


Note
====

this seems to be aimed at parallel SCSI. Most modern busses (USB, SATA, Firewire, Fibre Channel, etc) dynamically assign these values to provide a unique identifier and nothing
more.
