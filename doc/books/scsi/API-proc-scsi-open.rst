.. -*- coding: utf-8; mode: rst -*-

.. _API-proc-scsi-open:

==============
proc_scsi_open
==============

*man proc_scsi_open(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
