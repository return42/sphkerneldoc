.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_core_irq.c

.. _`dpu_core_irq_callback_handler`:

dpu_core_irq_callback_handler
=============================

.. c:function:: void dpu_core_irq_callback_handler(void *arg, int irq_idx)

    dispatch core interrupts

    :param arg:
        private data of callback handler
    :type arg: void \*

    :param irq_idx:
        interrupt index
    :type irq_idx: int

.. _`_dpu_core_irq_enable`:

\_dpu_core_irq_enable
=====================

.. c:function:: int _dpu_core_irq_enable(struct dpu_kms *dpu_kms, int irq_idx)

    enable core interrupt given by the index

    :param dpu_kms:
        Pointer to dpu kms context
    :type dpu_kms: struct dpu_kms \*

    :param irq_idx:
        interrupt index
    :type irq_idx: int

.. _`_dpu_core_irq_disable`:

\_dpu_core_irq_disable
======================

.. c:function:: int _dpu_core_irq_disable(struct dpu_kms *dpu_kms, int irq_idx)

    disable core interrupt given by the index

    :param dpu_kms:
        Pointer to dpu kms context
    :type dpu_kms: struct dpu_kms \*

    :param irq_idx:
        interrupt index
    :type irq_idx: int

.. This file was automatic generated / don't edit.

