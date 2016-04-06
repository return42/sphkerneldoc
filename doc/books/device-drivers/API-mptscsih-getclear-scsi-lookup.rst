
.. _API-mptscsih-getclear-scsi-lookup:

=============================
mptscsih_getclear_scsi_lookup
=============================

*man mptscsih_getclear_scsi_lookup(9)*

*4.6.0-rc1*

retrieves and clears scmd entry from ScsiLookup[] array list


Synopsis
========

.. c:function:: struct scsi_cmnd ⋆ mptscsih_getclear_scsi_lookup( MPT_ADAPTER * ioc, int i )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``i``
    index into the array


Description
===========

Returns the scsi_cmd pointer
