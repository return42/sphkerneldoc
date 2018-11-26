.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/cpu/mtrr/centaur.c

.. _`centaur_get_free_region`:

centaur_get_free_region
=======================

.. c:function:: int centaur_get_free_region(unsigned long base, unsigned long size, int replace_reg)

    Get a free MTRR.

    :param base:
        The starting (base) address of the region.
    :type base: unsigned long

    :param size:
        The size (in bytes) of the region.
    :type size: unsigned long

    :param replace_reg:
        *undescribed*
    :type replace_reg: int

.. _`centaur_get_free_region.return`:

Return
------

the index of the region on success, else -1 on error.

.. This file was automatic generated / don't edit.

