.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_wc_ppc64.c

.. _`qib_enable_wc`:

qib_enable_wc
=============

.. c:function:: int qib_enable_wc(struct qib_devdata *dd)

    enable write combining for MMIO writes to the device

    :param struct qib_devdata \*dd:
        qlogic_ib device

.. _`qib_enable_wc.description`:

Description
-----------

Nothing to do on PowerPC, so just return without error.

.. _`qib_unordered_wc`:

qib_unordered_wc
================

.. c:function:: int qib_unordered_wc( void)

    indicate whether write combining is unordered

    :param  void:
        no arguments

.. _`qib_unordered_wc.description`:

Description
-----------

Because our performance depends on our ability to do write
combining mmio writes in the most efficient way, we need to
know if we are on a processor that may reorder stores when
write combining.

.. This file was automatic generated / don't edit.

