.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_ptp.c

.. _`ixgbe_ptp_setup_sdp_x540`:

ixgbe_ptp_setup_sdp_x540
========================

.. c:function:: void ixgbe_ptp_setup_sdp_x540(struct ixgbe_adapter *adapter)

    :param adapter:
        private adapter structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ptp_setup_sdp_x540.description`:

Description
-----------

this function enables or disables the clock out feature on SDP0 for
the X540 device. It will create a 1second periodic output that can
be used as the PPS (via an interrupt).

It calculates when the systime will be on an exact second, and then
aligns the start of the PPS signal to that value. The shift is
necessary because it can change based on the link speed.

.. _`ixgbe_ptp_read_x550`:

ixgbe_ptp_read_X550
===================

.. c:function:: u64 ixgbe_ptp_read_X550(const struct cyclecounter *hw_cc)

    read cycle counter value

    :param hw_cc:
        cyclecounter structure
    :type hw_cc: const struct cyclecounter \*

.. _`ixgbe_ptp_read_x550.description`:

Description
-----------

This function reads SYSTIME registers. It is called by the cyclecounter
structure to convert from internal representation into nanoseconds. We need
this for X550 since some skews do not have expected clock frequency and
result of SYSTIME is 32bits of "billions of cycles" and 32 bits of
"cycles", rather than seconds and nanoseconds.

.. _`ixgbe_ptp_read_82599`:

ixgbe_ptp_read_82599
====================

.. c:function:: u64 ixgbe_ptp_read_82599(const struct cyclecounter *cc)

    read raw cycle counter (to be used by time counter)

    :param cc:
        the cyclecounter structure
    :type cc: const struct cyclecounter \*

.. _`ixgbe_ptp_read_82599.description`:

Description
-----------

this function reads the cyclecounter registers and is called by the
cyclecounter structure used to construct a ns counter from the
arbitrary fixed point registers

.. _`ixgbe_ptp_convert_to_hwtstamp`:

ixgbe_ptp_convert_to_hwtstamp
=============================

.. c:function:: void ixgbe_ptp_convert_to_hwtstamp(struct ixgbe_adapter *adapter, struct skb_shared_hwtstamps *hwtstamp, u64 timestamp)

    convert register value to hw timestamp

    :param adapter:
        private adapter structure
    :type adapter: struct ixgbe_adapter \*

    :param hwtstamp:
        stack timestamp structure
    :type hwtstamp: struct skb_shared_hwtstamps \*

    :param timestamp:
        unsigned 64bit system time value
    :type timestamp: u64

.. _`ixgbe_ptp_convert_to_hwtstamp.description`:

Description
-----------

We need to convert the adapter's RX/TXSTMP registers into a hwtstamp value
which can be used by the stack's ptp functions.

The lock is used to protect consistency of the cyclecounter and the SYSTIME
registers. However, it does not need to protect against the Rx or Tx
timestamp registers, as there can't be a new timestamp until the old one is
unlatched by reading.

In addition to the timestamp in hardware, some controllers need a software
overflow cyclecounter, and this function takes this into account as well.

.. _`ixgbe_ptp_adjfreq_82599`:

ixgbe_ptp_adjfreq_82599
=======================

.. c:function:: int ixgbe_ptp_adjfreq_82599(struct ptp_clock_info *ptp, s32 ppb)

    :param ptp:
        the ptp clock structure
    :type ptp: struct ptp_clock_info \*

    :param ppb:
        parts per billion adjustment from base
    :type ppb: s32

.. _`ixgbe_ptp_adjfreq_82599.description`:

Description
-----------

adjust the frequency of the ptp cycle counter by the
indicated ppb from the base frequency.

.. _`ixgbe_ptp_adjfreq_x550`:

ixgbe_ptp_adjfreq_X550
======================

.. c:function:: int ixgbe_ptp_adjfreq_X550(struct ptp_clock_info *ptp, s32 ppb)

    :param ptp:
        the ptp clock structure
    :type ptp: struct ptp_clock_info \*

    :param ppb:
        parts per billion adjustment from base
    :type ppb: s32

.. _`ixgbe_ptp_adjfreq_x550.description`:

Description
-----------

adjust the frequency of the SYSTIME registers by the indicated ppb from base
frequency

.. _`ixgbe_ptp_adjtime`:

ixgbe_ptp_adjtime
=================

.. c:function:: int ixgbe_ptp_adjtime(struct ptp_clock_info *ptp, s64 delta)

    :param ptp:
        the ptp clock structure
    :type ptp: struct ptp_clock_info \*

    :param delta:
        offset to adjust the cycle counter by
    :type delta: s64

.. _`ixgbe_ptp_adjtime.description`:

Description
-----------

adjust the timer by resetting the timecounter structure.

.. _`ixgbe_ptp_gettime`:

ixgbe_ptp_gettime
=================

.. c:function:: int ixgbe_ptp_gettime(struct ptp_clock_info *ptp, struct timespec64 *ts)

    :param ptp:
        the ptp clock structure
    :type ptp: struct ptp_clock_info \*

    :param ts:
        timespec structure to hold the current time value
    :type ts: struct timespec64 \*

.. _`ixgbe_ptp_gettime.description`:

Description
-----------

read the timecounter and return the correct value on ns,
after converting it into a struct timespec.

.. _`ixgbe_ptp_settime`:

ixgbe_ptp_settime
=================

.. c:function:: int ixgbe_ptp_settime(struct ptp_clock_info *ptp, const struct timespec64 *ts)

    :param ptp:
        the ptp clock structure
    :type ptp: struct ptp_clock_info \*

    :param ts:
        the timespec containing the new time for the cycle counter
    :type ts: const struct timespec64 \*

.. _`ixgbe_ptp_settime.description`:

Description
-----------

reset the timecounter to use a new base value instead of the kernel
wall timer value.

.. _`ixgbe_ptp_feature_enable`:

ixgbe_ptp_feature_enable
========================

.. c:function:: int ixgbe_ptp_feature_enable(struct ptp_clock_info *ptp, struct ptp_clock_request *rq, int on)

    :param ptp:
        the ptp clock structure
    :type ptp: struct ptp_clock_info \*

    :param rq:
        the requested feature to change
    :type rq: struct ptp_clock_request \*

    :param on:
        whether to enable or disable the feature
    :type on: int

.. _`ixgbe_ptp_feature_enable.description`:

Description
-----------

enable (or disable) ancillary features of the phc subsystem.
our driver only supports the PPS feature on the X540

.. _`ixgbe_ptp_check_pps_event`:

ixgbe_ptp_check_pps_event
=========================

.. c:function:: void ixgbe_ptp_check_pps_event(struct ixgbe_adapter *adapter)

    :param adapter:
        the private adapter structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ptp_check_pps_event.description`:

Description
-----------

This function is called by the interrupt routine when checking for
interrupts. It will check and handle a pps event.

.. _`ixgbe_ptp_overflow_check`:

ixgbe_ptp_overflow_check
========================

.. c:function:: void ixgbe_ptp_overflow_check(struct ixgbe_adapter *adapter)

    watchdog task to detect SYSTIME overflow

    :param adapter:
        private adapter struct
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ptp_overflow_check.description`:

Description
-----------

this watchdog task periodically reads the timecounter
in order to prevent missing when the system time registers wrap
around. This needs to be run approximately twice a minute.

.. _`ixgbe_ptp_rx_hang`:

ixgbe_ptp_rx_hang
=================

.. c:function:: void ixgbe_ptp_rx_hang(struct ixgbe_adapter *adapter)

    detect error case when Rx timestamp registers latched

    :param adapter:
        private network adapter structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ptp_rx_hang.description`:

Description
-----------

this watchdog task is scheduled to detect error case where hardware has
dropped an Rx packet that was timestamped when the ring is full. The
particular error is rare but leaves the device in a state unable to timestamp
any future packets.

.. _`ixgbe_ptp_clear_tx_timestamp`:

ixgbe_ptp_clear_tx_timestamp
============================

.. c:function:: void ixgbe_ptp_clear_tx_timestamp(struct ixgbe_adapter *adapter)

    utility function to clear Tx timestamp state

    :param adapter:
        the private adapter structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ptp_clear_tx_timestamp.description`:

Description
-----------

This function should be called whenever the state related to a Tx timestamp
needs to be cleared. This helps ensure that all related bits are reset for
the next Tx timestamp event.

.. _`ixgbe_ptp_tx_hang`:

ixgbe_ptp_tx_hang
=================

.. c:function:: void ixgbe_ptp_tx_hang(struct ixgbe_adapter *adapter)

    detect error case where Tx timestamp never finishes

    :param adapter:
        private network adapter structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ptp_tx_hwtstamp`:

ixgbe_ptp_tx_hwtstamp
=====================

.. c:function:: void ixgbe_ptp_tx_hwtstamp(struct ixgbe_adapter *adapter)

    utility function which checks for TX time stamp

    :param adapter:
        the private adapter struct
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ptp_tx_hwtstamp.description`:

Description
-----------

if the timestamp is valid, we convert it into the timecounter ns
value, then store that result into the shhwtstamps structure which
is passed up the network stack

.. _`ixgbe_ptp_tx_hwtstamp_work`:

ixgbe_ptp_tx_hwtstamp_work
==========================

.. c:function:: void ixgbe_ptp_tx_hwtstamp_work(struct work_struct *work)

    :param work:
        pointer to the work struct
    :type work: struct work_struct \*

.. _`ixgbe_ptp_tx_hwtstamp_work.description`:

Description
-----------

This work item polls TSYNCTXCTL valid bit to determine when a Tx hardware
timestamp has been taken for the current skb. It is necessary, because the
descriptor's "done" bit does not correlate with the timestamp event.

.. _`ixgbe_ptp_rx_pktstamp`:

ixgbe_ptp_rx_pktstamp
=====================

.. c:function:: void ixgbe_ptp_rx_pktstamp(struct ixgbe_q_vector *q_vector, struct sk_buff *skb)

    utility function to get RX time stamp from buffer

    :param q_vector:
        structure containing interrupt and ring information
    :type q_vector: struct ixgbe_q_vector \*

    :param skb:
        the packet
    :type skb: struct sk_buff \*

.. _`ixgbe_ptp_rx_pktstamp.description`:

Description
-----------

This function will be called by the Rx routine of the timestamp for this
packet is stored in the buffer. The value is stored in little endian format
starting at the end of the packet data.

.. _`ixgbe_ptp_rx_rgtstamp`:

ixgbe_ptp_rx_rgtstamp
=====================

.. c:function:: void ixgbe_ptp_rx_rgtstamp(struct ixgbe_q_vector *q_vector, struct sk_buff *skb)

    utility function which checks for RX time stamp

    :param q_vector:
        structure containing interrupt and ring information
    :type q_vector: struct ixgbe_q_vector \*

    :param skb:
        particular skb to send timestamp with
    :type skb: struct sk_buff \*

.. _`ixgbe_ptp_rx_rgtstamp.description`:

Description
-----------

if the timestamp is valid, we convert it into the timecounter ns
value, then store that result into the shhwtstamps structure which
is passed up the network stack

.. _`ixgbe_ptp_set_timestamp_mode`:

ixgbe_ptp_set_timestamp_mode
============================

.. c:function:: int ixgbe_ptp_set_timestamp_mode(struct ixgbe_adapter *adapter, struct hwtstamp_config *config)

    setup the hardware for the requested mode

    :param adapter:
        the private ixgbe adapter structure
    :type adapter: struct ixgbe_adapter \*

    :param config:
        the hwtstamp configuration requested
    :type config: struct hwtstamp_config \*

.. _`ixgbe_ptp_set_timestamp_mode.description`:

Description
-----------

Outgoing time stamping can be enabled and disabled. Play nice and
disable it when requested, although it shouldn't cause any overhead
when no packet needs it. At most one packet in the queue may be
marked for time stamping, otherwise it would be impossible to tell
for sure to which packet the hardware time stamp belongs.

Incoming time stamping has to be configured via the hardware
filters. Not all combinations are supported, in particular event
type has to be specified. Matching the kind of event packet is
not supported, with the exception of "all V2 events regardless of
level 2 or 4".

Since hardware always timestamps Path delay packets when timestamping V2
packets, regardless of the type specified in the register, only use V2
Event mode. This more accurately tells the user what the hardware is going
to do anyways.

.. _`ixgbe_ptp_set_timestamp_mode.note`:

Note
----

this may modify the hwtstamp configuration towards a more general
mode, if required to support the specifically requested mode.

.. _`ixgbe_ptp_set_ts_config`:

ixgbe_ptp_set_ts_config
=======================

.. c:function:: int ixgbe_ptp_set_ts_config(struct ixgbe_adapter *adapter, struct ifreq *ifr)

    user entry point for timestamp mode

    :param adapter:
        pointer to adapter struct
    :type adapter: struct ixgbe_adapter \*

    :param ifr:
        ioctl data
    :type ifr: struct ifreq \*

.. _`ixgbe_ptp_set_ts_config.description`:

Description
-----------

Set hardware to requested mode. If unsupported, return an error with no
changes. Otherwise, store the mode for future reference.

.. _`ixgbe_ptp_start_cyclecounter`:

ixgbe_ptp_start_cyclecounter
============================

.. c:function:: void ixgbe_ptp_start_cyclecounter(struct ixgbe_adapter *adapter)

    create the cycle counter from hw

    :param adapter:
        pointer to the adapter structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ptp_start_cyclecounter.description`:

Description
-----------

This function should be called to set the proper values for the TIMINCA
register and tell the cyclecounter structure what the tick rate of SYSTIME
is. It does not directly modify SYSTIME registers or the timecounter
structure. It should be called whenever a new TIMINCA value is necessary,
such as during initialization or when the link speed changes.

.. _`ixgbe_ptp_reset`:

ixgbe_ptp_reset
===============

.. c:function:: void ixgbe_ptp_reset(struct ixgbe_adapter *adapter)

    :param adapter:
        the ixgbe private board structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ptp_reset.description`:

Description
-----------

When the MAC resets, all the hardware bits for timesync are reset. This
function is used to re-enable the device for PTP based on current settings.
We do lose the current clock time, so just reset the cyclecounter to the
system real clock time.

This function will maintain hwtstamp_config settings, and resets the SDP
output if it was enabled.

.. _`ixgbe_ptp_create_clock`:

ixgbe_ptp_create_clock
======================

.. c:function:: long ixgbe_ptp_create_clock(struct ixgbe_adapter *adapter)

    :param adapter:
        the ixgbe private adapter structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ptp_create_clock.description`:

Description
-----------

This function performs setup of the user entry point function table and
initializes the PTP clock device, which is used to access the clock-like
features of the PTP core. It will be called by ixgbe_ptp_init, and may
reuse a previously initialized clock (such as during a suspend/resume
cycle).

.. _`ixgbe_ptp_init`:

ixgbe_ptp_init
==============

.. c:function:: void ixgbe_ptp_init(struct ixgbe_adapter *adapter)

    :param adapter:
        the ixgbe private adapter structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ptp_init.description`:

Description
-----------

This function performs the required steps for enabling PTP
support. If PTP support has already been loaded it simply calls the
cyclecounter init routine and exits.

.. _`ixgbe_ptp_suspend`:

ixgbe_ptp_suspend
=================

.. c:function:: void ixgbe_ptp_suspend(struct ixgbe_adapter *adapter)

    stop PTP work items

    :param adapter:
        pointer to adapter struct
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ptp_suspend.description`:

Description
-----------

this function suspends PTP activity, and prevents more PTP work from being
generated, but does not destroy the PTP clock device.

.. _`ixgbe_ptp_stop`:

ixgbe_ptp_stop
==============

.. c:function:: void ixgbe_ptp_stop(struct ixgbe_adapter *adapter)

    close the PTP device

    :param adapter:
        pointer to adapter struct
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ptp_stop.description`:

Description
-----------

completely destroy the PTP device, should only be called when the device is
being fully closed.

.. This file was automatic generated / don't edit.

