
.. _API-SCPNT-TO-LOOKUP-IDX:

===================
SCPNT_TO_LOOKUP_IDX
===================

*man SCPNT_TO_LOOKUP_IDX(9)*

*4.6.0-rc1*

searches for a given scmd in the ScsiLookup[] array list


Synopsis
========

.. c:function:: int SCPNT_TO_LOOKUP_IDX( MPT_ADAPTER * ioc, struct scsi_cmnd * sc )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``sc``
    scsi_cmnd pointer
