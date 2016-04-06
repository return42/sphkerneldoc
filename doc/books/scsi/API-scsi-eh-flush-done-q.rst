
.. _API-scsi-eh-flush-done-q:

====================
scsi_eh_flush_done_q
====================

*man scsi_eh_flush_done_q(9)*

*4.6.0-rc1*

finish processed commands or retry them.


Synopsis
========

.. c:function:: void scsi_eh_flush_done_q( struct list_head * done_q )

Arguments
=========

``done_q``
    list_head of processed commands.
