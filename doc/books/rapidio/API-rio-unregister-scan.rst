
.. _API-rio-unregister-scan:

===================
rio_unregister_scan
===================

*man rio_unregister_scan(9)*

*4.6.0-rc1*

removes enumeration/discovery method from mport


Synopsis
========

.. c:function:: int rio_unregister_scan( int mport_id, struct rio_scan * scan_ops )

Arguments
=========

``mport_id``
    mport device ID for which fabric scan routine has to be unregistered (RIO_MPORT_ANY = apply to all mports that use the specified scan_ops)

``scan_ops``
    enumeration/discovery operations structure


Description
===========

Removes enumeration or discovery method assigned to the specified mport device. If RIO_MPORT_ANY is specified, removes the specified operations from all mports that have them
attached.
