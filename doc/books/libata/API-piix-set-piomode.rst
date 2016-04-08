
.. _API-piix-set-piomode:

================
piix_set_piomode
================

*man piix_set_piomode(9)*

*4.6.0-rc1*

Initialize host controller PATA PIO timings


Synopsis
========

.. c:function:: void piix_set_piomode( struct ata_port * ap, struct ata_device * adev )

Arguments
=========

``ap``
    Port whose timings we are configuring

``adev``
    Drive in question


Description
===========

Set PIO mode for device, in host controller PCI config space.


LOCKING
=======

None (inherited from caller).
