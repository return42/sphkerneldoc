.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/mm/pgtable.c

.. _`ptep_force_prot`:

ptep_force_prot
===============

.. c:function:: int ptep_force_prot(struct mm_struct *mm, unsigned long addr, pte_t *ptep, int prot, unsigned long bit)

    change access rights of a locked pte

    :param struct mm_struct \*mm:
        pointer to the process mm_struct

    :param unsigned long addr:
        virtual address in the guest address space

    :param pte_t \*ptep:
        pointer to the page table entry

    :param int prot:
        indicates guest access rights: PROT_NONE, PROT_READ or PROT_WRITE

    :param unsigned long bit:
        pgste bit to set (e.g. for notification)

.. _`ptep_force_prot.description`:

Description
-----------

Returns 0 if the access rights were changed and -EAGAIN if the current
and requested access rights are incompatible.

.. _`cond_set_guest_storage_key`:

cond_set_guest_storage_key
==========================

.. c:function:: int cond_set_guest_storage_key(struct mm_struct *mm, unsigned long addr, unsigned char key, unsigned char *oldkey, bool nq, bool mr, bool mc)

    oldkey will be updated when either mr or mc is set and a pointer is given.

    :param struct mm_struct \*mm:
        *undescribed*

    :param unsigned long addr:
        *undescribed*

    :param unsigned char key:
        *undescribed*

    :param unsigned char \*oldkey:
        *undescribed*

    :param bool nq:
        *undescribed*

    :param bool mr:
        *undescribed*

    :param bool mc:
        *undescribed*

.. _`cond_set_guest_storage_key.description`:

Description
-----------

Returns 0 if a guests storage key update wasn't necessary, 1 if the guest
storage key was updated and -EFAULT on access errors.

.. _`reset_guest_reference_bit`:

reset_guest_reference_bit
=========================

.. c:function:: int reset_guest_reference_bit(struct mm_struct *mm, unsigned long addr)

    :param struct mm_struct \*mm:
        *undescribed*

    :param unsigned long addr:
        *undescribed*

.. _`reset_guest_reference_bit.description`:

Description
-----------

Returns < 0 in case of error, otherwise the cc to be reported to the guest.

.. _`pgste_perform_essa`:

pgste_perform_essa
==================

.. c:function:: int pgste_perform_essa(struct mm_struct *mm, unsigned long hva, int orc, unsigned long *oldpte, unsigned long *oldpgste)

    perform ESSA actions on the PGSTE.

    :param struct mm_struct \*mm:
        the memory context. It must have PGSTEs, no check is performed here!

    :param unsigned long hva:
        the host virtual address of the page whose PGSTE is to be processed

    :param int orc:
        the specific action to perform, see the ESSA_SET\_\* macros.

    :param unsigned long \*oldpte:
        the PTE will be saved there if the pointer is not NULL.

    :param unsigned long \*oldpgste:
        the old PGSTE will be saved there if the pointer is not NULL.

.. _`pgste_perform_essa.return`:

Return
------

1 if the page is to be added to the CBRL, otherwise 0,
or < 0 in case of error. -EINVAL is returned for invalid values
of orc, -EFAULT for invalid addresses.

.. _`set_pgste_bits`:

set_pgste_bits
==============

.. c:function:: int set_pgste_bits(struct mm_struct *mm, unsigned long hva, unsigned long bits, unsigned long value)

    set specific PGSTE bits.

    :param struct mm_struct \*mm:
        the memory context. It must have PGSTEs, no check is performed here!

    :param unsigned long hva:
        the host virtual address of the page whose PGSTE is to be processed

    :param unsigned long bits:
        a bitmask representing the bits that will be touched

    :param unsigned long value:
        the values of the bits to be written. Only the bits in the mask
        will be written.

.. _`set_pgste_bits.return`:

Return
------

0 on success, < 0 in case of error.

.. _`get_pgste`:

get_pgste
=========

.. c:function:: int get_pgste(struct mm_struct *mm, unsigned long hva, unsigned long *pgstep)

    get the current PGSTE for the given address.

    :param struct mm_struct \*mm:
        the memory context. It must have PGSTEs, no check is performed here!

    :param unsigned long hva:
        the host virtual address of the page whose PGSTE is to be processed

    :param unsigned long \*pgstep:
        will be written with the current PGSTE for the given address.

.. _`get_pgste.return`:

Return
------

0 on success, < 0 in case of error.

.. This file was automatic generated / don't edit.

