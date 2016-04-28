.. -*- coding: utf-8; mode: rst -*-

.. _API-mptscsih-set-scsi-lookup:

========================
mptscsih_set_scsi_lookup
========================

*man mptscsih_set_scsi_lookup(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
