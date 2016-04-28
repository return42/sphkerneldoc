.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-register-scan:

=================
rio_register_scan
=================

*man rio_register_scan(9)*

*4.6.0-rc5*

enumeration/discovery method registration interface


Synopsis
========

.. c:function:: int rio_register_scan( int mport_id, struct rio_scan * scan_ops )

Arguments
=========

``mport_id``
    mport device ID for which fabric scan routine has to be set
    (RIO_MPORT_ANY = set for all available mports)

``scan_ops``
    enumeration/discovery operations structure


Description
===========

Registers enumeration/discovery operations with RapidIO subsystem and
attaches it to the specified mport device (or all available mports if
RIO_MPORT_ANY is specified).

Returns error if the mport already has an enumerator attached to it. In
case of RIO_MPORT_ANY skips mports with valid scan routines (no
error).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
