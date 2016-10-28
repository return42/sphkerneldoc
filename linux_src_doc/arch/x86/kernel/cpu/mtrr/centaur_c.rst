.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/cpu/mtrr/centaur.c

.. _`centaur_get_free_region`:

centaur_get_free_region
=======================

.. c:function:: int centaur_get_free_region(unsigned long base, unsigned long size, int replace_reg)

    Get a free MTRR.

    :param unsigned long base:
        The starting (base) address of the region.

    :param unsigned long size:
        The size (in bytes) of the region.

    :param int replace_reg:
        *undescribed*

.. _`centaur_get_free_region.return`:

Return
------

the index of the region on success, else -1 on error.

.. This file was automatic generated / don't edit.

