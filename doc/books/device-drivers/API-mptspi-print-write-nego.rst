.. -*- coding: utf-8; mode: rst -*-

.. _API-mptspi-print-write-nego:

=======================
mptspi_print_write_nego
=======================

*man mptspi_print_write_nego(9)*

*4.6.0-rc5*

negotiation parameters debug info that is being sent


Synopsis
========

.. c:function:: void mptspi_print_write_nego( struct _MPT_SCSI_HOST * hd, struct scsi_target * starget, u32 ii )

Arguments
=========

``hd``
    Pointer to a SCSI HOST structure

``starget``
    SCSI target

``ii``
    negotiation parameters


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
