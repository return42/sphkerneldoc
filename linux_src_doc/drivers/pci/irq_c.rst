.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/irq.c

.. _`pci_lost_interrupt`:

pci_lost_interrupt
==================

.. c:function:: enum pci_lost_interrupt_reason pci_lost_interrupt(struct pci_dev *pdev)

    reports a lost PCI interrupt

    :param pdev:
        device whose interrupt is lost
    :type pdev: struct pci_dev \*

.. _`pci_lost_interrupt.description`:

Description
-----------

The primary function of this routine is to report a lost interrupt
in a standard way which users can recognise (instead of blaming the
driver).

.. _`pci_lost_interrupt.return`:

Return
------

a suggestion for fixing it (although the driver is not required to
act on this).

.. _`pci_request_irq`:

pci_request_irq
===============

.. c:function:: int pci_request_irq(struct pci_dev *dev, unsigned int nr, irq_handler_t handler, irq_handler_t thread_fn, void *dev_id, const char *fmt,  ...)

    allocate an interrupt line for a PCI device

    :param dev:
        PCI device to operate on
    :type dev: struct pci_dev \*

    :param nr:
        device-relative interrupt vector index (0-based).
    :type nr: unsigned int

    :param handler:
        Function to be called when the IRQ occurs.
        Primary handler for threaded interrupts.
        If NULL and thread_fn != NULL the default primary handler is
        installed.
    :type handler: irq_handler_t

    :param thread_fn:
        Function called from the IRQ handler thread
        If NULL, no IRQ thread is created
    :type thread_fn: irq_handler_t

    :param dev_id:
        Cookie passed back to the handler function
    :type dev_id: void \*

    :param fmt:
        Printf-like format string naming the handler
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`pci_request_irq.description`:

Description
-----------

This call allocates interrupt resources and enables the interrupt line and
IRQ handling. From the point this call is made \ ``handler``\  and \ ``thread_fn``\  may
be invoked.  All interrupts requested using this function might be shared.

\ ``dev_id``\  must not be NULL and must be globally unique.

.. _`pci_free_irq`:

pci_free_irq
============

.. c:function:: void pci_free_irq(struct pci_dev *dev, unsigned int nr, void *dev_id)

    free an interrupt allocated with pci_request_irq

    :param dev:
        PCI device to operate on
    :type dev: struct pci_dev \*

    :param nr:
        device-relative interrupt vector index (0-based).
    :type nr: unsigned int

    :param dev_id:
        Device identity to free
    :type dev_id: void \*

.. _`pci_free_irq.description`:

Description
-----------

Remove an interrupt handler. The handler is removed and if the interrupt
line is no longer in use by any driver it is disabled.  The caller must
ensure the interrupt is disabled on the device before calling this function.
The function does not return until any executing interrupts for this IRQ
have completed.

This function must not be called from interrupt context.

.. This file was automatic generated / don't edit.

