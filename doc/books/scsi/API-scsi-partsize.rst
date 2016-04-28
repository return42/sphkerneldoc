.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-partsize:

=============
scsi_partsize
=============

*man scsi_partsize(9)*

*4.6.0-rc5*

Parse cylinders/heads/sectors from PC partition table


Synopsis
========

.. c:function:: int scsi_partsize( unsigned char * buf, unsigned long capacity, unsigned int * cyls, unsigned int * hds, unsigned int * secs )

Arguments
=========

``buf``
    partition table, see ``scsi_bios_ptable``

``capacity``
    size of the disk in sectors

``cyls``
    put cylinders here

``hds``
    put heads here

``secs``
    put sectors here


Description
===========

determine the BIOS mapping/geometry used to create the partition table,
storing the results in *cyls, *hds, and *secs


Returns
=======

-1 on failure, 0 on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
