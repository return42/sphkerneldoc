.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_netvf_main.c

.. _`nfp_net_vf`:

struct nfp_net_vf
=================

.. c:type:: struct nfp_net_vf

    NFP VF-specific device structure

.. _`nfp_net_vf.definition`:

Definition
----------

.. code-block:: c

    struct nfp_net_vf {
        struct nfp_net *nn;
        struct msix_entry irq_entries[NFP_NET_NON_Q_VECTORS + NFP_NET_MAX_TX_RINGS];
        u8 __iomem *q_bar;
        struct dentry *ddir;
    }

.. _`nfp_net_vf.members`:

Members
-------

nn
    NFP Net structure for this device

irq_entries
    Pre-allocated array of MSI-X entries

q_bar
    Pointer to mapped QC memory (NULL if TX/RX mapped directly)

ddir
    Per-device debugfs directory

.. This file was automatic generated / don't edit.

