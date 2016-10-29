.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igb/igb_ptp.c

.. _`igb_ptp_systim_to_hwtstamp`:

igb_ptp_systim_to_hwtstamp
==========================

.. c:function:: void igb_ptp_systim_to_hwtstamp(struct igb_adapter *adapter, struct skb_shared_hwtstamps *hwtstamps, u64 systim)

    convert system time value to hw timestamp

    :param struct igb_adapter \*adapter:
        board private structure

    :param struct skb_shared_hwtstamps \*hwtstamps:
        timestamp structure to update

    :param u64 systim:
        unsigned 64bit system time value.

.. _`igb_ptp_systim_to_hwtstamp.description`:

Description
-----------

We need to convert the system time value stored in the RX/TXSTMP registers
into a hwtstamp which can be used by the upper level timestamping functions.

The 'tmreg_lock' spinlock is used to protect the consistency of the
system time value. This is needed because reading the 64 bit time
value involves reading two (or three) 32 bit registers. The first
read latches the value. Ditto for writing.

In addition, here have extended the system time with an overflow
counter in software.

.. _`igb_ptp_tx_work`:

igb_ptp_tx_work
===============

.. c:function:: void igb_ptp_tx_work(struct work_struct *work)

    :param struct work_struct \*work:
        pointer to work struct

.. _`igb_ptp_tx_work.description`:

Description
-----------

This work function polls the TSYNCTXCTL valid bit to determine when a
timestamp has been taken for the current stored skb.

.. _`igb_ptp_rx_hang`:

igb_ptp_rx_hang
===============

.. c:function:: void igb_ptp_rx_hang(struct igb_adapter *adapter)

    detect error case when Rx timestamp registers latched

    :param struct igb_adapter \*adapter:
        private network adapter structure

.. _`igb_ptp_rx_hang.description`:

Description
-----------

This watchdog task is scheduled to detect error case where hardware has
dropped an Rx packet that was timestamped when the ring is full. The
particular error is rare but leaves the device in a state unable to timestamp
any future packets.

.. _`igb_ptp_tx_hwtstamp`:

igb_ptp_tx_hwtstamp
===================

.. c:function:: void igb_ptp_tx_hwtstamp(struct igb_adapter *adapter)

    utility function which checks for TX time stamp

    :param struct igb_adapter \*adapter:
        Board private structure.

.. _`igb_ptp_tx_hwtstamp.description`:

Description
-----------

If we were asked to do hardware stamping and such a time stamp is
available, then it must have been for this skb here because we only
allow only one such packet into the queue.

.. _`igb_ptp_rx_pktstamp`:

igb_ptp_rx_pktstamp
===================

.. c:function:: void igb_ptp_rx_pktstamp(struct igb_q_vector *q_vector, unsigned char *va, struct sk_buff *skb)

    retrieve Rx per packet timestamp

    :param struct igb_q_vector \*q_vector:
        Pointer to interrupt specific structure

    :param unsigned char \*va:
        Pointer to address containing Rx buffer

    :param struct sk_buff \*skb:
        Buffer containing timestamp and packet

.. _`igb_ptp_rx_pktstamp.description`:

Description
-----------

This function is meant to retrieve a timestamp from the first buffer of an
incoming frame.  The value is stored in little endian format starting on
byte 8.

.. _`igb_ptp_rx_rgtstamp`:

igb_ptp_rx_rgtstamp
===================

.. c:function:: void igb_ptp_rx_rgtstamp(struct igb_q_vector *q_vector, struct sk_buff *skb)

    retrieve Rx timestamp stored in register

    :param struct igb_q_vector \*q_vector:
        Pointer to interrupt specific structure

    :param struct sk_buff \*skb:
        Buffer containing timestamp and packet

.. _`igb_ptp_rx_rgtstamp.description`:

Description
-----------

This function is meant to retrieve a timestamp from the internal registers
of the adapter and store it in the skb.

.. _`igb_ptp_get_ts_config`:

igb_ptp_get_ts_config
=====================

.. c:function:: int igb_ptp_get_ts_config(struct net_device *netdev, struct ifreq *ifr)

    get hardware time stamping config

    :param struct net_device \*netdev:
        *undescribed*

    :param struct ifreq \*ifr:
        *undescribed*

.. _`igb_ptp_get_ts_config.description`:

Description
-----------

Get the hwtstamp_config settings to return to the user. Rather than attempt
to deconstruct the settings from the registers, just return a shadow copy
of the last known settings.

.. _`igb_ptp_set_timestamp_mode`:

igb_ptp_set_timestamp_mode
==========================

.. c:function:: int igb_ptp_set_timestamp_mode(struct igb_adapter *adapter, struct hwtstamp_config *config)

    setup hardware for timestamping

    :param struct igb_adapter \*adapter:
        networking device structure

    :param struct hwtstamp_config \*config:
        hwtstamp configuration

.. _`igb_ptp_set_timestamp_mode.description`:

Description
-----------

Outgoing time stamping can be enabled and disabled. Play nice and
disable it when requested, although it shouldn't case any overhead
when no packet needs it. At most one packet in the queue may be
marked for time stamping, otherwise it would be impossible to tell
for sure to which packet the hardware time stamp belongs.

Incoming time stamping has to be configured via the hardware
filters. Not all combinations are supported, in particular event
type has to be specified. Matching the kind of event packet is
not supported, with the exception of "all V2 events regardless of
level 2 or 4".

.. _`igb_ptp_set_ts_config`:

igb_ptp_set_ts_config
=====================

.. c:function:: int igb_ptp_set_ts_config(struct net_device *netdev, struct ifreq *ifr)

    set hardware time stamping config

    :param struct net_device \*netdev:
        *undescribed*

    :param struct ifreq \*ifr:
        *undescribed*

.. _`igb_ptp_stop`:

igb_ptp_stop
============

.. c:function:: void igb_ptp_stop(struct igb_adapter *adapter)

    Disable PTP device and stop the overflow check.

    :param struct igb_adapter \*adapter:
        Board private structure.

.. _`igb_ptp_stop.description`:

Description
-----------

This function stops the PTP support and cancels the delayed work.

.. _`igb_ptp_reset`:

igb_ptp_reset
=============

.. c:function:: void igb_ptp_reset(struct igb_adapter *adapter)

    Re-enable the adapter for PTP following a reset.

    :param struct igb_adapter \*adapter:
        Board private structure.

.. _`igb_ptp_reset.description`:

Description
-----------

This function handles the reset work required to re-enable the PTP device.

.. This file was automatic generated / don't edit.
