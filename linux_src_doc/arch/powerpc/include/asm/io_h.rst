.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/asm/io.h

.. _`ioremap`:

ioremap
=======

.. c:function:: void __iomem *ioremap(phys_addr_t address, unsigned long size)

    map bus memory into CPU space

    :param address:
        bus address of the memory
    :type address: phys_addr_t

    :param size:
        size of the resource to map
    :type size: unsigned long

.. _`ioremap.description`:

Description
-----------

ioremap performs a platform specific sequence of operations to
make bus memory CPU accessible via the readb/readw/readl/writeb/
writew/writel functions and the other mmio helpers. The returned
address is not guaranteed to be usable directly as a virtual
address.

.. _`ioremap.we-provide-a-few-variations-of-it`:

We provide a few variations of it
---------------------------------


\* ioremap is the standard one and provides non-cacheable guarded mappings
and can be hooked by the platform via ppc_md

\* ioremap_prot allows to specify the page flags as an argument and can
also be hooked by the platform via ppc_md.

\* ioremap_nocache is identical to ioremap

\* ioremap_wc enables write combining

\* ioremap_wt enables write through

\* ioremap_coherent maps coherent cached memory

\* iounmap undoes such a mapping and can be hooked

\* \__ioremap_at (and the pending \__iounmap_at) are low level functions to
create hand-made mappings for use only by the PCI code and cannot
currently be hooked. Must be page aligned.

\* \__ioremap is the low level implementation used by ioremap and
ioremap_prot and cannot be hooked (but can be used by a hook on one
of the previous ones)

\* \__ioremap_caller is the same as above but takes an explicit caller
reference rather than using \__builtin_return_address(0)

\* \__iounmap, is the low level implementation used by iounmap and cannot
be hooked (but can be used by a hook on iounmap)

.. _`virt_to_phys`:

virt_to_phys
============

.. c:function:: unsigned long virt_to_phys(volatile void *address)

    map virtual addresses to physical

    :param address:
        address to remap
    :type address: volatile void \*

.. _`virt_to_phys.description`:

Description
-----------

The returned physical address is the physical (CPU) mapping for
the memory address given. It is only valid to use this function on
addresses directly mapped or allocated via kmalloc.

This function does not give bus mappings for DMA transfers. In
almost all conceivable cases a device driver should not be using
this function

.. _`phys_to_virt`:

phys_to_virt
============

.. c:function:: void *phys_to_virt(unsigned long address)

    map physical address to virtual

    :param address:
        address to remap
    :type address: unsigned long

.. _`phys_to_virt.description`:

Description
-----------

The returned virtual address is a current CPU mapping for
the memory address given. It is only valid to use this function on
addresses that have a kernel mapping

This function does not handle bus mappings for DMA transfers. In
almost all conceivable cases a device driver should not be using
this function

.. This file was automatic generated / don't edit.

