.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp6000_pcie.c

.. _`nfp_bar`:

struct nfp_bar
==============

.. c:type:: struct nfp_bar

    describes BAR configuration and usage

.. _`nfp_bar.definition`:

Definition
----------

.. code-block:: c

    struct nfp_bar {
        struct nfp6000_pcie *nfp;
        u32 barcfg;
        u64 base;
        u64 mask;
        u32 bitsize;
        int index;
        atomic_t refcnt;
        void __iomem *iomem;
        struct resource *resource;
    }

.. _`nfp_bar.members`:

Members
-------

nfp
    backlink to owner

barcfg
    cached contents of BAR config CSR

base
    the BAR's base CPP offset

mask
    mask for the BAR aperture (read only)

bitsize
    bitsize of BAR aperture (read only)

index
    index of the BAR

refcnt
    number of current users

iomem
    mapped IO memory

resource
    iomem resource window

.. _`nfp_cpp_from_nfp6000_pcie`:

nfp_cpp_from_nfp6000_pcie
=========================

.. c:function:: struct nfp_cpp *nfp_cpp_from_nfp6000_pcie(struct pci_dev *pdev)

    Build a NFP CPP bus from a NFP6000 PCI device

    :param struct pci_dev \*pdev:
        NFP6000 PCI device

.. _`nfp_cpp_from_nfp6000_pcie.return`:

Return
------

NFP CPP handle

.. This file was automatic generated / don't edit.

