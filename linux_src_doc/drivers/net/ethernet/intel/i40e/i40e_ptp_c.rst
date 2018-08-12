.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_ptp.c

.. _`i40e_ptp_read`:

i40e_ptp_read
=============

.. c:function:: void i40e_ptp_read(struct i40e_pf *pf, struct timespec64 *ts)

    Read the PHC time from the device

    :param struct i40e_pf \*pf:
        Board private structure

    :param struct timespec64 \*ts:
        timespec structure to hold the current time value

.. _`i40e_ptp_read.description`:

Description
-----------

This function reads the PRTTSYN_TIME registers and stores them in a
timespec. However, since the registers are 64 bits of nanoseconds, we must
convert the result to a timespec before we can return.

.. _`i40e_ptp_write`:

i40e_ptp_write
==============

.. c:function:: void i40e_ptp_write(struct i40e_pf *pf, const struct timespec64 *ts)

    Write the PHC time to the device

    :param struct i40e_pf \*pf:
        Board private structure

    :param const struct timespec64 \*ts:
        timespec structure that holds the new time value

.. _`i40e_ptp_write.description`:

Description
-----------

This function writes the PRTTSYN_TIME registers with the user value. Since
we receive a timespec from the stack, we must convert that timespec into
nanoseconds before programming the registers.

.. _`i40e_ptp_convert_to_hwtstamp`:

i40e_ptp_convert_to_hwtstamp
============================

.. c:function:: void i40e_ptp_convert_to_hwtstamp(struct skb_shared_hwtstamps *hwtstamps, u64 timestamp)

    Convert device clock to system time

    :param struct skb_shared_hwtstamps \*hwtstamps:
        Timestamp structure to update

    :param u64 timestamp:
        Timestamp from the hardware

.. _`i40e_ptp_convert_to_hwtstamp.description`:

Description
-----------

We need to convert the NIC clock value into a hwtstamp which can be used by
the upper level timestamping functions. Since the timestamp is simply a 64-
bit nanosecond value, we can call ns_to_ktime directly to handle this.

.. _`i40e_ptp_adjfreq`:

i40e_ptp_adjfreq
================

.. c:function:: int i40e_ptp_adjfreq(struct ptp_clock_info *ptp, s32 ppb)

    Adjust the PHC frequency

    :param struct ptp_clock_info \*ptp:
        The PTP clock structure

    :param s32 ppb:
        Parts per billion adjustment from the base

.. _`i40e_ptp_adjfreq.description`:

Description
-----------

Adjust the frequency of the PHC by the indicated parts per billion from the
base frequency.

.. _`i40e_ptp_adjtime`:

i40e_ptp_adjtime
================

.. c:function:: int i40e_ptp_adjtime(struct ptp_clock_info *ptp, s64 delta)

    Adjust the PHC time

    :param struct ptp_clock_info \*ptp:
        The PTP clock structure

    :param s64 delta:
        Offset in nanoseconds to adjust the PHC time by

.. _`i40e_ptp_adjtime.description`:

Description
-----------

Adjust the frequency of the PHC by the indicated parts per billion from the
base frequency.

.. _`i40e_ptp_gettime`:

i40e_ptp_gettime
================

.. c:function:: int i40e_ptp_gettime(struct ptp_clock_info *ptp, struct timespec64 *ts)

    Get the time of the PHC

    :param struct ptp_clock_info \*ptp:
        The PTP clock structure

    :param struct timespec64 \*ts:
        timespec structure to hold the current time value

.. _`i40e_ptp_gettime.description`:

Description
-----------

Read the device clock and return the correct value on ns, after converting it
into a timespec struct.

.. _`i40e_ptp_settime`:

i40e_ptp_settime
================

.. c:function:: int i40e_ptp_settime(struct ptp_clock_info *ptp, const struct timespec64 *ts)

    Set the time of the PHC

    :param struct ptp_clock_info \*ptp:
        The PTP clock structure

    :param const struct timespec64 \*ts:
        timespec structure that holds the new time value

.. _`i40e_ptp_settime.description`:

Description
-----------

Set the device clock to the user input value. The conversion from timespec
to ns happens in the write function.

.. _`i40e_ptp_feature_enable`:

i40e_ptp_feature_enable
=======================

.. c:function:: int i40e_ptp_feature_enable(struct ptp_clock_info *ptp, struct ptp_clock_request *rq, int on)

    Enable/disable ancillary features of the PHC subsystem

    :param struct ptp_clock_info \*ptp:
        The PTP clock structure

    :param struct ptp_clock_request \*rq:
        The requested feature to change

    :param int on:
        Enable/disable flag

.. _`i40e_ptp_feature_enable.description`:

Description
-----------

The XL710 does not support any of the ancillary features of the PHC
subsystem, so this function may just return.

.. _`i40e_ptp_get_rx_events`:

i40e_ptp_get_rx_events
======================

.. c:function:: u32 i40e_ptp_get_rx_events(struct i40e_pf *pf)

    Read I40E_PRTTSYN_STAT_1 and latch events

    :param struct i40e_pf \*pf:
        the PF data structure

.. _`i40e_ptp_get_rx_events.description`:

Description
-----------

This function reads I40E_PRTTSYN_STAT_1 and updates the corresponding timers
for noticed latch events. This allows the driver to keep track of the first
time a latch event was noticed which will be used to help clear out Rx
timestamps for packets that got dropped or lost.

This function will return the current value of I40E_PRTTSYN_STAT_1 and is
expected to be called only while under the ptp_rx_lock.

.. _`i40e_ptp_rx_hang`:

i40e_ptp_rx_hang
================

.. c:function:: void i40e_ptp_rx_hang(struct i40e_pf *pf)

    Detect error case when Rx timestamp registers are hung

    :param struct i40e_pf \*pf:
        The PF private data structure

.. _`i40e_ptp_rx_hang.description`:

Description
-----------

This watchdog task is scheduled to detect error case where hardware has
dropped an Rx packet that was timestamped when the ring is full. The
particular error is rare but leaves the device in a state unable to timestamp
any future packets.

.. _`i40e_ptp_tx_hang`:

i40e_ptp_tx_hang
================

.. c:function:: void i40e_ptp_tx_hang(struct i40e_pf *pf)

    Detect error case when Tx timestamp register is hung

    :param struct i40e_pf \*pf:
        The PF private data structure

.. _`i40e_ptp_tx_hang.description`:

Description
-----------

This watchdog task is run periodically to make sure that we clear the Tx
timestamp logic if we don't obtain a timestamp in a reasonable amount of
time. It is unexpected in the normal case but if it occurs it results in
permanently preventing timestamps of future packets.

.. _`i40e_ptp_tx_hwtstamp`:

i40e_ptp_tx_hwtstamp
====================

.. c:function:: void i40e_ptp_tx_hwtstamp(struct i40e_pf *pf)

    Utility function which returns the Tx timestamp

    :param struct i40e_pf \*pf:
        Board private structure

.. _`i40e_ptp_tx_hwtstamp.description`:

Description
-----------

Read the value of the Tx timestamp from the registers, convert it into a
value consumable by the stack, and store that result into the shhwtstamps
struct before returning it up the stack.

.. _`i40e_ptp_rx_hwtstamp`:

i40e_ptp_rx_hwtstamp
====================

.. c:function:: void i40e_ptp_rx_hwtstamp(struct i40e_pf *pf, struct sk_buff *skb, u8 index)

    Utility function which checks for an Rx timestamp

    :param struct i40e_pf \*pf:
        Board private structure

    :param struct sk_buff \*skb:
        Particular skb to send timestamp with

    :param u8 index:
        Index into the receive timestamp registers for the timestamp

.. _`i40e_ptp_rx_hwtstamp.description`:

Description
-----------

The XL710 receives a notification in the receive descriptor with an offset
into the set of RXTIME registers where the timestamp is for that skb. This
function goes and fetches the receive timestamp from that offset, if a valid
one exists. The RXTIME registers are in ns, so we must convert the result
first.

.. _`i40e_ptp_set_increment`:

i40e_ptp_set_increment
======================

.. c:function:: void i40e_ptp_set_increment(struct i40e_pf *pf)

    Utility function to update clock increment rate

    :param struct i40e_pf \*pf:
        Board private structure

.. _`i40e_ptp_set_increment.description`:

Description
-----------

During a link change, the DMA frequency that drives the 1588 logic will
change. In order to keep the PRTTSYN_TIME registers in units of nanoseconds,
we must update the increment value per clock tick.

.. _`i40e_ptp_get_ts_config`:

i40e_ptp_get_ts_config
======================

.. c:function:: int i40e_ptp_get_ts_config(struct i40e_pf *pf, struct ifreq *ifr)

    ioctl interface to read the HW timestamping

    :param struct i40e_pf \*pf:
        Board private structure

    :param struct ifreq \*ifr:
        ioctl data

.. _`i40e_ptp_get_ts_config.description`:

Description
-----------

Obtain the current hardware timestamping settigs as requested. To do this,
keep a shadow copy of the timestamp settings rather than attempting to
deconstruct it from the registers.

.. _`i40e_ptp_set_timestamp_mode`:

i40e_ptp_set_timestamp_mode
===========================

.. c:function:: int i40e_ptp_set_timestamp_mode(struct i40e_pf *pf, struct hwtstamp_config *config)

    setup hardware for requested timestamp mode

    :param struct i40e_pf \*pf:
        Board private structure

    :param struct hwtstamp_config \*config:
        hwtstamp settings requested or saved

.. _`i40e_ptp_set_timestamp_mode.description`:

Description
-----------

Control hardware registers to enter the specific mode requested by the
user. Also used during reset path to ensure that timestamp settings are
maintained.

.. _`i40e_ptp_set_timestamp_mode.note`:

Note
----

modifies config in place, and may update the requested mode to be
more broad if the specific filter is not directly supported.

.. _`i40e_ptp_set_ts_config`:

i40e_ptp_set_ts_config
======================

.. c:function:: int i40e_ptp_set_ts_config(struct i40e_pf *pf, struct ifreq *ifr)

    ioctl interface to control the HW timestamping

    :param struct i40e_pf \*pf:
        Board private structure

    :param struct ifreq \*ifr:
        ioctl data

.. _`i40e_ptp_set_ts_config.description`:

Description
-----------

Respond to the user filter requests and make the appropriate hardware
changes here. The XL710 cannot support splitting of the Tx/Rx timestamping
logic, so keep track in software of whether to indicate these timestamps
or not.

It is permissible to "upgrade" the user request to a broader filter, as long
as the user receives the timestamps they care about and the user is notified
the filter has been broadened.

.. _`i40e_ptp_create_clock`:

i40e_ptp_create_clock
=====================

.. c:function:: long i40e_ptp_create_clock(struct i40e_pf *pf)

    Create PTP clock device for userspace

    :param struct i40e_pf \*pf:
        Board private structure

.. _`i40e_ptp_create_clock.description`:

Description
-----------

This function creates a new PTP clock device. It only creates one if we
don't already have one, so it is safe to call. Will return error if it
can't create one, but success if we already have a device. Should be used
by i40e_ptp_init to create clock initially, and prevent global resets from
creating new clock devices.

.. _`i40e_ptp_init`:

i40e_ptp_init
=============

.. c:function:: void i40e_ptp_init(struct i40e_pf *pf)

    Initialize the 1588 support after device probe or reset

    :param struct i40e_pf \*pf:
        Board private structure

.. _`i40e_ptp_init.description`:

Description
-----------

This function sets device up for 1588 support. The first time it is run, it
will create a PHC clock device. It does not create a clock device if one
already exists. It also reconfigures the device after a reset.

.. _`i40e_ptp_stop`:

i40e_ptp_stop
=============

.. c:function:: void i40e_ptp_stop(struct i40e_pf *pf)

    Disable the driver/hardware support and unregister the PHC

    :param struct i40e_pf \*pf:
        Board private structure

.. _`i40e_ptp_stop.description`:

Description
-----------

This function handles the cleanup work required from the initialization by
clearing out the important information and unregistering the PHC.

.. This file was automatic generated / don't edit.

