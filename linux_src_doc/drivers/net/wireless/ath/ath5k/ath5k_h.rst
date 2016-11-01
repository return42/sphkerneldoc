.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/ath5k.h

.. _`ath5k_version`:

enum ath5k_version
==================

.. c:type:: enum ath5k_version

    MAC Chips

.. _`ath5k_version.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_version {
        AR5K_AR5210,
        AR5K_AR5211,
        AR5K_AR5212
    };

.. _`ath5k_version.constants`:

Constants
---------

AR5K_AR5210
    AR5210 (Crete)

AR5K_AR5211
    AR5211 (Oahu/Maui)

AR5K_AR5212
    AR5212 (Venice) and newer

.. _`ath5k_radio`:

enum ath5k_radio
================

.. c:type:: enum ath5k_radio

    PHY Chips

.. _`ath5k_radio.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_radio {
        AR5K_RF5110,
        AR5K_RF5111,
        AR5K_RF5112,
        AR5K_RF2413,
        AR5K_RF5413,
        AR5K_RF2316,
        AR5K_RF2317,
        AR5K_RF2425
    };

.. _`ath5k_radio.constants`:

Constants
---------

AR5K_RF5110
    RF5110 (Fez)

AR5K_RF5111
    RF5111 (Sombrero)

AR5K_RF5112
    RF2112/5112(A) (Derby/Derby2)

AR5K_RF2413
    RF2413/2414 (Griffin/Griffin-Lite)

AR5K_RF5413
    RF5413/5414/5424 (Eagle/Condor)

AR5K_RF2316
    RF2315/2316 (Cobra SoC)

AR5K_RF2317
    RF2317 (Spider SoC)

AR5K_RF2425
    RF2425/2417 (Swan/Nalla)

.. _`ath5k_driver_mode`:

enum ath5k_driver_mode
======================

.. c:type:: enum ath5k_driver_mode

    PHY operation mode

.. _`ath5k_driver_mode.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_driver_mode {
        AR5K_MODE_11A,
        AR5K_MODE_11B,
        AR5K_MODE_11G,
        AR5K_MODE_MAX
    };

.. _`ath5k_driver_mode.constants`:

Constants
---------

AR5K_MODE_11A
    802.11a

AR5K_MODE_11B
    802.11b

AR5K_MODE_11G
    801.11g

AR5K_MODE_MAX
    Used for boundary checks

.. _`ath5k_driver_mode.description`:

Description
-----------

Do not change the order here, we use these as
array indices and it also maps EEPROM structures.

.. _`ath5k_ant_mode`:

enum ath5k_ant_mode
===================

.. c:type:: enum ath5k_ant_mode

    Antenna operation mode

.. _`ath5k_ant_mode.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_ant_mode {
        AR5K_ANTMODE_DEFAULT,
        AR5K_ANTMODE_FIXED_A,
        AR5K_ANTMODE_FIXED_B,
        AR5K_ANTMODE_SINGLE_AP,
        AR5K_ANTMODE_SECTOR_AP,
        AR5K_ANTMODE_SECTOR_STA,
        AR5K_ANTMODE_DEBUG,
        AR5K_ANTMODE_MAX
    };

.. _`ath5k_ant_mode.constants`:

Constants
---------

AR5K_ANTMODE_DEFAULT
    Default antenna setup

AR5K_ANTMODE_FIXED_A
    Only antenna A is present

AR5K_ANTMODE_FIXED_B
    Only antenna B is present

AR5K_ANTMODE_SINGLE_AP
    STA locked on a single ap

AR5K_ANTMODE_SECTOR_AP
    AP with tx antenna set on tx desc

AR5K_ANTMODE_SECTOR_STA
    STA with tx antenna set on tx desc

AR5K_ANTMODE_DEBUG
    Debug mode -A -> Rx, B-> Tx-

AR5K_ANTMODE_MAX
    Used for boundary checks

.. _`ath5k_ant_mode.description`:

Description
-----------

For more infos on antenna control check out phy.c

.. _`ath5k_bw_mode`:

enum ath5k_bw_mode
==================

.. c:type:: enum ath5k_bw_mode

    Bandwidth operation mode

.. _`ath5k_bw_mode.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_bw_mode {
        AR5K_BWMODE_DEFAULT,
        AR5K_BWMODE_5MHZ,
        AR5K_BWMODE_10MHZ,
        AR5K_BWMODE_40MHZ
    };

.. _`ath5k_bw_mode.constants`:

Constants
---------

AR5K_BWMODE_DEFAULT
    20MHz, default operation

AR5K_BWMODE_5MHZ
    Quarter rate

AR5K_BWMODE_10MHZ
    Half rate

AR5K_BWMODE_40MHZ
    Turbo

.. _`ath5k_tx_status`:

struct ath5k_tx_status
======================

.. c:type:: struct ath5k_tx_status

    TX Status descriptor

.. _`ath5k_tx_status.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_tx_status {
        u16 ts_seqnum;
        u16 ts_tstamp;
        u8 ts_status;
        u8 ts_final_idx;
        u8 ts_final_retry;
        s8 ts_rssi;
        u8 ts_shortretry;
        u8 ts_virtcol;
        u8 ts_antenna;
    }

.. _`ath5k_tx_status.members`:

Members
-------

ts_seqnum
    Sequence number

ts_tstamp
    Timestamp

ts_status
    Status code

ts_final_idx
    Final transmission series index

ts_final_retry
    Final retry count

ts_rssi
    RSSI for received ACK

ts_shortretry
    Short retry count

ts_virtcol
    Virtual collision count

ts_antenna
    Antenna used

.. _`ath5k_tx_status.description`:

Description
-----------

TX status descriptor gets filled by the hw
on each transmission attempt.

.. _`ath5k_tx_queue`:

enum ath5k_tx_queue
===================

.. c:type:: enum ath5k_tx_queue

    Queue types used to classify tx queues.

.. _`ath5k_tx_queue.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_tx_queue {
        AR5K_TX_QUEUE_INACTIVE,
        AR5K_TX_QUEUE_DATA,
        AR5K_TX_QUEUE_BEACON,
        AR5K_TX_QUEUE_CAB,
        AR5K_TX_QUEUE_UAPSD
    };

.. _`ath5k_tx_queue.constants`:

Constants
---------

AR5K_TX_QUEUE_INACTIVE
    q is unused -- see ath5k_hw_release_tx_queue

AR5K_TX_QUEUE_DATA
    A normal data queue

AR5K_TX_QUEUE_BEACON
    The beacon queue

AR5K_TX_QUEUE_CAB
    The after-beacon queue

AR5K_TX_QUEUE_UAPSD
    Unscheduled Automatic Power Save Delivery queue

.. _`ath5k_tx_queue_subtype`:

enum ath5k_tx_queue_subtype
===========================

.. c:type:: enum ath5k_tx_queue_subtype

    Queue sub-types to classify normal data queues

.. _`ath5k_tx_queue_subtype.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_tx_queue_subtype {
        AR5K_WME_AC_BK,
        AR5K_WME_AC_BE,
        AR5K_WME_AC_VI,
        AR5K_WME_AC_VO
    };

.. _`ath5k_tx_queue_subtype.constants`:

Constants
---------

AR5K_WME_AC_BK
    Background traffic

AR5K_WME_AC_BE
    Best-effort (normal) traffic

AR5K_WME_AC_VI
    Video traffic

AR5K_WME_AC_VO
    Voice traffic

.. _`ath5k_tx_queue_subtype.description`:

Description
-----------

These are the 4 Access Categories as defined in
WME spec. 0 is the lowest priority and 4 is the
highest. Normal data that hasn't been classified
goes to the Best Effort AC.

.. _`ath5k_tx_queue_id`:

enum ath5k_tx_queue_id
======================

.. c:type:: enum ath5k_tx_queue_id

    Queue ID numbers as returned by the hw functions

.. _`ath5k_tx_queue_id.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_tx_queue_id {
        AR5K_TX_QUEUE_ID_NOQCU_DATA,
        AR5K_TX_QUEUE_ID_NOQCU_BEACON,
        AR5K_TX_QUEUE_ID_DATA_MIN,
        AR5K_TX_QUEUE_ID_DATA_MAX,
        AR5K_TX_QUEUE_ID_UAPSD,
        AR5K_TX_QUEUE_ID_CAB,
        AR5K_TX_QUEUE_ID_BEACON
    };

.. _`ath5k_tx_queue_id.constants`:

Constants
---------

AR5K_TX_QUEUE_ID_NOQCU_DATA
    Data queue on AR5210 (no QCU available)

AR5K_TX_QUEUE_ID_NOQCU_BEACON
    Beacon queue on AR5210 (no QCU available)

AR5K_TX_QUEUE_ID_DATA_MIN
    Data queue min index

AR5K_TX_QUEUE_ID_DATA_MAX
    Data queue max index

AR5K_TX_QUEUE_ID_UAPSD
    Urgent Automatic Power Save Delivery,

AR5K_TX_QUEUE_ID_CAB
    Content after beacon queue

AR5K_TX_QUEUE_ID_BEACON
    Beacon queue

.. _`ath5k_tx_queue_id.description`:

Description
-----------

Each number represents a hw queue. If hw does not support hw queues
(eg 5210) all data goes in one queue.

.. _`ath5k_txq`:

struct ath5k_txq
================

.. c:type:: struct ath5k_txq

    Transmit queue state

.. _`ath5k_txq.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_txq {
        unsigned int qnum;
        u32 *link;
        struct list_head q;
        spinlock_t lock;
        bool setup;
        int txq_len;
        int txq_max;
        bool txq_poll_mark;
        unsigned int txq_stuck;
    }

.. _`ath5k_txq.members`:

Members
-------

qnum
    Hardware q number

link
    Link ptr in last TX desc

q
    Transmit queue (&struct list_head)

lock
    Lock on q and link

setup
    Is the queue configured

txq_len
    Number of queued buffers

txq_max
    Max allowed num of queued buffers

txq_poll_mark
    Used to check if queue got stuck

txq_stuck
    Queue stuck counter

.. _`ath5k_txq.description`:

Description
-----------

One of these exists for each hardware transmit queue.
Packets sent to us from above are assigned to queues based
on their priority.  Not all devices support a complete set
of hardware transmit queues. For those devices the array
sc_ac2q will map multiple priorities to fewer hardware queues
(typically all to one hardware queue).

.. _`ath5k_txq_info`:

struct ath5k_txq_info
=====================

.. c:type:: struct ath5k_txq_info

    A struct to hold TX queue's parameters

.. _`ath5k_txq_info.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_txq_info {
        enum ath5k_tx_queue tqi_type;
        enum ath5k_tx_queue_subtype tqi_subtype;
        u16 tqi_flags;
        u8 tqi_aifs;
        u16 tqi_cw_min;
        u16 tqi_cw_max;
        u32 tqi_cbr_period;
        u32 tqi_cbr_overflow_limit;
        u32 tqi_burst_time;
        u32 tqi_ready_time;
    }

.. _`ath5k_txq_info.members`:

Members
-------

tqi_type
    One of enum ath5k_tx_queue

tqi_subtype
    One of enum ath5k_tx_queue_subtype

tqi_flags
    TX queue flags (see above)

tqi_aifs
    Arbitrated Inter-frame Space

tqi_cw_min
    Minimum Contention Window

tqi_cw_max
    Maximum Contention Window

tqi_cbr_period
    Constant bit rate period

tqi_cbr_overflow_limit
    *undescribed*

tqi_burst_time
    *undescribed*

tqi_ready_time
    Time queue waits after an event when RDYTIME is enabled

.. _`ath5k_pkt_type`:

enum ath5k_pkt_type
===================

.. c:type:: enum ath5k_pkt_type

    Transmit packet types

.. _`ath5k_pkt_type.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_pkt_type {
        AR5K_PKT_TYPE_NORMAL,
        AR5K_PKT_TYPE_ATIM,
        AR5K_PKT_TYPE_PSPOLL,
        AR5K_PKT_TYPE_BEACON,
        AR5K_PKT_TYPE_PROBE_RESP,
        AR5K_PKT_TYPE_PIFS
    };

.. _`ath5k_pkt_type.constants`:

Constants
---------

AR5K_PKT_TYPE_NORMAL
    Normal data

AR5K_PKT_TYPE_ATIM
    ATIM

AR5K_PKT_TYPE_PSPOLL
    PS-Poll

AR5K_PKT_TYPE_BEACON
    Beacon

AR5K_PKT_TYPE_PROBE_RESP
    Probe response

AR5K_PKT_TYPE_PIFS
    PIFS
    Used on tx control descriptor

.. _`ath5k_rx_status`:

struct ath5k_rx_status
======================

.. c:type:: struct ath5k_rx_status

    RX Status descriptor

.. _`ath5k_rx_status.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_rx_status {
        u16 rs_datalen;
        u16 rs_tstamp;
        u8 rs_status;
        u8 rs_phyerr;
        s8 rs_rssi;
        u8 rs_keyix;
        u8 rs_rate;
        u8 rs_antenna;
        u8 rs_more;
    }

.. _`ath5k_rx_status.members`:

Members
-------

rs_datalen
    Data length

rs_tstamp
    Timestamp

rs_status
    Status code

rs_phyerr
    PHY error mask

rs_rssi
    RSSI in 0.5dbm units

rs_keyix
    Index to the key used for decrypting

rs_rate
    Rate used to decode the frame

rs_antenna
    Antenna used to receive the frame

rs_more
    Indicates this is a frame fragment (Fast frames)

.. _`ath5k_rfgain`:

enum ath5k_rfgain
=================

.. c:type:: enum ath5k_rfgain

    RF Gain optimization engine state

.. _`ath5k_rfgain.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_rfgain {
        AR5K_RFGAIN_INACTIVE,
        AR5K_RFGAIN_ACTIVE,
        AR5K_RFGAIN_READ_REQUESTED,
        AR5K_RFGAIN_NEED_CHANGE
    };

.. _`ath5k_rfgain.constants`:

Constants
---------

AR5K_RFGAIN_INACTIVE
    Engine disabled

AR5K_RFGAIN_ACTIVE
    Probe active

AR5K_RFGAIN_READ_REQUESTED
    Probe requested

AR5K_RFGAIN_NEED_CHANGE
    Gain_F needs change

.. _`ath5k_gain`:

struct ath5k_gain
=================

.. c:type:: struct ath5k_gain

    RF Gain optimization engine state data

.. _`ath5k_gain.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_gain {
        u8 g_step_idx;
        u8 g_current;
        u8 g_target;
        u8 g_low;
        u8 g_high;
        u8 g_f_corr;
        u8 g_state;
    }

.. _`ath5k_gain.members`:

Members
-------

g_step_idx
    Current step index

g_current
    Current gain

g_target
    Target gain

g_low
    Low gain boundary

g_high
    High gain boundary

g_f_corr
    Gain_F correction

g_state
    One of enum ath5k_rfgain

.. _`ath5k_athchan_2ghz`:

struct ath5k_athchan_2ghz
=========================

.. c:type:: struct ath5k_athchan_2ghz

    2GHz to 5GHZ map for RF5111

.. _`ath5k_athchan_2ghz.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_athchan_2ghz {
        u32 a2_flags;
        u16 a2_athchan;
    }

.. _`ath5k_athchan_2ghz.members`:

Members
-------

a2_flags
    Channel flags (internal)

a2_athchan
    HW channel number (internal)

.. _`ath5k_athchan_2ghz.description`:

Description
-----------

This structure is used to map 2GHz channels to
5GHz Atheros channels on 2111 frequency converter
that comes together with RF5111

.. _`ath5k_athchan_2ghz.todo`:

TODO
----

Clean up

.. _`ath5k_dmasize`:

enum ath5k_dmasize
==================

.. c:type:: enum ath5k_dmasize

    DMA size definitions (2^(n+2))

.. _`ath5k_dmasize.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_dmasize {
        AR5K_DMASIZE_4B,
        AR5K_DMASIZE_8B,
        AR5K_DMASIZE_16B,
        AR5K_DMASIZE_32B,
        AR5K_DMASIZE_64B,
        AR5K_DMASIZE_128B,
        AR5K_DMASIZE_256B,
        AR5K_DMASIZE_512B
    };

.. _`ath5k_dmasize.constants`:

Constants
---------

AR5K_DMASIZE_4B
    4Bytes

AR5K_DMASIZE_8B
    8Bytes

AR5K_DMASIZE_16B
    16Bytes

AR5K_DMASIZE_32B
    32Bytes

AR5K_DMASIZE_64B
    64Bytes (Default)

AR5K_DMASIZE_128B
    128Bytes

AR5K_DMASIZE_256B
    256Bytes

AR5K_DMASIZE_512B
    512Bytes

.. _`ath5k_dmasize.description`:

Description
-----------

These are used to set DMA burst size on hw

.. _`ath5k_dmasize.note`:

Note
----

Some platforms can't handle more than 4Bytes
be careful on embedded boards.

.. _`ath5k_int`:

enum ath5k_int
==============

.. c:type:: enum ath5k_int

    Hardware interrupt masks helpers

.. _`ath5k_int.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_int {
        AR5K_INT_RXOK,
        AR5K_INT_RXDESC,
        AR5K_INT_RXERR,
        AR5K_INT_RXNOFRM,
        AR5K_INT_RXEOL,
        AR5K_INT_RXORN,
        AR5K_INT_TXOK,
        AR5K_INT_TXDESC,
        AR5K_INT_TXERR,
        AR5K_INT_TXNOFRM,
        AR5K_INT_TXEOL,
        AR5K_INT_TXURN,
        AR5K_INT_MIB,
        AR5K_INT_SWI,
        AR5K_INT_RXPHY,
        AR5K_INT_RXKCM,
        AR5K_INT_SWBA,
        AR5K_INT_BRSSI,
        AR5K_INT_BMISS,
        AR5K_INT_FATAL,
        AR5K_INT_BNR,
        AR5K_INT_TIM,
        AR5K_INT_DTIM,
        AR5K_INT_DTIM_SYNC,
        AR5K_INT_GPIO,
        AR5K_INT_BCN_TIMEOUT,
        AR5K_INT_CAB_TIMEOUT,
        AR5K_INT_QCBRORN,
        AR5K_INT_QCBRURN,
        AR5K_INT_QTRIG,
        AR5K_INT_GLOBAL,
        AR5K_INT_TX_ALL,
        AR5K_INT_RX_ALL,
        AR5K_INT_COMMON,
        AR5K_INT_NOCARD
    };

.. _`ath5k_int.constants`:

Constants
---------

AR5K_INT_RXOK
    Frame successfully received

AR5K_INT_RXDESC
    Request RX descriptor/Read RX descriptor

AR5K_INT_RXERR
    Frame reception failed

AR5K_INT_RXNOFRM
    No frame received within a specified time period

AR5K_INT_RXEOL
    Reached "End Of List", means we need more RX descriptors

AR5K_INT_RXORN
    Indicates we got RX FIFO overrun. Note that Rx overrun is
    not always fatal, on some chips we can continue operation
    without resetting the card, that's why \ ``AR5K_INT_FATAL``\  is not
    common for all chips.

AR5K_INT_TXOK
    Frame transmission success

AR5K_INT_TXDESC
    Request TX descriptor/Read TX status descriptor

AR5K_INT_TXERR
    Frame transmission failure

AR5K_INT_TXNOFRM
    No frame was transmitted within a specified time period

AR5K_INT_TXEOL
    Received End Of List for VEOL (Virtual End Of List). The
    Queue Control Unit (QCU) signals an EOL interrupt only if a
    descriptor's LinkPtr is NULL. For more details, refer to:
    "http://www.freepatentsonline.com/20030225739.html"

AR5K_INT_TXURN
    Indicates we got TX FIFO underrun. In such case we should
    increase the TX trigger threshold.

AR5K_INT_MIB
    Indicates the either Management Information Base counters or
    one of the PHY error counters reached the maximum value and
    should be read and cleared.

AR5K_INT_SWI
    Software triggered interrupt.

AR5K_INT_RXPHY
    RX PHY Error

AR5K_INT_RXKCM
    RX Key cache miss

AR5K_INT_SWBA
    SoftWare Beacon Alert - indicates its time to send a
    beacon that must be handled in software. The alternative is if
    you have VEOL support, in that case you let the hardware deal
    with things.

AR5K_INT_BRSSI
    Beacon received with an RSSI value below our threshold

AR5K_INT_BMISS
    If in STA mode this indicates we have stopped seeing
    beacons from the AP have associated with, we should probably
    try to reassociate. When in IBSS mode this might mean we have
    not received any beacons from any local stations. Note that
    every station in an IBSS schedules to send beacons at the
    Target Beacon Transmission Time (TBTT) with a random backoff.

AR5K_INT_FATAL
    Fatal errors were encountered, typically caused by bus/DMA
    errors. Indicates we need to reset the card.

AR5K_INT_BNR
    Beacon queue got triggered (DMA beacon alert) while empty.

AR5K_INT_TIM
    Beacon with local station's TIM bit set

AR5K_INT_DTIM
    Beacon with DTIM bit and zero DTIM count received

AR5K_INT_DTIM_SYNC
    DTIM sync lost

AR5K_INT_GPIO
    GPIO interrupt is used for RF Kill switches connected to
    our GPIO pins.

AR5K_INT_BCN_TIMEOUT
    Beacon timeout, we waited after TBTT but got noting

AR5K_INT_CAB_TIMEOUT
    We waited for CAB traffic after the beacon but got
    nothing or an incomplete CAB frame sequence.

AR5K_INT_QCBRORN
    A queue got it's CBR counter expired

AR5K_INT_QCBRURN
    A queue got triggered wile empty

AR5K_INT_QTRIG
    A queue got triggered

AR5K_INT_GLOBAL
    Used to clear and set the IER

AR5K_INT_TX_ALL
    Mask to identify all TX related interrupts

AR5K_INT_RX_ALL
    Mask to identify all RX related interrupts

AR5K_INT_COMMON
    Common interrupts shared among MACs with the same
    bit value

AR5K_INT_NOCARD
    Signals the card has been removed

.. _`ath5k_int.description`:

Description
-----------

These are mapped to take advantage of some common bits
between the MACs, to be able to set intr properties
easier. Some of them are not used yet inside hw.c. Most map
to the respective hw interrupt value as they are common among different
MACs.

.. _`ath5k_calibration_mask`:

enum ath5k_calibration_mask
===========================

.. c:type:: enum ath5k_calibration_mask

    Mask which calibration is active at the moment

.. _`ath5k_calibration_mask.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_calibration_mask {
        AR5K_CALIBRATION_FULL,
        AR5K_CALIBRATION_SHORT,
        AR5K_CALIBRATION_NF,
        AR5K_CALIBRATION_ANI
    };

.. _`ath5k_calibration_mask.constants`:

Constants
---------

AR5K_CALIBRATION_FULL
    Full calibration (AGC + SHORT)

AR5K_CALIBRATION_SHORT
    Short calibration (NF + I/Q)

AR5K_CALIBRATION_NF
    Noise Floor calibration

AR5K_CALIBRATION_ANI
    Adaptive Noise Immunity

.. _`ath5k_power_mode`:

enum ath5k_power_mode
=====================

.. c:type:: enum ath5k_power_mode

    Power management modes

.. _`ath5k_power_mode.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_power_mode {
        AR5K_PM_UNDEFINED,
        AR5K_PM_AUTO,
        AR5K_PM_AWAKE,
        AR5K_PM_FULL_SLEEP,
        AR5K_PM_NETWORK_SLEEP
    };

.. _`ath5k_power_mode.constants`:

Constants
---------

AR5K_PM_UNDEFINED
    Undefined

AR5K_PM_AUTO
    Allow card to sleep if possible

AR5K_PM_AWAKE
    Force card to wake up

AR5K_PM_FULL_SLEEP
    Force card to full sleep (DANGEROUS)

AR5K_PM_NETWORK_SLEEP
    Allow to sleep for a specified duration

.. _`ath5k_power_mode.description`:

Description
-----------

Currently only PM_AWAKE is used, FULL_SLEEP and NETWORK_SLEEP/AUTO
are also known to have problems on some cards. This is not a big
problem though because we can have almost the same effect as
FULL_SLEEP by putting card on warm reset (it's almost powered down).

.. This file was automatic generated / don't edit.

