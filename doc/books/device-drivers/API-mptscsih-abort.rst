.. -*- coding: utf-8; mode: rst -*-

.. _API-mptscsih-abort:

==============
mptscsih_abort
==============

*man mptscsih_abort(9)*

*4.6.0-rc5*

Abort linux scsi_cmnd routine, new_eh variant


Synopsis
========

.. c:function:: int mptscsih_abort( struct scsi_cmnd * SCpnt )

Arguments
=========

``SCpnt``
    Pointer to scsi_cmnd structure, IO to be aborted


Description
===========

(linux scsi_host_template.eh_abort_handler routine)

Returns SUCCESS or FAILED.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
