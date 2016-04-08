
.. _API-ata-dev-xfermask:

================
ata_dev_xfermask
================

*man ata_dev_xfermask(9)*

*4.6.0-rc1*

Compute supported xfermask of the given device


Synopsis
========

.. c:function:: void ata_dev_xfermask( struct ata_device * dev )

Arguments
=========

``dev``
    Device to compute xfermask for


Description
===========

Compute supported xfermask of ``dev`` and store it in dev->⋆_mask. This function is responsible for applying all known limits including host controller limits, device blacklist,
etc...


LOCKING
=======

None.
