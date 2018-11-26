.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/mm/pgtable_64.c

.. _`__ioremap_at`:

\__ioremap_at
=============

.. c:function:: void __iomem *__ioremap_at(phys_addr_t pa, void *ea, unsigned long size, pgprot_t prot)

    Low level function to establish the page tables for an IO mapping

    :param pa:
        *undescribed*
    :type pa: phys_addr_t

    :param ea:
        *undescribed*
    :type ea: void \*

    :param size:
        *undescribed*
    :type size: unsigned long

    :param prot:
        *undescribed*
    :type prot: pgprot_t

.. _`__iounmap_at`:

\__iounmap_at
=============

.. c:function:: void __iounmap_at(void *ea, unsigned long size)

    Low level function to tear down the page tables for an IO mapping. This is used for mappings that are manipulated manually, like partial unmapping of PCI IOs or ISA space.

    :param ea:
        *undescribed*
    :type ea: void \*

    :param size:
        *undescribed*
    :type size: unsigned long

.. This file was automatic generated / don't edit.

