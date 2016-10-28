.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/openrisc/mm/ioremap.c

.. _`pte_alloc_one_kernel`:

pte_alloc_one_kernel
====================

.. c:function:: pte_t __init_refok *pte_alloc_one_kernel(struct mm_struct *mm, unsigned long address)

    initialized (early serial console does this) and will want to alloc a page for its mapping.  No userspace pages will ever get allocated before memory is initialized so this applies only to kernel pages.  In the event that this is called before memory is initialized we allocate the page using the memblock infrastructure.

    :param struct mm_struct \*mm:
        *undescribed*

    :param unsigned long address:
        *undescribed*

.. This file was automatic generated / don't edit.

