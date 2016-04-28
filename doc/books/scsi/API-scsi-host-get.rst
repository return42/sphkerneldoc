.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-host-get:

=============
scsi_host_get
=============

*man scsi_host_get(9)*

*4.6.0-rc5*

inc a Scsi_Host ref count


Synopsis
========

.. c:function:: struct Scsi_Host * scsi_host_get( struct Scsi_Host * shost )

Arguments
=========

``shost``
    Pointer to Scsi_Host to inc.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
