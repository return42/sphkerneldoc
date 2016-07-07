.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/mbcs.c

.. _`mbcs_completion_intr_handler`:

mbcs_completion_intr_handler
============================

.. c:function:: irqreturn_t mbcs_completion_intr_handler(int irq, void *arg)

    Primary completion handler.

    :param int irq:
        irq

    :param void \*arg:
        soft struct for device

.. _`mbcs_intr_alloc`:

mbcs_intr_alloc
===============

.. c:function:: int mbcs_intr_alloc(struct cx_dev *dev)

    Allocate interrupts.

    :param struct cx_dev \*dev:
        device pointer

.. _`mbcs_intr_dealloc`:

mbcs_intr_dealloc
=================

.. c:function:: void mbcs_intr_dealloc(struct cx_dev *dev)

    Remove interrupts.

    :param struct cx_dev \*dev:
        device pointer

.. _`mbcs_probe`:

mbcs_probe
==========

.. c:function:: int mbcs_probe(struct cx_dev *dev, const struct cx_device_id *id)

    Initialize for device

    :param struct cx_dev \*dev:
        device pointer

    :param const struct cx_device_id \*id:
        *undescribed*

.. This file was automatic generated / don't edit.

