
.. _API-scsi-eh-get-sense:

=================
scsi_eh_get_sense
=================

*man scsi_eh_get_sense(9)*

*4.6.0-rc1*

Get device sense data.


Synopsis
========

.. c:function:: int scsi_eh_get_sense( struct list_head * work_q, struct list_head * done_q )

Arguments
=========

``work_q``
    Queue of commands to process.

``done_q``
    Queue of processed commands.


Description
===========

See if we need to request sense information. if so, then get it now, so we have a better idea of what to do.


Notes
=====

This has the unfortunate side effect that if a shost adapter does not automatically request sense information, we end up shutting it down before we request it.

All drivers should request sense information internally these days, so for now all I have to say is tough noogies if you end up in here.


XXX
===

Long term this code should go away, but that needs an audit of all LLDDs first.
