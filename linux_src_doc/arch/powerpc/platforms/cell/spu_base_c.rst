.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/cell/spu_base.c

.. _`__slb_present`:

\__slb_present
==============

.. c:function:: int __slb_present(struct copro_slb *slbs, int nr_slbs, void *new_addr)

    zero if the address \ ``new_addr``\  is present.

    :param slbs:
        *undescribed*
    :type slbs: struct copro_slb \*

    :param nr_slbs:
        *undescribed*
    :type nr_slbs: int

    :param new_addr:
        *undescribed*
    :type new_addr: void \*

.. _`spu_setup_kernel_slbs`:

spu_setup_kernel_slbs
=====================

.. c:function:: void spu_setup_kernel_slbs(struct spu *spu, struct spu_lscsa *lscsa, void *code, int code_size)

    need to map both the context save area, and the save/restore code.

    :param spu:
        *undescribed*
    :type spu: struct spu \*

    :param lscsa:
        *undescribed*
    :type lscsa: struct spu_lscsa \*

    :param code:
        *undescribed*
    :type code: void \*

    :param code_size:
        *undescribed*
    :type code_size: int

.. _`spu_setup_kernel_slbs.description`:

Description
-----------

Because the lscsa and code may cross segment boundaries, we check to see
if mappings are required for the start and end of each range. We currently
assume that the mappings are smaller that one segment - if not, something
is seriously wrong.

.. This file was automatic generated / don't edit.

