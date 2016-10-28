.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/xen/xen-pciback/pciback.h

.. _`xen_pcibk_get_pcifront_dev`:

xen_pcibk_get_pcifront_dev
==========================

.. c:function:: int xen_pcibk_get_pcifront_dev(struct pci_dev *pcidev, struct xen_pcibk_device *pdev, unsigned int *domain, unsigned int *bus, unsigned int *devfn)

    AER handling. Get guest domain/bus/devfn in xen_pcibk before sending aer request to pcifront, so that guest could identify device, coopearte with xen_pcibk to finish aer recovery job if device driver has the capability

    :param struct pci_dev \*pcidev:
        *undescribed*

    :param struct xen_pcibk_device \*pdev:
        *undescribed*

    :param unsigned int \*domain:
        *undescribed*

    :param unsigned int \*bus:
        *undescribed*

    :param unsigned int \*devfn:
        *undescribed*

.. This file was automatic generated / don't edit.

