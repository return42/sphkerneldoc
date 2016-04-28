.. -*- coding: utf-8; mode: rst -*-

.. _API-mptscsih-host-reset:

===================
mptscsih_host_reset
===================

*man mptscsih_host_reset(9)*

*4.6.0-rc5*

Perform a SCSI host adapter RESET (new_eh variant)


Synopsis
========

.. c:function:: int mptscsih_host_reset( struct scsi_cmnd * SCpnt )

Arguments
=========

``SCpnt``
    Pointer to scsi_cmnd structure, IO which reset is due to


Description
===========

(linux scsi_host_template.eh_host_reset_handler routine)

Returns SUCCESS or FAILED.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
