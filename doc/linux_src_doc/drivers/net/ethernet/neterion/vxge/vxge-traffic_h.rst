.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/neterion/vxge/vxge-traffic.h

.. _`vxge_hw_event`:

enum vxge_hw_event
==================

.. c:type:: enum vxge_hw_event

    Enumerates slow-path HW events.

.. _`vxge_hw_event.definition`:

Definition
----------

.. code-block:: c

    enum vxge_hw_event {
        VXGE_HW_EVENT_UNKNOWN,
        VXGE_HW_EVENT_RESET_START,
        VXGE_HW_EVENT_RESET_COMPLETE,
        VXGE_HW_EVENT_LINK_DOWN,
        VXGE_HW_EVENT_LINK_UP,
        VXGE_HW_EVENT_ALARM_CLEARED,
        VXGE_HW_EVENT_ECCERR,
        VXGE_HW_EVENT_MRPCIM_ECCERR,
        VXGE_HW_EVENT_FIFO_ERR,
        VXGE_HW_EVENT_VPATH_ERR,
        VXGE_HW_EVENT_CRITICAL_ERR,
        VXGE_HW_EVENT_SERR,
        VXGE_HW_EVENT_SRPCIM_SERR,
        VXGE_HW_EVENT_MRPCIM_SERR,
        VXGE_HW_EVENT_SLOT_FREEZE
    };

.. _`vxge_hw_event.constants`:

Constants
---------

VXGE_HW_EVENT_UNKNOWN
    Unknown (and invalid) event.

VXGE_HW_EVENT_RESET_START
    Privileged entity is starting device reset

VXGE_HW_EVENT_RESET_COMPLETE
    Device reset has been completed

VXGE_HW_EVENT_LINK_DOWN
    *undescribed*

VXGE_HW_EVENT_LINK_UP
    *undescribed*

VXGE_HW_EVENT_ALARM_CLEARED
    *undescribed*

VXGE_HW_EVENT_ECCERR
    vpath ECC error event.

VXGE_HW_EVENT_MRPCIM_ECCERR
    mrpcim ecc error event.

VXGE_HW_EVENT_FIFO_ERR
    FIFO Doorbell fifo error.

VXGE_HW_EVENT_VPATH_ERR
    Error local to the respective vpath

VXGE_HW_EVENT_CRITICAL_ERR
    *undescribed*

VXGE_HW_EVENT_SERR
    Serious vpath hardware error event.

VXGE_HW_EVENT_SRPCIM_SERR
    srpcim hardware error event.

VXGE_HW_EVENT_MRPCIM_SERR
    mrpcim hardware error event.

VXGE_HW_EVENT_SLOT_FREEZE
    Slot-freeze event. Driver tries to distinguish
    slot-freeze from the rest critical events (e.g. ECC) when it is
    impossible to PIO read "through" the bus, i.e. when getting all-foxes.

.. _`vxge_hw_event.description`:

Description
-----------

enum vxge_hw_event enumerates slow-path HW eventis.

.. _`vxge_hw_event.see-also`:

See also
--------

struct vxge_hw_uld_cbs{}, vxge_uld_link_up_f{},
vxge_uld_link_down_f{}.

.. _`vxge_hw_tim_intr_config`:

struct vxge_hw_tim_intr_config
==============================

.. c:type:: struct vxge_hw_tim_intr_config

    Titan Tim interrupt configuration.

.. _`vxge_hw_tim_intr_config.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_tim_intr_config {
        u32 intr_enable;
    #define VXGE_HW_TIM_INTR_ENABLE 1
    #define VXGE_HW_TIM_INTR_DISABLE 0
    #define VXGE_HW_TIM_INTR_DEFAULT 0
        u32 btimer_val;
    #define VXGE_HW_MIN_TIM_BTIMER_VAL 0
    #define VXGE_HW_MAX_TIM_BTIMER_VAL 67108864
    #define VXGE_HW_USE_FLASH_DEFAULT (~0)
        u32 timer_ac_en;
    #define VXGE_HW_TIM_TIMER_AC_ENABLE 1
    #define VXGE_HW_TIM_TIMER_AC_DISABLE 0
        u32 timer_ci_en;
    #define VXGE_HW_TIM_TIMER_CI_ENABLE 1
    #define VXGE_HW_TIM_TIMER_CI_DISABLE 0
        u32 timer_ri_en;
    #define VXGE_HW_TIM_TIMER_RI_ENABLE 1
    #define VXGE_HW_TIM_TIMER_RI_DISABLE 0
        u32 rtimer_val;
    #define VXGE_HW_MIN_TIM_RTIMER_VAL 0
    #define VXGE_HW_MAX_TIM_RTIMER_VAL 67108864
        u32 util_sel;
    #define VXGE_HW_TIM_UTIL_SEL_LEGACY_TX_NET_UTIL 17
    #define VXGE_HW_TIM_UTIL_SEL_LEGACY_RX_NET_UTIL 18
    #define VXGE_HW_TIM_UTIL_SEL_LEGACY_TX_RX_AVE_NET_UTIL 19
    #define VXGE_HW_TIM_UTIL_SEL_PER_VPATH 63
        u32 ltimer_val;
    #define VXGE_HW_MIN_TIM_LTIMER_VAL 0
    #define VXGE_HW_MAX_TIM_LTIMER_VAL 67108864
        u32 urange_a;
    #define VXGE_HW_MIN_TIM_URANGE_A 0
    #define VXGE_HW_MAX_TIM_URANGE_A 100
        u32 uec_a;
    #define VXGE_HW_MIN_TIM_UEC_A 0
    #define VXGE_HW_MAX_TIM_UEC_A 65535
        u32 urange_b;
    #define VXGE_HW_MIN_TIM_URANGE_B 0
    #define VXGE_HW_MAX_TIM_URANGE_B 100
        u32 uec_b;
    #define VXGE_HW_MIN_TIM_UEC_B 0
    #define VXGE_HW_MAX_TIM_UEC_B 65535
        u32 urange_c;
    #define VXGE_HW_MIN_TIM_URANGE_C 0
    #define VXGE_HW_MAX_TIM_URANGE_C 100
        u32 uec_c;
    #define VXGE_HW_MIN_TIM_UEC_C 0
    #define VXGE_HW_MAX_TIM_UEC_C 65535
        u32 uec_d;
    #define VXGE_HW_MIN_TIM_UEC_D 0
    #define VXGE_HW_MAX_TIM_UEC_D 65535
    }

.. _`vxge_hw_tim_intr_config.members`:

Members
-------

intr_enable
    Set to 1, if interrupt is enabled.

btimer_val
    Boundary Timer Initialization value in units of 272 ns.

timer_ac_en
    Timer Automatic Cancel. 1 : Automatic Canceling Enable: when
    asserted, other interrupt-generating entities will cancel the
    scheduled timer interrupt.

timer_ci_en
    Timer Continuous Interrupt. 1 : Continuous Interrupting Enable:
    When asserted, an interrupt will be generated every time the
    boundary timer expires, even if no traffic has been transmitted
    on this interrupt.

timer_ri_en
    Timer Consecutive (Re-) Interrupt 1 : Consecutive
    (Re-) Interrupt Enable: When asserted, an interrupt will be
    generated the next time the timer expires, even if no traffic has
    been transmitted on this interrupt. (This will only happen once
    each time that this value is written to the TIM.) This bit is
    cleared by H/W at the end of the current-timer-interval when
    the interrupt is triggered.

rtimer_val
    Restriction Timer Initialization value in units of 272 ns.

util_sel
    Utilization Selector. Selects which of the workload approximations
    to use (e.g. legacy Tx utilization, Tx/Rx utilization, host
    specified utilization etc.), selects one of
    the 17 host configured values.
    0-Virtual Path 0
    1-Virtual Path 1
    ...
    16-Virtual Path 17
    17-Legacy Tx network utilization, provided by TPA
    18-Legacy Rx network utilization, provided by FAU
    19-Average of legacy Rx and Tx utilization calculated from link
    utilization values.
    20-31-Invalid configurations
    32-Host utilization for Virtual Path 0
    33-Host utilization for Virtual Path 1
    ...
    48-Host utilization for Virtual Path 17
    49-Legacy Tx network utilization, provided by TPA
    50-Legacy Rx network utilization, provided by FAU
    51-Average of legacy Rx and Tx utilization calculated from
    link utilization values.
    52-63-Invalid configurations

ltimer_val
    Latency Timer Initialization Value in units of 272 ns.

urange_a
    Defines the upper limit (in percent) for this utilization range
    to be active. This range is considered active
    if 0 = UTIL = URNG_A
    and the UEC_A field (below) is non-zero.

uec_a
    Utilization Event Count A. If this range is active, the adapter will
    wait until UEC_A events have occurred on the interrupt before
    generating an interrupt.

urange_b
    Link utilization range B.

uec_b
    Utilization Event Count B.

urange_c
    Link utilization range C.

uec_c
    Utilization Event Count C.

uec_d
    Utilization Event Count D.
    Traffic Interrupt Controller Module interrupt configuration.

.. _`vxge_hw_xmac_aggr_stats`:

struct vxge_hw_xmac_aggr_stats
==============================

.. c:type:: struct vxge_hw_xmac_aggr_stats

    Per-Aggregator XMAC Statistics

.. _`vxge_hw_xmac_aggr_stats.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_xmac_aggr_stats {
        u64 tx_frms;
        u64 tx_data_octets;
        u64 tx_mcast_frms;
        u64 tx_bcast_frms;
        u64 tx_discarded_frms;
        u64 tx_errored_frms;
        u64 rx_frms;
        u64 rx_data_octets;
        u64 rx_mcast_frms;
        u64 rx_bcast_frms;
        u64 rx_discarded_frms;
        u64 rx_errored_frms;
        u64 rx_unknown_slow_proto_frms;
    }

.. _`vxge_hw_xmac_aggr_stats.members`:

Members
-------

tx_frms
    Count of data frames transmitted on this Aggregator on all
    its Aggregation ports. Does not include LACPDUs or Marker PDUs.
    However, does include frames discarded by the Distribution
    function.

tx_data_octets
    Count of data and padding octets of frames transmitted
    on this Aggregator on all its Aggregation ports. Does not include
    octets of LACPDUs or Marker PDUs. However, does include octets of
    frames discarded by the Distribution function.

tx_mcast_frms
    Count of data frames transmitted (to a group destination
    address other than the broadcast address) on this Aggregator on
    all its Aggregation ports. Does not include LACPDUs or Marker
    PDUs. However, does include frames discarded by the Distribution
    function.

tx_bcast_frms
    Count of broadcast data frames transmitted on this Aggregator
    on all its Aggregation ports. Does not include LACPDUs or Marker
    PDUs. However, does include frames discarded by the Distribution
    function.

tx_discarded_frms
    Count of data frames to be transmitted on this Aggregator
    that are discarded by the Distribution function. This occurs when
    conversation are allocated to different ports and have to be
    flushed on old ports

tx_errored_frms
    Count of data frames transmitted on this Aggregator that
    experience transmission errors on its Aggregation ports.

rx_frms
    Count of data frames received on this Aggregator on all its
    Aggregation ports. Does not include LACPDUs or Marker PDUs.
    Also, does not include frames discarded by the Collection
    function.

rx_data_octets
    Count of data and padding octets of frames received on this
    Aggregator on all its Aggregation ports. Does not include octets
    of LACPDUs or Marker PDUs. Also, does not include
    octets of frames
    discarded by the Collection function.

rx_mcast_frms
    Count of data frames received (from a group destination
    address other than the broadcast address) on this Aggregator on
    all its Aggregation ports. Does not include LACPDUs or Marker
    PDUs. Also, does not include frames discarded by the Collection
    function.

rx_bcast_frms
    Count of broadcast data frames received on this Aggregator on
    all its Aggregation ports. Does not include LACPDUs or Marker
    PDUs. Also, does not include frames discarded by the Collection
    function.

rx_discarded_frms
    Count of data frames received on this Aggregator that are
    discarded by the Collection function because the Collection
    function was disabled on the port which the frames are received.

rx_errored_frms
    Count of data frames received on this Aggregator that are
    discarded by its Aggregation ports, or are discarded by the
    Collection function of the Aggregator, or that are discarded by
    the Aggregator due to detection of an illegal Slow Protocols PDU.

rx_unknown_slow_proto_frms
    Count of data frames received on this Aggregator
    that are discarded by its Aggregation ports due to detection of
    an unknown Slow Protocols PDU.

.. _`vxge_hw_xmac_aggr_stats.description`:

Description
-----------

Per aggregator XMAC RX statistics.

.. _`vxge_hw_xmac_port_stats`:

struct vxge_hw_xmac_port_stats
==============================

.. c:type:: struct vxge_hw_xmac_port_stats

    XMAC Port Statistics

.. _`vxge_hw_xmac_port_stats.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_xmac_port_stats {
        u64 tx_ttl_frms;
        u64 tx_ttl_octets;
        u64 tx_data_octets;
        u64 tx_mcast_frms;
        u64 tx_bcast_frms;
        u64 tx_ucast_frms;
        u64 tx_tagged_frms;
        u64 tx_vld_ip;
        u64 tx_vld_ip_octets;
        u64 tx_icmp;
        u64 tx_tcp;
        u64 tx_rst_tcp;
        u64 tx_udp;
        u32 tx_parse_error;
        u32 tx_unknown_protocol;
        u64 tx_pause_ctrl_frms;
        u32 tx_marker_pdu_frms;
        u32 tx_lacpdu_frms;
        u32 tx_drop_ip;
        u32 tx_marker_resp_pdu_frms;
        u32 tx_xgmii_char2_match;
        u32 tx_xgmii_char1_match;
        u32 tx_xgmii_column2_match;
        u32 tx_xgmii_column1_match;
        u32 unused1;
        u16 tx_any_err_frms;
        u16 tx_drop_frms;
        u64 rx_ttl_frms;
        u64 rx_vld_frms;
        u64 rx_offload_frms;
        u64 rx_ttl_octets;
        u64 rx_data_octets;
        u64 rx_offload_octets;
        u64 rx_vld_mcast_frms;
        u64 rx_vld_bcast_frms;
        u64 rx_accepted_ucast_frms;
        u64 rx_accepted_nucast_frms;
        u64 rx_tagged_frms;
        u64 rx_long_frms;
        u64 rx_usized_frms;
        u64 rx_osized_frms;
        u64 rx_frag_frms;
        u64 rx_jabber_frms;
        u64 rx_ttl_64_frms;
        u64 rx_ttl_65_127_frms;
        u64 rx_ttl_128_255_frms;
        u64 rx_ttl_256_511_frms;
        u64 rx_ttl_512_1023_frms;
        u64 rx_ttl_1024_1518_frms;
        u64 rx_ttl_1519_4095_frms;
        u64 rx_ttl_4096_8191_frms;
        u64 rx_ttl_8192_max_frms;
        u64 rx_ttl_gt_max_frms;
        u64 rx_ip;
        u64 rx_accepted_ip;
        u64 rx_ip_octets;
        u64 rx_err_ip;
        u64 rx_icmp;
        u64 rx_tcp;
        u64 rx_udp;
        u64 rx_err_tcp;
        u64 rx_pause_count;
        u64 rx_pause_ctrl_frms;
        u64 rx_unsup_ctrl_frms;
        u64 rx_fcs_err_frms;
        u64 rx_in_rng_len_err_frms;
        u64 rx_out_rng_len_err_frms;
        u64 rx_drop_frms;
        u64 rx_discarded_frms;
        u64 rx_drop_ip;
        u64 rx_drop_udp;
        u32 rx_marker_pdu_frms;
        u32 rx_lacpdu_frms;
        u32 rx_unknown_pdu_frms;
        u32 rx_marker_resp_pdu_frms;
        u32 rx_fcs_discard;
        u32 rx_illegal_pdu_frms;
        u32 rx_switch_discard;
        u32 rx_len_discard;
        u32 rx_rpa_discard;
        u32 rx_l2_mgmt_discard;
        u32 rx_rts_discard;
        u32 rx_trash_discard;
        u32 rx_buff_full_discard;
        u32 rx_red_discard;
        u32 rx_xgmii_ctrl_err_cnt;
        u32 rx_xgmii_data_err_cnt;
        u32 rx_xgmii_char1_match;
        u32 rx_xgmii_err_sym;
        u32 rx_xgmii_column1_match;
        u32 rx_xgmii_char2_match;
        u32 rx_local_fault;
        u32 rx_xgmii_column2_match;
        u32 rx_jettison;
        u32 rx_remote_fault;
    }

.. _`vxge_hw_xmac_port_stats.members`:

Members
-------

tx_ttl_frms
    Count of successfully transmitted MAC frames

tx_ttl_octets
    Count of total octets of transmitted frames, not including
    framing characters (i.e. less framing bits). To determine the
    total octets of transmitted frames, including framing characters,
    multiply PORTn_TX_TTL_FRMS by 8 and add it to this stat (unless
    otherwise configured, this stat only counts frames that have
    8 bytes of preamble for each frame). This stat can be configured
    (see XMAC_STATS_GLOBAL_CFG.TTL_FRMS_HANDLING) to count everything
    including the preamble octets.

tx_data_octets
    Count of data and padding octets of successfully transmitted
    frames.

tx_mcast_frms
    Count of successfully transmitted frames to a group address
    other than the broadcast address.

tx_bcast_frms
    Count of successfully transmitted frames to the broadcast
    group address.

tx_ucast_frms
    Count of transmitted frames containing a unicast address.
    Includes discarded frames that are not sent to the network.

tx_tagged_frms
    Count of transmitted frames containing a VLAN tag.

tx_vld_ip
    Count of transmitted IP datagrams that are passed to the network.

tx_vld_ip_octets
    Count of total octets of transmitted IP datagrams that
    are passed to the network.

tx_icmp
    Count of transmitted ICMP messages. Includes messages not sent
    due to problems within ICMP.

tx_tcp
    Count of transmitted TCP segments. Does not include segments
    containing retransmitted octets.

tx_rst_tcp
    Count of transmitted TCP segments containing the RST flag.

tx_udp
    Count of transmitted UDP datagrams.

tx_parse_error
    Increments when the TPA is unable to parse a packet. This
    generally occurs when a packet is corrupt somehow, including
    packets that have IP version mismatches, invalid Layer 2 control
    fields, etc. L3/L4 checksums are not offloaded, but the packet
    is still be transmitted.

tx_unknown_protocol
    Increments when the TPA encounters an unknown
    protocol, such as a new IPv6 extension header, or an unsupported
    Routing Type. The packet still has a checksum calculated but it
    may be incorrect.

tx_pause_ctrl_frms
    Count of MAC PAUSE control frames that are transmitted.
    Since, the only control frames supported by this device are
    PAUSE frames, this register is a count of all transmitted MAC
    control frames.

tx_marker_pdu_frms
    Count of Marker PDUs transmitted
    on this Aggregation port.

tx_lacpdu_frms
    Count of LACPDUs transmitted on this Aggregation port.

tx_drop_ip
    Count of transmitted IP datagrams that could not be passed to
    the network. Increments because of:
    1) An internal processing error
    (such as an uncorrectable ECC error). 2) A frame parsing error
    during IP checksum calculation.

tx_marker_resp_pdu_frms
    Count of Marker Response PDUs transmitted on this
    Aggregation port.

tx_xgmii_char2_match
    Maintains a count of the number of transmitted XGMII
    characters that match a pattern that is programmable through
    register XMAC_STATS_TX_XGMII_CHAR_PORTn. By default, the pattern
    is set to /T/ (i.e. the terminate character), thus the statistic
    tracks the number of transmitted Terminate characters.

tx_xgmii_char1_match
    Maintains a count of the number of transmitted XGMII
    characters that match a pattern that is programmable through
    register XMAC_STATS_TX_XGMII_CHAR_PORTn. By default, the pattern
    is set to /S/ (i.e. the start character),
    thus the statistic tracks
    the number of transmitted Start characters.

tx_xgmii_column2_match
    Maintains a count of the number of transmitted XGMII
    columns that match a pattern that is programmable through register
    XMAC_STATS_TX_XGMII_COLUMN2_PORTn. By default, the pattern is set
    to 4 x /E/ (i.e. a column containing all error characters), thus
    the statistic tracks the number of Error columns transmitted at
    any time. If XMAC_STATS_TX_XGMII_BEHAV_COLUMN2_PORTn.NEAR_COL1 is
    set to 1, then this stat increments when COLUMN2 is found within
    'n' clocks after COLUMN1. Here, 'n' is defined by
    XMAC_STATS_TX_XGMII_BEHAV_COLUMN2_PORTn.NUM_COL (if 'n' is set
    to 0, then it means to search anywhere for COLUMN2).

tx_xgmii_column1_match
    Maintains a count of the number of transmitted XGMII
    columns that match a pattern that is programmable through register
    XMAC_STATS_TX_XGMII_COLUMN1_PORTn. By default, the pattern is set
    to 4 x /I/ (i.e. a column containing all idle characters),
    thus the statistic tracks the number of transmitted Idle columns.

unused1
    *undescribed*

tx_any_err_frms
    Count of transmitted frames containing any error that
    prevents them from being passed to the network. Increments if
    there is an ECC while reading the frame out of the transmit
    buffer. Also increments if the transmit protocol assist (TPA)
    block determines that the frame should not be sent.

tx_drop_frms
    Count of frames that could not be sent for no other reason
    than internal MAC processing. Increments once whenever the
    transmit buffer is flushed (due to an ECC error on a memory
    descriptor).

rx_ttl_frms
    Count of total received MAC frames, including frames received
    with frame-too-long, FCS, or length errors. This stat can be
    configured (see XMAC_STATS_GLOBAL_CFG.TTL_FRMS_HANDLING) to count
    everything, even "frames" as small one byte of preamble.

rx_vld_frms
    Count of successfully received MAC frames. Does not include
    frames received with frame-too-long, FCS, or length errors.

rx_offload_frms
    Count of offloaded received frames that are passed to
    the host.

rx_ttl_octets
    Count of total octets of received frames, not including
    framing characters (i.e. less framing bits). To determine the
    total octets of received frames, including framing characters,
    multiply PORTn_RX_TTL_FRMS by 8 and add it to this stat (unless
    otherwise configured, this stat only counts frames that have 8
    bytes of preamble for each frame). This stat can be configured
    (see XMAC_STATS_GLOBAL_CFG.TTL_FRMS_HANDLING) to count everything,
    even the preamble octets of "frames" as small one byte of preamble

rx_data_octets
    Count of data and padding octets of successfully received
    frames. Does not include frames received with frame-too-long,
    FCS, or length errors.

rx_offload_octets
    Count of total octets, not including framing
    characters, of offloaded received frames that are passed
    to the host.

rx_vld_mcast_frms
    Count of successfully received MAC frames containing a
    nonbroadcast group address. Does not include frames received
    with frame-too-long, FCS, or length errors.

rx_vld_bcast_frms
    Count of successfully received MAC frames containing
    the broadcast group address. Does not include frames received
    with frame-too-long, FCS, or length errors.

rx_accepted_ucast_frms
    Count of successfully received frames containing
    a unicast address. Only includes frames that are passed to
    the system.

rx_accepted_nucast_frms
    Count of successfully received frames containing
    a non-unicast (broadcast or multicast) address. Only includes
    frames that are passed to the system. Could include, for instance,
    non-unicast frames that contain FCS errors if the MAC_ERROR_CFG
    register is set to pass FCS-errored frames to the host.

rx_tagged_frms
    Count of received frames containing a VLAN tag.

rx_long_frms
    Count of received frames that are longer than RX_MAX_PYLD_LEN
    + 18 bytes (+ 22 bytes if VLAN-tagged).

rx_usized_frms
    Count of received frames of length (including FCS, but not
    framing bits) less than 64 octets, that are otherwise well-formed.
    In other words, counts runts.

rx_osized_frms
    Count of received frames of length (including FCS, but not
    framing bits) more than 1518 octets, that are otherwise
    well-formed. Note: If register XMAC_STATS_GLOBAL_CFG.VLAN_HANDLING
    is set to 1, then "more than 1518 octets" becomes "more than 1518
    (1522 if VLAN-tagged) octets".

rx_frag_frms
    Count of received frames of length (including FCS, but not
    framing bits) less than 64 octets that had bad FCS. In other
    words, counts fragments.

rx_jabber_frms
    Count of received frames of length (including FCS, but not
    framing bits) more than 1518 octets that had bad FCS. In other
    words, counts jabbers. Note: If register
    XMAC_STATS_GLOBAL_CFG.VLAN_HANDLING is set to 1, then "more than
    1518 octets" becomes "more than 1518 (1522 if VLAN-tagged)
    octets".

rx_ttl_64_frms
    Count of total received MAC frames with length (including
    FCS, but not framing bits) of exactly 64 octets. Includes frames
    received with frame-too-long, FCS, or length errors.

rx_ttl_65_127_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) of between 65 and 127
    octets inclusive. Includes frames received with frame-too-long,
    FCS, or length errors.

rx_ttl_128_255_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) of between 128 and 255
    octets inclusive. Includes frames received with frame-too-long,
    FCS, or length errors.

rx_ttl_256_511_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) of between 256 and 511
    octets inclusive. Includes frames received with frame-too-long,
    FCS, or length errors.

rx_ttl_512_1023_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) of between 512 and 1023
    octets inclusive. Includes frames received with frame-too-long,
    FCS, or length errors.

rx_ttl_1024_1518_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) of between 1024 and 1518
    octets inclusive. Includes frames received with frame-too-long,
    FCS, or length errors.

rx_ttl_1519_4095_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) of between 1519 and 4095
    octets inclusive. Includes frames received with frame-too-long,
    FCS, or length errors.

rx_ttl_4096_8191_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) of between 4096 and 8191
    octets inclusive. Includes frames received with frame-too-long,
    FCS, or length errors.

rx_ttl_8192_max_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) of between 8192 and
    RX_MAX_PYLD_LEN+18 octets inclusive. Includes frames received
    with frame-too-long, FCS, or length errors.

rx_ttl_gt_max_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) exceeding
    RX_MAX_PYLD_LEN+18 (+22 bytes if VLAN-tagged) octets inclusive.
    Includes frames received with frame-too-long,
    FCS, or length errors.

rx_ip
    Count of received IP datagrams. Includes errored IP datagrams.

rx_accepted_ip
    Count of received IP datagrams that
    are passed to the system.

rx_ip_octets
    Count of number of octets in received IP datagrams. Includes
    errored IP datagrams.

rx_err_ip
    Count of received IP datagrams containing errors. For example,
    bad IP checksum.

rx_icmp
    Count of received ICMP messages. Includes errored ICMP messages.

rx_tcp
    Count of received TCP segments. Includes errored TCP segments.
    Note: This stat contains a count of all received TCP segments,
    regardless of whether or not they pertain to an established
    connection.

rx_udp
    Count of received UDP datagrams.

rx_err_tcp
    Count of received TCP segments containing errors. For example,
    bad TCP checksum.

rx_pause_count
    Count of number of pause quanta that the MAC has been in
    the paused state. Recall, one pause quantum equates to 512
    bit times.

rx_pause_ctrl_frms
    Count of received MAC PAUSE control frames.

rx_unsup_ctrl_frms
    Count of received MAC control frames that do not
    contain the PAUSE opcode. The sum of RX_PAUSE_CTRL_FRMS and
    this register is a count of all received MAC control frames.
    Note: This stat may be configured to count all layer 2 errors
    (i.e. length errors and FCS errors).

rx_fcs_err_frms
    Count of received MAC frames that do not pass FCS. Does
    not include frames received with frame-too-long or
    frame-too-short error.

rx_in_rng_len_err_frms
    Count of received frames with a length/type field
    value between 46 (42 for VLAN-tagged frames) and 1500 (also 1500
    for VLAN-tagged frames), inclusive, that does not match the
    number of data octets (including pad) received. Also contains
    a count of received frames with a length/type field less than
    46 (42 for VLAN-tagged frames) and the number of data octets
    (including pad) received is greater than 46 (42 for VLAN-tagged
    frames).

rx_out_rng_len_err_frms
    Count of received frames with length/type field
    between 1501 and 1535 decimal, inclusive.

rx_drop_frms
    Count of received frames that could not be passed to the host.
    See PORTn_RX_L2_MGMT_DISCARD, PORTn_RX_RPA_DISCARD,
    PORTn_RX_TRASH_DISCARD, PORTn_RX_RTS_DISCARD, PORTn_RX_RED_DISCARD
    for a list of reasons. Because the RMAC drops one frame at a time,
    this stat also indicates the number of drop events.

rx_discarded_frms
    Count of received frames containing
    any error that prevents
    them from being passed to the system. See PORTn_RX_FCS_DISCARD,
    PORTn_RX_LEN_DISCARD, and PORTn_RX_SWITCH_DISCARD for a list of
    reasons.

rx_drop_ip
    Count of received IP datagrams that could not be passed to the
    host. See PORTn_RX_DROP_FRMS for a list of reasons.

rx_drop_udp
    Count of received UDP datagrams that are not delivered to the
    host. See PORTn_RX_DROP_FRMS for a list of reasons.

rx_marker_pdu_frms
    Count of valid Marker PDUs received on this Aggregation
    port.

rx_lacpdu_frms
    Count of valid LACPDUs received on this Aggregation port.

rx_unknown_pdu_frms
    Count of received frames (on this Aggregation port)
    that carry the Slow Protocols EtherType, but contain an unknown
    PDU. Or frames that contain the Slow Protocols group MAC address,
    but do not carry the Slow Protocols EtherType.

rx_marker_resp_pdu_frms
    Count of valid Marker Response PDUs received on
    this Aggregation port.

rx_fcs_discard
    Count of received frames that are discarded because the
    FCS check failed.

rx_illegal_pdu_frms
    Count of received frames (on this Aggregation port)
    that carry the Slow Protocols EtherType, but contain a badly
    formed PDU. Or frames that carry the Slow Protocols EtherType,
    but contain an illegal value of Protocol Subtype.

rx_switch_discard
    Count of received frames that are discarded by the
    internal switch because they did not have an entry in the
    Filtering Database. This includes frames that had an invalid
    destination MAC address or VLAN ID. It also includes frames are
    discarded because they did not satisfy the length requirements
    of the target VPATH.

rx_len_discard
    Count of received frames that are discarded because of an
    invalid frame length (includes fragments, oversized frames and
    mismatch between frame length and length/type field). This stat
    can be configured
    (see XMAC_STATS_GLOBAL_CFG.LEN_DISCARD_HANDLING).

rx_rpa_discard
    Count of received frames that were discarded because the
    receive protocol assist (RPA) discovered and error in the frame
    or was unable to parse the frame.

rx_l2_mgmt_discard
    Count of Layer 2 management frames (eg. pause frames,
    Link Aggregation Control Protocol (LACP) frames, etc.) that are
    discarded.

rx_rts_discard
    Count of received frames that are discarded by the receive
    traffic steering (RTS) logic. Includes those frame discarded
    because the SSC response contradicted the switch table, because
    the SSC timed out, or because the target queue could not fit the
    frame.

rx_trash_discard
    Count of received frames that are discarded because
    receive traffic steering (RTS) steered the frame to the trash
    queue.

rx_buff_full_discard
    Count of received frames that are discarded because
    internal buffers are full. Includes frames discarded because the
    RTS logic is waiting for an SSC lookup that has no timeout bound.
    Also, includes frames that are dropped because the MAC2FAU buffer
    is nearly full -- this can happen if the external receive buffer
    is full and the receive path is backing up.

rx_red_discard
    Count of received frames that are discarded because of RED
    (Random Early Discard).

rx_xgmii_ctrl_err_cnt
    Maintains a count of unexpected or misplaced control
    characters occurring between times of normal data transmission
    (i.e. not included in RX_XGMII_DATA_ERR_CNT). This counter is
    incremented when either -
    1) The Reconciliation Sublayer (RS) is expecting one control
    character and gets another (i.e. is expecting a Start
    character, but gets another control character).
    2) Start control character is not in lane 0
    Only increments the count by one for each XGMII column.

rx_xgmii_data_err_cnt
    Maintains a count of unexpected control characters
    during normal data transmission. If the Reconciliation Sublayer
    (RS) receives a control character, other than a terminate control
    character, during receipt of data octets then this register is
    incremented. Also increments if the start frame delimiter is not
    found in the correct location. Only increments the count by one
    for each XGMII column.

rx_xgmii_char1_match
    Maintains a count of the number of XGMII characters
    that match a pattern that is programmable through register
    XMAC_STATS_RX_XGMII_CHAR_PORTn. By default, the pattern is set
    to /E/ (i.e. the error character), thus the statistic tracks the
    number of Error characters received at any time.

rx_xgmii_err_sym
    Count of the number of symbol errors in the received
    XGMII data (i.e. PHY indicates "Receive Error" on the XGMII).
    Only includes symbol errors that are observed between the XGMII
    Start Frame Delimiter and End Frame Delimiter, inclusive. And
    only increments the count by one for each frame.

rx_xgmii_column1_match
    Maintains a count of the number of XGMII columns
    that match a pattern that is programmable through register
    XMAC_STATS_RX_XGMII_COLUMN1_PORTn. By default, the pattern is set
    to 4 x /E/ (i.e. a column containing all error characters), thus
    the statistic tracks the number of Error columns received at any
    time.

rx_xgmii_char2_match
    Maintains a count of the number of XGMII characters
    that match a pattern that is programmable through register
    XMAC_STATS_RX_XGMII_CHAR_PORTn. By default, the pattern is set
    to /E/ (i.e. the error character), thus the statistic tracks the
    number of Error characters received at any time.

rx_local_fault
    Maintains a count of the number of times that link
    transitioned from "up" to "down" due to a local fault.

rx_xgmii_column2_match
    Maintains a count of the number of XGMII columns
    that match a pattern that is programmable through register
    XMAC_STATS_RX_XGMII_COLUMN2_PORTn. By default, the pattern is set
    to 4 x /E/ (i.e. a column containing all error characters), thus
    the statistic tracks the number of Error columns received at any
    time. If XMAC_STATS_RX_XGMII_BEHAV_COLUMN2_PORTn.NEAR_COL1 is set
    to 1, then this stat increments when COLUMN2 is found within 'n'
    clocks after COLUMN1. Here, 'n' is defined by
    XMAC_STATS_RX_XGMII_BEHAV_COLUMN2_PORTn.NUM_COL (if 'n' is set to
    0, then it means to search anywhere for COLUMN2).

rx_jettison
    Count of received frames that are jettisoned because internal
    buffers are full.

rx_remote_fault
    Maintains a count of the number of times that link
    transitioned from "up" to "down" due to a remote fault.

.. _`vxge_hw_xmac_port_stats.description`:

Description
-----------

XMAC Port Statistics.

.. _`vxge_hw_xmac_vpath_tx_stats`:

struct vxge_hw_xmac_vpath_tx_stats
==================================

.. c:type:: struct vxge_hw_xmac_vpath_tx_stats

    XMAC Vpath Tx Statistics

.. _`vxge_hw_xmac_vpath_tx_stats.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_xmac_vpath_tx_stats {
        u64 tx_ttl_eth_frms;
        u64 tx_ttl_eth_octets;
        u64 tx_data_octets;
        u64 tx_mcast_frms;
        u64 tx_bcast_frms;
        u64 tx_ucast_frms;
        u64 tx_tagged_frms;
        u64 tx_vld_ip;
        u64 tx_vld_ip_octets;
        u64 tx_icmp;
        u64 tx_tcp;
        u64 tx_rst_tcp;
        u64 tx_udp;
        u32 tx_unknown_protocol;
        u32 tx_lost_ip;
        u32 unused1;
        u32 tx_parse_error;
        u64 tx_tcp_offload;
        u64 tx_retx_tcp_offload;
        u64 tx_lost_ip_offload;
    }

.. _`vxge_hw_xmac_vpath_tx_stats.members`:

Members
-------

tx_ttl_eth_frms
    Count of successfully transmitted MAC frames.

tx_ttl_eth_octets
    Count of total octets of transmitted frames,
    not including framing characters (i.e. less framing bits).
    To determine the total octets of transmitted frames, including
    framing characters, multiply TX_TTL_ETH_FRMS by 8 and add it to
    this stat (the device always prepends 8 bytes of preamble for
    each frame)

tx_data_octets
    Count of data and padding octets of successfully transmitted
    frames.

tx_mcast_frms
    Count of successfully transmitted frames to a group address
    other than the broadcast address.

tx_bcast_frms
    Count of successfully transmitted frames to the broadcast
    group address.

tx_ucast_frms
    Count of transmitted frames containing a unicast address.
    Includes discarded frames that are not sent to the network.

tx_tagged_frms
    Count of transmitted frames containing a VLAN tag.

tx_vld_ip
    Count of transmitted IP datagrams that are passed to the network.

tx_vld_ip_octets
    Count of total octets of transmitted IP datagrams that
    are passed to the network.

tx_icmp
    Count of transmitted ICMP messages. Includes messages not sent due
    to problems within ICMP.

tx_tcp
    Count of transmitted TCP segments. Does not include segments
    containing retransmitted octets.

tx_rst_tcp
    Count of transmitted TCP segments containing the RST flag.

tx_udp
    Count of transmitted UDP datagrams.

tx_unknown_protocol
    Increments when the TPA encounters an unknown protocol,
    such as a new IPv6 extension header, or an unsupported Routing
    Type. The packet still has a checksum calculated but it may be
    incorrect.

tx_lost_ip
    Count of transmitted IP datagrams that could not be passed
    to the network. Increments because of: 1) An internal processing
    error (such as an uncorrectable ECC error). 2) A frame parsing
    error during IP checksum calculation.

unused1
    *undescribed*

tx_parse_error
    Increments when the TPA is unable to parse a packet. This
    generally occurs when a packet is corrupt somehow, including
    packets that have IP version mismatches, invalid Layer 2 control
    fields, etc. L3/L4 checksums are not offloaded, but the packet
    is still be transmitted.

tx_tcp_offload
    For frames belonging to offloaded sessions only, a count
    of transmitted TCP segments. Does not include segments containing
    retransmitted octets.

tx_retx_tcp_offload
    For frames belonging to offloaded sessions only, the
    total number of segments retransmitted. Retransmitted segments
    that are sourced by the host are counted by the host.

tx_lost_ip_offload
    For frames belonging to offloaded sessions only, a count
    of transmitted IP datagrams that could not be passed to the
    network.

.. _`vxge_hw_xmac_vpath_tx_stats.description`:

Description
-----------

XMAC Vpath TX Statistics.

.. _`vxge_hw_xmac_vpath_rx_stats`:

struct vxge_hw_xmac_vpath_rx_stats
==================================

.. c:type:: struct vxge_hw_xmac_vpath_rx_stats

    XMAC Vpath RX Statistics

.. _`vxge_hw_xmac_vpath_rx_stats.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_xmac_vpath_rx_stats {
        u64 rx_ttl_eth_frms;
        u64 rx_vld_frms;
        u64 rx_offload_frms;
        u64 rx_ttl_eth_octets;
        u64 rx_data_octets;
        u64 rx_offload_octets;
        u64 rx_vld_mcast_frms;
        u64 rx_vld_bcast_frms;
        u64 rx_accepted_ucast_frms;
        u64 rx_accepted_nucast_frms;
        u64 rx_tagged_frms;
        u64 rx_long_frms;
        u64 rx_usized_frms;
        u64 rx_osized_frms;
        u64 rx_frag_frms;
        u64 rx_jabber_frms;
        u64 rx_ttl_64_frms;
        u64 rx_ttl_65_127_frms;
        u64 rx_ttl_128_255_frms;
        u64 rx_ttl_256_511_frms;
        u64 rx_ttl_512_1023_frms;
        u64 rx_ttl_1024_1518_frms;
        u64 rx_ttl_1519_4095_frms;
        u64 rx_ttl_4096_8191_frms;
        u64 rx_ttl_8192_max_frms;
        u64 rx_ttl_gt_max_frms;
        u64 rx_ip;
        u64 rx_accepted_ip;
        u64 rx_ip_octets;
        u64 rx_err_ip;
        u64 rx_icmp;
        u64 rx_tcp;
        u64 rx_udp;
        u64 rx_err_tcp;
        u64 rx_lost_frms;
        u64 rx_lost_ip;
        u64 rx_lost_ip_offload;
        u16 rx_various_discard;
        u16 rx_sleep_discard;
        u16 rx_red_discard;
        u16 rx_queue_full_discard;
        u64 rx_mpa_ok_frms;
    }

.. _`vxge_hw_xmac_vpath_rx_stats.members`:

Members
-------

rx_ttl_eth_frms
    Count of successfully received MAC frames.

rx_vld_frms
    Count of successfully received MAC frames. Does not include
    frames received with frame-too-long, FCS, or length errors.

rx_offload_frms
    Count of offloaded received frames that are passed to
    the host.

rx_ttl_eth_octets
    Count of total octets of received frames, not including
    framing characters (i.e. less framing bits). Only counts octets
    of frames that are at least 14 bytes (18 bytes for VLAN-tagged)
    before FCS. To determine the total octets of received frames,
    including framing characters, multiply RX_TTL_ETH_FRMS by 8 and
    add it to this stat (the stat RX_TTL_ETH_FRMS only counts frames
    that have the required 8 bytes of preamble).

rx_data_octets
    Count of data and padding octets of successfully received
    frames. Does not include frames received with frame-too-long,
    FCS, or length errors.

rx_offload_octets
    Count of total octets, not including framing characters,
    of offloaded received frames that are passed to the host.

rx_vld_mcast_frms
    Count of successfully received MAC frames containing a
    nonbroadcast group address. Does not include frames received with
    frame-too-long, FCS, or length errors.

rx_vld_bcast_frms
    Count of successfully received MAC frames containing the
    broadcast group address. Does not include frames received with
    frame-too-long, FCS, or length errors.

rx_accepted_ucast_frms
    Count of successfully received frames containing
    a unicast address. Only includes frames that are passed to the
    system.

rx_accepted_nucast_frms
    Count of successfully received frames containing
    a non-unicast (broadcast or multicast) address. Only includes
    frames that are passed to the system. Could include, for instance,
    non-unicast frames that contain FCS errors if the MAC_ERROR_CFG
    register is set to pass FCS-errored frames to the host.

rx_tagged_frms
    Count of received frames containing a VLAN tag.

rx_long_frms
    Count of received frames that are longer than RX_MAX_PYLD_LEN
    + 18 bytes (+ 22 bytes if VLAN-tagged).

rx_usized_frms
    Count of received frames of length (including FCS, but not
    framing bits) less than 64 octets, that are otherwise well-formed.
    In other words, counts runts.

rx_osized_frms
    Count of received frames of length (including FCS, but not
    framing bits) more than 1518 octets, that are otherwise
    well-formed.

rx_frag_frms
    Count of received frames of length (including FCS, but not
    framing bits) less than 64 octets that had bad FCS.
    In other words, counts fragments.

rx_jabber_frms
    Count of received frames of length (including FCS, but not
    framing bits) more than 1518 octets that had bad FCS. In other
    words, counts jabbers.

rx_ttl_64_frms
    Count of total received MAC frames with length (including
    FCS, but not framing bits) of exactly 64 octets. Includes frames
    received with frame-too-long, FCS, or length errors.

rx_ttl_65_127_frms
    Count of total received MAC frames
    with length (including
    FCS, but not framing bits) of between 65 and 127 octets inclusive.
    Includes frames received with frame-too-long, FCS,
    or length errors.

rx_ttl_128_255_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits)
    of between 128 and 255 octets
    inclusive. Includes frames received with frame-too-long, FCS,
    or length errors.

rx_ttl_256_511_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits)
    of between 256 and 511 octets
    inclusive. Includes frames received with frame-too-long, FCS, or
    length errors.

rx_ttl_512_1023_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) of between 512 and 1023
    octets inclusive. Includes frames received with frame-too-long,
    FCS, or length errors.

rx_ttl_1024_1518_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) of between 1024 and 1518
    octets inclusive. Includes frames received with frame-too-long,
    FCS, or length errors.

rx_ttl_1519_4095_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) of between 1519 and 4095
    octets inclusive. Includes frames received with frame-too-long,
    FCS, or length errors.

rx_ttl_4096_8191_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) of between 4096 and 8191
    octets inclusive. Includes frames received with frame-too-long,
    FCS, or length errors.

rx_ttl_8192_max_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) of between 8192 and
    RX_MAX_PYLD_LEN+18 octets inclusive. Includes frames received
    with frame-too-long, FCS, or length errors.

rx_ttl_gt_max_frms
    Count of total received MAC frames with length
    (including FCS, but not framing bits) exceeding RX_MAX_PYLD_LEN+18
    (+22 bytes if VLAN-tagged) octets inclusive. Includes frames
    received with frame-too-long, FCS, or length errors.

rx_ip
    Count of received IP datagrams. Includes errored IP datagrams.

rx_accepted_ip
    Count of received IP datagrams that
    are passed to the system.

rx_ip_octets
    Count of number of octets in received IP datagrams.
    Includes errored IP datagrams.

rx_err_ip
    Count of received IP datagrams containing errors. For example,
    bad IP checksum.

rx_icmp
    Count of received ICMP messages. Includes errored ICMP messages.

rx_tcp
    Count of received TCP segments. Includes errored TCP segments.
    Note: This stat contains a count of all received TCP segments,
    regardless of whether or not they pertain to an established
    connection.

rx_udp
    Count of received UDP datagrams.

rx_err_tcp
    Count of received TCP segments containing errors. For example,
    bad TCP checksum.

rx_lost_frms
    Count of received frames that could not be passed to the host.
    See RX_QUEUE_FULL_DISCARD and RX_RED_DISCARD
    for a list of reasons.

rx_lost_ip
    Count of received IP datagrams that could not be passed to
    the host. See RX_LOST_FRMS for a list of reasons.

rx_lost_ip_offload
    For frames belonging to offloaded sessions only, a count
    of received IP datagrams that could not be passed to the host.
    See RX_LOST_FRMS for a list of reasons.

rx_various_discard
    Count of received frames that are discarded because
    the target receive queue is full.

rx_sleep_discard
    Count of received frames that are discarded because the
    target VPATH is asleep (a Wake-on-LAN magic packet can be used
    to awaken the VPATH).

rx_red_discard
    Count of received frames that are discarded because of RED
    (Random Early Discard).

rx_queue_full_discard
    Count of received frames that are discarded because
    the target receive queue is full.

rx_mpa_ok_frms
    Count of received frames that pass the MPA checks.

.. _`vxge_hw_xmac_vpath_rx_stats.description`:

Description
-----------

XMAC Vpath RX Statistics.

.. _`vxge_hw_xmac_stats`:

struct vxge_hw_xmac_stats
=========================

.. c:type:: struct vxge_hw_xmac_stats

    XMAC Statistics

.. _`vxge_hw_xmac_stats.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_xmac_stats {
        struct vxge_hw_xmac_aggr_statsaggr_stats[VXGE_HW_MAC_MAX_MAC_PORT_ID];
        struct vxge_hw_xmac_port_statsport_stats[VXGE_HW_MAC_MAX_MAC_PORT_ID+1];
        struct vxge_hw_xmac_vpath_tx_statsvpath_tx_stats[VXGE_HW_MAX_VIRTUAL_PATHS];
        struct vxge_hw_xmac_vpath_rx_statsvpath_rx_stats[VXGE_HW_MAX_VIRTUAL_PATHS];
    }

.. _`vxge_hw_xmac_stats.members`:

Members
-------

.. _`vxge_hw_xmac_stats.description`:

Description
-----------

XMAC Statistics.

.. _`vxge_hw_vpath_stats_hw_info`:

struct vxge_hw_vpath_stats_hw_info
==================================

.. c:type:: struct vxge_hw_vpath_stats_hw_info

    Titan vpath hardware statistics.

.. _`vxge_hw_vpath_stats_hw_info.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_vpath_stats_hw_info {
        u32 ini_num_mwr_sent;
        u32 unused1;
        u32 ini_num_mrd_sent;
        u32 unused2;
        u32 ini_num_cpl_rcvd;
        u32 unused3;
        u64 ini_num_mwr_byte_sent;
        u64 ini_num_cpl_byte_rcvd;
        u32 wrcrdtarb_xoff;
        u32 unused4;
        u32 rdcrdtarb_xoff;
        u32 unused5;
        u32 vpath_genstats_count0;
        u32 vpath_genstats_count1;
        u32 vpath_genstats_count2;
        u32 vpath_genstats_count3;
        u32 vpath_genstats_count4;
        u32 unused6;
        u32 vpath_genstats_count5;
        u32 unused7;
        struct vxge_hw_xmac_vpath_tx_stats tx_stats;
        struct vxge_hw_xmac_vpath_rx_stats rx_stats;
        u64 unused9;
        u32 prog_event_vnum1;
        u32 prog_event_vnum0;
        u32 prog_event_vnum3;
        u32 prog_event_vnum2;
        u16 rx_multi_cast_frame_discard;
        u8 unused10[6];
        u32 rx_frm_transferred;
        u32 unused11;
        u16 rxd_returned;
        u8 unused12[6];
        u16 rx_mpa_len_fail_frms;
        u16 rx_mpa_mrk_fail_frms;
        u16 rx_mpa_crc_fail_frms;
        u16 rx_permitted_frms;
        u64 rx_vp_reset_discarded_frms;
        u64 rx_wol_frms;
        u64 tx_vp_reset_discarded_frms;
    }

.. _`vxge_hw_vpath_stats_hw_info.members`:

Members
-------

ini_num_mwr_sent
    The number of PCI memory writes initiated by the PIC block
    for the given VPATH

unused1
    *undescribed*

ini_num_mrd_sent
    The number of PCI memory reads initiated by the PIC block

unused2
    *undescribed*

ini_num_cpl_rcvd
    The number of PCI read completions received by the
    PIC block

unused3
    *undescribed*

ini_num_mwr_byte_sent
    The number of PCI memory write bytes sent by the PIC
    block to the host

ini_num_cpl_byte_rcvd
    The number of PCI read completion bytes received by
    the PIC block

wrcrdtarb_xoff
    TBD

unused4
    *undescribed*

rdcrdtarb_xoff
    TBD

unused5
    *undescribed*

vpath_genstats_count0
    TBD

vpath_genstats_count1
    TBD

vpath_genstats_count2
    TBD

vpath_genstats_count3
    TBD

vpath_genstats_count4
    TBD

unused6
    *undescribed*

vpath_genstats_count5
    *undescribed*

unused7
    *undescribed*

tx_stats
    Transmit stats

rx_stats
    Receive stats

unused9
    *undescribed*

prog_event_vnum1
    Programmable statistic. Increments when internal logic
    detects a certain event. See register
    XMAC_STATS_CFG.EVENT_VNUM1_CFG for more information.

prog_event_vnum0
    Programmable statistic. Increments when internal logic
    detects a certain event. See register
    XMAC_STATS_CFG.EVENT_VNUM0_CFG for more information.

prog_event_vnum3
    Programmable statistic. Increments when internal logic
    detects a certain event. See register
    XMAC_STATS_CFG.EVENT_VNUM3_CFG for more information.

prog_event_vnum2
    Programmable statistic. Increments when internal logic
    detects a certain event. See register
    XMAC_STATS_CFG.EVENT_VNUM2_CFG for more information.

rx_multi_cast_frame_discard
    TBD

rx_frm_transferred
    TBD

unused11
    *undescribed*

rxd_returned
    TBD

rx_mpa_len_fail_frms
    Count of received frames
    that fail the MPA length check

rx_mpa_mrk_fail_frms
    Count of received frames
    that fail the MPA marker check

rx_mpa_crc_fail_frms
    Count of received frames that fail the MPA CRC check

rx_permitted_frms
    Count of frames that pass through the FAU and on to the
    frame buffer (and subsequently to the host).

rx_vp_reset_discarded_frms
    Count of receive frames that are discarded
    because the VPATH is in reset

rx_wol_frms
    Count of received "magic packet" frames. Stat increments
    whenever the received frame matches the VPATH's Wake-on-LAN
    signature(s) CRC.

tx_vp_reset_discarded_frms
    Count of transmit frames that are discarded
    because the VPATH is in reset. Includes frames that are discarded
    because the current VPIN does not match that VPIN of the frame

.. _`vxge_hw_vpath_stats_hw_info.description`:

Description
-----------

Titan vpath hardware statistics.

.. _`vxge_hw_device_stats_mrpcim_info`:

struct vxge_hw_device_stats_mrpcim_info
=======================================

.. c:type:: struct vxge_hw_device_stats_mrpcim_info

    Titan mrpcim hardware statistics. \ ``pic``\ .ini_rd_drop      0x0000          4       Number of DMA reads initiated by the adapter that were discarded because the VPATH is out of service \ ``pic``\ .ini_wr_drop     0x0004  4       Number of DMA writes initiated by the adapter that were discared because the VPATH is out of service \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane0]     0x0008  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane1]     0x0010  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane2]     0x0018  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane3]     0x0020  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane4]     0x0028  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane5]     0x0030  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane6]     0x0038  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane7]     0x0040  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane8]     0x0048  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane9]     0x0050  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane10]    0x0058  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane11]    0x0060  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane12]    0x0068  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane13]    0x0070  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane14]    0x0078  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane15]    0x0080  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_ph_crdt_depleted[vplane16]    0x0088  4       Number of times the posted header credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane0]     0x0090  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane1]     0x0098  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane2]     0x00a0  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane3]     0x00a8  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane4]     0x00b0  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane5]     0x00b8  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane6]     0x00c0  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane7]     0x00c8  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane8]     0x00d0  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane9]     0x00d8  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane10]    0x00e0  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane11]    0x00e8  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane12]    0x00f0  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane13]    0x00f8  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane14]    0x0100  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane15]    0x0108  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .wrcrdtarb_pd_crdt_depleted[vplane16]    0x0110  4       Number of times the posted data credits for upstream PCI writes were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane0]    0x0118  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane1]    0x0120  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane2]    0x0128  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane3]    0x0130  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane4]    0x0138  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane5]    0x0140  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane6]    0x0148  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane7]    0x0150  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane8]    0x0158  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane9]    0x0160  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane10]   0x0168  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane11]   0x0170  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane12]   0x0178  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane13]   0x0180  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane14]   0x0188  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane15]   0x0190  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .rdcrdtarb_nph_crdt_depleted[vplane16]   0x0198  4       Number of times the non-posted header credits for upstream PCI reads were depleted \ ``pic``\ .ini_rd_vpin_drop        0x01a0  4       Number of DMA reads initiated by the adapter that were discarded because the VPATH instance number does not match \ ``pic``\ .ini_wr_vpin_drop        0x01a4  4       Number of DMA writes initiated by the adapter that were discarded because the VPATH instance number does not match \ ``pic``\ .genstats_count0         0x01a8  4       Configurable statistic #1. Refer to the GENSTATS0_CFG for information on configuring this statistic \ ``pic``\ .genstats_count1         0x01ac  4       Configurable statistic #2. Refer to the GENSTATS1_CFG for information on configuring this statistic \ ``pic``\ .genstats_count2         0x01b0  4       Configurable statistic #3. Refer to the GENSTATS2_CFG for information on configuring this statistic \ ``pic``\ .genstats_count3         0x01b4  4       Configurable statistic #4. Refer to the GENSTATS3_CFG for information on configuring this statistic \ ``pic``\ .genstats_count4         0x01b8  4       Configurable statistic #5. Refer to the GENSTATS4_CFG for information on configuring this statistic \ ``pic``\ .genstats_count5         0x01c0  4       Configurable statistic #6. Refer to the GENSTATS5_CFG for information on configuring this statistic \ ``pci``\ .rstdrop_cpl     0x01c8  4 \ ``pci``\ .rstdrop_msg     0x01cc  4 \ ``pci``\ .rstdrop_client1         0x01d0  4 \ ``pci``\ .rstdrop_client0         0x01d4  4 \ ``pci``\ .rstdrop_client2         0x01d8  4 \ ``pci``\ .depl_cplh[vplane0]      0x01e2  2       Number of times completion header credits were depleted \ ``pci``\ .depl_nph[vplane0]       0x01e4  2       Number of times non posted header credits were depleted \ ``pci``\ .depl_ph[vplane0]        0x01e6  2       Number of times the posted header credits were depleted \ ``pci``\ .depl_cplh[vplane1]      0x01ea  2 \ ``pci``\ .depl_nph[vplane1]       0x01ec  2 \ ``pci``\ .depl_ph[vplane1]        0x01ee  2 \ ``pci``\ .depl_cplh[vplane2]      0x01f2  2 \ ``pci``\ .depl_nph[vplane2]       0x01f4  2 \ ``pci``\ .depl_ph[vplane2]        0x01f6  2 \ ``pci``\ .depl_cplh[vplane3]      0x01fa  2 \ ``pci``\ .depl_nph[vplane3]       0x01fc  2 \ ``pci``\ .depl_ph[vplane3]        0x01fe  2 \ ``pci``\ .depl_cplh[vplane4]      0x0202  2 \ ``pci``\ .depl_nph[vplane4]       0x0204  2 \ ``pci``\ .depl_ph[vplane4]        0x0206  2 \ ``pci``\ .depl_cplh[vplane5]      0x020a  2 \ ``pci``\ .depl_nph[vplane5]       0x020c  2 \ ``pci``\ .depl_ph[vplane5]        0x020e  2 \ ``pci``\ .depl_cplh[vplane6]      0x0212  2 \ ``pci``\ .depl_nph[vplane6]       0x0214  2 \ ``pci``\ .depl_ph[vplane6]        0x0216  2 \ ``pci``\ .depl_cplh[vplane7]      0x021a  2 \ ``pci``\ .depl_nph[vplane7]       0x021c  2 \ ``pci``\ .depl_ph[vplane7]        0x021e  2 \ ``pci``\ .depl_cplh[vplane8]      0x0222  2 \ ``pci``\ .depl_nph[vplane8]       0x0224  2 \ ``pci``\ .depl_ph[vplane8]        0x0226  2 \ ``pci``\ .depl_cplh[vplane9]      0x022a  2 \ ``pci``\ .depl_nph[vplane9]       0x022c  2 \ ``pci``\ .depl_ph[vplane9]        0x022e  2 \ ``pci``\ .depl_cplh[vplane10]     0x0232  2 \ ``pci``\ .depl_nph[vplane10]      0x0234  2 \ ``pci``\ .depl_ph[vplane10]       0x0236  2 \ ``pci``\ .depl_cplh[vplane11]     0x023a  2 \ ``pci``\ .depl_nph[vplane11]      0x023c  2 \ ``pci``\ .depl_ph[vplane11]       0x023e  2 \ ``pci``\ .depl_cplh[vplane12]     0x0242  2 \ ``pci``\ .depl_nph[vplane12]      0x0244  2 \ ``pci``\ .depl_ph[vplane12]       0x0246  2 \ ``pci``\ .depl_cplh[vplane13]     0x024a  2 \ ``pci``\ .depl_nph[vplane13]      0x024c  2 \ ``pci``\ .depl_ph[vplane13]       0x024e  2 \ ``pci``\ .depl_cplh[vplane14]     0x0252  2 \ ``pci``\ .depl_nph[vplane14]      0x0254  2 \ ``pci``\ .depl_ph[vplane14]       0x0256  2 \ ``pci``\ .depl_cplh[vplane15]     0x025a  2 \ ``pci``\ .depl_nph[vplane15]      0x025c  2 \ ``pci``\ .depl_ph[vplane15]       0x025e  2 \ ``pci``\ .depl_cplh[vplane16]     0x0262  2 \ ``pci``\ .depl_nph[vplane16]      0x0264  2 \ ``pci``\ .depl_ph[vplane16]       0x0266  2 \ ``pci``\ .depl_cpld[vplane0]      0x026a  2       Number of times completion data credits were depleted \ ``pci``\ .depl_npd[vplane0]       0x026c  2       Number of times non posted data credits were depleted \ ``pci``\ .depl_pd[vplane0]        0x026e  2       Number of times the posted data credits were depleted \ ``pci``\ .depl_cpld[vplane1]      0x0272  2 \ ``pci``\ .depl_npd[vplane1]       0x0274  2 \ ``pci``\ .depl_pd[vplane1]        0x0276  2 \ ``pci``\ .depl_cpld[vplane2]      0x027a  2 \ ``pci``\ .depl_npd[vplane2]       0x027c  2 \ ``pci``\ .depl_pd[vplane2]        0x027e  2 \ ``pci``\ .depl_cpld[vplane3]      0x0282  2 \ ``pci``\ .depl_npd[vplane3]       0x0284  2 \ ``pci``\ .depl_pd[vplane3]        0x0286  2 \ ``pci``\ .depl_cpld[vplane4]      0x028a  2 \ ``pci``\ .depl_npd[vplane4]       0x028c  2 \ ``pci``\ .depl_pd[vplane4]        0x028e  2 \ ``pci``\ .depl_cpld[vplane5]      0x0292  2 \ ``pci``\ .depl_npd[vplane5]       0x0294  2 \ ``pci``\ .depl_pd[vplane5]        0x0296  2 \ ``pci``\ .depl_cpld[vplane6]      0x029a  2 \ ``pci``\ .depl_npd[vplane6]       0x029c  2 \ ``pci``\ .depl_pd[vplane6]        0x029e  2 \ ``pci``\ .depl_cpld[vplane7]      0x02a2  2 \ ``pci``\ .depl_npd[vplane7]       0x02a4  2 \ ``pci``\ .depl_pd[vplane7]        0x02a6  2 \ ``pci``\ .depl_cpld[vplane8]      0x02aa  2 \ ``pci``\ .depl_npd[vplane8]       0x02ac  2 \ ``pci``\ .depl_pd[vplane8]        0x02ae  2 \ ``pci``\ .depl_cpld[vplane9]      0x02b2  2 \ ``pci``\ .depl_npd[vplane9]       0x02b4  2 \ ``pci``\ .depl_pd[vplane9]        0x02b6  2 \ ``pci``\ .depl_cpld[vplane10]     0x02ba  2 \ ``pci``\ .depl_npd[vplane10]      0x02bc  2 \ ``pci``\ .depl_pd[vplane10]       0x02be  2 \ ``pci``\ .depl_cpld[vplane11]     0x02c2  2 \ ``pci``\ .depl_npd[vplane11]      0x02c4  2 \ ``pci``\ .depl_pd[vplane11]       0x02c6  2 \ ``pci``\ .depl_cpld[vplane12]     0x02ca  2 \ ``pci``\ .depl_npd[vplane12]      0x02cc  2 \ ``pci``\ .depl_pd[vplane12]       0x02ce  2 \ ``pci``\ .depl_cpld[vplane13]     0x02d2  2 \ ``pci``\ .depl_npd[vplane13]      0x02d4  2 \ ``pci``\ .depl_pd[vplane13]       0x02d6  2 \ ``pci``\ .depl_cpld[vplane14]     0x02da  2 \ ``pci``\ .depl_npd[vplane14]      0x02dc  2 \ ``pci``\ .depl_pd[vplane14]       0x02de  2 \ ``pci``\ .depl_cpld[vplane15]     0x02e2  2 \ ``pci``\ .depl_npd[vplane15]      0x02e4  2 \ ``pci``\ .depl_pd[vplane15]       0x02e6  2 \ ``pci``\ .depl_cpld[vplane16]     0x02ea  2 \ ``pci``\ .depl_npd[vplane16]      0x02ec  2 \ ``pci``\ .depl_pd[vplane16]       0x02ee  2 \ ``xgmac_port``\ [3]; \ ``xgmac_aggr``\ [2]; \ ``xgmac``\ .global_prog_event_gnum0       0x0ae0  8       Programmable statistic. Increments when internal logic detects a certain event. See register XMAC_STATS_GLOBAL_CFG.EVENT_GNUM0_CFG for more information. \ ``xgmac``\ .global_prog_event_gnum1       0x0ae8  8       Programmable statistic. Increments when internal logic detects a certain event. See register XMAC_STATS_GLOBAL_CFG.EVENT_GNUM1_CFG for more information. \ ``xgmac``\ .orp_lro_events        0x0af8  8 \ ``xgmac``\ .orp_bs_events         0x0b00  8 \ ``xgmac``\ .orp_iwarp_events      0x0b08  8 \ ``xgmac``\ .tx_permitted_frms     0x0b14  4 \ ``xgmac``\ .port2_tx_any_frms     0x0b1d  1 \ ``xgmac``\ .port1_tx_any_frms     0x0b1e  1 \ ``xgmac``\ .port0_tx_any_frms     0x0b1f  1 \ ``xgmac``\ .port2_rx_any_frms     0x0b25  1 \ ``xgmac``\ .port1_rx_any_frms     0x0b26  1 \ ``xgmac``\ .port0_rx_any_frms     0x0b27  1

.. _`vxge_hw_device_stats_mrpcim_info.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_device_stats_mrpcim_info {
        u32 pic_ini_rd_drop;
        u32 pic_ini_wr_drop;
        struct pci_depl_d_vplane[17];
        struct vxge_hw_xmac_port_stats xgmac_port[3];
        struct vxge_hw_xmac_aggr_stats xgmac_aggr[2];
        u64 xgmac_global_prog_event_gnum0;
        u64 xgmac_global_prog_event_gnum1;
        u64 unused7;
        u64 unused8;
        u64 unused9;
        u64 unused10;
        u32 unused11;
        u32 xgmac_tx_permitted_frms;
        u32 unused12;
        u8 unused13;
        u8 xgmac_port2_tx_any_frms;
        u8 xgmac_port1_tx_any_frms;
        u8 xgmac_port0_tx_any_frms;
        u32 unused14;
        u8 unused15;
        u8 xgmac_port2_rx_any_frms;
        u8 xgmac_port1_rx_any_frms;
        u8 xgmac_port0_rx_any_frms;
    }

.. _`vxge_hw_device_stats_mrpcim_info.members`:

Members
-------

pic_ini_rd_drop
    *undescribed*

pic_ini_wr_drop
    *undescribed*

xgmac_global_prog_event_gnum0
    *undescribed*

xgmac_global_prog_event_gnum1
    *undescribed*

unused7
    *undescribed*

unused8
    *undescribed*

unused9
    *undescribed*

unused10
    *undescribed*

unused11
    *undescribed*

xgmac_tx_permitted_frms
    *undescribed*

unused12
    *undescribed*

unused13
    *undescribed*

xgmac_port2_tx_any_frms
    *undescribed*

xgmac_port1_tx_any_frms
    *undescribed*

xgmac_port0_tx_any_frms
    *undescribed*

unused14
    *undescribed*

unused15
    *undescribed*

xgmac_port2_rx_any_frms
    *undescribed*

xgmac_port1_rx_any_frms
    *undescribed*

xgmac_port0_rx_any_frms
    *undescribed*

.. _`vxge_hw_device_stats_mrpcim_info.description`:

Description
-----------

Titan mrpcim hardware statistics.

.. _`vxge_hw_device_stats_hw_info`:

struct vxge_hw_device_stats_hw_info
===================================

.. c:type:: struct vxge_hw_device_stats_hw_info

    Titan hardware statistics.

.. _`vxge_hw_device_stats_hw_info.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_device_stats_hw_info {
        struct vxge_hw_vpath_stats_hw_info*vpath_info[VXGE_HW_MAX_VIRTUAL_PATHS];
        struct vxge_hw_vpath_stats_hw_infovpath_info_sav[VXGE_HW_MAX_VIRTUAL_PATHS];
    }

.. _`vxge_hw_device_stats_hw_info.members`:

Members
-------

.. _`vxge_hw_device_stats_hw_info.description`:

Description
-----------

Titan hardware statistics.

.. _`vxge_hw_vpath_stats_sw_common_info`:

struct vxge_hw_vpath_stats_sw_common_info
=========================================

.. c:type:: struct vxge_hw_vpath_stats_sw_common_info

    HW common statistics for queues.

.. _`vxge_hw_vpath_stats_sw_common_info.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_vpath_stats_sw_common_info {
        u32 full_cnt;
        u32 usage_cnt;
        u32 usage_max;
        u32 reserve_free_swaps_cnt;
        u32 total_compl_cnt;
    }

.. _`vxge_hw_vpath_stats_sw_common_info.members`:

Members
-------

full_cnt
    Number of times the queue was full

usage_cnt
    usage count.

usage_max
    Maximum usage

reserve_free_swaps_cnt
    Reserve/free swap counter. Internal usage.

total_compl_cnt
    Total descriptor completion count.

.. _`vxge_hw_vpath_stats_sw_common_info.description`:

Description
-----------

Hw queue counters

.. _`vxge_hw_vpath_stats_sw_common_info.see-also`:

See also
--------

struct vxge_hw_vpath_stats_sw_fifo_info{},
struct vxge_hw_vpath_stats_sw_ring_info{},

.. _`vxge_hw_vpath_stats_sw_fifo_info`:

struct vxge_hw_vpath_stats_sw_fifo_info
=======================================

.. c:type:: struct vxge_hw_vpath_stats_sw_fifo_info

    HW fifo statistics

.. _`vxge_hw_vpath_stats_sw_fifo_info.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_vpath_stats_sw_fifo_info {
        struct vxge_hw_vpath_stats_sw_common_info common_stats;
        u32 total_posts;
        u32 total_buffers;
        u32 txd_t_code_err_cnt[VXGE_HW_DTR_MAX_T_CODE];
    }

.. _`vxge_hw_vpath_stats_sw_fifo_info.members`:

Members
-------

common_stats
    Common counters for all queues

total_posts
    Total number of postings on the queue.

total_buffers
    Total number of buffers posted.

txd_t_code_err_cnt
    Array of transmit transfer codes. The position
    (index) in this array reflects the transfer code type, for instance
    0xA - "loss of link".
    Value txd_t_code_err_cnt[i] reflects the
    number of times the corresponding transfer code was encountered.

.. _`vxge_hw_vpath_stats_sw_fifo_info.description`:

Description
-----------

HW fifo counters

.. _`vxge_hw_vpath_stats_sw_fifo_info.see-also`:

See also
--------

struct vxge_hw_vpath_stats_sw_common_info{},
struct vxge_hw_vpath_stats_sw_ring_info{},

.. _`vxge_hw_vpath_stats_sw_ring_info`:

struct vxge_hw_vpath_stats_sw_ring_info
=======================================

.. c:type:: struct vxge_hw_vpath_stats_sw_ring_info

    HW ring statistics

.. _`vxge_hw_vpath_stats_sw_ring_info.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_vpath_stats_sw_ring_info {
        struct vxge_hw_vpath_stats_sw_common_info common_stats;
        u32 rxd_t_code_err_cnt[VXGE_HW_DTR_MAX_T_CODE];
    }

.. _`vxge_hw_vpath_stats_sw_ring_info.members`:

Members
-------

common_stats
    Common counters for all queues

rxd_t_code_err_cnt
    Array of receive transfer codes. The position
    (index) in this array reflects the transfer code type,
    for instance
    0x7 - for "invalid receive buffer size", or 0x8 - for ECC.
    Value rxd_t_code_err_cnt[i] reflects the
    number of times the corresponding transfer code was encountered.

.. _`vxge_hw_vpath_stats_sw_ring_info.description`:

Description
-----------

HW ring counters

.. _`vxge_hw_vpath_stats_sw_ring_info.see-also`:

See also
--------

struct vxge_hw_vpath_stats_sw_common_info{},
struct vxge_hw_vpath_stats_sw_fifo_info{},

.. _`vxge_hw_vpath_stats_sw_err`:

struct vxge_hw_vpath_stats_sw_err
=================================

.. c:type:: struct vxge_hw_vpath_stats_sw_err

    HW vpath error statistics

.. _`vxge_hw_vpath_stats_sw_err.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_vpath_stats_sw_err {
        u32 unknown_alarms;
        u32 network_sustained_fault;
        u32 network_sustained_ok;
        u32 kdfcctl_fifo0_overwrite;
        u32 kdfcctl_fifo0_poison;
        u32 kdfcctl_fifo0_dma_error;
        u32 dblgen_fifo0_overflow;
        u32 statsb_pif_chain_error;
        u32 statsb_drop_timeout;
        u32 target_illegal_access;
        u32 ini_serr_det;
        u32 prc_ring_bumps;
        u32 prc_rxdcm_sc_err;
        u32 prc_rxdcm_sc_abort;
        u32 prc_quanta_size_err;
    }

.. _`vxge_hw_vpath_stats_sw_err.members`:

Members
-------

unknown_alarms
    *undescribed*

network_sustained_fault
    *undescribed*

network_sustained_ok
    *undescribed*

kdfcctl_fifo0_overwrite
    *undescribed*

kdfcctl_fifo0_poison
    *undescribed*

kdfcctl_fifo0_dma_error
    *undescribed*

dblgen_fifo0_overflow
    *undescribed*

statsb_pif_chain_error
    *undescribed*

statsb_drop_timeout
    *undescribed*

target_illegal_access
    *undescribed*

ini_serr_det
    *undescribed*

prc_ring_bumps
    *undescribed*

prc_rxdcm_sc_err
    *undescribed*

prc_rxdcm_sc_abort
    *undescribed*

prc_quanta_size_err
    *undescribed*

.. _`vxge_hw_vpath_stats_sw_err.description`:

Description
-----------

HW vpath error statistics

.. _`vxge_hw_vpath_stats_sw_info`:

struct vxge_hw_vpath_stats_sw_info
==================================

.. c:type:: struct vxge_hw_vpath_stats_sw_info

    HW vpath sw statistics

.. _`vxge_hw_vpath_stats_sw_info.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_vpath_stats_sw_info {
        u32 soft_reset_cnt;
        struct vxge_hw_vpath_stats_sw_err error_stats;
        struct vxge_hw_vpath_stats_sw_ring_info ring_stats;
        struct vxge_hw_vpath_stats_sw_fifo_info fifo_stats;
    }

.. _`vxge_hw_vpath_stats_sw_info.members`:

Members
-------

soft_reset_cnt
    Number of times soft reset is done on this vpath.

error_stats
    error counters for the vpath

ring_stats
    counters for ring belonging to the vpath

fifo_stats
    counters for fifo belonging to the vpath

.. _`vxge_hw_vpath_stats_sw_info.description`:

Description
-----------

HW vpath sw statistics

.. _`vxge_hw_vpath_stats_sw_info.see-also`:

See also
--------

struct vxge_hw_device_info{} }.

.. _`vxge_hw_device_stats_sw_info`:

struct vxge_hw_device_stats_sw_info
===================================

.. c:type:: struct vxge_hw_device_stats_sw_info

    HW own per-device statistics.

.. _`vxge_hw_device_stats_sw_info.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_device_stats_sw_info {
        u32 not_traffic_intr_cnt;
        u32 traffic_intr_cnt;
        u32 total_intr_cnt;
        u32 soft_reset_cnt;
        struct vxge_hw_vpath_stats_sw_infovpath_info[VXGE_HW_MAX_VIRTUAL_PATHS];
    }

.. _`vxge_hw_device_stats_sw_info.members`:

Members
-------

not_traffic_intr_cnt
    Number of times the host was interrupted
    without new completions.
    "Non-traffic interrupt counter".

traffic_intr_cnt
    Number of traffic interrupts for the device.

total_intr_cnt
    Total number of traffic interrupts for the device.
    \ ``total_intr_cnt``\  == \ ``traffic_intr_cnt``\  +
    \ ``not_traffic_intr_cnt``\ 

soft_reset_cnt
    Number of times soft reset is done on this device.

.. _`vxge_hw_device_stats_sw_err`:

struct vxge_hw_device_stats_sw_err
==================================

.. c:type:: struct vxge_hw_device_stats_sw_err

    HW device error statistics.

.. _`vxge_hw_device_stats_sw_err.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_device_stats_sw_err {
        u32 vpath_alarms;
    }

.. _`vxge_hw_device_stats_sw_err.members`:

Members
-------

vpath_alarms
    Number of vpath alarms

.. _`vxge_hw_device_stats_sw_err.description`:

Description
-----------

HW Device error stats

.. _`vxge_hw_device_stats`:

struct vxge_hw_device_stats
===========================

.. c:type:: struct vxge_hw_device_stats

    Contains HW per-device statistics, including hw.

.. _`vxge_hw_device_stats.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_device_stats {
        struct __vxge_hw_device *devh;
        struct vxge_hw_device_stats_hw_info hw_dev_info_stats;
        struct vxge_hw_device_stats_sw_err sw_dev_err_stats;
        struct vxge_hw_device_stats_sw_info sw_dev_info_stats;
    }

.. _`vxge_hw_device_stats.members`:

Members
-------

devh
    HW device handle.

hw_dev_info_stats
    Titan statistics maintained by the hardware.

sw_dev_err_stats
    HW's "soft" device error statistics.

sw_dev_info_stats
    HW's "soft" device informational statistics, e.g. number
    of completions per interrupt.

.. _`vxge_hw_device_stats.description`:

Description
-----------

Structure-container of HW per-device statistics. Note that per-channel
statistics are kept in separate structures under HW's fifo and ring
channels.

.. _`vxge_hw_mgmt_reg_type`:

enum vxge_hw_mgmt_reg_type
==========================

.. c:type:: enum vxge_hw_mgmt_reg_type

    Register types.

.. _`vxge_hw_mgmt_reg_type.definition`:

Definition
----------

.. code-block:: c

    enum vxge_hw_mgmt_reg_type {
        vxge_hw_mgmt_reg_type_legacy,
        vxge_hw_mgmt_reg_type_toc,
        vxge_hw_mgmt_reg_type_common,
        vxge_hw_mgmt_reg_type_mrpcim,
        vxge_hw_mgmt_reg_type_srpcim,
        vxge_hw_mgmt_reg_type_vpmgmt,
        vxge_hw_mgmt_reg_type_vpath
    };

.. _`vxge_hw_mgmt_reg_type.constants`:

Constants
---------

vxge_hw_mgmt_reg_type_legacy
    Legacy registers

vxge_hw_mgmt_reg_type_toc
    TOC Registers

vxge_hw_mgmt_reg_type_common
    Common Registers

vxge_hw_mgmt_reg_type_mrpcim
    mrpcim registers

vxge_hw_mgmt_reg_type_srpcim
    srpcim registers

vxge_hw_mgmt_reg_type_vpmgmt
    vpath management registers

vxge_hw_mgmt_reg_type_vpath
    vpath registers

.. _`vxge_hw_mgmt_reg_type.description`:

Description
-----------

Register type enumaration

.. _`vxge_hw_rxd_state`:

enum vxge_hw_rxd_state
======================

.. c:type:: enum vxge_hw_rxd_state

    Descriptor (RXD) state.

.. _`vxge_hw_rxd_state.definition`:

Definition
----------

.. code-block:: c

    enum vxge_hw_rxd_state {
        VXGE_HW_RXD_STATE_NONE,
        VXGE_HW_RXD_STATE_AVAIL,
        VXGE_HW_RXD_STATE_POSTED,
        VXGE_HW_RXD_STATE_FREED
    };

.. _`vxge_hw_rxd_state.constants`:

Constants
---------

VXGE_HW_RXD_STATE_NONE
    Invalid state.

VXGE_HW_RXD_STATE_AVAIL
    Descriptor is available for reservation.

VXGE_HW_RXD_STATE_POSTED
    Descriptor is posted for processing by the
    device.

VXGE_HW_RXD_STATE_FREED
    Descriptor is free and can be reused for
    filling-in and posting later.

.. _`vxge_hw_rxd_state.description`:

Description
-----------

Titan/HW descriptor states.

.. _`vxge_hw_ring_rxd_info`:

struct vxge_hw_ring_rxd_info
============================

.. c:type:: struct vxge_hw_ring_rxd_info

    Extended information associated with a completed ring descriptor.

.. _`vxge_hw_ring_rxd_info.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_ring_rxd_info {
        u32 syn_flag;
        u32 is_icmp;
        u32 fast_path_eligible;
        u32 l3_cksum_valid;
        u32 l3_cksum;
        u32 l4_cksum_valid;
        u32 l4_cksum;
        u32 frame;
        u32 proto;
        u32 is_vlan;
        u32 vlan;
        u32 rth_bucket;
        u32 rth_it_hit;
        u32 rth_spdm_hit;
        u32 rth_hash_type;
        u32 rth_value;
    }

.. _`vxge_hw_ring_rxd_info.members`:

Members
-------

syn_flag
    SYN flag

is_icmp
    Is ICMP

fast_path_eligible
    Fast Path Eligible flag

l3_cksum_valid
    *undescribed*

l3_cksum
    Result of IP checksum check (by Titan hardware).
    This field containing VXGE_HW_L3_CKSUM_OK would mean that
    the checksum is correct, otherwise - the datagram is
    corrupted.

l4_cksum_valid
    *undescribed*

l4_cksum
    Result of TCP/UDP checksum check (by Titan hardware).
    This field containing VXGE_HW_L4_CKSUM_OK would mean that
    the checksum is correct. Otherwise - the packet is
    corrupted.

frame
    Zero or more of enum vxge_hw_frame_type flags.
    See enum vxge_hw_frame_type{}.

proto
    zero or more of enum vxge_hw_frame_proto flags.  Reporting bits for
    various higher-layer protocols, including (but note restricted to)
    TCP and UDP. See enum vxge_hw_frame_proto{}.

is_vlan
    If vlan tag is valid

vlan
    VLAN tag extracted from the received frame.

rth_bucket
    RTH bucket

rth_it_hit
    Set, If RTH hash value calculated by the Titan hardware
    has a matching entry in the Indirection table.

rth_spdm_hit
    Set, If RTH hash value calculated by the Titan hardware
    has a matching entry in the Socket Pair Direct Match table.

rth_hash_type
    RTH hash code of the function used to calculate the hash.

rth_value
    Receive Traffic Hashing(RTH) hash value. Produced by Titan
    hardware if RTH is enabled.

.. _`vxge_hw_ring_tcode`:

enum vxge_hw_ring_tcode
=======================

.. c:type:: enum vxge_hw_ring_tcode

    Transfer codes returned by adapter

.. _`vxge_hw_ring_tcode.definition`:

Definition
----------

.. code-block:: c

    enum vxge_hw_ring_tcode {
        VXGE_HW_RING_T_CODE_OK,
        VXGE_HW_RING_T_CODE_L3_CKSUM_MISMATCH,
        VXGE_HW_RING_T_CODE_L4_CKSUM_MISMATCH,
        VXGE_HW_RING_T_CODE_L3_L4_CKSUM_MISMATCH,
        VXGE_HW_RING_T_CODE_L3_PKT_ERR,
        VXGE_HW_RING_T_CODE_L2_FRM_ERR,
        VXGE_HW_RING_T_CODE_BUF_SIZE_ERR,
        VXGE_HW_RING_T_CODE_INT_ECC_ERR,
        VXGE_HW_RING_T_CODE_BENIGN_OVFLOW,
        VXGE_HW_RING_T_CODE_ZERO_LEN_BUFF,
        VXGE_HW_RING_T_CODE_FRM_DROP,
        VXGE_HW_RING_T_CODE_UNUSED,
        VXGE_HW_RING_T_CODE_MULTI_ERR
    };

.. _`vxge_hw_ring_tcode.constants`:

Constants
---------

VXGE_HW_RING_T_CODE_OK
    Transfer ok.

VXGE_HW_RING_T_CODE_L3_CKSUM_MISMATCH
    Layer 3 checksum presentation
    configuration mismatch.

VXGE_HW_RING_T_CODE_L4_CKSUM_MISMATCH
    Layer 4 checksum presentation
    configuration mismatch.

VXGE_HW_RING_T_CODE_L3_L4_CKSUM_MISMATCH
    Layer 3 and Layer 4 checksum
    presentation configuration mismatch.

VXGE_HW_RING_T_CODE_L3_PKT_ERR
    Layer 3 error unparseable packet,
    such as unknown IPv6 header.

VXGE_HW_RING_T_CODE_L2_FRM_ERR
    Layer 2 error frame integrity
    error, such as FCS or ECC).

VXGE_HW_RING_T_CODE_BUF_SIZE_ERR
    Buffer size error the RxD buffer(
    s) were not appropriately sized and data loss occurred.

VXGE_HW_RING_T_CODE_INT_ECC_ERR
    Internal ECC error RxD corrupted.

VXGE_HW_RING_T_CODE_BENIGN_OVFLOW
    Benign overflow the contents of
    Segment1 exceeded the capacity of Buffer1 and the remainder
    was placed in Buffer2. Segment2 now starts in Buffer3.
    No data loss or errors occurred.

VXGE_HW_RING_T_CODE_ZERO_LEN_BUFF
    Buffer size 0 one of the RxDs
    assigned buffers has a size of 0 bytes.

VXGE_HW_RING_T_CODE_FRM_DROP
    Frame dropped either due to
    VPath Reset or because of a VPIN mismatch.

VXGE_HW_RING_T_CODE_UNUSED
    Unused

VXGE_HW_RING_T_CODE_MULTI_ERR
    Multiple errors more than one
    transfer code condition occurred.

.. _`vxge_hw_ring_tcode.description`:

Description
-----------

Transfer codes returned by adapter.

.. _`vxge_hw_frame_proto`:

enum vxge_hw_frame_proto
========================

.. c:type:: enum vxge_hw_frame_proto

    Higher-layer ethernet protocols.

.. _`vxge_hw_frame_proto.definition`:

Definition
----------

.. code-block:: c

    enum vxge_hw_frame_proto {
        VXGE_HW_FRAME_PROTO_VLAN_TAGGED,
        VXGE_HW_FRAME_PROTO_IPV4,
        VXGE_HW_FRAME_PROTO_IPV6,
        VXGE_HW_FRAME_PROTO_IP_FRAG,
        VXGE_HW_FRAME_PROTO_TCP,
        VXGE_HW_FRAME_PROTO_UDP,
        VXGE_HW_FRAME_PROTO_TCP_OR_UDP
    };

.. _`vxge_hw_frame_proto.constants`:

Constants
---------

VXGE_HW_FRAME_PROTO_VLAN_TAGGED
    VLAN.

VXGE_HW_FRAME_PROTO_IPV4
    IPv4.

VXGE_HW_FRAME_PROTO_IPV6
    IPv6.

VXGE_HW_FRAME_PROTO_IP_FRAG
    IP fragmented.

VXGE_HW_FRAME_PROTO_TCP
    TCP.

VXGE_HW_FRAME_PROTO_UDP
    UDP.

VXGE_HW_FRAME_PROTO_TCP_OR_UDP
    TCP or UDP.

.. _`vxge_hw_frame_proto.description`:

Description
-----------

Higher layer ethernet protocols and options.

.. _`vxge_hw_fifo_gather_code`:

enum vxge_hw_fifo_gather_code
=============================

.. c:type:: enum vxge_hw_fifo_gather_code

    Gather codes used in fifo TxD

.. _`vxge_hw_fifo_gather_code.definition`:

Definition
----------

.. code-block:: c

    enum vxge_hw_fifo_gather_code {
        VXGE_HW_FIFO_GATHER_CODE_FIRST,
        VXGE_HW_FIFO_GATHER_CODE_MIDDLE,
        VXGE_HW_FIFO_GATHER_CODE_LAST,
        VXGE_HW_FIFO_GATHER_CODE_FIRST_LAST
    };

.. _`vxge_hw_fifo_gather_code.constants`:

Constants
---------

VXGE_HW_FIFO_GATHER_CODE_FIRST
    First TxDL

VXGE_HW_FIFO_GATHER_CODE_MIDDLE
    Middle TxDL

VXGE_HW_FIFO_GATHER_CODE_LAST
    Last TxDL

VXGE_HW_FIFO_GATHER_CODE_FIRST_LAST
    First and Last TxDL.

.. _`vxge_hw_fifo_gather_code.description`:

Description
-----------

These gather codes are used to indicate the position of a TxD in a TxD list

.. _`vxge_hw_fifo_tcode`:

enum vxge_hw_fifo_tcode
=======================

.. c:type:: enum vxge_hw_fifo_tcode

    tcodes used in fifo

.. _`vxge_hw_fifo_tcode.definition`:

Definition
----------

.. code-block:: c

    enum vxge_hw_fifo_tcode {
        VXGE_HW_FIFO_T_CODE_OK,
        VXGE_HW_FIFO_T_CODE_PCI_READ_CORRUPT,
        VXGE_HW_FIFO_T_CODE_PCI_READ_FAIL,
        VXGE_HW_FIFO_T_CODE_INVALID_MSS,
        VXGE_HW_FIFO_T_CODE_LSO_ERROR,
        VXGE_HW_FIFO_T_CODE_UNUSED,
        VXGE_HW_FIFO_T_CODE_MULTI_ERROR
    };

.. _`vxge_hw_fifo_tcode.constants`:

Constants
---------

VXGE_HW_FIFO_T_CODE_OK
    Transfer OK

VXGE_HW_FIFO_T_CODE_PCI_READ_CORRUPT
    PCI read transaction (either TxD or
    frame data) returned with corrupt data.

VXGE_HW_FIFO_T_CODE_PCI_READ_FAIL
    PCI read transaction was returned
    with no data.

VXGE_HW_FIFO_T_CODE_INVALID_MSS
    The host attempted to send either a
    frame or LSO MSS that was too long (>9800B).

VXGE_HW_FIFO_T_CODE_LSO_ERROR
    Error detected during TCP/UDP Large Send
    Offload operation, due to improper header template,
    unsupported protocol, etc.

VXGE_HW_FIFO_T_CODE_UNUSED
    Unused

VXGE_HW_FIFO_T_CODE_MULTI_ERROR
    Set to 1 by the adapter if multiple
    data buffer transfer errors are encountered (see below).
    Otherwise it is set to 0.

.. _`vxge_hw_fifo_tcode.description`:

Description
-----------

These tcodes are returned in various API for TxD status

.. This file was automatic generated / don't edit.

