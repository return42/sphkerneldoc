.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/broadcom/bnxt/bnxt.c

.. _`bnxt_io_error_detected`:

bnxt_io_error_detected
======================

.. c:function:: pci_ers_result_t bnxt_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

    :param state:
        The current pci connection state
    :type state: pci_channel_state_t

.. _`bnxt_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`bnxt_io_slot_reset`:

bnxt_io_slot_reset
==================

.. c:function:: pci_ers_result_t bnxt_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset.

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`bnxt_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot.
At this point, the card has exprienced a hard reset,
followed by fixups by BIOS, and has its config space
set up identically to what it was at cold boot.

.. _`bnxt_io_resume`:

bnxt_io_resume
==============

.. c:function:: void bnxt_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`bnxt_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells
us that its OK to resume normal operation.

.. This file was automatic generated / don't edit.

