
.. _API-ata-host-activate:

=================
ata_host_activate
=================

*man ata_host_activate(9)*

*4.6.0-rc1*

start host, request IRQ and register it


Synopsis
========

.. c:function:: int ata_host_activate( struct ata_host * host, int irq, irq_handler_t irq_handler, unsigned long irq_flags, struct scsi_host_template * sht )

Arguments
=========

``host``
    target ATA host

``irq``
    IRQ to request

``irq_handler``
    irq_handler used when requesting IRQ

``irq_flags``
    irq_flags used when requesting IRQ

``sht``
    scsi_host_template to use when registering the host


Description
===========

After allocating an ATA host and initializing it, most libata LLDs perform three steps to activate the host - start host, request IRQ and register it. This helper takes necessasry
arguments and performs the three steps in one go.

An invalid IRQ skips the IRQ registration and expects the host to have set polling mode on the port. In this case, ``irq_handler`` should be NULL.


LOCKING
=======

Inherited from calling layer (may sleep).


RETURNS
=======

0 on success, -errno otherwise.
