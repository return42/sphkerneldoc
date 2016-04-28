.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-add-host-with-dma:

======================
scsi_add_host_with_dma
======================

*man scsi_add_host_with_dma(9)*

*4.6.0-rc5*

add a scsi host with dma device


Synopsis
========

.. c:function:: int scsi_add_host_with_dma( struct Scsi_Host * shost, struct device * dev, struct device * dma_dev )

Arguments
=========

``shost``
    scsi host pointer to add

``dev``
    a struct device of type scsi class

``dma_dev``
    dma device for the host


Note
====

You rarely need to worry about this unless you're in a virtualised host
environments, so use the simpler ``scsi_add_host`` function instead.


Return value
============

0 on success / != 0 for error


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
