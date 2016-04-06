
.. _API-mptscsih-get-scsi-lookup:

========================
mptscsih_get_scsi_lookup
========================

*man mptscsih_get_scsi_lookup(9)*

*4.6.0-rc1*

retrieves scmd entry


Synopsis
========

.. c:function:: struct scsi_cmnd ⋆ mptscsih_get_scsi_lookup( MPT_ADAPTER * ioc, int i )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``i``
    index into the array


Description
===========

Returns the scsi_cmd pointer
