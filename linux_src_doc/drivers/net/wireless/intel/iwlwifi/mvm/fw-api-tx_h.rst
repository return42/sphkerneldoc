.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/fw-api-tx.h

.. _`iwl_tx_flags`:

enum iwl_tx_flags
=================

.. c:type:: enum iwl_tx_flags

    bitmasks for tx_flags in TX command

.. _`iwl_tx_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tx_flags {
        TX_CMD_FLG_PROT_REQUIRE,
        TX_CMD_FLG_WRITE_TX_POWER,
        TX_CMD_FLG_ACK,
        TX_CMD_FLG_STA_RATE,
        TX_CMD_FLG_BAR,
        TX_CMD_FLG_TXOP_PROT,
        TX_CMD_FLG_VHT_NDPA,
        TX_CMD_FLG_HT_NDPA,
        TX_CMD_FLG_CSI_FDBK2HOST,
        TX_CMD_FLG_BT_PRIO_POS,
        TX_CMD_FLG_BT_DIS,
        TX_CMD_FLG_SEQ_CTL,
        TX_CMD_FLG_MORE_FRAG,
        TX_CMD_FLG_TSF,
        TX_CMD_FLG_CALIB,
        TX_CMD_FLG_KEEP_SEQ_CTL,
        TX_CMD_FLG_MH_PAD,
        TX_CMD_FLG_RESP_TO_DRV,
        TX_CMD_FLG_TKIP_MIC_DONE,
        TX_CMD_FLG_DUR,
        TX_CMD_FLG_FW_DROP,
        TX_CMD_FLG_EXEC_PAPD,
        TX_CMD_FLG_PAPD_TYPE,
        TX_CMD_FLG_HCCA_CHUNK
    };

.. _`iwl_tx_flags.constants`:

Constants
---------

TX_CMD_FLG_PROT_REQUIRE
    use RTS or CTS-to-self to protect the frame

TX_CMD_FLG_WRITE_TX_POWER
    update current tx power value in the mgmt frame

TX_CMD_FLG_ACK
    expect ACK from receiving station

TX_CMD_FLG_STA_RATE
    use RS table with initial index from the TX command.
    Otherwise, use rate_n_flags from the TX command

TX_CMD_FLG_BAR
    this frame is a BA request, immediate BAR is expected
    Must set TX_CMD_FLG_ACK with this flag.

TX_CMD_FLG_TXOP_PROT
    *undescribed*

TX_CMD_FLG_VHT_NDPA
    mark frame is NDPA for VHT beamformer sequence

TX_CMD_FLG_HT_NDPA
    mark frame is NDPA for HT beamformer sequence

TX_CMD_FLG_CSI_FDBK2HOST
    mark to send feedback to host (only if good CRC)

TX_CMD_FLG_BT_PRIO_POS
    the position of the BT priority (bit 11 is ignored
    on old firmwares).

TX_CMD_FLG_BT_DIS
    disable BT priority for this frame

TX_CMD_FLG_SEQ_CTL
    set if FW should override the sequence control.
    Should be set for mgmt, non-QOS data, mcast, bcast and in scan command

TX_CMD_FLG_MORE_FRAG
    this frame is non-last MPDU

TX_CMD_FLG_TSF
    FW should calculate and insert TSF in the frame
    Should be set for beacons and probe responses

TX_CMD_FLG_CALIB
    activate PA TX power calibrations

TX_CMD_FLG_KEEP_SEQ_CTL
    if seq_ctl is set, don't increase inner seq count

TX_CMD_FLG_MH_PAD
    driver inserted 2 byte padding after MAC header.
    Should be set for 26/30 length MAC headers

TX_CMD_FLG_RESP_TO_DRV
    zero this if the response should go only to FW

TX_CMD_FLG_TKIP_MIC_DONE
    FW already performed TKIP MIC calculation

TX_CMD_FLG_DUR
    disable duration overwriting used in PS-Poll Assoc-id

TX_CMD_FLG_FW_DROP
    FW should mark frame to be dropped

TX_CMD_FLG_EXEC_PAPD
    execute PAPD

TX_CMD_FLG_PAPD_TYPE
    0 for reference power, 1 for nominal power

TX_CMD_FLG_HCCA_CHUNK
    mark start of TSPEC chunk

.. _`iwl_tx_pm_timeouts`:

enum iwl_tx_pm_timeouts
=======================

.. c:type:: enum iwl_tx_pm_timeouts

    pm timeout values in TX command

.. _`iwl_tx_pm_timeouts.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tx_pm_timeouts {
        PM_FRAME_NONE,
        PM_FRAME_MGMT,
        PM_FRAME_ASSOC
    };

.. _`iwl_tx_pm_timeouts.constants`:

Constants
---------

PM_FRAME_NONE
    no need to suspend sleep mode

PM_FRAME_MGMT
    fw suspend sleep mode for 100TU

PM_FRAME_ASSOC
    fw suspend sleep mode for 10sec

.. _`iwl_tx_cmd_sec_ctrl`:

enum iwl_tx_cmd_sec_ctrl
========================

.. c:type:: enum iwl_tx_cmd_sec_ctrl

    bitmasks for security control in TX command

.. _`iwl_tx_cmd_sec_ctrl.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tx_cmd_sec_ctrl {
        TX_CMD_SEC_WEP,
        TX_CMD_SEC_CCM,
        TX_CMD_SEC_TKIP,
        TX_CMD_SEC_EXT,
        TX_CMD_SEC_GCMP,
        TX_CMD_SEC_KEY128,
        TX_CMD_SEC_KEY_FROM_TABLE
    };

.. _`iwl_tx_cmd_sec_ctrl.constants`:

Constants
---------

TX_CMD_SEC_WEP
    WEP encryption algorithm.

TX_CMD_SEC_CCM
    CCM encryption algorithm.

TX_CMD_SEC_TKIP
    TKIP encryption algorithm.

TX_CMD_SEC_EXT
    extended cipher algorithm.

TX_CMD_SEC_GCMP
    GCMP encryption algorithm.

TX_CMD_SEC_KEY128
    set for 104 bits WEP key.

TX_CMD_SEC_KEY_FROM_TABLE
    for a non-WEP key, set if the key should be taken
    from the table instead of from the TX command.
    If the key is taken from the key table its index should be given by the
    first byte of the TX command key field.

.. _`iwl_tx_offload_assist_flags_pos`:

enum iwl_tx_offload_assist_flags_pos
====================================

.. c:type:: enum iwl_tx_offload_assist_flags_pos

    set \ ``iwl_tx_cmd``\  offload_assist values

.. _`iwl_tx_offload_assist_flags_pos.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tx_offload_assist_flags_pos {
        TX_CMD_OFFLD_IP_HDR,
        TX_CMD_OFFLD_L4_EN,
        TX_CMD_OFFLD_L3_EN,
        TX_CMD_OFFLD_MH_SIZE,
        TX_CMD_OFFLD_PAD,
        TX_CMD_OFFLD_AMSDU
    };

.. _`iwl_tx_offload_assist_flags_pos.constants`:

Constants
---------

TX_CMD_OFFLD_IP_HDR
    *undescribed*

TX_CMD_OFFLD_L4_EN
    enable TCP/UDP checksum

TX_CMD_OFFLD_L3_EN
    enable IP header checksum

TX_CMD_OFFLD_MH_SIZE
    size of the mac header in words. Includes the IV
    field. Doesn't include the pad.

TX_CMD_OFFLD_PAD
    mark 2-byte pad was inserted after the mac header for
    alignment

TX_CMD_OFFLD_AMSDU
    mark TX command is A-MSDU

.. _`iwl_tx_offload_assist_flags_pos.note`:

note
----

tx_cmd, mac header and pad are not counted in the offset.
This is used to help the offload in case there is tunneling such as
IPv6 in IPv4, in such case the ip header offset should point to the
inner ip header and IPv4 checksum of the external header should be
calculated by driver.

.. _`iwl_tx_cmd`:

struct iwl_tx_cmd
=================

.. c:type:: struct iwl_tx_cmd

    TX command struct to FW ( TX_CMD = 0x1c )

.. _`iwl_tx_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tx_cmd {
        __le16 len;
        __le16 offload_assist;
        __le32 tx_flags;
        struct scratch;
        __le32 rate_n_flags;
        u8 sta_id;
        u8 sec_ctl;
        u8 initial_rate_index;
        u8 reserved2;
        u8 key[16];
        __le32 reserved3;
        __le32 life_time;
        __le32 dram_lsb_ptr;
        u8 dram_msb_ptr;
        u8 rts_retry_limit;
        u8 data_retry_limit;
        u8 tid_tspec;
        __le16 pm_frame_timeout;
        __le16 reserved4;
        u8 payload[0];
        struct ieee80211_hdr hdr[0];
    }

.. _`iwl_tx_cmd.members`:

Members
-------

len
    in bytes of the payload, see below for details

offload_assist
    TX offload configuration

tx_flags
    combination of TX_CMD_FLG\_\*

scratch
    *undescribed*

rate_n_flags
    rate for \*all\* Tx attempts, if TX_CMD_FLG_STA_RATE_MSK is
    cleared. Combination of RATE_MCS\_\*

sta_id
    index of destination station in FW station table

sec_ctl
    security control, TX_CMD_SEC\_\*

initial_rate_index
    index into the the rate table for initial TX attempt.
    Applied if TX_CMD_FLG_STA_RATE_MSK is set, normally 0 for data frames.

reserved2
    *undescribed*

key
    security key

reserved3
    *undescribed*

life_time
    frame life time (usecs??)

dram_lsb_ptr
    Physical address of scratch area in the command (try_cnt +
    btkill_cnd + reserved), first 32 bits. "0" disables usage.

dram_msb_ptr
    upper bits of the scratch physical address

rts_retry_limit
    max attempts for RTS

data_retry_limit
    max attempts to send the data packet

tid_tspec
    *undescribed*

pm_frame_timeout
    PM TX frame timeout

reserved4
    *undescribed*

.. _`iwl_tx_cmd.description`:

Description
-----------

The byte count (both len and next_frame_len) includes MAC header
(24/26/30/32 bytes)
+ 2 bytes pad if 26/30 header size
+ 8 byte IV for CCM or TKIP (not used for WEP)
+ Data payload
+ 8-byte MIC (not used for CCM/WEP)
It does not include post-MAC padding, i.e.,
MIC (CCM) 8 bytes, ICV (WEP/TKIP/CKIP) 4 bytes, CRC 4 bytes.

.. _`iwl_tx_cmd.range-of-len`:

Range of len
------------

14-2342 bytes.

After the struct fields the MAC header is placed, plus any padding,
and then the actial payload.

.. _`agg_tx_status`:

struct agg_tx_status
====================

.. c:type:: struct agg_tx_status

    per packet TX aggregation status

.. _`agg_tx_status.definition`:

Definition
----------

.. code-block:: c

    struct agg_tx_status {
        __le16 status;
        __le16 sequence;
    }

.. _`agg_tx_status.members`:

Members
-------

status
    enum iwl_tx_agg_status

sequence
    Sequence # for this frame's Tx cmd (not SSN!)

.. _`iwl_mvm_tx_resp`:

struct iwl_mvm_tx_resp
======================

.. c:type:: struct iwl_mvm_tx_resp

    notifies that fw is TXing a packet ( REPLY_TX = 0x1c )

.. _`iwl_mvm_tx_resp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_tx_resp {
        u8 frame_count;
        u8 bt_kill_count;
        u8 failure_rts;
        u8 failure_frame;
        __le32 initial_rate;
        __le16 wireless_media_time;
        u8 pa_status;
        u8 pa_integ_res_a[3];
        u8 pa_integ_res_b[3];
        u8 pa_integ_res_c[3];
        __le16 measurement_req_id;
        u8 reduced_tpc;
        u8 reserved;
        __le32 tfd_info;
        __le16 seq_ctl;
        __le16 byte_cnt;
        u8 tlc_info;
        u8 ra_tid;
        __le16 frame_ctrl;
        struct agg_tx_status status;
    }

.. _`iwl_mvm_tx_resp.members`:

Members
-------

frame_count
    1 no aggregation, >1 aggregation

bt_kill_count
    num of times blocked by bluetooth (unused for agg)

failure_rts
    num of failures due to unsuccessful RTS

failure_frame
    num failures due to no ACK (unused for agg)

initial_rate
    for non-agg: rate of the successful Tx. For agg: rate of the
    Tx of all the batch. RATE_MCS\_\*

wireless_media_time
    for non-agg: RTS + CTS + frame tx attempts time + ACK.

pa_status
    tx power info

pa_integ_res_a
    tx power info

pa_integ_res_b
    tx power info

pa_integ_res_c
    tx power info

measurement_req_id
    tx power info

reduced_tpc
    *undescribed*

reserved
    *undescribed*

tfd_info
    TFD information set by the FH

seq_ctl
    sequence control from the Tx cmd

byte_cnt
    byte count from the Tx cmd

tlc_info
    TLC rate info

ra_tid
    bits [3:0] = ra, bits [7:4] = tid

frame_ctrl
    frame control

status
    for non-agg:  frame status TX_STATUS\_\*

.. _`iwl_mvm_tx_resp.for-agg`:

for agg
-------

RTS + CTS + aggregation tx time + block-ack time.
in usec.

status of 1st frame, AGG_TX_STATE\_\*; other frame status fields
follow this one, up to frame_count.

After the array of statuses comes the SSN of the SCD. Look at
\ ``iwl_mvm_get_scd_ssn``\  for more details.

.. _`iwl_mvm_ba_notif`:

struct iwl_mvm_ba_notif
=======================

.. c:type:: struct iwl_mvm_ba_notif

    notifies about reception of BA ( BA_NOTIF = 0xc5 )

.. _`iwl_mvm_ba_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_ba_notif {
        __le32 sta_addr_lo32;
        __le16 sta_addr_hi16;
        __le16 reserved;
        u8 sta_id;
        u8 tid;
        __le16 seq_ctl;
        __le64 bitmap;
        __le16 scd_flow;
        __le16 scd_ssn;
        u8 txed;
        u8 txed_2_done;
        u8 reduced_txp;
        u8 reserved1;
    }

.. _`iwl_mvm_ba_notif.members`:

Members
-------

sta_addr_lo32
    lower 32 bits of the MAC address

sta_addr_hi16
    upper 16 bits of the MAC address

reserved
    *undescribed*

sta_id
    Index of recipient (BA-sending) station in fw's station table

tid
    tid of the session

seq_ctl
    *undescribed*

bitmap
    the bitmap of the BA notification as seen in the air

scd_flow
    the tx queue this BA relates to

scd_ssn
    the index of the last contiguously sent packet

txed
    number of Txed frames in this batch

txed_2_done
    number of Acked frames in this batch

reduced_txp
    power reduced according to TPC. This is the actual value and
    not a copy from the LQ command. Thus, if not the first rate was used
    for Tx-ing then this value will be set to 0 by FW.

reserved1
    *undescribed*

.. _`iwl_mvm_compressed_ba_tfd`:

struct iwl_mvm_compressed_ba_tfd
================================

.. c:type:: struct iwl_mvm_compressed_ba_tfd

    progress of a TFD queue

.. _`iwl_mvm_compressed_ba_tfd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_compressed_ba_tfd {
        u8 q_num;
        u8 reserved;
        __le16 tfd_index;
    }

.. _`iwl_mvm_compressed_ba_tfd.members`:

Members
-------

q_num
    TFD queue number

reserved
    *undescribed*

tfd_index
    Index of first un-acked frame in the  TFD queue

.. _`iwl_mvm_compressed_ba_ratid`:

struct iwl_mvm_compressed_ba_ratid
==================================

.. c:type:: struct iwl_mvm_compressed_ba_ratid

    progress of a RA TID queue

.. _`iwl_mvm_compressed_ba_ratid.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_compressed_ba_ratid {
        u8 q_num;
        u8 tid;
        __le16 ssn;
    }

.. _`iwl_mvm_compressed_ba_ratid.members`:

Members
-------

q_num
    RA TID queue number

tid
    TID of the queue

ssn
    BA window current SSN

.. _`iwl_mvm_compressed_ba_notif`:

struct iwl_mvm_compressed_ba_notif
==================================

.. c:type:: struct iwl_mvm_compressed_ba_notif

    notifies about reception of BA ( BA_NOTIF = 0xc5 )

.. _`iwl_mvm_compressed_ba_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_compressed_ba_notif {
        __le32 flags;
        u8 sta_id;
        u8 reduced_txp;
        u8 initial_rate;
        u8 retry_cnt;
        __le32 query_byte_cnt;
        __le16 query_frame_cnt;
        __le16 txed;
        __le16 done;
        __le32 wireless_time;
        __le32 tx_rate;
        __le16 tfd_cnt;
        __le16 ra_tid_cnt;
        struct iwl_mvm_compressed_ba_tfd tfd[1];
        struct iwl_mvm_compressed_ba_ratid ra_tid[0];
    }

.. _`iwl_mvm_compressed_ba_notif.members`:

Members
-------

flags
    status flag, see the \ :c:type:`struct iwl_mvm_ba_resp_flags <iwl_mvm_ba_resp_flags>`\ 

sta_id
    Index of recipient (BA-sending) station in fw's station table

reduced_txp
    power reduced according to TPC. This is the actual value and
    not a copy from the LQ command. Thus, if not the first rate was used
    for Tx-ing then this value will be set to 0 by FW.

initial_rate
    TLC rate info, initial rate index, TLC table color

retry_cnt
    retry count

query_byte_cnt
    SCD query byte count

query_frame_cnt
    SCD query frame count

txed
    number of frames sent in the aggregation (all-TIDs)

done
    number of frames that were Acked by the BA (all-TIDs)

wireless_time
    Wireless-media time

tx_rate
    the rate the aggregation was sent at

tfd_cnt
    number of TFD-Q elements

ra_tid_cnt
    number of RATID-Q elements

.. _`iwl_mac_beacon_cmd_v6`:

struct iwl_mac_beacon_cmd_v6
============================

.. c:type:: struct iwl_mac_beacon_cmd_v6

    beacon template command

.. _`iwl_mac_beacon_cmd_v6.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mac_beacon_cmd_v6 {
        struct iwl_tx_cmd tx;
        __le32 template_id;
        __le32 tim_idx;
        __le32 tim_size;
        struct ieee80211_hdr frame[0];
    }

.. _`iwl_mac_beacon_cmd_v6.members`:

Members
-------

tx
    the tx commands associated with the beacon frame

template_id
    currently equal to the mac context id of the coresponding
    mac.

tim_idx
    the offset of the tim IE in the beacon

tim_size
    the length of the tim IE

frame
    the template of the beacon frame

.. _`iwl_mac_beacon_cmd`:

struct iwl_mac_beacon_cmd
=========================

.. c:type:: struct iwl_mac_beacon_cmd

    beacon template command with offloaded CSA

.. _`iwl_mac_beacon_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mac_beacon_cmd {
        struct iwl_tx_cmd tx;
        __le32 template_id;
        __le32 tim_idx;
        __le32 tim_size;
        __le32 ecsa_offset;
        __le32 csa_offset;
        struct ieee80211_hdr frame[0];
    }

.. _`iwl_mac_beacon_cmd.members`:

Members
-------

tx
    the tx commands associated with the beacon frame

template_id
    currently equal to the mac context id of the coresponding
    mac.

tim_idx
    the offset of the tim IE in the beacon

tim_size
    the length of the tim IE

ecsa_offset
    offset to the ECSA IE if present

csa_offset
    offset to the CSA IE if present

frame
    the template of the beacon frame

.. _`iwl_extended_beacon_notif`:

struct iwl_extended_beacon_notif
================================

.. c:type:: struct iwl_extended_beacon_notif

    notifies about beacon transmission

.. _`iwl_extended_beacon_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_extended_beacon_notif {
        struct iwl_mvm_tx_resp beacon_notify_hdr;
        __le64 tsf;
        __le32 ibss_mgr_status;
        __le32 gp2;
    }

.. _`iwl_extended_beacon_notif.members`:

Members
-------

beacon_notify_hdr
    tx response command associated with the beacon

tsf
    last beacon tsf

ibss_mgr_status
    whether IBSS is manager

gp2
    last beacon time in gp2

.. _`iwl_dump_control`:

enum iwl_dump_control
=====================

.. c:type:: enum iwl_dump_control

    dump (flush) control flags

.. _`iwl_dump_control.definition`:

Definition
----------

.. code-block:: c

    enum iwl_dump_control {
        DUMP_TX_FIFO_FLUSH
    };

.. _`iwl_dump_control.constants`:

Constants
---------

DUMP_TX_FIFO_FLUSH
    Dump MSDUs until the the FIFO is empty
    and the TFD queues are empty.

.. _`iwl_tx_path_flush_cmd`:

struct iwl_tx_path_flush_cmd
============================

.. c:type:: struct iwl_tx_path_flush_cmd

    - queue/FIFO flush command

.. _`iwl_tx_path_flush_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tx_path_flush_cmd {
        __le32 queues_ctl;
        __le16 flush_ctl;
        __le16 reserved;
    }

.. _`iwl_tx_path_flush_cmd.members`:

Members
-------

queues_ctl
    bitmap of queues to flush

flush_ctl
    control flags

reserved
    reserved

.. _`iwl_mvm_get_scd_ssn`:

iwl_mvm_get_scd_ssn
===================

.. c:function:: u32 iwl_mvm_get_scd_ssn(struct iwl_mvm_tx_resp *tx_resp)

    returns the SSN of the SCD

    :param struct iwl_mvm_tx_resp \*tx_resp:
        the Tx response from the fw (agg or non-agg)

.. _`iwl_mvm_get_scd_ssn.description`:

Description
-----------

When the fw sends an AMPDU, it fetches the MPDUs one after the other. Since
it can't know that everything will go well until the end of the AMPDU, it
can't know in advance the number of MPDUs that will be sent in the current
batch. This is why it writes the agg Tx response while it fetches the MPDUs.
Hence, it can't know in advance what the SSN of the SCD will be at the end
of the batch. This is why the SSN of the SCD is written at the end of the
whole struct at a variable offset. This function knows how to cope with the
variable offset and returns the SSN of the SCD.

.. _`iwl_scd_txq_cfg_cmd`:

struct iwl_scd_txq_cfg_cmd
==========================

.. c:type:: struct iwl_scd_txq_cfg_cmd

    New txq hw scheduler config command

.. _`iwl_scd_txq_cfg_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scd_txq_cfg_cmd {
        u8 token;
        u8 sta_id;
        u8 tid;
        u8 scd_queue;
        u8 action;
        u8 aggregate;
        u8 tx_fifo;
        u8 window;
        __le16 ssn;
        __le16 reserved;
    }

.. _`iwl_scd_txq_cfg_cmd.members`:

Members
-------

token
    *undescribed*

sta_id
    station id

tid
    *undescribed*

scd_queue
    scheduler queue to confiug

action
    1 queue enable, 0 queue disable, 2 change txq's tid owner
    Value is one of \ ``iwl_scd_cfg_actions``\  options

aggregate
    1 aggregated queue, 0 otherwise

tx_fifo
    %enum iwl_mvm_tx_fifo

window
    BA window size

ssn
    SSN for the BA agreement

reserved
    *undescribed*

.. _`iwl_scd_txq_cfg_rsp`:

struct iwl_scd_txq_cfg_rsp
==========================

.. c:type:: struct iwl_scd_txq_cfg_rsp


.. _`iwl_scd_txq_cfg_rsp.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scd_txq_cfg_rsp {
        u8 token;
        u8 sta_id;
        u8 tid;
        u8 scd_queue;
    }

.. _`iwl_scd_txq_cfg_rsp.members`:

Members
-------

token
    taken from the command

sta_id
    station id from the command

tid
    tid from the command

scd_queue
    scd_queue from the command

.. This file was automatic generated / don't edit.

