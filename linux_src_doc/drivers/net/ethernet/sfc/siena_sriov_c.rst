.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/siena_sriov.c

.. _`efx_vf_tx_filter_mode`:

enum efx_vf_tx_filter_mode
==========================

.. c:type:: enum efx_vf_tx_filter_mode

    TX MAC filtering behaviour

.. _`efx_vf_tx_filter_mode.definition`:

Definition
----------

.. code-block:: c

    enum efx_vf_tx_filter_mode {
        VF_TX_FILTER_OFF,
        VF_TX_FILTER_AUTO,
        VF_TX_FILTER_ON
    };

.. _`efx_vf_tx_filter_mode.constants`:

Constants
---------

VF_TX_FILTER_OFF
    Disabled

VF_TX_FILTER_AUTO
    Enabled if MAC address assigned to VF and only
    2 TX queues allowed per VF.

VF_TX_FILTER_ON
    Enabled

.. _`siena_vf`:

struct siena_vf
===============

.. c:type:: struct siena_vf

    Back-end resource and protocol state for a PCI VF

.. _`siena_vf.definition`:

Definition
----------

.. code-block:: c

    struct siena_vf {
        struct efx_nic *efx;
        unsigned int pci_rid;
        char pci_name;
        unsigned int index;
        struct work_struct req;
        u64 req_addr;
        int req_type;
        unsigned req_seqno;
        unsigned msg_seqno;
        bool busy;
        struct efx_buffer buf;
        unsigned buftbl_base;
        bool rx_filtering;
        enum efx_filter_flags rx_filter_flags;
        unsigned rx_filter_qid;
        int rx_filter_id;
        enum efx_vf_tx_filter_mode tx_filter_mode;
        int tx_filter_id;
        struct vfdi_endpoint addr;
        u64 status_addr;
        struct mutex status_lock;
        u64 *peer_page_addrs;
        unsigned peer_page_count;
        u64 evq0_addrs;
        unsigned evq0_count;
        wait_queue_head_t flush_waitq;
        struct mutex txq_lock;
        unsigned long txq_mask;
        unsigned txq_count;
        unsigned long rxq_mask;
        unsigned rxq_count;
        unsigned long rxq_retry_mask;
        atomic_t rxq_retry_count;
        struct work_struct reset_work;
    }

.. _`siena_vf.members`:

Members
-------

efx
    The Efx NIC owning this VF

pci_rid
    The PCI requester ID for this VF

pci_name
    The PCI name (formatted address) of this VF

index
    Index of VF within its port and PF.

req
    VFDI incoming request work item. Incoming USR_EV events are received
    by the NAPI handler, but must be handled by executing MCDI requests
    inside a work item.

req_addr
    VFDI incoming request DMA address (in VF's PCI address space).

req_type
    Expected next incoming (from VF) \ ``VFDI_EV_TYPE``\  member.

req_seqno
    Expected next incoming (from VF) \ ``VFDI_EV_SEQ``\  member.

msg_seqno
    Next \ ``VFDI_EV_SEQ``\  member to reply to VF. Protected by
    \ ``status_lock``\ 

busy
    VFDI request queued to be processed or being processed. Receiving
    a VFDI request when \ ``busy``\  is set is an error condition.

buf
    Incoming VFDI requests are DMA from the VF into this buffer.

buftbl_base
    Buffer table entries for this VF start at this index.

rx_filtering
    Receive filtering has been requested by the VF driver.

rx_filter_flags
    The flags sent in the \ ``VFDI_OP_INSERT_FILTER``\  request.

rx_filter_qid
    VF relative qid for RX filter requested by VF.

rx_filter_id
    Receive MAC filter ID. Only one filter per VF is supported.

tx_filter_mode
    Transmit MAC filtering mode.

tx_filter_id
    Transmit MAC filter ID.

addr
    The MAC address and outer vlan tag of the VF.

status_addr
    VF DMA address of page for \ :c:type:`struct vfdi_status <vfdi_status>`\  updates.

status_lock
    Mutex protecting \ ``msg_seqno``\ , \ ``status_addr``\ , \ ``addr``\ ,
    \ ``peer_page_addrs``\  and \ ``peer_page_count``\  from simultaneous
    updates by the VM and consumption by
    \ :c:func:`efx_siena_sriov_update_vf_addr`\ 

peer_page_addrs
    Pointer to an array of guest pages for local addresses.

peer_page_count
    Number of entries in \ ``peer_page_count``\ .

evq0_addrs
    Array of guest pages backing evq0.

evq0_count
    Number of entries in \ ``evq0_addrs``\ .

flush_waitq
    wait queue used by \ ``VFDI_OP_FINI_ALL_QUEUES``\  handler
    to wait for flush completions.

txq_lock
    Mutex for TX queue allocation.

txq_mask
    Mask of initialized transmit queues.

txq_count
    Number of initialized transmit queues.

rxq_mask
    Mask of initialized receive queues.

rxq_count
    Number of initialized receive queues.

rxq_retry_mask
    Mask or receive queues that need to be flushed again
    due to flush failure.

rxq_retry_count
    Number of receive queues in \ ``rxq_retry_mask``\ .

reset_work
    Work item to schedule a VF reset.

.. _`efx_local_addr`:

struct efx_local_addr
=====================

.. c:type:: struct efx_local_addr

    A MAC address on the vswitch without a VF.

.. _`efx_local_addr.definition`:

Definition
----------

.. code-block:: c

    struct efx_local_addr {
        struct list_head link;
        u8 addr;
    }

.. _`efx_local_addr.members`:

Members
-------

link
    List head for insertion into efx->local_addr_list.

addr
    Ethernet address

.. _`efx_local_addr.description`:

Description
-----------

Siena does not have a switch, so VFs can't transmit data to each
other. Instead the VFs must be made aware of the local addresses
on the vswitch, so that they can arrange for an alternative
software datapath to be used.

.. _`efx_endpoint_page`:

struct efx_endpoint_page
========================

.. c:type:: struct efx_endpoint_page

    Page of vfdi_endpoint structures

.. _`efx_endpoint_page.definition`:

Definition
----------

.. code-block:: c

    struct efx_endpoint_page {
        struct list_head link;
        void *ptr;
        dma_addr_t addr;
    }

.. _`efx_endpoint_page.members`:

Members
-------

link
    List head for insertion into efx->local_page_list.

ptr
    Pointer to page.

addr
    DMA address of page.

.. This file was automatic generated / don't edit.

