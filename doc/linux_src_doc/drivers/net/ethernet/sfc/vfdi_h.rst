.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/vfdi.h

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
        union u;
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
    Array of DMA addresses of pages.
    If the number of peers exceeds 256, then the VF must provide
    additional pages in this array. The PF will then DMA up to
    512 vfdi_endpoint structures into each page.  These addresses
    must be page-aligned.

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
    than ARRAY_SIZE(\ ``peers``\ ), then the VF must provide sufficient
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

