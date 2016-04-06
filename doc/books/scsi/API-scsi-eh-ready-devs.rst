
.. _API-scsi-eh-ready-devs:

==================
scsi_eh_ready_devs
==================

*man scsi_eh_ready_devs(9)*

*4.6.0-rc1*

check device ready state and recover if not.


Synopsis
========

.. c:function:: void scsi_eh_ready_devs( struct Scsi_Host * shost, struct list_head * work_q, struct list_head * done_q )

Arguments
=========

``shost``
    host to be recovered.

``work_q``
    ``list_head`` for pending commands.

``done_q``
    ``list_head`` for processed commands.
