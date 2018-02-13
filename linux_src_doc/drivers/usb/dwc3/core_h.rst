.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc3/core.h

.. _`dwc3_event_buffer`:

struct dwc3_event_buffer
========================

.. c:type:: struct dwc3_event_buffer

    Software event buffer representation

.. _`dwc3_event_buffer.definition`:

Definition
----------

.. code-block:: c

    struct dwc3_event_buffer {
        void *buf;
        void *cache;
        unsigned length;
        unsigned int lpos;
        unsigned int count;
        unsigned int flags;
    #define DWC3_EVENT_PENDING BIT(0)
        dma_addr_t dma;
        struct dwc3 *dwc;
    }

.. _`dwc3_event_buffer.members`:

Members
-------

buf
    _THE_ buffer

cache
    The buffer cache used in the threaded interrupt

length
    size of this buffer

lpos
    event offset

count
    cache of last read event count register

flags
    flags related to this event buffer

dma
    dma_addr_t

dwc
    pointer to DWC controller

.. _`dwc3_ep`:

struct dwc3_ep
==============

.. c:type:: struct dwc3_ep

    device side endpoint representation

.. _`dwc3_ep.definition`:

Definition
----------

.. code-block:: c

    struct dwc3_ep {
        struct usb_ep endpoint;
        struct list_head pending_list;
        struct list_head started_list;
        wait_queue_head_t wait_end_transfer;
        spinlock_t lock;
        void __iomem *regs;
        struct dwc3_trb *trb_pool;
        dma_addr_t trb_pool_dma;
        struct dwc3 *dwc;
        u32 saved_state;
        unsigned flags;
    #define DWC3_EP_ENABLED BIT(0)
    #define DWC3_EP_STALL BIT(1)
    #define DWC3_EP_WEDGE BIT(2)
    #define DWC3_EP_BUSY BIT(4)
    #define DWC3_EP_PENDING_REQUEST BIT(5)
    #define DWC3_EP_MISSED_ISOC BIT(6)
    #define DWC3_EP_END_TRANSFER_PENDING BIT(7)
    #define DWC3_EP_TRANSFER_STARTED BIT(8)
    #define DWC3_EP0_DIR_IN BIT(31)
        u8 trb_enqueue;
        u8 trb_dequeue;
        u8 number;
        u8 type;
        u8 resource_index;
        u32 allocated_requests;
        u32 queued_requests;
        u32 frame_number;
        u32 interval;
        char name[20];
        unsigned direction:1;
        unsigned stream_capable:1;
    }

.. _`dwc3_ep.members`:

Members
-------

endpoint
    usb endpoint

pending_list
    list of pending requests for this endpoint

started_list
    list of started requests on this endpoint

wait_end_transfer
    wait_queue_head_t for waiting on End Transfer complete

lock
    spinlock for endpoint request queue traversal

regs
    pointer to first endpoint register

trb_pool
    array of transaction buffers

trb_pool_dma
    dma address of \ ``trb_pool``\ 

dwc
    pointer to DWC controller

saved_state
    ep state saved during hibernation

flags
    endpoint flags (wedged, stalled, ...)

trb_enqueue
    enqueue 'pointer' into TRB array

trb_dequeue
    dequeue 'pointer' into TRB array

number
    endpoint number (1 - 15)

type
    set to bmAttributes & USB_ENDPOINT_XFERTYPE_MASK

resource_index
    Resource transfer index

allocated_requests
    number of requests allocated

queued_requests
    number of requests queued for transfer

frame_number
    set to the frame number we want this transfer to start (ISOC)

interval
    the interval on which the ISOC transfer is started

name
    a human readable name e.g. ep1out-bulk

direction
    true for TX, false for RX

stream_capable
    true when streams are enabled

.. _`dwc3_trb`:

struct dwc3_trb
===============

.. c:type:: struct dwc3_trb

    transfer request block (hw format)

.. _`dwc3_trb.definition`:

Definition
----------

.. code-block:: c

    struct dwc3_trb {
        u32 bpl;
        u32 bph;
        u32 size;
        u32 ctrl;
    }

.. _`dwc3_trb.members`:

Members
-------

bpl
    DW0-3

bph
    DW4-7

size
    DW8-B

ctrl
    DWC-F

.. _`dwc3_hwparams`:

struct dwc3_hwparams
====================

.. c:type:: struct dwc3_hwparams

    copy of HWPARAMS registers

.. _`dwc3_hwparams.definition`:

Definition
----------

.. code-block:: c

    struct dwc3_hwparams {
        u32 hwparams0;
        u32 hwparams1;
        u32 hwparams2;
        u32 hwparams3;
        u32 hwparams4;
        u32 hwparams5;
        u32 hwparams6;
        u32 hwparams7;
        u32 hwparams8;
    }

.. _`dwc3_hwparams.members`:

Members
-------

hwparams0
    GHWPARAMS0

hwparams1
    GHWPARAMS1

hwparams2
    GHWPARAMS2

hwparams3
    GHWPARAMS3

hwparams4
    GHWPARAMS4

hwparams5
    GHWPARAMS5

hwparams6
    GHWPARAMS6

hwparams7
    GHWPARAMS7

hwparams8
    GHWPARAMS8

.. _`dwc3_request`:

struct dwc3_request
===================

.. c:type:: struct dwc3_request

    representation of a transfer request

.. _`dwc3_request.definition`:

Definition
----------

.. code-block:: c

    struct dwc3_request {
        struct usb_request request;
        struct list_head list;
        struct dwc3_ep *dep;
        struct scatterlist *sg;
        unsigned num_pending_sgs;
        unsigned remaining;
        u8 epnum;
        struct dwc3_trb *trb;
        dma_addr_t trb_dma;
        unsigned unaligned:1;
        unsigned direction:1;
        unsigned mapped:1;
        unsigned started:1;
        unsigned zero:1;
    }

.. _`dwc3_request.members`:

Members
-------

request
    struct usb_request to be transferred

list
    a list_head used for request queueing

dep
    struct dwc3_ep owning this request

sg
    pointer to first incomplete sg

num_pending_sgs
    counter to pending sgs

remaining
    amount of data remaining

epnum
    endpoint number to which this request refers

trb
    pointer to struct dwc3_trb

trb_dma
    DMA address of \ ``trb``\ 

unaligned
    true for OUT endpoints with length not divisible by maxp

direction
    IN or OUT direction flag

mapped
    true when request has been dma-mapped

started
    request is started

zero
    wants a ZLP

.. _`dwc3`:

struct dwc3
===========

.. c:type:: struct dwc3

    representation of our controller

.. _`dwc3.definition`:

Definition
----------

.. code-block:: c

    struct dwc3 {
        struct work_struct drd_work;
        struct dwc3_trb *ep0_trb;
        void *bounce;
        void *scratchbuf;
        u8 *setup_buf;
        dma_addr_t ep0_trb_addr;
        dma_addr_t bounce_addr;
        dma_addr_t scratch_addr;
        struct dwc3_request ep0_usb_req;
        struct completion ep0_in_setup;
        spinlock_t lock;
        struct device *dev;
        struct device *sysdev;
        struct platform_device *xhci;
        struct resource xhci_resources[DWC3_XHCI_RESOURCES_NUM];
        struct dwc3_event_buffer *ev_buf;
        struct dwc3_ep *eps[DWC3_ENDPOINTS_NUM];
        struct usb_gadget gadget;
        struct usb_gadget_driver *gadget_driver;
        struct usb_phy *usb2_phy;
        struct usb_phy *usb3_phy;
        struct phy *usb2_generic_phy;
        struct phy *usb3_generic_phy;
        struct ulpi *ulpi;
        void __iomem *regs;
        size_t regs_size;
        enum usb_dr_mode dr_mode;
        u32 current_dr_role;
        u32 desired_dr_role;
        struct extcon_dev *edev;
        struct notifier_block edev_nb;
        enum usb_phy_interface hsphy_mode;
        u32 fladj;
        u32 irq_gadget;
        u32 nr_scratch;
        u32 u1u2;
        u32 maximum_speed;
        u32 revision;
    #define DWC3_REVISION_173A 0x5533173a
    #define DWC3_REVISION_175A 0x5533175a
    #define DWC3_REVISION_180A 0x5533180a
    #define DWC3_REVISION_183A 0x5533183a
    #define DWC3_REVISION_185A 0x5533185a
    #define DWC3_REVISION_187A 0x5533187a
    #define DWC3_REVISION_188A 0x5533188a
    #define DWC3_REVISION_190A 0x5533190a
    #define DWC3_REVISION_194A 0x5533194a
    #define DWC3_REVISION_200A 0x5533200a
    #define DWC3_REVISION_202A 0x5533202a
    #define DWC3_REVISION_210A 0x5533210a
    #define DWC3_REVISION_220A 0x5533220a
    #define DWC3_REVISION_230A 0x5533230a
    #define DWC3_REVISION_240A 0x5533240a
    #define DWC3_REVISION_250A 0x5533250a
    #define DWC3_REVISION_260A 0x5533260a
    #define DWC3_REVISION_270A 0x5533270a
    #define DWC3_REVISION_280A 0x5533280a
    #define DWC3_REVISION_290A 0x5533290a
    #define DWC3_REVISION_300A 0x5533300a
    #define DWC3_REVISION_310A 0x5533310a
    #define DWC3_REVISION_IS_DWC31 0x80000000
    #define DWC3_USB31_REVISION_110A (0x3131302a | DWC3_REVISION_IS_DWC31)
    #define DWC3_USB31_REVISION_120A (0x3132302a | DWC3_REVISION_IS_DWC31)
        enum dwc3_ep0_next ep0_next_event;
        enum dwc3_ep0_state ep0state;
        enum dwc3_link_state link_state;
        u16 u2sel;
        u16 u2pel;
        u8 u1sel;
        u8 u1pel;
        u8 speed;
        u8 num_eps;
        struct dwc3_hwparams hwparams;
        struct dentry *root;
        struct debugfs_regset32 *regset;
        u8 test_mode;
        u8 test_mode_nr;
        u8 lpm_nyet_threshold;
        u8 hird_threshold;
        const char *hsphy_interface;
        unsigned connected:1;
        unsigned delayed_status:1;
        unsigned ep0_bounced:1;
        unsigned ep0_expect_in:1;
        unsigned has_hibernation:1;
        unsigned sysdev_is_parent:1;
        unsigned has_lpm_erratum:1;
        unsigned is_utmi_l1_suspend:1;
        unsigned is_fpga:1;
        unsigned pending_events:1;
        unsigned pullups_connected:1;
        unsigned setup_packet_pending:1;
        unsigned three_stage_setup:1;
        unsigned usb3_lpm_capable:1;
        unsigned disable_scramble_quirk:1;
        unsigned u2exit_lfps_quirk:1;
        unsigned u2ss_inp3_quirk:1;
        unsigned req_p1p2p3_quirk:1;
        unsigned del_p1p2p3_quirk:1;
        unsigned del_phy_power_chg_quirk:1;
        unsigned lfps_filter_quirk:1;
        unsigned rx_detect_poll_quirk:1;
        unsigned dis_u3_susphy_quirk:1;
        unsigned dis_u2_susphy_quirk:1;
        unsigned dis_enblslpm_quirk:1;
        unsigned dis_rxdet_inp3_quirk:1;
        unsigned dis_u2_freeclk_exists_quirk:1;
        unsigned dis_del_phy_power_chg_quirk:1;
        unsigned dis_tx_ipgap_linecheck_quirk:1;
        unsigned tx_de_emphasis_quirk:1;
        unsigned tx_de_emphasis:2;
        unsigned dis_metastability_quirk:1;
        u16 imod_interval;
    }

.. _`dwc3.members`:

Members
-------

drd_work
    workqueue used for role swapping

ep0_trb
    trb which is used for the ctrl_req

bounce
    address of bounce buffer

scratchbuf
    address of scratch buffer

setup_buf
    used while precessing STD USB requests

ep0_trb_addr
    dma address of \ ``ep0_trb``\ 

bounce_addr
    dma address of \ ``bounce``\ 

scratch_addr
    dma address of scratchbuf

ep0_usb_req
    dummy req used while handling STD USB requests

ep0_in_setup
    one control transfer is completed and enter setup phase

lock
    for synchronizing

dev
    pointer to our struct device

sysdev
    pointer to the DMA-capable device

xhci
    pointer to our xHCI child

xhci_resources
    struct resources for our \ ``xhci``\  child

ev_buf
    struct dwc3_event_buffer pointer

eps
    endpoint array

gadget
    device side representation of the peripheral controller

gadget_driver
    pointer to the gadget driver

usb2_phy
    pointer to USB2 PHY

usb3_phy
    pointer to USB3 PHY

usb2_generic_phy
    pointer to USB2 PHY

usb3_generic_phy
    pointer to USB3 PHY

ulpi
    pointer to ulpi interface

regs
    base address for our registers

regs_size
    address space size

dr_mode
    requested mode of operation

current_dr_role
    current role of operation when in dual-role mode

desired_dr_role
    desired role of operation when in dual-role mode

edev
    extcon handle

edev_nb
    extcon notifier

hsphy_mode
    UTMI phy mode, one of following:
    - USBPHY_INTERFACE_MODE_UTMI
    - USBPHY_INTERFACE_MODE_UTMIW

fladj
    frame length adjustment

irq_gadget
    peripheral controller's IRQ number

nr_scratch
    number of scratch buffers

u1u2
    only used on revisions <1.83a for workaround

maximum_speed
    maximum speed requested (mainly for testing purposes)

revision
    revision register contents

ep0_next_event
    hold the next expected event

ep0state
    state of endpoint zero

link_state
    link state

u2sel
    parameter from Set SEL request.

u2pel
    parameter from Set SEL request.

u1sel
    parameter from Set SEL request.

u1pel
    parameter from Set SEL request.

speed
    device speed (super, high, full, low)

num_eps
    number of endpoints

hwparams
    copy of hwparams registers

root
    debugfs root folder pointer

regset
    debugfs pointer to regdump file

test_mode
    true when we're entering a USB test mode

test_mode_nr
    test feature selector

lpm_nyet_threshold
    LPM NYET response threshold

hird_threshold
    HIRD threshold

hsphy_interface
    "utmi" or "ulpi"

connected
    true when we're connected to a host, false otherwise

delayed_status
    true when gadget driver asks for delayed status

ep0_bounced
    true when we used bounce buffer

ep0_expect_in
    true when we expect a DATA IN transfer

has_hibernation
    true when dwc3 was configured with Hibernation

sysdev_is_parent
    true when dwc3 device has a parent driver

has_lpm_erratum
    true when core was configured with LPM Erratum. Note that
    there's now way for software to detect this in runtime.

is_utmi_l1_suspend
    the core asserts output signal
    0       - utmi_sleep_n
    1       - utmi_l1_suspend_n

is_fpga
    true when we are using the FPGA board

pending_events
    true when we have pending IRQs to be handled

pullups_connected
    true when Run/Stop bit is set

setup_packet_pending
    true when there's a Setup Packet in FIFO. Workaround

three_stage_setup
    set if we perform a three phase setup

usb3_lpm_capable
    set if hadrware supports Link Power Management

disable_scramble_quirk
    set if we enable the disable scramble quirk

u2exit_lfps_quirk
    set if we enable u2exit lfps quirk

u2ss_inp3_quirk
    set if we enable P3 OK for U2/SS Inactive quirk

req_p1p2p3_quirk
    set if we enable request p1p2p3 quirk

del_p1p2p3_quirk
    set if we enable delay p1p2p3 quirk

del_phy_power_chg_quirk
    set if we enable delay phy power change quirk

lfps_filter_quirk
    set if we enable LFPS filter quirk

rx_detect_poll_quirk
    set if we enable rx_detect to polling lfps quirk

dis_u3_susphy_quirk
    set if we disable usb3 suspend phy

dis_u2_susphy_quirk
    set if we disable usb2 suspend phy

dis_enblslpm_quirk
    set if we clear enblslpm in GUSB2PHYCFG,
    disabling the suspend signal to the PHY.

dis_rxdet_inp3_quirk
    set if we disable Rx.Detect in P3

dis_u2_freeclk_exists_quirk
    set if we clear u2_freeclk_exists
    in GUSB2PHYCFG, specify that USB2 PHY doesn't
    provide a free-running PHY clock.

dis_del_phy_power_chg_quirk
    set if we disable delay phy power
    change quirk.

dis_tx_ipgap_linecheck_quirk
    set if we disable u2mac linestate
    check during HS transmit.

tx_de_emphasis_quirk
    set if we enable Tx de-emphasis quirk

tx_de_emphasis
    Tx de-emphasis value
    0       - -6dB de-emphasis
    1       - -3.5dB de-emphasis
    2       - No de-emphasis
    3       - Reserved

dis_metastability_quirk
    set to disable metastability quirk.

imod_interval
    set the interrupt moderation interval in 250ns
    increments or 0 to disable.

.. _`dwc3_event_depevt`:

struct dwc3_event_depevt
========================

.. c:type:: struct dwc3_event_depevt

    Device Endpoint Events

.. _`dwc3_event_depevt.definition`:

Definition
----------

.. code-block:: c

    struct dwc3_event_depevt {
        u32 one_bit:1;
        u32 endpoint_number:5;
        u32 endpoint_event:4;
        u32 reserved11_10:2;
        u32 status:4;
    #define DEPEVT_STATUS_TRANSFER_ACTIVE BIT(3)
    #define DEPEVT_STATUS_BUSERR BIT(0)
    #define DEPEVT_STATUS_SHORT BIT(1)
    #define DEPEVT_STATUS_IOC BIT(2)
    #define DEPEVT_STATUS_LST BIT(3)
    #define DEPEVT_STREAMEVT_FOUND 1
    #define DEPEVT_STREAMEVT_NOTFOUND 2
    #define DEPEVT_STATUS_CONTROL_DATA 1
    #define DEPEVT_STATUS_CONTROL_STATUS 2
    #define DEPEVT_STATUS_CONTROL_PHASE(n) ((n) & 3)
    #define DEPEVT_TRANSFER_NO_RESOURCE 1
    #define DEPEVT_TRANSFER_BUS_EXPIRY 2
        u32 parameters:16;
    #define DEPEVT_PARAMETER_CMD(n) (((n) & (0xf << 8)) >> 8)
    }

.. _`dwc3_event_depevt.members`:

Members
-------

one_bit
    indicates this is an endpoint event (not used)

endpoint_number
    number of the endpoint

endpoint_event
    The event we have:
    0x00    - Reserved
    0x01    - XferComplete
    0x02    - XferInProgress
    0x03    - XferNotReady
    0x04    - RxTxFifoEvt (IN->Underrun, OUT->Overrun)
    0x05    - Reserved
    0x06    - StreamEvt
    0x07    - EPCmdCmplt

reserved11_10
    Reserved, don't use.

status
    Indicates the status of the event. Refer to databook for
    more information.

parameters
    Parameters of the current event. Refer to databook for
    more information.

.. _`dwc3_event_devt`:

struct dwc3_event_devt
======================

.. c:type:: struct dwc3_event_devt

    Device Events

.. _`dwc3_event_devt.definition`:

Definition
----------

.. code-block:: c

    struct dwc3_event_devt {
        u32 one_bit:1;
        u32 device_event:7;
        u32 type:4;
        u32 reserved15_12:4;
        u32 event_info:9;
        u32 reserved31_25:7;
    }

.. _`dwc3_event_devt.members`:

Members
-------

one_bit
    indicates this is a non-endpoint event (not used)

device_event
    indicates it's a device event. Should read as 0x00

type
    indicates the type of device event.
    0       - DisconnEvt
    1       - USBRst
    2       - ConnectDone
    3       - ULStChng
    4       - WkUpEvt
    5       - Reserved
    6       - EOPF
    7       - SOF
    8       - Reserved
    9       - ErrticErr
    10      - CmdCmplt
    11      - EvntOverflow
    12      - VndrDevTstRcved

reserved15_12
    Reserved, not used

event_info
    Information about this event

reserved31_25
    Reserved, not used

.. _`dwc3_event_gevt`:

struct dwc3_event_gevt
======================

.. c:type:: struct dwc3_event_gevt

    Other Core Events

.. _`dwc3_event_gevt.definition`:

Definition
----------

.. code-block:: c

    struct dwc3_event_gevt {
        u32 one_bit:1;
        u32 device_event:7;
        u32 phy_port_number:4;
        u32 reserved31_12:20;
    }

.. _`dwc3_event_gevt.members`:

Members
-------

one_bit
    indicates this is a non-endpoint event (not used)

device_event
    indicates it's (0x03) Carkit or (0x04) I2C event.

phy_port_number
    self-explanatory

reserved31_12
    Reserved, not used.

.. _`dwc3_event`:

union dwc3_event
================

.. c:type:: struct dwc3_event

    representation of Event Buffer contents

.. _`dwc3_event.definition`:

Definition
----------

.. code-block:: c

    union dwc3_event {
        u32 raw;
        struct dwc3_event_type type;
        struct dwc3_event_depevt depevt;
        struct dwc3_event_devt devt;
        struct dwc3_event_gevt gevt;
    }

.. _`dwc3_event.members`:

Members
-------

raw
    raw 32-bit event

type
    the type of the event

depevt
    Device Endpoint Event

devt
    Device Event

gevt
    Global Event

.. _`dwc3_gadget_ep_cmd_params`:

struct dwc3_gadget_ep_cmd_params
================================

.. c:type:: struct dwc3_gadget_ep_cmd_params

    representation of endpoint command parameters

.. _`dwc3_gadget_ep_cmd_params.definition`:

Definition
----------

.. code-block:: c

    struct dwc3_gadget_ep_cmd_params {
        u32 param2;
        u32 param1;
        u32 param0;
    }

.. _`dwc3_gadget_ep_cmd_params.members`:

Members
-------

param2
    third parameter

param1
    second parameter

param0
    first parameter

.. This file was automatic generated / don't edit.

