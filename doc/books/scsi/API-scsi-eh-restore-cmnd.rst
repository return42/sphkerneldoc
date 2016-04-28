.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-eh-restore-cmnd:

====================
scsi_eh_restore_cmnd
====================

*man scsi_eh_restore_cmnd(9)*

*4.6.0-rc5*

Restore a scsi command info as part of error recovery


Synopsis
========

.. c:function:: void scsi_eh_restore_cmnd( struct scsi_cmnd * scmd, struct scsi_eh_save * ses )

Arguments
=========

``scmd``
    SCSI command structure to restore

``ses``
    saved information from a coresponding call to scsi_eh_prep_cmnd


Description
===========

Undo any damage done by above ``scsi_eh_prep_cmnd``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
