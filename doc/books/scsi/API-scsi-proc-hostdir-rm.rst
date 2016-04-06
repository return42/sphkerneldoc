
.. _API-scsi-proc-hostdir-rm:

====================
scsi_proc_hostdir_rm
====================

*man scsi_proc_hostdir_rm(9)*

*4.6.0-rc1*

remove directory in /proc for a scsi host


Synopsis
========

.. c:function:: void scsi_proc_hostdir_rm( struct scsi_host_template * sht )

Arguments
=========

``sht``
    owner of directory
