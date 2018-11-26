.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/mm/pgtable.c

.. _`reserve_top_address`:

reserve_top_address
===================

.. c:function:: void reserve_top_address(unsigned long reserve)

    reserves a hole in the top of kernel address space \ ``reserve``\  - size of hole to reserve

    :param reserve:
        *undescribed*
    :type reserve: unsigned long

.. _`reserve_top_address.description`:

Description
-----------

Can be used to relocate the fixmap area and poke a hole in the top
of kernel address space to make room for a hypervisor.

.. _`p4d_set_huge`:

p4d_set_huge
============

.. c:function:: int p4d_set_huge(p4d_t *p4d, phys_addr_t addr, pgprot_t prot)

    setup kernel P4D mapping

    :param p4d:
        *undescribed*
    :type p4d: p4d_t \*

    :param addr:
        *undescribed*
    :type addr: phys_addr_t

    :param prot:
        *undescribed*
    :type prot: pgprot_t

.. _`p4d_set_huge.description`:

Description
-----------

No 512GB pages yet -- always return 0

.. _`p4d_clear_huge`:

p4d_clear_huge
==============

.. c:function:: int p4d_clear_huge(p4d_t *p4d)

    clear kernel P4D mapping when it is set

    :param p4d:
        *undescribed*
    :type p4d: p4d_t \*

.. _`p4d_clear_huge.description`:

Description
-----------

No 512GB pages yet -- always return 0

.. _`pud_set_huge`:

pud_set_huge
============

.. c:function:: int pud_set_huge(pud_t *pud, phys_addr_t addr, pgprot_t prot)

    setup kernel PUD mapping

    :param pud:
        *undescribed*
    :type pud: pud_t \*

    :param addr:
        *undescribed*
    :type addr: phys_addr_t

    :param prot:
        *undescribed*
    :type prot: pgprot_t

.. _`pud_set_huge.description`:

Description
-----------

MTRRs can override PAT memory types with 4KiB granularity. Therefore, this

.. _`pud_set_huge.function-sets-up-a-huge-page-only-if-any-of-the-following-conditions-are-met`:

function sets up a huge page only if any of the following conditions are met
----------------------------------------------------------------------------


- MTRRs are disabled, or

- MTRRs are enabled and the range is completely covered by a single MTRR, or

- MTRRs are enabled and the corresponding MTRR memory type is WB, which
has no effect on the requested PAT memory type.

Callers should try to decrease page size (1GB -> 2MB -> 4K) if the bigger
page mapping attempt fails.

Returns 1 on success and 0 on failure.

.. _`pmd_set_huge`:

pmd_set_huge
============

.. c:function:: int pmd_set_huge(pmd_t *pmd, phys_addr_t addr, pgprot_t prot)

    setup kernel PMD mapping

    :param pmd:
        *undescribed*
    :type pmd: pmd_t \*

    :param addr:
        *undescribed*
    :type addr: phys_addr_t

    :param prot:
        *undescribed*
    :type prot: pgprot_t

.. _`pmd_set_huge.description`:

Description
-----------

See text over \ :c:func:`pud_set_huge`\  above.

Returns 1 on success and 0 on failure.

.. _`pud_clear_huge`:

pud_clear_huge
==============

.. c:function:: int pud_clear_huge(pud_t *pud)

    clear kernel PUD mapping when it is set

    :param pud:
        *undescribed*
    :type pud: pud_t \*

.. _`pud_clear_huge.description`:

Description
-----------

Returns 1 on success and 0 on failure (no PUD map is found).

.. _`pmd_clear_huge`:

pmd_clear_huge
==============

.. c:function:: int pmd_clear_huge(pmd_t *pmd)

    clear kernel PMD mapping when it is set

    :param pmd:
        *undescribed*
    :type pmd: pmd_t \*

.. _`pmd_clear_huge.description`:

Description
-----------

Returns 1 on success and 0 on failure (no PMD map is found).

.. _`pud_free_pmd_page`:

pud_free_pmd_page
=================

.. c:function:: int pud_free_pmd_page(pud_t *pud, unsigned long addr)

    Clear pud entry and free pmd page.

    :param pud:
        Pointer to a PUD.
    :type pud: pud_t \*

    :param addr:
        Virtual address associated with pud.
    :type addr: unsigned long

.. _`pud_free_pmd_page.context`:

Context
-------

The pud range has been unmapped and TLB purged.

.. _`pud_free_pmd_page.return`:

Return
------

1 if clearing the entry succeeded. 0 otherwise.

.. _`pud_free_pmd_page.note`:

NOTE
----

Callers must allow a single page allocation.

.. _`pmd_free_pte_page`:

pmd_free_pte_page
=================

.. c:function:: int pmd_free_pte_page(pmd_t *pmd, unsigned long addr)

    Clear pmd entry and free pte page.

    :param pmd:
        Pointer to a PMD.
    :type pmd: pmd_t \*

    :param addr:
        Virtual address associated with pmd.
    :type addr: unsigned long

.. _`pmd_free_pte_page.context`:

Context
-------

The pmd range has been unmapped and TLB purged.

.. _`pmd_free_pte_page.return`:

Return
------

1 if clearing the entry succeeded. 0 otherwise.

.. This file was automatic generated / don't edit.

