
.. _API-parport-register-port:

=====================
parport_register_port
=====================

*man parport_register_port(9)*

*4.6.0-rc1*

register a parallel port


Synopsis
========

.. c:function:: struct parport ⋆ parport_register_port( unsigned long base, int irq, int dma, struct parport_operations * ops )

Arguments
=========

``base``
    base I/O address

``irq``
    IRQ line

``dma``
    DMA channel

``ops``
    pointer to the port driver's port operations structure


Description
===========

When a parallel port (lowlevel) driver finds a port that should be made available to parallel port device drivers, it should call ``parport_register_port``. The ``base``, ``irq``,
and ``dma`` parameters are for the convenience of port drivers, and for ports where they aren't meaningful needn't be set to anything special. They can be altered afterwards by
adjusting the relevant members of the parport structure that is returned and represents the port. They should not be tampered with after calling parport_announce_port, however.

If there are parallel port device drivers in the system that have registered themselves using ``parport_register_driver``, they are not told about the port at this time; that is
done by ``parport_announce_port``.

The ``ops`` structure is allocated by the caller, and must not be deallocated before calling ``parport_remove_port``.

If there is no memory to allocate a new parport structure, this function will return ``NULL``.
