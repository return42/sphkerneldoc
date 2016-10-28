.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/ptp.c

.. _`efx_ptp_match`:

struct efx_ptp_match
====================

.. c:type:: struct efx_ptp_match

    Matching structure, stored in sk_buff's cb area.

.. _`efx_ptp_match.definition`:

Definition
----------

.. code-block:: c

    struct efx_ptp_match {
        u32 words[DIV_ROUND_UP(PTP_V1_UUID_LENGTH# 4)];
        unsigned long expiry;
        enum ptp_packet_state state;
    }

.. _`efx_ptp_match.members`:

Members
-------

words
    UUID and (partial) sequence number

expiry
    Time after which the packet should be delivered irrespective of
    event arrival.

state
    The state of the packet - whether it is ready for processing or
    whether that is of no interest.

.. _`efx_ptp_event_rx`:

struct efx_ptp_event_rx
=======================

.. c:type:: struct efx_ptp_event_rx

    A PTP receive event (from MC)

.. _`efx_ptp_event_rx.definition`:

Definition
----------

.. code-block:: c

    struct efx_ptp_event_rx {
        struct list_head link;
        u32 seq0;
        u32 seq1;
        ktime_t hwtimestamp;
        unsigned long expiry;
    }

.. _`efx_ptp_event_rx.members`:

Members
-------

link
    *undescribed*

seq0
    First part of (PTP) UUID

seq1
    Second part of (PTP) UUID and sequence number

hwtimestamp
    Event timestamp

expiry
    *undescribed*

.. _`efx_ptp_timeset`:

struct efx_ptp_timeset
======================

.. c:type:: struct efx_ptp_timeset

    Synchronisation between host and MC

.. _`efx_ptp_timeset.definition`:

Definition
----------

.. code-block:: c

    struct efx_ptp_timeset {
        u32 host_start;
        u32 major;
        u32 minor;
        u32 host_end;
        u32 wait;
        u32 window;
    }

.. _`efx_ptp_timeset.members`:

Members
-------

host_start
    Host time immediately before hardware timestamp taken

major
    Hardware timestamp, major

minor
    Hardware timestamp, minor

host_end
    Host time immediately after hardware timestamp taken

wait
    Number of NIC clock ticks between hardware timestamp being read and
    host end time being seen

window
    Difference of host_end and host_start

.. _`efx_ptp_data`:

struct efx_ptp_data
===================

.. c:type:: struct efx_ptp_data

    Precision Time Protocol (PTP) state

.. _`efx_ptp_data.definition`:

Definition
----------

.. code-block:: c

    struct efx_ptp_data {
        struct efx_nic *efx;
        struct efx_channel *channel;
        bool rx_ts_inline;
        struct sk_buff_head rxq;
        struct sk_buff_head txq;
        struct list_head evt_list;
        struct list_head evt_free_list;
        spinlock_t evt_lock;
        struct efx_ptp_event_rx rx_evts[MAX_RECEIVE_EVENTS];
        struct workqueue_struct *workwq;
        struct work_struct work;
        bool reset_required;
        u32 rxfilter_event;
        u32 rxfilter_general;
        bool rxfilter_installed;
        struct hwtstamp_config config;
        bool enabled;
        unsigned int mode;
        unsigned int time_format;
        void (*ns_to_nic_time)(s64 ns, u32 *nic_major, u32 *nic_minor);
        ktime_t (*nic_to_kernel_time)(u32 nic_major, u32 nic_minor,s32 correction);
        unsigned int min_synchronisation_ns;
        struct ts_corrections;
        efx_qword_t evt_frags[MAX_EVENT_FRAGS];
        int evt_frag_idx;
        int evt_code;
        struct efx_buffer start;
        struct pps_event_time host_time_pps;
        s64 current_adjfreq;
        struct ptp_clock *phc_clock;
        struct ptp_clock_info phc_clock_info;
        struct work_struct pps_work;
        struct workqueue_struct *pps_workwq;
        bool nic_ts_enabled;
        _MCDI_DECLARE_BUF(txbuf# MC_CMD_PTP_IN_TRANSMIT_LENMAX);
        unsigned int good_syncs;
        unsigned int fast_syncs;
        unsigned int bad_syncs;
        unsigned int sync_timeouts;
        unsigned int no_time_syncs;
        unsigned int invalid_sync_windows;
        unsigned int undersize_sync_windows;
        unsigned int oversize_sync_windows;
        unsigned int rx_no_timestamp;
        struct efx_ptp_timesettimeset[MC_CMD_PTP_OUT_SYNCHRONIZE_TIMESET_MAXNUM];
    }

.. _`efx_ptp_data.members`:

Members
-------

efx
    The NIC context

channel
    The PTP channel (Siena only)

rx_ts_inline
    Flag for whether RX timestamps are inline (else they are
    separate events)

rxq
    Receive queue (awaiting timestamps)

txq
    Transmit queue

evt_list
    List of MC receive events awaiting packets

evt_free_list
    List of free events

evt_lock
    Lock for manipulating evt_list and evt_free_list

rx_evts
    Instantiated events (on evt_list and evt_free_list)

workwq
    Work queue for processing pending PTP operations

work
    Work task

reset_required
    A serious error has occurred and the PTP task needs to be
    reset (disable, enable).

rxfilter_event
    Receive filter when operating

rxfilter_general
    Receive filter when operating

rxfilter_installed
    *undescribed*

config
    Current timestamp configuration

enabled
    PTP operation enabled

mode
    Mode in which PTP operating (PTP version)

time_format
    Time format supported by this NIC

ns_to_nic_time
    Function to convert from scalar nanoseconds to NIC time

nic_to_kernel_time
    Function to convert from NIC to kernel time

min_synchronisation_ns
    Minimum acceptable corrected sync window

ts_corrections
    *undescribed*

ts_corrections.tx
    Required driver correction of transmit timestamps

ts_corrections.rx
    Required driver correction of receive timestamps

ts_corrections.pps_out
    PPS output error (information only)

ts_corrections.pps_in
    Required driver correction of PPS input timestamps

evt_frags
    Partly assembled PTP events

evt_frag_idx
    Current fragment number

evt_code
    Last event code

start
    Address at which MC indicates ready for synchronisation

host_time_pps
    Host time at last PPS

current_adjfreq
    Current ppb adjustment.

phc_clock
    Pointer to registered phc device (if primary function)

phc_clock_info
    Registration structure for phc device

pps_work
    pps work task for handling pps events

pps_workwq
    pps work queue

nic_ts_enabled
    Flag indicating if NIC generated TS events are handled

MC_CMD_PTP_IN_TRANSMIT_LENMAX)
    *undescribed*

good_syncs
    Number of successful synchronisations.

fast_syncs
    Number of synchronisations requiring short delay

bad_syncs
    Number of failed synchronisations.

sync_timeouts
    Number of synchronisation timeouts

no_time_syncs
    Number of synchronisations with no good times.

invalid_sync_windows
    Number of sync windows with bad durations.

undersize_sync_windows
    Number of corrected sync windows that are too small

oversize_sync_windows
    Number of corrected sync windows that are too large

rx_no_timestamp
    Number of packets received without a timestamp.

.. This file was automatic generated / don't edit.

