.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/cpu/mtrr/amd.c

.. _`amd_set_mtrr`:

amd_set_mtrr
============

.. c:function:: void amd_set_mtrr(unsigned int reg, unsigned long base, unsigned long size, mtrr_type type)

    Set variable MTRR register on the local CPU.

    :param unsigned int reg:
        *undescribed*

    :param unsigned long base:
        *undescribed*

    :param unsigned long size:
        *undescribed*

    :param mtrr_type type:
        *undescribed*

.. _`amd_set_mtrr.description`:

Description
-----------

\ ``reg``\  The register to set.
\ ``base``\  The base address of the region.
\ ``size``\  The size of the region. If this is 0 the region is disabled.
\ ``type``\  The type of the region.

Returns nothing.

.. This file was automatic generated / don't edit.

