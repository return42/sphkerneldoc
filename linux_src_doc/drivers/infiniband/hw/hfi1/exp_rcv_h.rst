.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/exp_rcv.h

.. _`hfi1_tid_group_to_idx`:

hfi1_tid_group_to_idx
=====================

.. c:function:: u16 hfi1_tid_group_to_idx(struct hfi1_ctxtdata *rcd, struct tid_group *grp)

    convert an index to a group \ ``rcd``\  - the receive context \ ``grp``\  - the group pointer

    :param struct hfi1_ctxtdata \*rcd:
        *undescribed*

    :param struct tid_group \*grp:
        *undescribed*

.. _`hfi1_idx_to_tid_group`:

hfi1_idx_to_tid_group
=====================

.. c:function:: struct tid_group *hfi1_idx_to_tid_group(struct hfi1_ctxtdata *rcd, u16 idx)

    convert a group to an index \ ``rcd``\  - the receive context \ ``idx``\  - the index

    :param struct hfi1_ctxtdata \*rcd:
        *undescribed*

    :param u16 idx:
        *undescribed*

.. This file was automatic generated / don't edit.

