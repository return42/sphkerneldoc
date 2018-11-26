.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/host/mic_intr.c

.. _`mic_interrupt`:

mic_interrupt
=============

.. c:function:: irqreturn_t mic_interrupt(int irq, void *dev)

    Generic interrupt handler for MSI and INTx based interrupts.

    :param irq:
        *undescribed*
    :type irq: int

    :param dev:
        *undescribed*
    :type dev: void \*

.. _`mic_register_intr_callback`:

mic_register_intr_callback
==========================

.. c:function:: struct mic_intr_cb *mic_register_intr_callback(struct mic_device *mdev, u8 idx, irq_handler_t handler, irq_handler_t thread_fn, void *data)

    Register a callback handler for the given source id.

    :param mdev:
        pointer to the mic_device instance
    :type mdev: struct mic_device \*

    :param idx:
        The source id to be registered.
    :type idx: u8

    :param handler:
        The function to be called when the source id receives
        the interrupt.
    :type handler: irq_handler_t

    :param thread_fn:
        thread fn. corresponding to the handler
    :type thread_fn: irq_handler_t

    :param data:
        Private data of the requester.
        Return the callback structure that was registered or an
        appropriate error on failure.
    :type data: void \*

.. _`mic_unregister_intr_callback`:

mic_unregister_intr_callback
============================

.. c:function:: u8 mic_unregister_intr_callback(struct mic_device *mdev, u32 idx)

    Unregister the callback handler identified by its callback id.

    :param mdev:
        pointer to the mic_device instance
    :type mdev: struct mic_device \*

    :param idx:
        The callback structure id to be unregistered.
        Return the source id that was unregistered or MIC_NUM_OFFSETS if no
        such callback handler was found.
    :type idx: u32

.. _`mic_setup_msix`:

mic_setup_msix
==============

.. c:function:: int mic_setup_msix(struct mic_device *mdev, struct pci_dev *pdev)

    Initializes MSIx interrupts.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

.. _`mic_setup_msix.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_setup_callbacks`:

mic_setup_callbacks
===================

.. c:function:: int mic_setup_callbacks(struct mic_device *mdev)

    Initialize data structures needed to handle callbacks.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_release_callbacks`:

mic_release_callbacks
=====================

.. c:function:: void mic_release_callbacks(struct mic_device *mdev)

    Uninitialize data structures needed to handle callbacks.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_setup_msi`:

mic_setup_msi
=============

.. c:function:: int mic_setup_msi(struct mic_device *mdev, struct pci_dev *pdev)

    Initializes MSI interrupts.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`mic_setup_msi.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_setup_intx`:

mic_setup_intx
==============

.. c:function:: int mic_setup_intx(struct mic_device *mdev, struct pci_dev *pdev)

    Initializes legacy interrupts.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`mic_setup_intx.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_next_db`:

mic_next_db
===========

.. c:function:: int mic_next_db(struct mic_device *mdev)

    Retrieve the next doorbell interrupt source id. The id is picked sequentially from the available pool of doorlbell ids.

    :param mdev:
        pointer to the mic_device instance.
    :type mdev: struct mic_device \*

.. _`mic_next_db.description`:

Description
-----------

Returns the next doorbell interrupt source.

.. _`mic_request_threaded_irq`:

mic_request_threaded_irq
========================

.. c:function:: struct mic_irq *mic_request_threaded_irq(struct mic_device *mdev, irq_handler_t handler, irq_handler_t thread_fn, const char *name, void *data, int intr_src, enum mic_intr_type type)

    request an irq. mic_mutex needs to be held before calling this function.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param handler:
        The callback function that handles the interrupt.
        The function needs to call ack_interrupts
        (mdev->ops->ack_interrupt(mdev)) when handling the interrupts.
    :type handler: irq_handler_t

    :param thread_fn:
        thread fn required by request_threaded_irq.
    :type thread_fn: irq_handler_t

    :param name:
        The ASCII name of the callee requesting the irq.
    :type name: const char \*

    :param data:
        private data that is returned back when calling the
        function handler.
    :type data: void \*

    :param intr_src:
        The source id of the requester. Its the doorbell id
        for Doorbell interrupts and DMA channel id for DMA interrupts.
    :type intr_src: int

    :param type:
        The type of interrupt. Values defined in mic_intr_type
    :type type: enum mic_intr_type

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

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param cookie:
        cookie obtained during a successful call to mic_request_threaded_irq
    :type cookie: struct mic_irq \*

    :param data:
        private data specified by the calling function during the
        mic_request_threaded_irq
    :type data: void \*

.. _`mic_free_irq.return`:

Return
------

none.

.. _`mic_setup_interrupts`:

mic_setup_interrupts
====================

.. c:function:: int mic_setup_interrupts(struct mic_device *mdev, struct pci_dev *pdev)

    Initializes interrupts.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`mic_setup_interrupts.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_free_interrupts`:

mic_free_interrupts
===================

.. c:function:: void mic_free_interrupts(struct mic_device *mdev, struct pci_dev *pdev)

    Frees interrupts setup by mic_setup_interrupts

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`mic_free_interrupts.description`:

Description
-----------

returns none.

.. _`mic_intr_restore`:

mic_intr_restore
================

.. c:function:: void mic_intr_restore(struct mic_device *mdev)

    Restore MIC interrupt registers.

    :param mdev:
        pointer to mic_device instance.
    :type mdev: struct mic_device \*

.. _`mic_intr_restore.description`:

Description
-----------

Restore the interrupt registers to values previously
stored in the SW data structures. mic_mutex needs to
be held before calling this function.

returns None.

.. This file was automatic generated / don't edit.

