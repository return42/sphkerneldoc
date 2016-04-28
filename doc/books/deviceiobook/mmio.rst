.. -*- coding: utf-8; mode: rst -*-

.. _mmio:

================
Memory Mapped IO
================


.. _getting_access_to_the_device:

Getting Access to the Device
============================

The most widely supported form of IO is memory mapped IO. That is, a
part of the CPU's address space is interpreted not as accesses to
memory, but as accesses to a device. Some architectures define devices
to be at a fixed address, but most have some method of discovering
devices. The PCI bus walk is a good example of such a scheme. This
document does not cover how to receive such an address, but assumes you
are starting with one. Physical addresses are of type unsigned long.

This address should not be used directly. Instead, to get an address
suitable for passing to the accessor functions described below, you
should call ``ioremap``. An address suitable for accessing the device
will be returned to you.

After you've finished using the device (say, in your module's exit
routine), call ``iounmap`` in order to return the address space to the
kernel. Most architectures allocate new address space each time you call
``ioremap``, and they can run out unless you call ``iounmap``.


.. _accessing_the_device:

Accessing the device
====================

The part of the interface most used by drivers is reading and writing
memory-mapped registers on the device. Linux provides interfaces to read
and write 8-bit, 16-bit, 32-bit and 64-bit quantities. Due to a
historical accident, these are named byte, word, long and quad accesses.
Both read and write accesses are supported; there is no prefetch support
at this time.

The functions are named ``readb``, ``readw``, ``readl``, ``readq``,
``readb_relaxed``, ``readw_relaxed``, ``readl_relaxed``,
``readq_relaxed``, ``writeb``, ``writew``, ``writel`` and ``writeq``.

Some devices (such as framebuffers) would like to use larger transfers
than 8 bytes at a time. For these devices, the ``memcpy_toio``,
``memcpy_fromio`` and ``memset_io`` functions are provided. Do not use
memset or memcpy on IO addresses; they are not guaranteed to copy data
in order.

The read and write functions are defined to be ordered. That is the
compiler is not permitted to reorder the I/O sequence. When the ordering
can be compiler optimised, you can use ``
    __readb`` and friends to indicate the relaxed ordering. Use this
with care.

While the basic functions are defined to be synchronous with respect to
each other and ordered with respect to each other the busses the devices
sit on may themselves have asynchronicity. In particular many authors
are burned by the fact that PCI bus writes are posted asynchronously. A
driver author must issue a read from the same device to ensure that
writes have occurred in the specific cases the author cares. This kind
of property cannot be hidden from driver writers in the API. In some
cases, the read used to flush the device may be expected to fail (if the
card is resetting, for example). In that case, the read should be done
from config space, which is guaranteed to soft-fail if the card doesn't
respond.

The following is an example of flushing a write to a device when the
driver would like to ensure the write's effects are visible prior to
continuing execution.


.. code-block:: c

    static inline void
    qla1280_disable_intrs(struct scsi_qla_host *ha)
    {
        struct device_reg *reg;

        reg = ha->iobase;
        /* disable risc and host interrupts */
        WRT_REG_WORD(&reg->ictrl, 0);
        /*
         * The following read will ensure that the above write
         * has been received by the device before we return from this
         * function.
         */
        RD_REG_WORD(&reg->ictrl);
        ha->flags.ints_enabled = 0;
    }

In addition to write posting, on some large multiprocessing systems
(e.g. SGI Challenge, Origin and Altix machines) posted writes won't be
strongly ordered coming from different CPUs. Thus it's important to
properly protect parts of your driver that do memory-mapped writes with
locks and use the ``mmiowb`` to make sure they arrive in the order
intended. Issuing a regular ``readX
    `` will also ensure write ordering, but should only be used when the
driver has to be sure that the write has actually arrived at the device
(not that it's simply ordered with respect to other writes), since a
full ``readX`` is a relatively expensive operation.

Generally, one should use ``mmiowb`` prior to releasing a spinlock that
protects regions using ``writeb
    `` or similar functions that aren't surrounded by ``
    readb`` calls, which will ensure ordering and flushing. The
following pseudocode illustrates what might occur if write ordering
isn't guaranteed via ``mmiowb`` or one of the ``readX`` functions.


.. code-block:: c

    CPU A:  spin_lock_irqsave(&dev_lock, flags)
    CPU A:  ...
    CPU A:  writel(newval, ring_ptr);
    CPU A:  spin_unlock_irqrestore(&dev_lock, flags)
            ...
    CPU B:  spin_lock_irqsave(&dev_lock, flags)
    CPU B:  writel(newval2, ring_ptr);
    CPU B:  ...
    CPU B:  spin_unlock_irqrestore(&dev_lock, flags)

In the case above, newval2 could be written to ring_ptr before newval.
Fixing it is easy though:


.. code-block:: c

    CPU A:  spin_lock_irqsave(&dev_lock, flags)
    CPU A:  ...
    CPU A:  writel(newval, ring_ptr);
    CPU A:  mmiowb(); /* ensure no other writes beat us to the device */
    CPU A:  spin_unlock_irqrestore(&dev_lock, flags)
            ...
    CPU B:  spin_lock_irqsave(&dev_lock, flags)
    CPU B:  writel(newval2, ring_ptr);
    CPU B:  ...
    CPU B:  mmiowb();
    CPU B:  spin_unlock_irqrestore(&dev_lock, flags)

See tg3.c for a real world example of how to use ``mmiowb
    ``

PCI ordering rules also guarantee that PIO read responses arrive after
any outstanding DMA writes from that bus, since for some devices the
result of a ``readb`` call may signal to the driver that a DMA
transaction is complete. In many cases, however, the driver may want to
indicate that the next ``readb`` call has no relation to any previous
DMA writes performed by the device. The driver can use ``readb_relaxed``
for these cases, although only some platforms will honor the relaxed
semantics. Using the relaxed read functions will provide significant
performance benefits on platforms that support it. The qla2xxx driver
provides examples of how to use ``readX_relaxed``. In many cases, a
majority of the driver's ``readX`` calls can safely be converted to
``readX_relaxed`` calls, since only a few will indicate or depend on DMA
completion.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
