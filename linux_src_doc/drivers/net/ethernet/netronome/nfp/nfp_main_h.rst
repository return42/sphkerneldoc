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
        struct nfp_app *app;
        struct nfp_cpp_area *data_vnic_bar;
        struct nfp_cpp_area *ctrl_vnic_bar;
        struct nfp_cpp_area *qc_area;
        struct nfp_cpp_area *mac_stats_bar;
        u8 __iomem *mac_stats_mem;
        struct nfp_cpp_area *vf_cfg_bar;
        u8 __iomem *vf_cfg_mem;
        struct nfp_cpp_area *vfcfg_tbl2_area;
        u8 __iomem *vfcfg_tbl2;
        struct msix_entry *irq_entries;
        unsigned int limit_vfs;
        unsigned int num_vfs;
        bool fw_loaded;
        struct nfp_net *ctrl_vnic;
        const struct nfp_mip *mip;
        struct nfp_rtsym_table *rtbl;
        struct nfp_hwinfo *hwinfo;
        struct nfp_eth_table *eth_tbl;
        struct nfp_nsp_identify *nspi;
        struct device *hwmon_dev;
        struct dentry *ddir;
        unsigned int max_data_vnics;
        unsigned int num_vnics;
        struct list_head vnics;
        struct list_head ports;
        struct workqueue_struct *wq;
        struct work_struct port_refresh_work;
        struct mutex lock;
    }

.. _`nfp_pf.members`:

Members
-------

pdev
    Backpointer to PCI device

cpp
    Pointer to the CPP handle

app
    Pointer to the APP handle

data_vnic_bar
    Pointer to the CPP area for the data vNICs' BARs

ctrl_vnic_bar
    Pointer to the CPP area for the ctrl vNIC's BAR

qc_area
    Pointer to the CPP area for the queues

mac_stats_bar
    Pointer to the CPP area for the MAC stats

mac_stats_mem
    Pointer to mapped MAC stats area

vf_cfg_bar
    Pointer to the CPP area for the VF configuration BAR

vf_cfg_mem
    Pointer to mapped VF configuration area

vfcfg_tbl2_area
    Pointer to the CPP area for the VF config table

vfcfg_tbl2
    Pointer to mapped VF config table

irq_entries
    Array of MSI-X entries for all vNICs

limit_vfs
    Number of VFs supported by firmware (~0 for PCI limit)

num_vfs
    Number of SR-IOV VFs enabled

fw_loaded
    Is the firmware loaded?

ctrl_vnic
    Pointer to the control vNIC if available

mip
    MIP handle

rtbl
    RTsym table

hwinfo
    HWInfo table

eth_tbl
    NSP ETH table

nspi
    NSP identification info

hwmon_dev
    pointer to hwmon device

ddir
    Per-device debugfs directory

max_data_vnics
    Number of data vNICs app firmware supports

num_vnics
    Number of vNICs spawned

vnics
    Linked list of vNIC structures (struct nfp_net)

ports
    Linked list of port structures (struct nfp_port)

wq
    Workqueue for running works which need to grab \ ``lock``\ 

port_refresh_work
    Work entry for taking netdevs out

lock
    Protects all fields which may change after probe

.. This file was automatic generated / don't edit.

