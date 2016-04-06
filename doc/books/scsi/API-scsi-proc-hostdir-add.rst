
.. _API-scsi-proc-hostdir-add:

=====================
scsi_proc_hostdir_add
=====================

*man scsi_proc_hostdir_add(9)*

*4.6.0-rc1*

Create directory in /proc for a scsi host


Synopsis
========

.. c:function:: void scsi_proc_hostdir_add( struct scsi_host_template * sht )

Arguments
=========

``sht``
    owner of this directory


Description
===========

Sets sht->proc_dir to the new directory.
