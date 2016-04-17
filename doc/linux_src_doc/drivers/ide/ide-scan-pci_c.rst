.. -*- coding: utf-8; mode: rst -*-

==============
ide-scan-pci.c
==============


.. _`ide_scan_pcidev`:

ide_scan_pcidev
===============

.. c:function:: int ide_scan_pcidev (struct pci_dev *dev)

    find an IDE driver for a device

    :param struct pci_dev \*dev:
        PCI device to check



.. _`ide_scan_pcidev.description`:

Description
-----------

Look for an IDE driver to handle the device we are considering.
This is only used during boot up to get the ordering correct. After
boot up the pci layer takes over the job.



.. _`ide_scan_pcibus`:

ide_scan_pcibus
===============

.. c:function:: int ide_scan_pcibus ( void)

    perform the initial IDE driver scan

    :param void:
        no arguments



.. _`ide_scan_pcibus.description`:

Description
-----------


Perform the initial bus rather than driver ordered scan of the
PCI drivers. After this all IDE pci handling becomes standard
module ordering not traditionally ordered.

