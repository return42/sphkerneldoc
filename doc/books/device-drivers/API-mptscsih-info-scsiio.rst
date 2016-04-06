
.. _API-mptscsih-info-scsiio:

====================
mptscsih_info_scsiio
====================

*man mptscsih_info_scsiio(9)*

*4.6.0-rc1*

debug print info on reply frame


Synopsis
========

.. c:function:: void mptscsih_info_scsiio( MPT_ADAPTER * ioc, struct scsi_cmnd * sc, SCSIIOReply_t * pScsiReply )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``sc``
    original scsi cmnd pointer

``pScsiReply``
    Pointer to MPT reply frame


Description
===========

MPT_DEBUG_REPLY needs to be enabled to obtain this info

Refer to lsi/mpi.h.
