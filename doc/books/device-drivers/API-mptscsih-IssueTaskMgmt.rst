.. -*- coding: utf-8; mode: rst -*-

.. _API-mptscsih-IssueTaskMgmt:

======================
mptscsih_IssueTaskMgmt
======================

*man mptscsih_IssueTaskMgmt(9)*

*4.6.0-rc5*

Generic send Task Management function.


Synopsis
========

.. c:function:: int mptscsih_IssueTaskMgmt( MPT_SCSI_HOST * hd, u8 type, u8 channel, u8 id, u64 lun, int ctx2abort, ulong timeout )

Arguments
=========

``hd``
    Pointer to MPT_SCSI_HOST structure

``type``
    Task Management type

``channel``
    channel number for task management

``id``
    Logical Target ID for reset (if appropriate)

``lun``
    Logical Unit for reset (if appropriate)

``ctx2abort``
    Context for the task to be aborted (if appropriate)

``timeout``
    timeout for task management control


Remark
======

_HardResetHandler can be invoked from an interrupt thread (timer) or a
non-interrupt thread. In the former, must not call ``schedule``.

Not all fields are meaningfull for all task types.

Returns 0 for SUCCESS, or FAILED.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
