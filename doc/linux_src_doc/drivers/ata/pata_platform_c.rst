.. -*- coding: utf-8; mode: rst -*-

===============
pata_platform.c
===============


.. _`__pata_platform_probe`:

__pata_platform_probe
=====================

.. c:function:: int __pata_platform_probe (struct device *dev, struct resource *io_res, struct resource *ctl_res, struct resource *irq_res, unsigned int ioport_shift, int __pio_mask, struct scsi_host_template *sht)

    attach a platform interface

    :param struct device \*dev:
        device

    :param struct resource \*io_res:
        Resource representing I/O base

    :param struct resource \*ctl_res:
        Resource representing CTL base

    :param struct resource \*irq_res:
        Resource representing IRQ and its flags

    :param unsigned int ioport_shift:
        I/O port shift

    :param int __pio_mask:
        PIO mask

    :param struct scsi_host_template \*sht:
        scsi_host_template to use when registering



.. _`__pata_platform_probe.description`:

Description
-----------

Register a platform bus IDE interface. Such interfaces are PIO and we
assume do not support IRQ sharing.



.. _`__pata_platform_probe.platform-devices-are-expected-to-contain-at-least-2-resources-per-port`:

Platform devices are expected to contain at least 2 resources per port
----------------------------------------------------------------------


- I/O Base (IORESOURCE_IO or IORESOURCE_MEM)
- CTL Base (IORESOURCE_IO or IORESOURCE_MEM)



.. _`__pata_platform_probe.and-optionally`:

and optionally
--------------


- IRQ           (IORESOURCE_IRQ)

        If the base resources are both mem types, the :c:func:`ioremap` is handled
        here. For IORESOURCE_IO, it's assumed that there's no remapping
        necessary.

        If no IRQ resource is present, PIO polling mode is used instead.

