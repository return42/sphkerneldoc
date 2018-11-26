.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/exp_rcv.c

.. _`hfi1_exp_tid_set_init`:

hfi1_exp_tid_set_init
=====================

.. c:function:: void hfi1_exp_tid_set_init(struct exp_tid_set *set)

    initialize exp_tid_set \ ``set``\  - the set

    :param set:
        *undescribed*
    :type set: struct exp_tid_set \*

.. _`hfi1_exp_tid_group_init`:

hfi1_exp_tid_group_init
=======================

.. c:function:: void hfi1_exp_tid_group_init(struct hfi1_ctxtdata *rcd)

    initialize rcd expected receive \ ``rcd``\  - the rcd

    :param rcd:
        *undescribed*
    :type rcd: struct hfi1_ctxtdata \*

.. _`hfi1_alloc_ctxt_rcv_groups`:

hfi1_alloc_ctxt_rcv_groups
==========================

.. c:function:: int hfi1_alloc_ctxt_rcv_groups(struct hfi1_ctxtdata *rcd)

    initialize expected receive groups \ ``rcd``\  - the context to add the groupings to

    :param rcd:
        *undescribed*
    :type rcd: struct hfi1_ctxtdata \*

.. _`hfi1_free_ctxt_rcv_groups`:

hfi1_free_ctxt_rcv_groups
=========================

.. c:function:: void hfi1_free_ctxt_rcv_groups(struct hfi1_ctxtdata *rcd)

    free  expected receive groups \ ``rcd``\  - the context to free

    :param rcd:
        *undescribed*
    :type rcd: struct hfi1_ctxtdata \*

.. _`hfi1_free_ctxt_rcv_groups.description`:

Description
-----------

The routine dismantles the expect receive linked
list and clears any tids associated with the receive
context.

This should only be called for kernel contexts and the
a base user context.

.. This file was automatic generated / don't edit.

