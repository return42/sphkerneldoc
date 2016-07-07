.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/host/mic_intr.c

.. _`mic_interrupt`:

mic_interrupt
=============

.. c:function:: irqreturn_t mic_interrupt(int irq, void *dev)

    Generic interrupt handler for MSI and INTx based interrupts.

    :param int irq:
        *undescribed*

    :param void \*dev:
        *undescribed*

.. _`mic_register_intr_callback`:

mic_register_intr_callback
==========================

.. c:function:: struct mic_intr_cb *mic_register_intr_callback(struct mic_device *mdev, u8 idx, irq_handler_t handler, irq_handler_t thread_fn, void *data)

    Register a callback handler for the given source id.

    :param struct mic_device \*mdev:
        pointer to the mic_device instance

    :param u8 idx:
        The source id to be registered.

    :param irq_handler_t handler:
        The function to be called when the source id receives
        the interrupt.

    :param irq_handler_t thread_fn:
        thread fn. corresponding to the handler

    :param void \*data:
        Private data of the requester.
        Return the callback structure that was registered or an
        appropriate error on failure.

.. _`mic_unregister_intr_callback`:

mic_unregister_intr_callback
============================

.. c:function:: u8 mic_unregister_intr_callback(struct mic_device *mdev, u32 idx)

    Unregister the callback handler identified by its callback id.

    :param struct mic_device \*mdev:
        pointer to the mic_device instance

    :param u32 idx:
        The callback structure id to be unregistered.
        Return the source id that was unregistered or MIC_NUM_OFFSETS if no
        such callback handler was found.

.. _`mic_setup_msix`:

mic_setup_msix
==============

.. c:function:: int mic_setup_msix(struct mic_device *mdev, struct pci_dev *pdev)

    Initializes MSIx interrupts.

    :param struct mic_device \*mdev:
        pointer to mic_device instance

    :param struct pci_dev \*pdev:
        *undescribed*

.. _`mic_setup_msix.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_setup_callbacks`:

mic_setup_callbacks
===================

.. c:function:: int mic_setup_callbacks(struct mic_device *mdev)

    Initialize data structures needed to handle callbacks.

    :param struct mic_device \*mdev:
        pointer to mic_device instance

.. _`mic_release_callbacks`:

mic_release_callbacks
=====================

.. c:function:: void mic_release_callbacks(struct mic_device *mdev)

    Uninitialize data structures needed to handle callbacks.

    :param struct mic_device \*mdev:
        pointer to mic_device instance

.. _`mic_setup_msi`:

mic_setup_msi
=============

.. c:function:: int mic_setup_msi(struct mic_device *mdev, struct pci_dev *pdev)

    Initializes MSI interrupts.

    :param struct mic_device \*mdev:
        pointer to mic_device instance

    :param struct pci_dev \*pdev:
        PCI device structure

.. _`mic_setup_msi.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_setup_intx`:

mic_setup_intx
==============

.. c:function:: int mic_setup_intx(struct mic_device *mdev, struct pci_dev *pdev)

    Initializes legacy interrupts.

    :param struct mic_device \*mdev:
        pointer to mic_device instance

    :param struct pci_dev \*pdev:
        PCI device structure

.. _`mic_setup_intx.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_next_db`:

mic_next_db
===========

.. c:function:: int mic_next_db(struct mic_device *mdev)

    Retrieve the next doorbell interrupt source id. The id is picked sequentially from the available pool of doorlbell ids.

    :param struct mic_device \*mdev:
        pointer to the mic_device instance.

.. _`mic_next_db.description`:

Description
-----------

Returns the next doorbell interrupt source.

.. _`mic_request_threaded_irq`:

mic_request_threaded_irq
========================

.. c:function:: struct mic_irq *mic_request_threaded_irq(struct mic_device *mdev, irq_handler_t handler, irq_handler_t thread_fn, const char *name, void *data, int intr_src, enum mic_intr_type type)

    request an irq. mic_mutex needs to be held before calling this function.

    :param struct mic_device \*mdev:
        pointer to mic_device instance

    :param irq_handler_t handler:
        The callback function that handles the interrupt.
        The function needs to call ack_interrupts
        (mdev->ops->ack_interrupt(mdev)) when handling the interrupts.

    :param irq_handler_t thread_fn:
        thread fn required by request_threaded_irq.

    :param const char \*name:
        The ASCII name of the callee requesting the irq.

    :param void \*data:
        private data that is returned back when calling the
        function handler.

    :param int intr_src:
        The source id of the requester. Its the doorbell id
        for Doorbell interrupts and DMA channel id for DMA interrupts.

    :param enum mic_intr_type type:
        The type of interrupt. Values defined in mic_intr_type

.. _`mic_request_threaded_irq.return`:

Return
------

The cookie that is transparent to the caller. Passed
back when calling mic_free_irq. An appropriate error code
is returned on failure. Caller needs to use IS_ERR(return_val)
to check for failure and PTR_ERR(return_val) to obtained the
error code.

.. _`mic_free_irq`:

mic_free_irq
============

.. c:function:: void mic_free_irq(struct mic_device *mdev, struct mic_irq *cookie, void *data)

    free irq. mic_mutex needs to be held before calling this function.

    :param struct mic_device \*mdev:
        pointer to mic_device instance

    :param struct mic_irq \*cookie:
        cookie obtained during a successful call to mic_request_threaded_irq

    :param void \*data:
        private data specified by the calling function during the
        mic_request_threaded_irq

.. _`mic_free_irq.return`:

Return
------

none.

.. _`mic_setup_interrupts`:

mic_setup_interrupts
====================

.. c:function:: int mic_setup_interrupts(struct mic_device *mdev, struct pci_dev *pdev)

    Initializes interrupts.

    :param struct mic_device \*mdev:
        pointer to mic_device instance

    :param struct pci_dev \*pdev:
        PCI device structure

.. _`mic_setup_interrupts.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_free_interrupts`:

mic_free_interrupts
===================

.. c:function:: void mic_free_interrupts(struct mic_device *mdev, struct pci_dev *pdev)

    Frees interrupts setup by mic_setup_interrupts

    :param struct mic_device \*mdev:
        pointer to mic_device instance

    :param struct pci_dev \*pdev:
        PCI device structure

.. _`mic_free_interrupts.description`:

Description
-----------

returns none.

.. _`mic_intr_restore`:

mic_intr_restore
================

.. c:function:: void mic_intr_restore(struct mic_device *mdev)

    Restore MIC interrupt registers.

    :param struct mic_device \*mdev:
        pointer to mic_device instance.

.. _`mic_intr_restore.description`:

Description
-----------

Restore the interrupt registers to values previously
stored in the SW data structures. mic_mutex needs to
be held before calling this function.

returns None.

.. This file was automatic generated / don't edit.

