.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_pcie.c

.. _`qib_cache_msi_info`:

qib_cache_msi_info
==================

.. c:function:: void qib_cache_msi_info(struct qib_devdata *dd, int pos)

    chip reset (the kernel PCI infrastructure doesn't yet handle that correctly.

    :param struct qib_devdata \*dd:
        *undescribed*

    :param int pos:
        *undescribed*

.. _`qib_free_irq`:

qib_free_irq
============

.. c:function:: void qib_free_irq(struct qib_devdata *dd)

    Cleanup INTx and MSI interrupts

    :param struct qib_devdata \*dd:
        valid pointer to qib dev data

.. _`qib_free_irq.description`:

Description
-----------

Since cleanup for INTx and MSI interrupts is trivial, have a common
routine.

.. This file was automatic generated / don't edit.

