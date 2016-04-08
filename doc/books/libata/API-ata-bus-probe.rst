
.. _API-ata-bus-probe:

=============
ata_bus_probe
=============

*man ata_bus_probe(9)*

*4.6.0-rc1*

Reset and probe ATA bus


Synopsis
========

.. c:function:: int ata_bus_probe( struct ata_port * ap )

Arguments
=========

``ap``
    Bus to probe


Description
===========

Master ATA bus probing function. Initiates a hardware-dependent bus reset, then attempts to identify any devices found on the bus.


LOCKING
=======

PCI/etc. bus probe sem.


RETURNS
=======

Zero on success, negative errno otherwise.
