.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wil6210/txrx_edma.c

.. _`wil_ring_alloc_skb_edma`:

wil_ring_alloc_skb_edma
=======================

.. c:function:: int wil_ring_alloc_skb_edma(struct wil6210_priv *wil, struct wil_ring *ring, u32 i)

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param ring:
        *undescribed*
    :type ring: struct wil_ring \*

    :param i:
        *undescribed*
    :type i: u32

.. _`wil_tx_sring_handler`:

wil_tx_sring_handler
====================

.. c:function:: int wil_tx_sring_handler(struct wil6210_priv *wil, struct wil_status_ring *sring)

    Return number of descriptors cleared.

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param sring:
        *undescribed*
    :type sring: struct wil_status_ring \*

.. _`wil_tx_desc_offload_setup_tso_edma`:

wil_tx_desc_offload_setup_tso_edma
==================================

.. c:function:: void wil_tx_desc_offload_setup_tso_edma(struct wil_tx_enhanced_desc *d, int tso_desc_type, bool is_ipv4, int tcp_hdr_len, int skb_net_hdr_len, int mss)

    \ ``skb``\  is used to obtain the protocol and headers length.

    :param d:
        *undescribed*
    :type d: struct wil_tx_enhanced_desc \*

    :param tso_desc_type:
        0 - a header, 1 - first data,
        2 - middle, 3 - last descriptor.
    :type tso_desc_type: int

    :param is_ipv4:
        *undescribed*
    :type is_ipv4: bool

    :param tcp_hdr_len:
        *undescribed*
    :type tcp_hdr_len: int

    :param skb_net_hdr_len:
        *undescribed*
    :type skb_net_hdr_len: int

    :param mss:
        *undescribed*
    :type mss: int

.. This file was automatic generated / don't edit.

