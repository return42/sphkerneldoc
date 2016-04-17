.. -*- coding: utf-8; mode: rst -*-

========
devres.c
========


.. _`devm_request_threaded_irq`:

devm_request_threaded_irq
=========================

.. c:function:: int devm_request_threaded_irq (struct device *dev, unsigned int irq, irq_handler_t handler, irq_handler_t thread_fn, unsigned long irqflags, const char *devname, void *dev_id)

    allocate an interrupt line for a managed device

    :param struct device \*dev:
        device to request interrupt for

    :param unsigned int irq:
        Interrupt line to allocate

    :param irq_handler_t handler:
        Function to be called when the IRQ occurs

    :param irq_handler_t thread_fn:
        function to be called in a threaded interrupt context. NULL
        for devices which handle everything in ``handler``

    :param unsigned long irqflags:
        Interrupt type flags

    :param const char \*devname:
        An ascii name for the claiming device

    :param void \*dev_id:
        A cookie passed back to the handler function



.. _`devm_request_threaded_irq.description`:

Description
-----------

Except for the extra ``dev`` argument, this function takes the
same arguments and performs the same function as
:c:func:`request_threaded_irq`.  IRQs requested with this function will be
automatically freed on driver detach.

If an IRQ allocated with this function needs to be freed
separately, :c:func:`devm_free_irq` must be used.



.. _`devm_request_any_context_irq`:

devm_request_any_context_irq
============================

.. c:function:: int devm_request_any_context_irq (struct device *dev, unsigned int irq, irq_handler_t handler, unsigned long irqflags, const char *devname, void *dev_id)

    allocate an interrupt line for a managed device

    :param struct device \*dev:
        device to request interrupt for

    :param unsigned int irq:
        Interrupt line to allocate

    :param irq_handler_t handler:
        Function to be called when the IRQ occurs

    :param unsigned long irqflags:
        Interrupt type flags

    :param const char \*devname:
        An ascii name for the claiming device

    :param void \*dev_id:
        A cookie passed back to the handler function



.. _`devm_request_any_context_irq.description`:

Description
-----------

Except for the extra ``dev`` argument, this function takes the
same arguments and performs the same function as
:c:func:`request_any_context_irq`.  IRQs requested with this function will be
automatically freed on driver detach.

If an IRQ allocated with this function needs to be freed
separately, :c:func:`devm_free_irq` must be used.



.. _`devm_free_irq`:

devm_free_irq
=============

.. c:function:: void devm_free_irq (struct device *dev, unsigned int irq, void *dev_id)

    free an interrupt

    :param struct device \*dev:
        device to free interrupt for

    :param unsigned int irq:
        Interrupt line to free

    :param void \*dev_id:
        Device identity to free



.. _`devm_free_irq.description`:

Description
-----------

Except for the extra ``dev`` argument, this function takes the
same arguments and performs the same function as :c:func:`free_irq`.
This function instead of :c:func:`free_irq` should be used to manually
free IRQs allocated with :c:func:`devm_request_irq`.

