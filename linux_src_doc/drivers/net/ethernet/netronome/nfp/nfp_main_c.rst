.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_main.c

.. _`nfp_net_fw_find`:

nfp_net_fw_find
===============

.. c:function:: const struct firmware *nfp_net_fw_find(struct pci_dev *pdev, struct nfp_pf *pf)

    Find the correct firmware image for netdev mode

    :param pdev:
        PCI Device structure
    :type pdev: struct pci_dev \*

    :param pf:
        NFP PF Device structure
    :type pf: struct nfp_pf \*

.. _`nfp_net_fw_find.return`:

Return
------

firmware if found and requested successfully.

.. _`nfp_fw_load`:

nfp_fw_load
===========

.. c:function:: int nfp_fw_load(struct pci_dev *pdev, struct nfp_pf *pf, struct nfp_nsp *nsp)

    Load the firmware image

    :param pdev:
        PCI Device structure
    :type pdev: struct pci_dev \*

    :param pf:
        NFP PF Device structure
    :type pf: struct nfp_pf \*

    :param nsp:
        NFP SP handle
    :type nsp: struct nfp_nsp \*

.. _`nfp_fw_load.return`:

Return
------

-ERRNO, 0 for no firmware loaded, 1 for firmware loaded

.. This file was automatic generated / don't edit.

