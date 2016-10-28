.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/sym53c8xx_2/sym_glue.c

.. _`sym2_io_error_detected`:

sym2_io_error_detected
======================

.. c:function:: pci_ers_result_t sym2_io_error_detected(struct pci_dev *pdev, enum pci_channel_state state)

    called when PCI error is detected

    :param struct pci_dev \*pdev:
        pointer to PCI device

    :param enum pci_channel_state state:
        current state of the PCI slot

.. _`sym2_io_slot_dump`:

sym2_io_slot_dump
=================

.. c:function:: pci_ers_result_t sym2_io_slot_dump(struct pci_dev *pdev)

    Enable MMIO and dump debug registers

    :param struct pci_dev \*pdev:
        pointer to PCI device

.. _`sym2_reset_workarounds`:

sym2_reset_workarounds
======================

.. c:function:: void sym2_reset_workarounds(struct pci_dev *pdev)

    hardware-specific work-arounds

    :param struct pci_dev \*pdev:
        *undescribed*

.. _`sym2_reset_workarounds.description`:

Description
-----------

This routine is similar to \ :c:func:`sym_set_workarounds`\ , except
that, at this point, we already know that the device was
successfully initialized at least once before, and so most
of the steps taken there are un-needed here.

.. _`sym2_io_slot_reset`:

sym2_io_slot_reset
==================

.. c:function:: pci_ers_result_t sym2_io_slot_reset(struct pci_dev *pdev)

    called when the pci bus has been reset.

    :param struct pci_dev \*pdev:
        pointer to PCI device

.. _`sym2_io_slot_reset.description`:

Description
-----------

Restart the card from scratch.

.. _`sym2_io_resume`:

sym2_io_resume
==============

.. c:function:: void sym2_io_resume(struct pci_dev *pdev)

    resume normal ops after PCI reset

    :param struct pci_dev \*pdev:
        pointer to PCI device

.. _`sym2_io_resume.description`:

Description
-----------

Called when the error recovery driver tells us that its
OK to resume normal operation. Use completion to allow
halted scsi ops to resume.

.. This file was automatic generated / don't edit.

