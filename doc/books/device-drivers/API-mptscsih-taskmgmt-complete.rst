.. -*- coding: utf-8; mode: rst -*-

.. _API-mptscsih-taskmgmt-complete:

==========================
mptscsih_taskmgmt_complete
==========================

*man mptscsih_taskmgmt_complete(9)*

*4.6.0-rc5*

Registered with Fusion MPT base driver


Synopsis
========

.. c:function:: int mptscsih_taskmgmt_complete( MPT_ADAPTER * ioc, MPT_FRAME_HDR * mf, MPT_FRAME_HDR * mr )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``mf``
    Pointer to SCSI task mgmt request frame

``mr``
    Pointer to SCSI task mgmt reply frame


Description
===========

This routine is called from mptbase.c::\ ``mpt_interrupt`` at the
completion of any SCSI task management request. This routine is
registered with the MPT (base) driver at driver load/init time via the
``mpt_register`` API call.

Returns 1 indicating alloc'd request frame ptr should be freed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
