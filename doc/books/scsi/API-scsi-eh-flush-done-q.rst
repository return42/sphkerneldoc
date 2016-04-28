.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-eh-flush-done-q:

====================
scsi_eh_flush_done_q
====================

*man scsi_eh_flush_done_q(9)*

*4.6.0-rc5*

finish processed commands or retry them.


Synopsis
========

.. c:function:: void scsi_eh_flush_done_q( struct list_head * done_q )

Arguments
=========

``done_q``
    list_head of processed commands.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
