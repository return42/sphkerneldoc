.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/io.h

.. _`virt_to_phys`:

virt_to_phys
============

.. c:function:: phys_addr_t virt_to_phys(volatile void *address)

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

.. c:function:: void *phys_to_virt(phys_addr_t address)

    map physical address to virtual

    :param address:
        address to remap
    :type address: phys_addr_t

.. _`phys_to_virt.description`:

Description
-----------

     The returned virtual address is a current CPU mapping for
     the memory address given. It is only valid to use this function on
     addresses that have a kernel mapping

     This function does not handle bus mappings for DMA transfers. In
     almost all conceivable cases a device driver should not be using
     this function

.. _`ioremap`:

ioremap
=======

.. c:function:: void __iomem *ioremap(resource_size_t offset, unsigned long size)

    map bus memory into CPU space

    :param offset:
        bus address of the memory
    :type offset: resource_size_t

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

If the area you are trying to map is a PCI BAR you should have a
look at \ :c:func:`pci_iomap`\ .

.. This file was automatic generated / don't edit.

