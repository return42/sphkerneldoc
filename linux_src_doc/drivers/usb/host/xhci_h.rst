.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/xhci.h

.. _`xhci_cap_regs`:

struct xhci_cap_regs
====================

.. c:type:: struct xhci_cap_regs

    xHCI Host Controller Capability Registers.

.. _`xhci_cap_regs.definition`:

Definition
----------

.. code-block:: c

    struct xhci_cap_regs {
        __le32 hc_capbase;
        __le32 hcs_params1;
        __le32 hcs_params2;
        __le32 hcs_params3;
        __le32 hcc_params;
        __le32 db_off;
        __le32 run_regs_off;
        __le32 hcc_params2;
    }

.. _`xhci_cap_regs.members`:

Members
-------

hc_capbase
    length of the capabilities register and HC version number

hcs_params1
    HCSPARAMS1 - Structural Parameters 1

hcs_params2
    HCSPARAMS2 - Structural Parameters 2

hcs_params3
    HCSPARAMS3 - Structural Parameters 3

hcc_params
    HCCPARAMS - Capability Parameters

db_off
    DBOFF - Doorbell array offset

run_regs_off
    RTSOFF - Runtime register space offset

hcc_params2
    HCCPARAMS2 Capability Parameters 2, xhci 1.1 only

.. _`xhci_op_regs`:

struct xhci_op_regs
===================

.. c:type:: struct xhci_op_regs

    xHCI Host Controller Operational Registers.

.. _`xhci_op_regs.definition`:

Definition
----------

.. code-block:: c

    struct xhci_op_regs {
        __le32 command;
        __le32 status;
        __le32 page_size;
        __le32 reserved1;
        __le32 reserved2;
        __le32 dev_notification;
        __le64 cmd_ring;
        __le32 reserved3[4];
        __le64 dcbaa_ptr;
        __le32 config_reg;
        __le32 reserved4[241];
        __le32 port_status_base;
        __le32 port_power_base;
        __le32 port_link_base;
        __le32 reserved5;
        __le32 reserved6[NUM_PORT_REGS*254];
    }

.. _`xhci_op_regs.members`:

Members
-------

command
    USBCMD - xHC command register

status
    USBSTS - xHC status register

page_size
    This indicates the page size that the host controller
    supports.  If bit n is set, the HC supports a page size
    of 2^(n+12), up to a 128MB page size.
    4K is the minimum page size.

reserved1
    *undescribed*

reserved2
    *undescribed*

dev_notification
    *undescribed*

cmd_ring
    CRP - 64-bit Command Ring Pointer

reserved3
    *undescribed*

dcbaa_ptr
    DCBAAP - 64-bit Device Context Base Address Array Pointer

config_reg
    CONFIG - Configure Register

reserved4
    *undescribed*

port_status_base
    PORTSCn - base address for Port Status and Control
    Each port has a Port Status and Control register,
    followed by a Port Power Management Status and Control
    register, a Port Link Info register, and a reserved
    register.

port_power_base
    PORTPMSCn - base address for
    Port Power Management Status and Control

port_link_base
    PORTLIn - base address for Port Link Info (current
    Link PM state and control) for USB 2.1 and USB 3.0
    devices.

reserved5
    *undescribed*

reserved6
    *undescribed*

.. _`xhci_intr_reg`:

struct xhci_intr_reg
====================

.. c:type:: struct xhci_intr_reg

    Interrupt Register Set

.. _`xhci_intr_reg.definition`:

Definition
----------

.. code-block:: c

    struct xhci_intr_reg {
        __le32 irq_pending;
        __le32 irq_control;
        __le32 erst_size;
        __le32 rsvd;
        __le64 erst_base;
        __le64 erst_dequeue;
    }

.. _`xhci_intr_reg.members`:

Members
-------

irq_pending
    IMAN - Interrupt Management Register.  Used to enable
    interrupts and check for pending interrupts.

irq_control
    IMOD - Interrupt Moderation Register.
    Used to throttle interrupts.

erst_size
    Number of segments in the Event Ring Segment Table (ERST).

rsvd
    *undescribed*

erst_base
    ERST base address.

erst_dequeue
    Event ring dequeue pointer.

.. _`xhci_intr_reg.description`:

Description
-----------

Each interrupter (defined by a MSI-X vector) has an event ring and an Event
Ring Segment Table (ERST) associated with it.  The event ring is comprised of
multiple segments of the same size.  The HC places events on the ring and
"updates the Cycle bit in the TRBs to indicate to software the current
position of the Enqueue Pointer." The HCD (Linux) processes those events and
updates the dequeue pointer.

.. _`xhci_run_regs`:

struct xhci_run_regs
====================

.. c:type:: struct xhci_run_regs


.. _`xhci_run_regs.definition`:

Definition
----------

.. code-block:: c

    struct xhci_run_regs {
        __le32 microframe_index;
        __le32 rsvd[7];
        struct xhci_intr_reg ir_set[128];
    }

.. _`xhci_run_regs.members`:

Members
-------

microframe_index
    MFINDEX - current microframe number

rsvd
    *undescribed*

ir_set
    *undescribed*

.. _`xhci_run_regs.description`:

Description
-----------

Section 5.5 Host Controller Runtime Registers:
"Software should read and write these registers using only Dword (32 bit)
or larger accesses"

.. _`xhci_doorbell_array`:

struct xhci_doorbell_array
==========================

.. c:type:: struct xhci_doorbell_array


.. _`xhci_doorbell_array.definition`:

Definition
----------

.. code-block:: c

    struct xhci_doorbell_array {
        __le32 doorbell[256];
    }

.. _`xhci_doorbell_array.members`:

Members
-------

doorbell
    *undescribed*

.. _`xhci_doorbell_array.description`:

Description
-----------

Bits  0 -  7: Endpoint target
Bits  8 - 15: RsvdZ
Bits 16 - 31: Stream ID

Section 5.6

.. _`xhci_protocol_caps`:

struct xhci_protocol_caps
=========================

.. c:type:: struct xhci_protocol_caps


.. _`xhci_protocol_caps.definition`:

Definition
----------

.. code-block:: c

    struct xhci_protocol_caps {
        u32 revision;
        u32 name_string;
        u32 port_info;
    }

.. _`xhci_protocol_caps.members`:

Members
-------

revision
    major revision, minor revision, capability ID,
    and next capability pointer.

name_string
    Four ASCII characters to say which spec this xHC
    follows, typically "USB ".

port_info
    Port offset, count, and protocol-defined information.

.. _`xhci_container_ctx`:

struct xhci_container_ctx
=========================

.. c:type:: struct xhci_container_ctx


.. _`xhci_container_ctx.definition`:

Definition
----------

.. code-block:: c

    struct xhci_container_ctx {
        unsigned type;
    #define XHCI_CTX_TYPE_DEVICE 0x1
    #define XHCI_CTX_TYPE_INPUT 0x2
        int size;
        u8 *bytes;
        dma_addr_t dma;
    }

.. _`xhci_container_ctx.members`:

Members
-------

type
    Type of context.  Used to calculated offsets to contained contexts.

size
    Size of the context data

bytes
    The raw context data given to HW

dma
    dma address of the bytes

.. _`xhci_container_ctx.description`:

Description
-----------

Represents either a Device or Input context.  Holds a pointer to the raw
memory used for the context (bytes) and dma address of it (dma).

.. _`xhci_slot_ctx`:

struct xhci_slot_ctx
====================

.. c:type:: struct xhci_slot_ctx


.. _`xhci_slot_ctx.definition`:

Definition
----------

.. code-block:: c

    struct xhci_slot_ctx {
        __le32 dev_info;
        __le32 dev_info2;
        __le32 tt_info;
        __le32 dev_state;
        __le32 reserved[4];
    }

.. _`xhci_slot_ctx.members`:

Members
-------

dev_info
    Route string, device speed, hub info, and last valid endpoint

dev_info2
    Max exit latency for device number, root hub port number

tt_info
    tt_info is used to construct split transaction tokens

dev_state
    slot state and device address

reserved
    *undescribed*

.. _`xhci_slot_ctx.description`:

Description
-----------

Slot Context - section 6.2.1.1.  This assumes the HC uses 32-byte context
structures.  If the HC uses 64-byte contexts, there is an additional 32 bytes
reserved at the end of the slot context for HC internal use.

.. _`xhci_ep_ctx`:

struct xhci_ep_ctx
==================

.. c:type:: struct xhci_ep_ctx


.. _`xhci_ep_ctx.definition`:

Definition
----------

.. code-block:: c

    struct xhci_ep_ctx {
        __le32 ep_info;
        __le32 ep_info2;
        __le64 deq;
        __le32 tx_info;
        __le32 reserved[3];
    }

.. _`xhci_ep_ctx.members`:

Members
-------

ep_info
    endpoint state, streams, mult, and interval information.

ep_info2
    information on endpoint type, max packet size, max burst size,
    error count, and whether the HC will force an event for all
    transactions.

deq
    64-bit ring dequeue pointer address.  If the endpoint only
    defines one stream, this points to the endpoint transfer ring.
    Otherwise, it points to a stream context array, which has a
    ring pointer for each flow.

tx_info
    Average TRB lengths for the endpoint ring and
    max payload within an Endpoint Service Interval Time (ESIT).

reserved
    *undescribed*

.. _`xhci_ep_ctx.description`:

Description
-----------

Endpoint Context - section 6.2.1.2.  This assumes the HC uses 32-byte context
structures.  If the HC uses 64-byte contexts, there is an additional 32 bytes
reserved at the end of the endpoint context for HC internal use.

.. _`xhci_input_control_ctx`:

struct xhci_input_control_ctx
=============================

.. c:type:: struct xhci_input_control_ctx

    Input control context; see section 6.2.5.

.. _`xhci_input_control_ctx.definition`:

Definition
----------

.. code-block:: c

    struct xhci_input_control_ctx {
        __le32 drop_flags;
        __le32 add_flags;
        __le32 rsvd2[6];
    }

.. _`xhci_input_control_ctx.members`:

Members
-------

drop_flags
    *undescribed*

add_flags
    *undescribed*

rsvd2
    *undescribed*

.. _`xhci_device_context_array`:

struct xhci_device_context_array
================================

.. c:type:: struct xhci_device_context_array

    @dev_context_ptr     array of 64-bit DMA addresses for device contexts

.. _`xhci_device_context_array.definition`:

Definition
----------

.. code-block:: c

    struct xhci_device_context_array {
        __le64 dev_context_ptrs[MAX_HC_SLOTS];
        dma_addr_t dma;
    }

.. _`xhci_device_context_array.members`:

Members
-------

dev_context_ptrs
    *undescribed*

dma
    *undescribed*

.. This file was automatic generated / don't edit.

