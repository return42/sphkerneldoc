.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/pseries/lpar.c

.. _`call_block_remove`:

call_block_remove
=================

.. c:function:: unsigned long call_block_remove(unsigned long idx, unsigned long *param, bool retry_busy)

    \ ``idx``\  should point to the latest \ ``param``\  entry set with a PTEX. If PTE cannot be processed because another CPUs has already locked that group, those entries are put back in \ ``param``\  starting at index 1. If entries has to be retried and \ ``retry_busy``\  is set to true, these entries are retried until success. If \ ``retry_busy``\  is set to false, the returned is the number of entries yet to process.

    :param idx:
        *undescribed*
    :type idx: unsigned long

    :param param:
        *undescribed*
    :type param: unsigned long \*

    :param retry_busy:
        *undescribed*
    :type retry_busy: bool

.. _`do_block_remove`:

do_block_remove
===============

.. c:function:: void do_block_remove(unsigned long number, struct ppc64_tlb_batch *batch, unsigned long *param)

    "all within the same naturally aligned 8 page virtual address block".

    :param number:
        *undescribed*
    :type number: unsigned long

    :param batch:
        *undescribed*
    :type batch: struct ppc64_tlb_batch \*

    :param param:
        *undescribed*
    :type param: unsigned long \*

.. _`h_get_mpp`:

h_get_mpp
=========

.. c:function:: int h_get_mpp(struct hvcall_mpp_data *mpp_data)

    H_GET_MPP hcall returns info in 7 parms

    :param mpp_data:
        *undescribed*
    :type mpp_data: struct hvcall_mpp_data \*

.. This file was automatic generated / don't edit.

