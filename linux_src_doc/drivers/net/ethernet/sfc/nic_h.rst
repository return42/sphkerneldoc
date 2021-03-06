.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/nic.h

.. _`siena_nic_data`:

struct siena_nic_data
=====================

.. c:type:: struct siena_nic_data

    Siena NIC state

.. _`siena_nic_data.definition`:

Definition
----------

.. code-block:: c

    struct siena_nic_data {
        struct efx_nic *efx;
        int wol_filter_id;
        u64 stats[SIENA_STAT_COUNT];
    #ifdef CONFIG_SFC_SRIOV
        struct siena_vf *vf;
        struct efx_channel *vfdi_channel;
        unsigned vf_buftbl_base;
        struct efx_buffer vfdi_status;
        struct list_head local_addr_list;
        struct list_head local_page_list;
        struct mutex local_lock;
        struct work_struct peer_work;
    #endif
    }

.. _`siena_nic_data.members`:

Members
-------

efx
    Pointer back to main interface structure

wol_filter_id
    Wake-on-LAN packet filter id

stats
    Hardware statistics

vf
    Array of \ :c:type:`struct siena_vf <siena_vf>`\  objects

vfdi_channel
    *undescribed*

vf_buftbl_base
    The zeroth buffer table index used to back VF queues.

vfdi_status
    Common VFDI status page to be dmad to VF address space.

local_addr_list
    List of local addresses. Protected by \ ``local_lock``\ .

local_page_list
    List of DMA addressable pages used to broadcast
    \ ``local_addr_list``\ . Protected by \ ``local_lock``\ .

local_lock
    Mutex protecting \ ``local_addr_list``\  and \ ``local_page_list``\ .

peer_work
    Work item to broadcast peer addresses to VMs.

.. _`efx_ef10_nic_data`:

struct efx_ef10_nic_data
========================

.. c:type:: struct efx_ef10_nic_data

    EF10 architecture NIC state

.. _`efx_ef10_nic_data.definition`:

Definition
----------

.. code-block:: c

    struct efx_ef10_nic_data {
        struct efx_buffer mcdi_buf;
        u16 warm_boot_count;
        unsigned int vi_base;
        unsigned int n_allocated_vis;
        bool must_realloc_vis;
        bool must_restore_rss_contexts;
        bool must_restore_filters;
        unsigned int n_piobufs;
        void __iomem *wc_membase, *pio_write_base;
        unsigned int pio_write_vi_base;
        unsigned int piobuf_handle[EF10_TX_PIOBUF_COUNT];
        u16 piobuf_size;
        bool must_restore_piobufs;
        bool rx_rss_context_exclusive;
        u64 stats[EF10_STAT_COUNT];
        bool workaround_35388;
        bool workaround_26807;
        bool workaround_61265;
        bool must_check_datapath_caps;
        u32 datapath_caps;
        u32 datapath_caps2;
        unsigned int rx_dpcpu_fw_id;
        unsigned int tx_dpcpu_fw_id;
        unsigned int vport_id;
        bool must_probe_vswitching;
        unsigned int pf_index;
        u8 port_id[ETH_ALEN];
    #ifdef CONFIG_SFC_SRIOV
        unsigned int vf_index;
        struct ef10_vf *vf;
    #endif
        u8 vport_mac[ETH_ALEN];
        struct list_head vlan_list;
        struct mutex vlan_lock;
        struct efx_udp_tunnel udp_tunnels[16];
        bool udp_tunnels_dirty;
        struct mutex udp_tunnels_lock;
        u64 licensed_features;
    }

.. _`efx_ef10_nic_data.members`:

Members
-------

mcdi_buf
    DMA buffer for MCDI

warm_boot_count
    Last seen MC warm boot count

vi_base
    Absolute index of first VI in this function

n_allocated_vis
    Number of VIs allocated to this function

must_realloc_vis
    Flag: VIs have yet to be reallocated after MC reboot

must_restore_rss_contexts
    Flag: RSS contexts have yet to be restored after
    MC reboot

must_restore_filters
    Flag: filters have yet to be restored after MC reboot

n_piobufs
    Number of PIO buffers allocated to this function

wc_membase
    Base address of write-combining mapping of the memory BAR

pio_write_base
    Base address for writing PIO buffers

pio_write_vi_base
    Relative VI number for \ ``pio_write_base``\ 

piobuf_handle
    Handle of each PIO buffer allocated

piobuf_size
    size of a single PIO buffer

must_restore_piobufs
    Flag: PIO buffers have yet to be restored after MC
    reboot

rx_rss_context_exclusive
    Whether our RSS context is exclusive or shared

stats
    Hardware statistics

workaround_35388
    Flag: firmware supports workaround for bug 35388

workaround_26807
    Flag: firmware supports workaround for bug 26807

workaround_61265
    Flag: firmware supports workaround for bug 61265

must_check_datapath_caps
    Flag: \ ``datapath_caps``\  needs to be revalidated
    after MC reboot

datapath_caps
    Capabilities of datapath firmware (FLAGS1 field of
    \ ``MC_CMD_GET_CAPABILITIES``\  response)

datapath_caps2
    Further Capabilities of datapath firmware (FLAGS2 field of
    \ ``MC_CMD_GET_CAPABILITIES``\  response)

rx_dpcpu_fw_id
    Firmware ID of the RxDPCPU

tx_dpcpu_fw_id
    Firmware ID of the TxDPCPU

vport_id
    The function's vport ID, only relevant for PFs

must_probe_vswitching
    Flag: vswitching has yet to be setup after MC reboot

pf_index
    The number for this PF, or the parent PF if this is a VF

port_id
    *undescribed*

vf_index
    *undescribed*

vf
    Pointer to VF data structure

vport_mac
    The MAC address on the vport, only for PFs; VFs will be zero

vlan_list
    List of VLANs added over the interface. Serialised by vlan_lock.

vlan_lock
    Lock to serialize access to vlan_list.

udp_tunnels
    UDP tunnel port numbers and types.

udp_tunnels_dirty
    flag indicating a reboot occurred while pushing
    \ ``udp_tunnels``\  to hardware and thus the push must be re-done.

udp_tunnels_lock
    Serialises writes to \ ``udp_tunnels``\  and \ ``udp_tunnels_dirty``\ .

licensed_features
    *undescribed*

.. This file was automatic generated / don't edit.

