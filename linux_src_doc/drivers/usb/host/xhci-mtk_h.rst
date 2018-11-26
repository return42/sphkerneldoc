.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/xhci-mtk.h

.. _`xhci_mtk_max_esit`:

XHCI_MTK_MAX_ESIT
=================

.. c:function::  XHCI_MTK_MAX_ESIT()

    if a synchromous ep's ESIT is larger than \ ``XHCI_MTK_MAX_ESIT``\ , round down to the limit value, that means allocating more bandwidth to it.

.. _`mu3h_sch_bw_info`:

struct mu3h_sch_bw_info
=======================

.. c:type:: struct mu3h_sch_bw_info

    schedule information for bandwidth domain

.. _`mu3h_sch_bw_info.definition`:

Definition
----------

.. code-block:: c

    struct mu3h_sch_bw_info {
        u32 bus_bw[XHCI_MTK_MAX_ESIT];
        struct list_head bw_ep_list;
    }

.. _`mu3h_sch_bw_info.members`:

Members
-------

bus_bw
    array to keep track of bandwidth already used at each uframes

bw_ep_list
    eps in the bandwidth domain

.. _`mu3h_sch_bw_info.description`:

Description
-----------

treat a HS root port as a bandwidth domain, but treat a SS root port as
two bandwidth domains, one for IN eps and another for OUT eps.

.. _`mu3h_sch_ep_info`:

struct mu3h_sch_ep_info
=======================

.. c:type:: struct mu3h_sch_ep_info

    schedule information for endpoint

.. _`mu3h_sch_ep_info.definition`:

Definition
----------

.. code-block:: c

    struct mu3h_sch_ep_info {
        u32 esit;
        u32 num_budget_microframes;
        u32 bw_cost_per_microframe;
        struct list_head endpoint;
        struct list_head tt_endpoint;
        struct mu3h_sch_tt *sch_tt;
        u32 ep_type;
        u32 maxpkt;
        void *ep;
        u32 offset;
        u32 repeat;
        u32 pkts;
        u32 cs_count;
        u32 burst_mode;
        u32 bw_budget_table[0];
    }

.. _`mu3h_sch_ep_info.members`:

Members
-------

esit
    unit is 125us, equal to 2 << Interval field in ep-context

num_budget_microframes
    number of continuous uframes
    (@repeat==1) scheduled within the interval

bw_cost_per_microframe
    bandwidth cost per microframe

endpoint
    linked into bandwidth domain which it belongs to

tt_endpoint
    linked into mu3h_sch_tt's list which it belongs to

sch_tt
    mu3h_sch_tt linked into

ep_type
    endpoint type

maxpkt
    max packet size of endpoint

ep
    address of usb_host_endpoint struct

offset
    which uframe of the interval that transfer should be
    scheduled first time within the interval

repeat
    the time gap between two uframes that transfers are
    scheduled within a interval. in the simple algorithm, only
    assign 0 or 1 to it; 0 means using only one uframe in a
    interval, and 1 means using \ ``num_budget_microframes``\ 
    continuous uframes

pkts
    number of packets to be transferred in the scheduled uframes

cs_count
    number of CS that host will trigger

burst_mode
    burst mode for scheduling. 0: normal burst mode,
    distribute the bMaxBurst+1 packets for a single burst
    according to \ ``pkts``\  and \ ``repeat``\ , repeate the burst multiple
    times; 1: distribute the (bMaxBurst+1)\*(Mult+1) packets
    according to \ ``pkts``\  and \ ``repeat``\ . normal mode is used by
    default

bw_budget_table
    table to record bandwidth budget per microframe

.. _`mu3c_ippc_regs`:

struct mu3c_ippc_regs
=====================

.. c:type:: struct mu3c_ippc_regs

    MTK ssusb ip port control registers

.. _`mu3c_ippc_regs.definition`:

Definition
----------

.. code-block:: c

    struct mu3c_ippc_regs {
        __le32 ip_pw_ctr0;
        __le32 ip_pw_ctr1;
        __le32 ip_pw_ctr2;
        __le32 ip_pw_ctr3;
        __le32 ip_pw_sts1;
        __le32 ip_pw_sts2;
        __le32 reserved0[3];
        __le32 ip_xhci_cap;
        __le32 reserved1[2];
        __le64 u3_ctrl_p[MU3C_U3_PORT_MAX];
        __le64 u2_ctrl_p[MU3C_U2_PORT_MAX];
        __le32 reserved2;
        __le32 u2_phy_pll;
        __le32 reserved3[33];
    }

.. _`mu3c_ippc_regs.members`:

Members
-------

ip_pw_ctr0
    ip power and clock control registers

ip_pw_ctr1
    *undescribed*

ip_pw_ctr2
    *undescribed*

ip_pw_ctr3
    *undescribed*

ip_pw_sts1
    ip power and clock status registers

ip_pw_sts2
    *undescribed*

reserved0
    *undescribed*

ip_xhci_cap
    ip xHCI capability register

reserved1
    *undescribed*

u3_ctrl_p
    ip usb3 port x control register, only low 4bytes are used

u2_ctrl_p
    ip usb2 port x control register, only low 4bytes are used

reserved2
    *undescribed*

u2_phy_pll
    usb2 phy pll control register

reserved3
    *undescribed*

.. This file was automatic generated / don't edit.

