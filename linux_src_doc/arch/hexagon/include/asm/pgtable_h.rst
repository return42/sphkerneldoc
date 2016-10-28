.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/hexagon/include/asm/pgtable.h

.. _`pmd_index`:

pmd_index
=========

.. c:function::  pmd_index( address)

    returns the index of the entry in the PMD page which would control the given virtual address

    :param  address:
        *undescribed*

.. _`pgd_index`:

pgd_index
=========

.. c:function::  pgd_index( address)

    returns the index of the entry in the PGD page which would control the given virtual address

    :param  address:
        *undescribed*

.. _`pgd_index.description`:

Description
-----------

This returns the \*index\* for the address in the pgd_t

.. _`pmd_none`:

pmd_none
========

.. c:function:: int pmd_none(pmd_t pmd)

    check if pmd_entry is mapped

    :param pmd_t pmd:
        *undescribed*

.. _`pmd_none.description`:

Description
-----------

MIPS checks it against that "invalid pte table" thing.

.. _`pmd_present`:

pmd_present
===========

.. c:function:: int pmd_present(pmd_t pmd)

    is there a page table behind this? Essentially the inverse of pmd_none.  We maybe save an inline instruction by defining it this way, instead of simply "!pmd_none".

    :param pmd_t pmd:
        *undescribed*

.. _`pmd_bad`:

pmd_bad
=======

.. c:function:: int pmd_bad(pmd_t pmd)

    check if a PMD entry is "bad". That might mean swapped out. As we have no known cause of badness, it's null, as it is for many architectures.

    :param pmd_t pmd:
        *undescribed*

.. _`pte_none`:

pte_none
========

.. c:function:: int pte_none(pte_t pte)

    check if pte is mapped

    :param pte_t pte:
        pte_t entry

.. This file was automatic generated / don't edit.

