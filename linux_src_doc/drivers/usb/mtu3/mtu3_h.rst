.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/mtu3/mtu3.h

.. _`mtu3_ep_fifo_unit`:

MTU3_EP_FIFO_UNIT
=================

.. c:function::  MTU3_EP_FIFO_UNIT()

    devide fifo into some 512B parts, use bitmap to manage it; And 128 bits size of bitmap is large enough, that means it can manage up to 64KB fifo size.

.. _`mtu3_ep_fifo_unit.note`:

NOTE
----

MTU3_EP_FIFO_UNIT should be power of two

.. _`ep0_response_buf`:

EP0_RESPONSE_BUF
================

.. c:function::  EP0_RESPONSE_BUF()

    the SET_SEL request uses 6 so far, and GET_STATUS is 2

.. _`mtu3`:

struct mtu3
===========

.. c:type:: struct mtu3

    device driver instance data.

.. _`mtu3.definition`:

Definition
----------

.. code-block:: c

    struct mtu3 {
        spinlock_t lock;
        struct ssusb_mtk *ssusb;
        struct device *dev;
        void __iomem *mac_base;
        void __iomem *ippc_base;
        int irq;
        struct mtu3_fifo_info tx_fifo;
        struct mtu3_fifo_info rx_fifo;
        struct mtu3_ep *ep_array;
        struct mtu3_ep *in_eps;
        struct mtu3_ep *out_eps;
        struct mtu3_ep *ep0;
        int num_eps;
        int slot;
        int active_ep;
        struct dma_pool *qmu_gpd_pool;
        enum mtu3_g_ep0_state ep0_state;
        struct usb_gadget g;
        struct usb_gadget_driver *gadget_driver;
        struct mtu3_request ep0_req;
        u8 setup_buf;
        u32 max_speed;
        unsigned is_active:1;
        unsigned may_wakeup:1;
        unsigned is_self_powered:1;
        unsigned test_mode:1;
        unsigned softconnect:1;
        unsigned u1_enable:1;
        unsigned u2_enable:1;
        unsigned is_u3_ip:1;
        u8 address;
        u8 test_mode_nr;
        u32 hw_version;
    }

.. _`mtu3.members`:

Members
-------

lock
    *undescribed*

ssusb
    *undescribed*

dev
    *undescribed*

mac_base
    *undescribed*

ippc_base
    *undescribed*

irq
    *undescribed*

tx_fifo
    *undescribed*

rx_fifo
    *undescribed*

ep_array
    *undescribed*

in_eps
    *undescribed*

out_eps
    *undescribed*

ep0
    *undescribed*

num_eps
    *undescribed*

slot
    MTU3_U2_IP_SLOT_DEFAULT for U2 IP only,
    MTU3_U3_IP_SLOT_DEFAULT for U3 IP

active_ep
    *undescribed*

qmu_gpd_pool
    *undescribed*

ep0_state
    *undescribed*

g
    *undescribed*

gadget_driver
    *undescribed*

ep0_req
    dummy request used while handling standard USB requests
    for GET_STATUS and SET_SEL

setup_buf
    ep0 response buffer for GET_STATUS and SET_SEL requests

max_speed
    *undescribed*

is_active
    *undescribed*

may_wakeup
    means device's remote wakeup is enabled

is_self_powered
    is reported in device status and the config descriptor

test_mode
    *undescribed*

softconnect
    *undescribed*

u1_enable
    *undescribed*

u2_enable
    *undescribed*

is_u3_ip
    *undescribed*

address
    *undescribed*

test_mode_nr
    *undescribed*

hw_version
    *undescribed*

.. This file was automatic generated / don't edit.

