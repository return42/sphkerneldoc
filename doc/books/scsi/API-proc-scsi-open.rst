
.. _API-proc-scsi-open:

==============
proc_scsi_open
==============

*man proc_scsi_open(9)*

*4.6.0-rc1*

glue function


Synopsis
========

.. c:function:: int proc_scsi_open( struct inode * inode, struct file * file )

Arguments
=========

``inode``
    not used

``file``
    passed to ``single_open``


Description
===========

Associates proc_scsi_show with this file
