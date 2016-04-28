.. -*- coding: utf-8; mode: rst -*-

.. _API-SCPNT-TO-LOOKUP-IDX:

===================
SCPNT_TO_LOOKUP_IDX
===================

*man SCPNT_TO_LOOKUP_IDX(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
