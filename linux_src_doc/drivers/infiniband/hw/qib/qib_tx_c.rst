.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_tx.c

.. _`qib_disarm_piobufs`:

qib_disarm_piobufs
==================

.. c:function:: void qib_disarm_piobufs(struct qib_devdata *dd, unsigned first, unsigned cnt)

    cancel a range of PIO buffers

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

    :param first:
        the first PIO buffer to cancel
    :type first: unsigned

    :param cnt:
        the number of PIO buffers to cancel
    :type cnt: unsigned

.. _`qib_disarm_piobufs.description`:

Description
-----------

Cancel a range of PIO buffers. Used at user process close,
in case it died while writing to a PIO buffer.

.. _`update_send_bufs`:

update_send_bufs
================

.. c:function:: void update_send_bufs(struct qib_devdata *dd)

    update shadow copy of the PIO availability map

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

.. _`update_send_bufs.description`:

Description
-----------

called whenever our local copy indicates we have run out of send buffers

.. _`qib_chg_pioavailkernel`:

qib_chg_pioavailkernel
======================

.. c:function:: void qib_chg_pioavailkernel(struct qib_devdata *dd, unsigned start, unsigned len, u32 avail, struct qib_ctxtdata *rcd)

    change which send buffers are available for kernel

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

    :param start:
        the starting send buffer number
    :type start: unsigned

    :param len:
        the number of send buffers
    :type len: unsigned

    :param avail:
        true if the buffers are available for kernel use, false otherwise
    :type avail: u32

    :param rcd:
        *undescribed*
    :type rcd: struct qib_ctxtdata \*

.. This file was automatic generated / don't edit.

