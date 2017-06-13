.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/mm/pgtable.c

.. _`reserve_top_address`:

reserve_top_address
===================

.. c:function:: void reserve_top_address(unsigned long reserve)

    reserves a hole in the top of kernel address space \ ``reserve``\  - size of hole to reserve

    :param unsigned long reserve:
        *undescribed*

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

    :param p4d_t \*p4d:
        *undescribed*

    :param phys_addr_t addr:
        *undescribed*

    :param pgprot_t prot:
        *undescribed*

.. _`p4d_set_huge.description`:

Description
-----------

No 512GB pages yet -- always return 0

.. _`p4d_clear_huge`:

p4d_clear_huge
==============

.. c:function:: int p4d_clear_huge(p4d_t *p4d)

    clear kernel P4D mapping when it is set

    :param p4d_t \*p4d:
        *undescribed*

.. _`p4d_clear_huge.description`:

Description
-----------

No 512GB pages yet -- always return 0

.. _`pud_set_huge`:

pud_set_huge
============

.. c:function:: int pud_set_huge(pud_t *pud, phys_addr_t addr, pgprot_t prot)

    setup kernel PUD mapping

    :param pud_t \*pud:
        *undescribed*

    :param phys_addr_t addr:
        *undescribed*

    :param pgprot_t prot:
        *undescribed*

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

    :param pmd_t \*pmd:
        *undescribed*

    :param phys_addr_t addr:
        *undescribed*

    :param pgprot_t prot:
        *undescribed*

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

    :param pud_t \*pud:
        *undescribed*

.. _`pud_clear_huge.description`:

Description
-----------

Returns 1 on success and 0 on failure (no PUD map is found).

.. _`pmd_clear_huge`:

pmd_clear_huge
==============

.. c:function:: int pmd_clear_huge(pmd_t *pmd)

    clear kernel PMD mapping when it is set

    :param pmd_t \*pmd:
        *undescribed*

.. _`pmd_clear_huge.description`:

Description
-----------

Returns 1 on success and 0 on failure (no PMD map is found).

.. This file was automatic generated / don't edit.

