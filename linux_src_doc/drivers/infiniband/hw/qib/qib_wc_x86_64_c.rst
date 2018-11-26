.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_wc_x86_64.c

.. _`qib_enable_wc`:

qib_enable_wc
=============

.. c:function:: int qib_enable_wc(struct qib_devdata *dd)

    enable write combining for MMIO writes to the device

    :param dd:
        qlogic_ib device
    :type dd: struct qib_devdata \*

.. _`qib_enable_wc.description`:

Description
-----------

This routine is x86_64-specific; it twiddles the CPU's MTRRs to enable
write combining.

.. _`qib_disable_wc`:

qib_disable_wc
==============

.. c:function:: void qib_disable_wc(struct qib_devdata *dd)

    disable write combining for MMIO writes to the device

    :param dd:
        qlogic_ib device
    :type dd: struct qib_devdata \*

.. _`qib_unordered_wc`:

qib_unordered_wc
================

.. c:function:: int qib_unordered_wc( void)

    indicate whether write combining is ordered

    :param void:
        no arguments
    :type void: 

.. _`qib_unordered_wc.description`:

Description
-----------

Because our performance depends on our ability to do write combining mmio
writes in the most efficient way, we need to know if we are on an Intel
or AMD x86_64 processor.  AMD x86_64 processors flush WC buffers out in
the order completed, and so no special flushing is required to get
correct ordering.  Intel processors, however, will flush write buffers
out in "random" orders, and so explicit ordering is needed at times.

.. This file was automatic generated / don't edit.

