.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-eh-finish-cmd:

==================
scsi_eh_finish_cmd
==================

*man scsi_eh_finish_cmd(9)*

*4.6.0-rc5*

Handle a cmd that eh is finished with.


Synopsis
========

.. c:function:: void scsi_eh_finish_cmd( struct scsi_cmnd * scmd, struct list_head * done_q )

Arguments
=========

``scmd``
    Original SCSI cmd that eh has finished.

``done_q``
    Queue for processed commands.


Notes
=====

We don't want to use the normal command completion while we are are
still handling errors - it may cause other commands to be queued, and
that would disturb what we are doing. Thus we really want to keep a list
of pending commands for final completion, and once we are ready to leave
error handling we handle completion for real.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
