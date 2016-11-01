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

.. This file was automatic generated / don't edit.

