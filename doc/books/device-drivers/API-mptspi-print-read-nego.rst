
.. _API-mptspi-print-read-nego:

======================
mptspi_print_read_nego
======================

*man mptspi_print_read_nego(9)*

*4.6.0-rc1*

negotiation parameters debug info that is being read


Synopsis
========

.. c:function:: void mptspi_print_read_nego( struct _MPT_SCSI_HOST * hd, struct scsi_target * starget, u32 ii )

Arguments
=========

``hd``
    Pointer to a SCSI HOST structure

``starget``
    SCSI target

``ii``
    negotiation parameters
