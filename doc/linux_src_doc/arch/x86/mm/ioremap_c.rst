.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/mm/ioremap.c

.. _`ioremap_nocache`:

ioremap_nocache
===============

.. c:function:: void __iomem *ioremap_nocache(resource_size_t phys_addr, unsigned long size)

    map bus memory into CPU space

    :param resource_size_t phys_addr:
        bus address of the memory

    :param unsigned long size:
        size of the resource to map

.. _`ioremap_nocache.description`:

Description
-----------

ioremap_nocache performs a platform specific sequence of operations to
make bus memory CPU accessible via the readb/readw/readl/writeb/
writew/writel functions and the other mmio helpers. The returned
address is not guaranteed to be usable directly as a virtual
address.

This version of ioremap ensures that the memory is marked uncachable
on the CPU as well as honouring existing caching rules from things like
the PCI bus. Note that there are other caches and buffers on many
busses. In particular driver authors should read up on PCI writes

It's useful if some control registers are in such an area and

.. _`ioremap_nocache.write-combining-or-read-caching-is-not-desirable`:

write combining or read caching is not desirable
------------------------------------------------


Must be freed with iounmap.

.. _`ioremap_uc`:

ioremap_uc
==========

.. c:function:: void __iomem *ioremap_uc(resource_size_t phys_addr, unsigned long size)

    map bus memory into CPU space as strongly uncachable

    :param resource_size_t phys_addr:
        bus address of the memory

    :param unsigned long size:
        size of the resource to map

.. _`ioremap_uc.description`:

Description
-----------

ioremap_uc performs a platform specific sequence of operations to
make bus memory CPU accessible via the readb/readw/readl/writeb/
writew/writel functions and the other mmio helpers. The returned
address is not guaranteed to be usable directly as a virtual
address.

This version of ioremap ensures that the memory is marked with a strong
preference as completely uncachable on the CPU when possible. For non-PAT
systems this ends up setting page-attribute flags PCD=1, PWT=1. For PAT
systems this will set the PAT entry for the pages as strong UC.  This call
will honor existing caching rules from things like the PCI bus. Note that
there are other caches and buffers on many busses. In particular driver
authors should read up on PCI writes.

It's useful if some control registers are in such an area and

.. _`ioremap_uc.write-combining-or-read-caching-is-not-desirable`:

write combining or read caching is not desirable
------------------------------------------------


Must be freed with iounmap.

.. _`ioremap_wc`:

ioremap_wc
==========

.. c:function:: void __iomem *ioremap_wc(resource_size_t phys_addr, unsigned long size)

    map memory into CPU space write combined

    :param resource_size_t phys_addr:
        bus address of the memory

    :param unsigned long size:
        size of the resource to map

.. _`ioremap_wc.description`:

Description
-----------

This version of ioremap ensures that the memory is marked write combining.
Write combining allows faster writes to some hardware devices.

Must be freed with iounmap.

.. _`ioremap_wt`:

ioremap_wt
==========

.. c:function:: void __iomem *ioremap_wt(resource_size_t phys_addr, unsigned long size)

    map memory into CPU space write through

    :param resource_size_t phys_addr:
        bus address of the memory

    :param unsigned long size:
        size of the resource to map

.. _`ioremap_wt.description`:

Description
-----------

This version of ioremap ensures that the memory is marked write through.
Write through stores data into memory while keeping the cache up-to-date.

Must be freed with iounmap.

.. _`iounmap`:

iounmap
=======

.. c:function:: void iounmap(volatile void __iomem *addr)

    Free a IO remapping

    :param volatile void __iomem \*addr:
        virtual address from ioremap\_\*

.. _`iounmap.description`:

Description
-----------

Caller must ensure there is only one unmapping for the same pointer.

.. This file was automatic generated / don't edit.

