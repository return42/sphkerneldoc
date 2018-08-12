.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wil6210/txrx.c

.. _`wil_vring_alloc_skb`:

wil_vring_alloc_skb
===================

.. c:function:: int wil_vring_alloc_skb(struct wil6210_priv *wil, struct vring *vring, u32 i, int headroom)

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param struct vring \*vring:
        *undescribed*

    :param u32 i:
        *undescribed*

    :param int headroom:
        *undescribed*

.. _`wil_vring_alloc_skb.description`:

Description
-----------

Safe to call from IRQ

.. _`wil_rx_add_radiotap_header`:

wil_rx_add_radiotap_header
==========================

.. c:function:: void wil_rx_add_radiotap_header(struct wil6210_priv *wil, struct sk_buff *skb)

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`wil_rx_add_radiotap_header.description`:

Description
-----------

Any error indicated as "Bad FCS"

Vendor data for 04:ce:14-1 (Wilocity-1) consists of:
- Rx descriptor: 32 bytes
- Phy info

.. _`wil_vring_reap_rx`:

wil_vring_reap_rx
=================

.. c:function:: struct sk_buff *wil_vring_reap_rx(struct wil6210_priv *wil, struct vring *vring)

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param struct vring \*vring:
        *undescribed*

.. _`wil_vring_reap_rx.description`:

Description
-----------

Rx descriptor copied to skb->cb

Safe to call from IRQ

.. _`wil_rx_refill`:

wil_rx_refill
=============

.. c:function:: int wil_rx_refill(struct wil6210_priv *wil, int count)

    buffers posted at \ ``swtail``\ 

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param int count:
        *undescribed*

.. _`wil_rx_refill.note`:

Note
----

we have a single RX queue for servicing all VIFs, but we
allocate skbs with headroom according to main interface only. This
means it will not work with monitor interface together with other VIFs.
Currently we only support monitor interface on its own without other VIFs,
and we will need to fix this code once we add support.

.. _`reverse_memcmp`:

reverse_memcmp
==============

.. c:function:: int reverse_memcmp(const void *cs, const void *ct, size_t count)

    Compare two areas of memory, in reverse order

    :param const void \*cs:
        One area of memory

    :param const void \*ct:
        Another area of memory

    :param size_t count:
        The size of the area.

.. _`reverse_memcmp.description`:

Description
-----------

Cut'n'paste from original memcmp (see lib/string.c)
with minimal modifications

.. _`wil_rx_handle`:

wil_rx_handle
=============

.. c:function:: void wil_rx_handle(struct wil6210_priv *wil, int *quota)

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param int \*quota:
        *undescribed*

.. _`wil_rx_handle.description`:

Description
-----------

Safe to call from NAPI poll, i.e. softirq with interrupts enabled

.. _`wil_tx_desc_offload_setup_tso`:

wil_tx_desc_offload_setup_tso
=============================

.. c:function:: void wil_tx_desc_offload_setup_tso(struct vring_tx_desc *d, struct sk_buff *skb, int tso_desc_type, bool is_ipv4, int tcp_hdr_len, int skb_net_hdr_len)

    \ ``skb``\  is used to obtain the protocol and headers length.

    :param struct vring_tx_desc \*d:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

    :param int tso_desc_type:
        0 - a header, 1 - first data,
        2 - middle, 3 - last descriptor.

    :param bool is_ipv4:
        *undescribed*

    :param int tcp_hdr_len:
        *undescribed*

    :param int skb_net_hdr_len:
        *undescribed*

.. _`wil_tx_desc_offload_setup`:

wil_tx_desc_offload_setup
=========================

.. c:function:: int wil_tx_desc_offload_setup(struct vring_tx_desc *d, struct sk_buff *skb)

    \ ``skb``\  is used to obtain the protocol and headers length.

    :param struct vring_tx_desc \*d:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`wil_tx_desc_offload_setup.returns-the-protocol`:

Returns the protocol
--------------------

0 - not TCP, 1 - TCPv4, 2 - TCPv6.
Note, if d==NULL, the function only returns the protocol result.

It is very similar to previous wil_tx_desc_offload_setup_tso. This
is "if unrolling" to optimize the critical path.

.. _`__wil_update_net_queues`:

\__wil_update_net_queues
========================

.. c:function:: void __wil_update_net_queues(struct wil6210_priv *wil, struct wil6210_vif *vif, struct vring *vring, bool check_stop)

    It will start/stop net queues of a specific VIF net_device.

    :param struct wil6210_priv \*wil:
        *undescribed*

    :param struct wil6210_vif \*vif:
        *undescribed*

    :param struct vring \*vring:
        *undescribed*

    :param bool check_stop:
        *undescribed*

.. _`__wil_update_net_queues.this-function-does-one-of-two-checks`:

This function does one of two checks
------------------------------------

In case check_stop is true, will check if net queues need to be stopped. If
the conditions for stopping are met, \ :c:func:`netif_tx_stop_all_queues`\  is called.
In case check_stop is false, will check if net queues need to be waked. If
the conditions for waking are met, \ :c:func:`netif_tx_wake_all_queues`\  is called.
vring is the vring which is currently being modified by either adding
descriptors (tx) into it or removing descriptors (tx complete) from it. Can
be null when irrelevant (e.g. connect/disconnect events).

The implementation is to stop net queues if modified vring has low
descriptor availability. Wake if all vrings are not in low descriptor
availability and modified vring has high descriptor availability.

.. _`wil_tx_complete`:

wil_tx_complete
===============

.. c:function:: int wil_tx_complete(struct wil6210_vif *vif, int ringid)

    :param struct wil6210_vif \*vif:
        *undescribed*

    :param int ringid:
        *undescribed*

.. _`wil_tx_complete.description`:

Description
-----------

Return number of descriptors cleared

Safe to call from IRQ

.. This file was automatic generated / don't edit.

