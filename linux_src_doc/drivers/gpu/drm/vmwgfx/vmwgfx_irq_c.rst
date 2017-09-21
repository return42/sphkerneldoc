.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_irq.c

.. _`vmw_thread_fn`:

vmw_thread_fn
=============

.. c:function:: irqreturn_t vmw_thread_fn(int irq, void *arg)

    Deferred (process context) irq handler

    :param int irq:
        irq number

    :param void \*arg:
        Closure argument. Pointer to a struct drm_device cast to void \*

.. _`vmw_thread_fn.description`:

Description
-----------

This function implements the deferred part of irq processing.
The function is guaranteed to run at least once after the
vmw_irq_handler has returned with IRQ_WAKE_THREAD.

.. _`vmw_irq_handler`:

vmw_irq_handler
===============

.. c:function:: irqreturn_t vmw_irq_handler(int irq, void *arg)

    :param int irq:
        irq number

    :param void \*arg:
        Closure argument. Pointer to a struct drm_device cast to void \*

.. _`vmw_irq_handler.description`:

Description
-----------

This function implements the quick part of irq processing.
The function performs fast actions like clearing the device interrupt
flags and also reasonably quick actions like waking processes waiting for
FIFO space. Other IRQ actions are deferred to the IRQ thread.

.. _`vmw_irq_install`:

vmw_irq_install
===============

.. c:function:: int vmw_irq_install(struct drm_device *dev, int irq)

    Install the irq handlers

    :param struct drm_device \*dev:
        Pointer to the drm device.

    :param int irq:
        The irq number.

.. _`vmw_irq_install.return`:

Return
------

Zero if successful. Negative number otherwise.

.. This file was automatic generated / don't edit.

