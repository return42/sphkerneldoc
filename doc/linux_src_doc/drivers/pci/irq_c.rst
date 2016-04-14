.. -*- coding: utf-8; mode: rst -*-

=====
irq.c
=====

.. _`pci_lost_interrupt`:

pci_lost_interrupt
==================

.. c:function:: enum pci_lost_interrupt_reason pci_lost_interrupt (struct pci_dev *pdev)

    reports a lost PCI interrupt

    :param struct pci_dev \*pdev:
        device whose interrupt is lost


.. _`pci_lost_interrupt.description`:

Description
-----------

The primary function of this routine is to report a lost interrupt
in a standard way which users can recognise (instead of blaming the
driver).

Returns::

 a suggestion for fixing it (although the driver is not required to

act on this).

