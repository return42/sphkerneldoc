.. -*- coding: utf-8; mode: rst -*-

.. _API-mptscsih-bus-reset:

==================
mptscsih_bus_reset
==================

*man mptscsih_bus_reset(9)*

*4.6.0-rc5*

Perform a SCSI BUS_RESET! new_eh variant


Synopsis
========

.. c:function:: int mptscsih_bus_reset( struct scsi_cmnd * SCpnt )

Arguments
=========

``SCpnt``
    Pointer to scsi_cmnd structure, IO which reset is due to


Description
===========

(linux scsi_host_template.eh_bus_reset_handler routine)

Returns SUCCESS or FAILED.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
