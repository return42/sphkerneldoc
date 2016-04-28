.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-complete-async-scans:

=========================
scsi_complete_async_scans
=========================

*man scsi_complete_async_scans(9)*

*4.6.0-rc5*

Wait for asynchronous scans to complete


Synopsis
========

.. c:function:: int scsi_complete_async_scans( void )

Arguments
=========

``void``
    no arguments


Description
===========

When this function returns, any host which started scanning before this
function was called will have finished its scan. Hosts which started
scanning after this function was called may or may not have finished.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
