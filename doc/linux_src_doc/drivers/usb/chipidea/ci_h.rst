.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/chipidea/ci.h

.. _`ci_hw_ep`:

struct ci_hw_ep
===============

.. c:type:: struct ci_hw_ep

    endpoint representation

.. _`ci_hw_ep.definition`:

Definition
----------

.. code-block:: c

    struct ci_hw_ep {
        struct usb_ep ep;
        u8 dir;
        u8 num;
        u8 type;
        char name[16];
        struct qh;
        int wedge;
        struct ci_hdrc *ci;
        spinlock_t *lock;
        struct dma_pool *td_pool;
        struct td_node *pending_td;
    }

.. _`ci_hw_ep.members`:

Members
-------

ep
    endpoint structure for gadget drivers

dir
    endpoint direction (TX/RX)

num
    endpoint number

type
    endpoint type

name
    string description of the endpoint

qh
    queue head for this endpoint

wedge
    is the endpoint wedged

ci
    pointer to the controller

lock
    pointer to controller's spinlock

td_pool
    pointer to controller's TD pool

pending_td
    *undescribed*

.. _`ci_role_driver`:

struct ci_role_driver
=====================

.. c:type:: struct ci_role_driver

    host/gadget role driver

.. _`ci_role_driver.definition`:

Definition
----------

.. code-block:: c

    struct ci_role_driver {
        int (*start)(struct ci_hdrc *);
        void (*stop)(struct ci_hdrc *);
        irqreturn_t (*irq)(struct ci_hdrc *);
        const char *name;
    }

.. _`ci_role_driver.members`:

Members
-------

start
    start this role

stop
    stop this role

irq
    irq handler for this role

name
    role name string (host/gadget)

.. _`hw_bank`:

struct hw_bank
==============

.. c:type:: struct hw_bank

    hardware register mapping representation

.. _`hw_bank.definition`:

Definition
----------

.. code-block:: c

    struct hw_bank {
        unsigned lpm;
        resource_size_t phys;
        void __iomem *abs;
        void __iomem *cap;
        void __iomem *op;
        size_t size;
        void __iomem  *regmap[OP_LAST + 1];
    }

.. _`hw_bank.members`:

Members
-------

lpm
    set if the device is LPM capable

phys
    physical address of the controller's registers

abs
    absolute address of the beginning of register window

cap
    capability registers

op
    operational registers

size
    size of the register window

regmap
    register lookup table

.. _`ci_hdrc`:

struct ci_hdrc
==============

.. c:type:: struct ci_hdrc

    chipidea device representation

.. _`ci_hdrc.definition`:

Definition
----------

.. code-block:: c

    struct ci_hdrc {
        struct device *dev;
        spinlock_t lock;
        struct hw_bank hw_bank;
        int irq;
        struct ci_role_driver  *roles[CI_ROLE_END];
        enum ci_role role;
        bool is_otg;
        struct usb_otg otg;
        struct otg_fsm fsm;
        struct hrtimer otg_fsm_hrtimer;
        ktime_t hr_timeouts[NUM_OTG_FSM_TIMERS];
        unsigned enabled_otg_timer_bits;
        enum otg_fsm_timer next_otg_timer;
        struct work_struct work;
        struct workqueue_struct *wq;
        struct dma_pool *qh_pool;
        struct dma_pool *td_pool;
        struct usb_gadget gadget;
        struct usb_gadget_driver *driver;
        unsigned hw_ep_max;
        struct ci_hw_ep ci_hw_ep[ENDPT_MAX];
        u32 ep0_dir;
        struct ci_hw_ep *ep0out;
        struct ci_hw_ep * *ep0in;
        struct usb_request *status;
        bool setaddr;
        u8 address;
        u8 remote_wakeup;
        u8 suspended;
        u8 test_mode;
        struct ci_hdrc_platform_data *platdata;
        int vbus_active;
        struct phy *phy;
        struct usb_phy *usb_phy;
        struct usb_hcd *hcd;
        struct dentry *debugfs;
        bool id_event;
        bool b_sess_valid_event;
        bool imx28_write_fix;
        bool supports_runtime_pm;
        bool in_lpm;
        bool wakeup_int;
        enum ci_revision rev;
    }

.. _`ci_hdrc.members`:

Members
-------

dev
    pointer to parent device

lock
    access synchronization

hw_bank
    hardware register mapping

irq
    IRQ number

roles
    array of supported roles for this controller

role
    current role

is_otg
    if the device is otg-capable

otg
    *undescribed*

fsm
    otg finite state machine

otg_fsm_hrtimer
    hrtimer for otg fsm timers

hr_timeouts
    time out list for active otg fsm timers

enabled_otg_timer_bits
    bits of enabled otg timers

next_otg_timer
    next nearest enabled timer to be expired

work
    work for role changing

wq
    workqueue thread

qh_pool
    allocation pool for queue heads

td_pool
    allocation pool for transfer descriptors

gadget
    device side representation for peripheral controller

driver
    gadget driver

hw_ep_max
    total number of endpoints supported by hardware

ci_hw_ep
    array of endpoints

ep0_dir
    ep0 direction

ep0out
    pointer to ep0 OUT endpoint

ep0in
    pointer to ep0 IN endpoint

status
    ep0 status request

setaddr
    if we should set the address on status completion

address
    usb address received from the host

remote_wakeup
    host-enabled remote wakeup

suspended
    suspended by host

test_mode
    the selected test mode

platdata
    platform specific information supplied by parent device

vbus_active
    is VBUS active

phy
    pointer to PHY, if any

usb_phy
    pointer to USB PHY, if any and if using the USB PHY framework

hcd
    pointer to usb_hcd for ehci host driver

debugfs
    root dentry for this controller in debugfs

id_event
    indicates there is an id event, and handled at ci_otg_work

b_sess_valid_event
    indicates there is a vbus event, and handled
    at ci_otg_work

imx28_write_fix
    Freescale imx28 needs swp instruction for writing

supports_runtime_pm
    if runtime pm is supported

in_lpm
    if the core in low power mode

wakeup_int
    if wakeup interrupt occur

rev
    The revision number for controller

.. _`hw_read_id_reg`:

hw_read_id_reg
==============

.. c:function:: u32 hw_read_id_reg(struct ci_hdrc *ci, u32 offset, u32 mask)

    reads from a identification register

    :param struct ci_hdrc \*ci:
        the controller

    :param u32 offset:
        offset from the beginning of identification registers region

    :param u32 mask:
        bitfield mask

.. _`hw_read_id_reg.description`:

Description
-----------

This function returns register contents

.. _`hw_write_id_reg`:

hw_write_id_reg
===============

.. c:function:: void hw_write_id_reg(struct ci_hdrc *ci, u32 offset, u32 mask, u32 data)

    writes to a identification register

    :param struct ci_hdrc \*ci:
        the controller

    :param u32 offset:
        offset from the beginning of identification registers region

    :param u32 mask:
        bitfield mask

    :param u32 data:
        new value

.. _`hw_read`:

hw_read
=======

.. c:function:: u32 hw_read(struct ci_hdrc *ci, enum ci_hw_regs reg, u32 mask)

    reads from a hw register

    :param struct ci_hdrc \*ci:
        the controller

    :param enum ci_hw_regs reg:
        register index

    :param u32 mask:
        bitfield mask

.. _`hw_read.description`:

Description
-----------

This function returns register contents

.. _`hw_write`:

hw_write
========

.. c:function:: void hw_write(struct ci_hdrc *ci, enum ci_hw_regs reg, u32 mask, u32 data)

    writes to a hw register

    :param struct ci_hdrc \*ci:
        the controller

    :param enum ci_hw_regs reg:
        register index

    :param u32 mask:
        bitfield mask

    :param u32 data:
        new value

.. _`hw_test_and_clear`:

hw_test_and_clear
=================

.. c:function:: u32 hw_test_and_clear(struct ci_hdrc *ci, enum ci_hw_regs reg, u32 mask)

    tests & clears a hw register

    :param struct ci_hdrc \*ci:
        the controller

    :param enum ci_hw_regs reg:
        register index

    :param u32 mask:
        bitfield mask

.. _`hw_test_and_clear.description`:

Description
-----------

This function returns register contents

.. _`hw_test_and_write`:

hw_test_and_write
=================

.. c:function:: u32 hw_test_and_write(struct ci_hdrc *ci, enum ci_hw_regs reg, u32 mask, u32 data)

    tests & writes a hw register

    :param struct ci_hdrc \*ci:
        the controller

    :param enum ci_hw_regs reg:
        register index

    :param u32 mask:
        bitfield mask

    :param u32 data:
        new value

.. _`hw_test_and_write.description`:

Description
-----------

This function returns register contents

.. _`ci_otg_is_fsm_mode`:

ci_otg_is_fsm_mode
==================

.. c:function:: bool ci_otg_is_fsm_mode(struct ci_hdrc *ci)

    runtime check if otg controller is in otg fsm mode.

    :param struct ci_hdrc \*ci:
        chipidea device

.. This file was automatic generated / don't edit.

