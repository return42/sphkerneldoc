.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/vfdi.h

.. _`virtual-function-driver-interface`:

Virtual Function Driver Interface
=================================

This file contains software structures used to form a two way
communication channel between the VF driver and the PF driver,
named Virtual Function Driver Interface (VFDI).

For the purposes of VFDI, a page is a memory region with size and
alignment of 4K.  All addresses are DMA addresses to be used within
the domain of the relevant VF.

The only hardware-defined channels for a VF driver to communicate
with the PF driver are the event mailboxes (%FR_CZ_USR_EV
registers).  Writing to these registers generates an event with
EV_CODE = EV_CODE_USR_EV, USER_QID set to the index of the mailbox
and USER_EV_REG_VALUE set to the value written.  The PF driver may
direct or disable delivery of these events by setting
\ ``FR_CZ_USR_EV_CFG``\ .

The PF driver can send arbitrary events to arbitrary event queues.
However, for consistency, VFDI events from the PF are defined to
follow the same form and be sent to the first event queue assigned
to the VF while that queue is enabled by the VF driver.

The general form of the variable bits of VFDI events is:

0             16                       24   31
\| DATA        \| TYPE                   \| SEQ   \|

SEQ is a sequence number which should be incremented by 1 (modulo
256) for each event.  The sequence numbers used in each direction
are independent.

The VF submits requests of type \ :c:type:`struct vfdi_req <vfdi_req>`\  by sending the
address of the request (ADDR) in a series of 4 events:

0             16                       24   31
\| ADDR[0:15]  \| VFDI_EV_TYPE_REQ_WORD0 \| SEQ   \|
\| ADDR[16:31] \| VFDI_EV_TYPE_REQ_WORD1 \| SEQ+1 \|
\| ADDR[32:47] \| VFDI_EV_TYPE_REQ_WORD2 \| SEQ+2 \|
\| ADDR[48:63] \| VFDI_EV_TYPE_REQ_WORD3 \| SEQ+3 \|

The address must be page-aligned.  After receiving such a valid
series of events, the PF driver will attempt to read the request
and write a response to the same address.  In case of an invalid
sequence of events or a DMA error, there will be no response.

The VF driver may request that the PF driver writes status
information into its domain asynchronously.  After writing the
status, the PF driver will send an event of the form:

0             16                       24   31
\| reserved    \| VFDI_EV_TYPE_STATUS    \| SEQ   \|

In case the VF must be reset for any reason, the PF driver will
send an event of the form:

0             16                       24   31
\| reserved    \| VFDI_EV_TYPE_RESET     \| SEQ   \|

It is then the responsibility of the VF driver to request
reinitialisation of its queues.

.. _`vfdi_op`:

enum vfdi_op
============

.. c:type:: enum vfdi_op

    VFDI operation enumeration

.. _`vfdi_op.definition`:

Definition
----------

.. code-block:: c

    enum vfdi_op {
        VFDI_OP_RESPONSE,
        VFDI_OP_INIT_EVQ,
        VFDI_OP_INIT_RXQ,
        VFDI_OP_INIT_TXQ,
        VFDI_OP_FINI_ALL_QUEUES,
        VFDI_OP_INSERT_FILTER,
        VFDI_OP_REMOVE_ALL_FILTERS,
        VFDI_OP_SET_STATUS_PAGE,
        VFDI_OP_CLEAR_STATUS_PAGE,
        VFDI_OP_LIMIT
    };

.. _`vfdi_op.constants`:

Constants
---------

VFDI_OP_RESPONSE
    Indicates a response to the request.

VFDI_OP_INIT_EVQ
    Initialize SRAM entries and initialize an EVQ.

VFDI_OP_INIT_RXQ
    Initialize SRAM entries and initialize an RXQ.

VFDI_OP_INIT_TXQ
    Initialize SRAM entries and initialize a TXQ.

VFDI_OP_FINI_ALL_QUEUES
    Flush all queues, finalize all queues, then
    finalize the SRAM entries.

VFDI_OP_INSERT_FILTER
    Insert a MAC filter targeting the given RXQ.

VFDI_OP_REMOVE_ALL_FILTERS
    Remove all filters.

VFDI_OP_SET_STATUS_PAGE
    Set the DMA page(s) used for status updates
    from PF and write the initial status.

VFDI_OP_CLEAR_STATUS_PAGE
    Clear the DMA page(s) used for status
    updates from PF.

VFDI_OP_LIMIT
    *undescribed*

.. _`vfdi_req`:

struct vfdi_req
===============

.. c:type:: struct vfdi_req

    Request from VF driver to PF driver

.. _`vfdi_req.definition`:

Definition
----------

.. code-block:: c

    struct vfdi_req {
        u32 op;
        u32 reserved1;
        s32 rc;
        u32 reserved2;
        union {
            struct {
                u32 index;
                u32 buf_count;
                u64 addr[];
            } init_evq;
            struct {
                u32 index;
                u32 buf_count;
                u32 evq;
                u32 label;
                u32 flags;
    #define VFDI_RXQ_FLAG_SCATTER_EN 1
                u32 reserved;
                u64 addr[];
            } init_rxq;
            struct {
                u32 index;
                u32 buf_count;
                u32 evq;
                u32 label;
                u32 flags;
    #define VFDI_TXQ_FLAG_IP_CSUM_DIS 1
    #define VFDI_TXQ_FLAG_TCPUDP_CSUM_DIS 2
                u32 reserved;
                u64 addr[];
            } init_txq;
            struct {
                u32 rxq;
                u32 flags;
    #define VFDI_MAC_FILTER_FLAG_RSS 1
    #define VFDI_MAC_FILTER_FLAG_SCATTER 2
            } mac_filter;
            struct {
                u64 dma_addr;
                u64 peer_page_count;
                u64 peer_page_addr[];
            } set_status_page;
        } u;
    }

.. _`vfdi_req.members`:

Members
-------

op
    Operation code or response indicator, taken from \ :c:type:`enum vfdi_op <vfdi_op>`\ .

reserved1
    *undescribed*

rc
    Response code.  Set to 0 on success or a negative error code on failure.

reserved2
    *undescribed*

u
    *undescribed*

u.init_evq.index
    Index of event queue to create.

u.init_evq.buf_count
    Number of 4k buffers backing event queue.

u.init_evq.addr
    Array of length \ ``u``\ .init_evq.buf_count containing DMA
    address of each page backing the event queue.

u.init_rxq.index
    Index of receive queue to create.

u.init_rxq.buf_count
    Number of 4k buffers backing receive queue.

u.init_rxq.evq
    Instance of event queue to target receive events at.

u.init_rxq.label
    Label used in receive events.

u.init_rxq.flags
    Unused.

u.init_rxq.addr
    Array of length \ ``u``\ .init_rxq.buf_count containing DMA
    address of each page backing the receive queue.

u.init_txq.index
    Index of transmit queue to create.

u.init_txq.buf_count
    Number of 4k buffers backing transmit queue.

u.init_txq.evq
    Instance of event queue to target transmit completion
    events at.

u.init_txq.label
    Label used in transmit completion events.

u.init_txq.flags
    Checksum offload flags.

u.init_txq.addr
    Array of length \ ``u``\ .init_txq.buf_count containing DMA
    address of each page backing the transmit queue.

u.mac_filter.rxq
    Insert MAC filter at VF local address/VLAN targeting
    all traffic at this receive queue.

u.mac_filter.flags
    MAC filter flags.

u.set_status_page.dma_addr
    Base address for the \ :c:type:`struct vfdi_status <vfdi_status>`\ .
    This address must be page-aligned and the PF may write up to a
    whole page (allowing for extension of the structure).

u.set_status_page.peer_page_count
    Number of additional pages the VF
    has provided into which peer addresses may be DMAd.

u.set_status_page.peer_page_addr
    Array of DMA addresses of pages.
    If the number of peers exceeds 256, then the VF must provide
    additional pages in this array. The PF will then DMA up to
    512 vfdi_endpoint structures into each page.  These addresses
    must be page-aligned.

init_evq
    *undescribed*

index
    *undescribed*

buf_count
    *undescribed*

addr
    *undescribed*

init_rxq
    *undescribed*

index
    *undescribed*

buf_count
    *undescribed*

evq
    *undescribed*

label
    *undescribed*

flags
    *undescribed*

reserved
    *undescribed*

addr
    *undescribed*

init_txq
    *undescribed*

index
    *undescribed*

buf_count
    *undescribed*

evq
    *undescribed*

label
    *undescribed*

flags
    *undescribed*

reserved
    *undescribed*

addr
    *undescribed*

mac_filter
    *undescribed*

rxq
    *undescribed*

flags
    *undescribed*

set_status_page
    *undescribed*

dma_addr
    *undescribed*

peer_page_count
    *undescribed*

peer_page_addr
    *undescribed*

.. _`vfdi_status`:

struct vfdi_status
==================

.. c:type:: struct vfdi_status

    Status provided by PF driver to VF driver

.. _`vfdi_status.definition`:

Definition
----------

.. code-block:: c

    struct vfdi_status {
        u32 generation_start;
        u32 generation_end;
        u32 version;
        u32 length;
        u8 vi_scale;
        u8 max_tx_channels;
        u8 rss_rxq_count;
        u8 reserved1;
        u16 peer_count;
        u16 reserved2;
        struct vfdi_endpoint local;
        struct vfdi_endpoint peers[256];
        u32 timer_quantum_ns;
    }

.. _`vfdi_status.members`:

Members
-------

generation_start
    A generation count DMA'd to VF \*before\* the
    rest of the structure.

generation_end
    A generation count DMA'd to VF \*after\* the
    rest of the structure.

version
    Version of this structure; currently set to 1.  Later
    versions must either be layout-compatible or only be sent to VFs
    that specifically request them.

length
    Total length of this structure including embedded tables

vi_scale
    log2 the number of VIs available on this VF. This quantity
    is used by the hardware for register decoding.

max_tx_channels
    The maximum number of transmit queues the VF can use.

rss_rxq_count
    The number of receive queues present in the shared RSS
    indirection table.

reserved1
    *undescribed*

peer_count
    Total number of peers in the complete peer list. If larger
    than ARRAY_SIZE(%peers), then the VF must provide sufficient
    additional pages each of which is filled with vfdi_endpoint structures.

reserved2
    *undescribed*

local
    The MAC address and outer VLAN tag of \*this\* VF

peers
    Table of peer addresses.  The \ ``tci``\  fields in these structures
    are currently unused and must be ignored.  Additional peers are
    written into any additional pages provided by the VF.

timer_quantum_ns
    Timer quantum (nominal period between timer ticks)
    for interrupt moderation timers, in nanoseconds. This member is only
    present if \ ``length``\  is sufficiently large.

.. This file was automatic generated / don't edit.

