.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/broadcom/bnx2.c

.. _`bnx2_io_error_detected`:

bnx2_io_error_detected
======================

.. c:function:: pci_ers_result_t bnx2_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param struct pci_dev \*pdev:
        Pointer to PCI device

    :param pci_channel_state_t state:
        The current pci connection state

.. _`bnx2_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`bnx2_io_slot_reset`:

bnx2_io_slot_reset
==================

.. c:function:: pci_ers_result_t bnx2_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`bnx2_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot.

.. _`bnx2_io_resume`:

bnx2_io_resume
==============

.. c:function:: void bnx2_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`bnx2_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells us that
its OK to resume normal operation.

.. This file was automatic generated / don't edit.

