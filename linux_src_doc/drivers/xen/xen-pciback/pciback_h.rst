.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/xen/xen-pciback/pciback.h

.. _`xen_pcibk_get_pcifront_dev`:

xen_pcibk_get_pcifront_dev
==========================

.. c:function:: int xen_pcibk_get_pcifront_dev(struct pci_dev *pcidev, struct xen_pcibk_device *pdev, unsigned int *domain, unsigned int *bus, unsigned int *devfn)

    AER handling. Get guest domain/bus/devfn in xen_pcibk before sending aer request to pcifront, so that guest could identify device, coopearte with xen_pcibk to finish aer recovery job if device driver has the capability

    :param pcidev:
        *undescribed*
    :type pcidev: struct pci_dev \*

    :param pdev:
        *undescribed*
    :type pdev: struct xen_pcibk_device \*

    :param domain:
        *undescribed*
    :type domain: unsigned int \*

    :param bus:
        *undescribed*
    :type bus: unsigned int \*

    :param devfn:
        *undescribed*
    :type devfn: unsigned int \*

.. This file was automatic generated / don't edit.

