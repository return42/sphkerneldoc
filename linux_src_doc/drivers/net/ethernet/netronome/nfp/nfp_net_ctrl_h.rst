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

    \ ``NFP_NET_LSO_MAX_HDR_SZ``\ :     Maximum header size supported for LSO frames \ ``NFP_NET_LSO_MAX_SEGS``\ :       Maximum number of segments LSO frame can produce

.. _`nfp_net_meta_field_size`:

NFP_NET_META_FIELD_SIZE
=======================

.. c:function::  NFP_NET_META_FIELD_SIZE()

.. _`nfp_net_rss_none`:

NFP_NET_RSS_NONE
================

.. c:function::  NFP_NET_RSS_NONE()

    pended when a RSS hash was computed

.. _`nfp_net_txr_max`:

NFP_NET_TXR_MAX
===============

.. c:function::  NFP_NET_TXR_MAX()

    \ ``NFP_NET_TXR_MAX``\ :         Maximum number of TX rings \ ``NFP_NET_RXR_MAX``\ :         Maximum number of RX rings

.. _`nfp_net_cfg_ctrl`:

NFP_NET_CFG_CTRL
================

.. c:function::  NFP_NET_CFG_CTRL()

    0x002c) \ ``NFP_NET_CFG_CTRL``\ :        Global control \ ``NFP_NET_CFG_UPDATE``\ :      Indicate which fields are updated \ ``NFP_NET_CFG_TXRS_ENABLE``\ : Bitmask of enabled TX rings \ ``NFP_NET_CFG_RXRS_ENABLE``\ : Bitmask of enabled RX rings \ ``NFP_NET_CFG_MTU``\ :         Set MTU size \ ``NFP_NET_CFG_FLBUFSZ``\ :     Set freelist buffer size (must be larger than MTU) \ ``NFP_NET_CFG_EXN``\ :         MSI-X table entry for exceptions \ ``NFP_NET_CFG_LSC``\ :         MSI-X table entry for link state changes \ ``NFP_NET_CFG_MACADDR``\ :     MAC address

.. _`nfp_net_cfg_ctrl.todo`:

TODO
----

- define Error details in UPDATE

.. _`nfp_net_cfg_version`:

NFP_NET_CFG_VERSION
===================

.. c:function::  NFP_NET_CFG_VERSION()

    only words (0x0030 - 0x0050): \ ``NFP_NET_CFG_VERSION``\ :     Firmware version number \ ``NFP_NET_CFG_STS``\ :         Status \ ``NFP_NET_CFG_CAP``\ :         Capabilities (same bits as \ ``NFP_NET_CFG_CTRL``\ ) \ ``NFP_NET_CFG_MAX_TXRINGS``\ : Maximum number of TX rings \ ``NFP_NET_CFG_MAX_RXRINGS``\ : Maximum number of RX rings \ ``NFP_NET_CFG_MAX_MTU``\ :     Maximum support MTU \ ``NFP_NET_CFG_START_TXQ``\ :   Start Queue Control Queue to use for TX (PF only) \ ``NFP_NET_CFG_START_RXQ``\ :   Start Queue Control Queue to use for RX (PF only)

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

    \ ``NFP_NET_CFG_RSS_CAP_HFUNC``\ :  supported hash functions (same bits as \ ``NFP_NET_CFG_RSS_HFUNC``\ )

.. _`nfp_net_cfg_tlv_base`:

NFP_NET_CFG_TLV_BASE
====================

.. c:function::  NFP_NET_CFG_TLV_BASE()

    \ ``NFP_NET_CFG_TLV_BASE``\ :       start anchor of the TLV area

.. _`nfp_net_cfg_vxlan_port`:

NFP_NET_CFG_VXLAN_PORT
======================

.. c:function::  NFP_NET_CFG_VXLAN_PORT()

    \ ``NFP_NET_CFG_VXLAN_PORT``\ :     Base address of table of tunnels' UDP dst ports \ ``NFP_NET_CFG_VXLAN_SZ``\ :       Size of the UDP port table in bytes

.. _`nfp_net_cfg_bpf_abi`:

NFP_NET_CFG_BPF_ABI
===================

.. c:function::  NFP_NET_CFG_BPF_ABI()

    \ ``NFP_NET_CFG_BPF_ABI``\ :        BPF ABI version \ ``NFP_NET_CFG_BPF_CAP``\ :        BPF capabilities \ ``NFP_NET_CFG_BPF_MAX_LEN``\ :    Maximum size of JITed BPF code in bytes \ ``NFP_NET_CFG_BPF_START``\ :      Offset at which BPF will be loaded \ ``NFP_NET_CFG_BPF_DONE``\ :       Offset to jump to on exit \ ``NFP_NET_CFG_BPF_STACK_SZ``\ :   Total size of stack area in 64B chunks \ ``NFP_NET_CFG_BPF_INL_MTU``\ :    Packet data split offset in 64B chunks \ ``NFP_NET_CFG_BPF_SIZE``\ :       Size of the JITed BPF code in instructions \ ``NFP_NET_CFG_BPF_ADDR``\ :       DMA address of the buffer with JITed BPF code

.. _`nfp_net_cfg_reserved`:

NFP_NET_CFG_RESERVED
====================

.. c:function::  NFP_NET_CFG_RESERVED()

    0x00c0)

.. _`nfp_net_cfg_rss_base`:

NFP_NET_CFG_RSS_BASE
====================

.. c:function::  NFP_NET_CFG_RSS_BASE()

    0x01ac): Used only when NFP_NET_CFG_CTRL_RSS is enabled \ ``NFP_NET_CFG_RSS_CFG``\ :     RSS configuration word \ ``NFP_NET_CFG_RSS_KEY``\ :     RSS "secret" key \ ``NFP_NET_CFG_RSS_ITBL``\ :    RSS indirection table

.. _`nfp_net_cfg_txr_base`:

NFP_NET_CFG_TXR_BASE
====================

.. c:function::  NFP_NET_CFG_TXR_BASE()

    0x800) \ ``NFP_NET_CFG_TXR_BASE``\ :    Base offset for TX ring configuration \ ``NFP_NET_CFG_TXR_ADDR``\ :    Per TX ring DMA address (8B entries) \ ``NFP_NET_CFG_TXR_WB_ADDR``\ : Per TX ring write back DMA address (8B entries) \ ``NFP_NET_CFG_TXR_SZ``\ :      Per TX ring ring size (1B entries) \ ``NFP_NET_CFG_TXR_VEC``\ :     Per TX ring MSI-X table entry (1B entries) \ ``NFP_NET_CFG_TXR_PRIO``\ :    Per TX ring priority (1B entries) \ ``NFP_NET_CFG_TXR_IRQ_MOD``\ : Per TX ring interrupt moderation packet

.. _`nfp_net_cfg_rxr_base`:

NFP_NET_CFG_RXR_BASE
====================

.. c:function::  NFP_NET_CFG_RXR_BASE()

    0x0c00) \ ``NFP_NET_CFG_RXR_BASE``\ :    Base offset for RX ring configuration \ ``NFP_NET_CFG_RXR_ADDR``\ :    Per RX ring DMA address (8B entries) \ ``NFP_NET_CFG_RXR_SZ``\ :      Per RX ring ring size (1B entries) \ ``NFP_NET_CFG_RXR_VEC``\ :     Per RX ring MSI-X table entry (1B entries) \ ``NFP_NET_CFG_RXR_PRIO``\ :    Per RX ring priority (1B entries) \ ``NFP_NET_CFG_RXR_IRQ_MOD``\ : Per RX ring interrupt moderation (4B entries)

.. _`nfp_net_cfg_icr_base`:

NFP_NET_CFG_ICR_BASE
====================

.. c:function::  NFP_NET_CFG_ICR_BASE()

    0x0d00) These registers are only used when MSI-X auto-masking is not enabled (%NFP_NET_CFG_CTRL_MSIXAUTO not set).  The array is index by MSI-X entry and are 1B in size.  If an entry is zero, the corresponding entry is enabled.  If the FW generates an interrupt, it writes a cause into the corresponding field.  This also masks the MSI-X entry and the host driver must clear the register to re-enable the interrupt.

.. _`nfp_net_cfg_stats_base`:

NFP_NET_CFG_STATS_BASE
======================

.. c:function::  NFP_NET_CFG_STATS_BASE()

    0x0d90) all counters are 64bit.

.. _`nfp_net_cfg_txr_stats_base`:

NFP_NET_CFG_TXR_STATS_BASE
==========================

.. c:function::  NFP_NET_CFG_TXR_STATS_BASE()

    0x1800) options, 64bit per entry \ ``NFP_NET_CFG_TXR_STATS``\ :   TX ring statistics (Packet and Byte count) \ ``NFP_NET_CFG_RXR_STATS``\ :   RX ring statistics (Packet and Byte count)

.. _`nfp_net_cfg_mbox_base`:

NFP_NET_CFG_MBOX_BASE
=====================

.. c:function::  NFP_NET_CFG_MBOX_BASE()

    0x19ff) 4B used for update command and 4B return code followed by a max of 504B of variable length value

.. _`nfp_net_cfg_vlan_filter`:

NFP_NET_CFG_VLAN_FILTER
=======================

.. c:function::  NFP_NET_CFG_VLAN_FILTER()

    \ ``NFP_NET_CFG_VLAN_FILTER``\ :            Base address of VLAN filter mailbox \ ``NFP_NET_CFG_VLAN_FILTER_VID``\ :        VLAN ID to filter \ ``NFP_NET_CFG_VLAN_FILTER_PROTO``\ :      VLAN proto to filter \ ``NFP_NET_CFG_VXLAN_SZ``\ :               Size of the VLAN filter mailbox in bytes

.. _`nfp_net_cfg_tlv_type`:

NFP_NET_CFG_TLV_TYPE
====================

.. c:function::  NFP_NET_CFG_TLV_TYPE()

    \ ``NFP_NET_CFG_TLV_TYPE``\ :       Offset of type within the TLV \ ``NFP_NET_CFG_TLV_TYPE_REQUIRED``\ : Driver must be able to parse the TLV \ ``NFP_NET_CFG_TLV_LENGTH``\ :     Offset of length within the TLV \ ``NFP_NET_CFG_TLV_LENGTH_INC``\ : TLV length increments \ ``NFP_NET_CFG_TLV_VALUE``\ :      Offset of value with the TLV

.. _`nfp_net_cfg_tlv_type.description`:

Description
-----------

List of simple TLV structures, first one starts at \ ``NFP_NET_CFG_TLV_BASE``\ .
Last structure must be of type \ ``NFP_NET_CFG_TLV_TYPE_END``\ .  Presence of TLVs
is indicated by \ ``NFP_NET_CFG_TLV_BASE``\  being non-zero.  TLV structures may
fill the entire remainder of the BAR or be shorter.  FW must make sure TLVs
don't conflict with other features which allocate space beyond
\ ``NFP_NET_CFG_TLV_BASE``\ .  \ ``NFP_NET_CFG_TLV_TYPE_RESERVED``\  should be used to wrap
space used by such features.
Note that the 4 byte TLV header is not counted in \ ``NFP_NET_CFG_TLV_LENGTH``\ .

.. _`nfp_net_cfg_tlv_type_unknown`:

NFP_NET_CFG_TLV_TYPE_UNKNOWN
============================

.. c:function::  NFP_NET_CFG_TLV_TYPE_UNKNOWN()

.. _`nfp_net_cfg_tlv_type_unknown.description`:

Description
-----------

\ ``NFP_NET_CFG_TLV_TYPE_UNKNOWN``\ :
Special TLV type to catch bugs, should never be encountered.  Drivers should
treat encountering this type as error and refuse to probe.

\ ``NFP_NET_CFG_TLV_TYPE_RESERVED``\ :
Reserved space, may contain legacy fixed-offset fields, or be used for
padding.  The use of this type should be otherwise avoided.

\ ``NFP_NET_CFG_TLV_TYPE_END``\ :
Empty, end of TLV list.  Must be the last TLV.  Drivers will stop processing
further TLVs when encountered.

\ ``NFP_NET_CFG_TLV_TYPE_ME_FREQ``\ :
Single word, ME frequency in MHz as used in calculation for
\ ``NFP_NET_CFG_RXR_IRQ_MOD``\  and \ ``NFP_NET_CFG_TXR_IRQ_MOD``\ .

\ ``NFP_NET_CFG_TLV_TYPE_MBOX``\ :
Variable, mailbox area.  Overwrites the default location which is
\ ``NFP_NET_CFG_MBOX_BASE``\  and length \ ``NFP_NET_CFG_MBOX_VAL_MAX_SZ``\ .

\ ``NFP_NET_CFG_TLV_TYPE_EXPERIMENTAL0``\ :
\ ``NFP_NET_CFG_TLV_TYPE_EXPERIMENTAL1``\ :
Variable, experimental IDs.  IDs designated for internal development and
experiments before a stable TLV ID has been allocated to a feature.  Should
never be present in production firmware.

.. _`nfp_net_tlv_caps`:

struct nfp_net_tlv_caps
=======================

.. c:type:: struct nfp_net_tlv_caps

    parsed control BAR TLV capabilities

.. _`nfp_net_tlv_caps.definition`:

Definition
----------

.. code-block:: c

    struct nfp_net_tlv_caps {
        u32 me_freq_mhz;
        unsigned int mbox_off;
        unsigned int mbox_len;
    }

.. _`nfp_net_tlv_caps.members`:

Members
-------

me_freq_mhz
    ME clock_freq (MHz)

mbox_off
    vNIC mailbox area offset

mbox_len
    vNIC mailbox area length

.. This file was automatic generated / don't edit.

