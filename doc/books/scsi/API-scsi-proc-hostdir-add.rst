.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-proc-hostdir-add:

=====================
scsi_proc_hostdir_add
=====================

*man scsi_proc_hostdir_add(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
