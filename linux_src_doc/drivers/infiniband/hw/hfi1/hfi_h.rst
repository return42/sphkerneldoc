.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/hfi.h

.. _`rcvhdrq_size`:

rcvhdrq_size
============

.. c:function:: u32 rcvhdrq_size(struct hfi1_ctxtdata *rcd)

    return total size in bytes for header queue

    :param rcd:
        the receive context
    :type rcd: struct hfi1_ctxtdata \*

.. _`rcvhdrq_size.description`:

Description
-----------

rcvhdrqentsize is in DWs, so we have to convert to bytes

.. _`sc_to_vlt`:

sc_to_vlt
=========

.. c:function:: u8 sc_to_vlt(struct hfi1_devdata *dd, u8 sc5)

    \ ``dd``\  - devdata \ ``sc5``\  - 5 bit sc

    :param dd:
        *undescribed*
    :type dd: struct hfi1_devdata \*

    :param sc5:
        *undescribed*
    :type sc5: u8

.. This file was automatic generated / don't edit.

