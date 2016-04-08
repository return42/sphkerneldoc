
.. _API-ata-platform-remove-one:

=======================
ata_platform_remove_one
=======================

*man ata_platform_remove_one(9)*

*4.6.0-rc1*

Platform layer callback for device removal


Synopsis
========

.. c:function:: int ata_platform_remove_one( struct platform_device * pdev )

Arguments
=========

``pdev``
    Platform device that was removed


Description
===========

Platform layer indicates to libata via this hook that hot-unplug or module unload event has occurred. Detach all ports. Resource release is handled via devres.


LOCKING
=======

Inherited from platform layer (may sleep).
