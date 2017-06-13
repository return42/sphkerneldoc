.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_net_ctrl.h

.. _`nfp_net_cfg_bar_sz`:

NFP_NET_CFG_BAR_SZ
==================

.. c:function::  NFP_NET_CFG_BAR_SZ()

.. _`nfp_net_cfg_bar_sz.description`:

Description
-----------

The configuration BAR is 8K in size, but due to
THB-350, 32k needs to be reserved.

.. _`nfp_net_rx_offset`:

NFP_NET_RX_OFFSET
=================

.. c:function::  NFP_NET_RX_OFFSET()

.. _`nfp_net_lso_max_hdr_sz`:

NFP_NET_LSO_MAX_HDR_SZ
======================

.. c:function::  NFP_NET_LSO_MAX_HDR_SZ()

.. _`nfp_net_meta_field_size`:

NFP_NET_META_FIELD_SIZE
=======================

.. c:function::  NFP_NET_META_FIELD_SIZE()

.. _`nfp_net_rss_none`:

NFP_NET_RSS_NONE
================

.. c:function::  NFP_NET_RSS_NONE()

    pended when a RSS hash was computed

.. _`nfp_net_cfg_ctrl`:

NFP_NET_CFG_CTRL
================

.. c:function::  NFP_NET_CFG_CTRL()

    0x002c)

.. _`nfp_net_cfg_ctrl.todo`:

TODO
----

- define Error details in UPDATE

.. _`nfp_net_cfg_version`:

NFP_NET_CFG_VERSION
===================

.. c:function::  NFP_NET_CFG_VERSION()

    only words (0x0030 - 0x0050):

.. _`nfp_net_cfg_version.todo`:

TODO
----

- define more STS bits

.. _`nfp_net_cfg_rx_offset`:

NFP_NET_CFG_RX_OFFSET
=====================

.. c:function::  NFP_NET_CFG_RX_OFFSET()

.. _`nfp_net_cfg_rss_cap`:

NFP_NET_CFG_RSS_CAP
===================

.. c:function::  NFP_NET_CFG_RSS_CAP()

.. _`nfp_net_cfg_vxlan_port`:

NFP_NET_CFG_VXLAN_PORT
======================

.. c:function::  NFP_NET_CFG_VXLAN_PORT()

.. _`nfp_net_cfg_bpf_abi`:

NFP_NET_CFG_BPF_ABI
===================

.. c:function::  NFP_NET_CFG_BPF_ABI()

.. _`nfp_net_cfg_reserved`:

NFP_NET_CFG_RESERVED
====================

.. c:function::  NFP_NET_CFG_RESERVED()

    0x00c0)

.. _`nfp_net_cfg_rss_base`:

NFP_NET_CFG_RSS_BASE
====================

.. c:function::  NFP_NET_CFG_RSS_BASE()

    0x01ac): Used only when NFP_NET_CFG_CTRL_RSS is enabled

.. _`nfp_net_cfg_txr_base`:

NFP_NET_CFG_TXR_BASE
====================

.. c:function::  NFP_NET_CFG_TXR_BASE()

    0x800)

.. _`nfp_net_cfg_rxr_base`:

NFP_NET_CFG_RXR_BASE
====================

.. c:function::  NFP_NET_CFG_RXR_BASE()

    0x0c00)

.. _`nfp_net_cfg_icr_base`:

NFP_NET_CFG_ICR_BASE
====================

.. c:function::  NFP_NET_CFG_ICR_BASE()

    0x0d00) These registers are only used when MSI-X auto-masking is not enabled (@NFP_NET_CFG_CTRL_MSIXAUTO not set).  The array is index by MSI-X entry and are 1B in size.  If an entry is zero, the corresponding entry is enabled.  If the FW generates an interrupt, it writes a cause into the corresponding field.  This also masks the MSI-X entry and the host driver must clear the register to re-enable the interrupt.

.. _`nfp_net_cfg_stats_base`:

NFP_NET_CFG_STATS_BASE
======================

.. c:function::  NFP_NET_CFG_STATS_BASE()

    0x0d90) all counters are 64bit.

.. _`nfp_net_cfg_txr_stats_base`:

NFP_NET_CFG_TXR_STATS_BASE
==========================

.. c:function::  NFP_NET_CFG_TXR_STATS_BASE()

    0x1800) options, 64bit per entry

.. This file was automatic generated / don't edit.

