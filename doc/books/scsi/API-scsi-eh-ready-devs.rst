.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-eh-ready-devs:

==================
scsi_eh_ready_devs
==================

*man scsi_eh_ready_devs(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
