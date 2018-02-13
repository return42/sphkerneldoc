.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/mm/pgtable_64.c

.. _`__ioremap_at`:

\__ioremap_at
=============

.. c:function:: void __iomem *__ioremap_at(phys_addr_t pa, void *ea, unsigned long size, unsigned long flags)

    Low level function to establish the page tables for an IO mapping

    :param phys_addr_t pa:
        *undescribed*

    :param void \*ea:
        *undescribed*

    :param unsigned long size:
        *undescribed*

    :param unsigned long flags:
        *undescribed*

.. _`__iounmap_at`:

\__iounmap_at
=============

.. c:function:: void __iounmap_at(void *ea, unsigned long size)

    Low level function to tear down the page tables for an IO mapping. This is used for mappings that are manipulated manually, like partial unmapping of PCI IOs or ISA space.

    :param void \*ea:
        *undescribed*

    :param unsigned long size:
        *undescribed*

.. This file was automatic generated / don't edit.

