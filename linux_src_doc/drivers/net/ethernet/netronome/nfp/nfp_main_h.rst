.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_main.h

.. _`nfp_pf`:

struct nfp_pf
=============

.. c:type:: struct nfp_pf

    NFP PF-specific device structure

.. _`nfp_pf.definition`:

Definition
----------

.. code-block:: c

    struct nfp_pf {
        struct pci_dev *pdev;
        struct nfp_cpp *cpp;
        struct nfp_cpp_area *ctrl_area;
        struct nfp_cpp_area *tx_area;
        struct nfp_cpp_area *rx_area;
        struct msix_entry *irq_entries;
        unsigned int limit_vfs;
        unsigned int num_vfs;
        bool fw_loaded;
        struct nfp_eth_table *eth_tbl;
        struct dentry *ddir;
        unsigned int num_ports;
        unsigned int num_netdevs;
        struct list_head ports;
        struct work_struct port_refresh_work;
        struct mutex port_lock;
    }

.. _`nfp_pf.members`:

Members
-------

pdev
    Backpointer to PCI device

cpp
    Pointer to the CPP handle

ctrl_area
    Pointer to the CPP area for the control BAR

tx_area
    Pointer to the CPP area for the TX queues

rx_area
    Pointer to the CPP area for the FL/RX queues

irq_entries
    Array of MSI-X entries for all ports

limit_vfs
    Number of VFs supported by firmware (~0 for PCI limit)

num_vfs
    Number of SR-IOV VFs enabled

fw_loaded
    Is the firmware loaded?

eth_tbl
    NSP ETH table

ddir
    Per-device debugfs directory

num_ports
    Number of adapter ports app firmware supports

num_netdevs
    Number of netdevs spawned

ports
    Linked list of port structures (struct nfp_net)

port_refresh_work
    Work entry for taking netdevs out

port_lock
    Protects \ ``ports``\ , \ ``num_ports``\ , \ ``num_netdevs``\ 

.. This file was automatic generated / don't edit.

