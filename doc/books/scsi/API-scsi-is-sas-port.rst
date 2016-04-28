.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-is-sas-port:

================
scsi_is_sas_port
================

*man scsi_is_sas_port(9)*

*4.6.0-rc5*

check if a struct device represents a SAS port


Synopsis
========

.. c:function:: int scsi_is_sas_port( const struct device * dev )

Arguments
=========

``dev``
    device to check


Returns
=======

``1`` if the device represents a SAS Port, ``0`` else


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
