
.. _API-mptscsih-set-scsi-lookup:

========================
mptscsih_set_scsi_lookup
========================

*man mptscsih_set_scsi_lookup(9)*

*4.6.0-rc1*

write a scmd entry into the ScsiLookup[] array list


Synopsis
========

.. c:function:: void mptscsih_set_scsi_lookup( MPT_ADAPTER * ioc, int i, struct scsi_cmnd * scmd )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``i``
    index into the array

``scmd``
    scsi_cmnd pointer
