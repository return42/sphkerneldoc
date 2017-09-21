.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4/cxgb4_ptp.c

.. _`cxgb4_ptp_is_ptp_tx`:

cxgb4_ptp_is_ptp_tx
===================

.. c:function:: bool cxgb4_ptp_is_ptp_tx(struct sk_buff *skb)

    determine whether TX packet is PTP or not

    :param struct sk_buff \*skb:
        skb of outgoing ptp request

.. _`cxgb4_ptp_is_ptp_rx`:

cxgb4_ptp_is_ptp_rx
===================

.. c:function:: bool cxgb4_ptp_is_ptp_rx(struct sk_buff *skb)

    determine whether RX packet is PTP or not

    :param struct sk_buff \*skb:
        skb of incoming ptp request

.. _`cxgb4_ptp_read_hwstamp`:

cxgb4_ptp_read_hwstamp
======================

.. c:function:: void cxgb4_ptp_read_hwstamp(struct adapter *adapter, struct port_info *pi)

    read timestamp for TX event PTP message

    :param struct adapter \*adapter:
        board private structure

    :param struct port_info \*pi:
        port private structure

.. _`cxgb4_ptprx_timestamping`:

cxgb4_ptprx_timestamping
========================

.. c:function:: int cxgb4_ptprx_timestamping(struct port_info *pi, u8 port, u16 mode)

    Enable Timestamp for RX PTP event message

    :param struct port_info \*pi:
        port private structure

    :param u8 port:
        pot number

    :param u16 mode:
        RX mode

.. _`cxgb4_ptp_fineadjtime`:

cxgb4_ptp_fineadjtime
=====================

.. c:function:: int cxgb4_ptp_fineadjtime(struct adapter *adapter, s64 delta)

    Shift the time of the hardware clock

    :param struct adapter \*adapter:
        *undescribed*

    :param s64 delta:
        Desired change in nanoseconds

.. _`cxgb4_ptp_fineadjtime.description`:

Description
-----------

Adjust the timer by resetting the timecounter structure.

.. _`cxgb4_ptp_adjtime`:

cxgb4_ptp_adjtime
=================

.. c:function:: int cxgb4_ptp_adjtime(struct ptp_clock_info *ptp, s64 delta)

    Shift the time of the hardware clock

    :param struct ptp_clock_info \*ptp:
        ptp clock structure

    :param s64 delta:
        Desired change in nanoseconds

.. _`cxgb4_ptp_adjtime.description`:

Description
-----------

Adjust the timer by resetting the timecounter structure.

.. _`cxgb4_ptp_gettime`:

cxgb4_ptp_gettime
=================

.. c:function:: int cxgb4_ptp_gettime(struct ptp_clock_info *ptp, struct timespec64 *ts)

    Reads the current time from the hardware clock

    :param struct ptp_clock_info \*ptp:
        ptp clock structure

    :param struct timespec64 \*ts:
        timespec structure to hold the current time value

.. _`cxgb4_ptp_gettime.description`:

Description
-----------

Read the timecounter and return the correct value in ns after converting
it into a struct timespec.

.. _`cxgb4_ptp_settime`:

cxgb4_ptp_settime
=================

.. c:function:: int cxgb4_ptp_settime(struct ptp_clock_info *ptp, const struct timespec64 *ts)

    Set the current time on the hardware clock

    :param struct ptp_clock_info \*ptp:
        ptp clock structure

    :param const struct timespec64 \*ts:
        timespec containing the new time for the cycle counter

.. _`cxgb4_ptp_settime.description`:

Description
-----------

Reset value to new base value instead of the kernel
wall timer value.

.. _`cxgb4_ptp_enable`:

cxgb4_ptp_enable
================

.. c:function:: int cxgb4_ptp_enable(struct ptp_clock_info __always_unused *ptp, struct ptp_clock_request __always_unused *request, int __always_unused on)

    enable or disable an ancillary feature

    :param struct ptp_clock_info __always_unused \*ptp:
        ptp clock structure

    :param struct ptp_clock_request __always_unused \*request:
        Desired resource to enable or disable

    :param int __always_unused on:
        Caller passes one to enable or zero to disable

.. _`cxgb4_ptp_enable.description`:

Description
-----------

Enable (or disable) ancillary features of the PHC subsystem.
Currently, no ancillary features are supported.

.. _`cxgb4_ptp_init`:

cxgb4_ptp_init
==============

.. c:function:: void cxgb4_ptp_init(struct adapter *adapter)

    initialize PTP for devices which support it

    :param struct adapter \*adapter:
        board private structure

.. _`cxgb4_ptp_init.description`:

Description
-----------

This function performs the required steps for enabling PTP support.

.. _`cxgb4_ptp_stop`:

cxgb4_ptp_stop
==============

.. c:function:: void cxgb4_ptp_stop(struct adapter *adapter)

    disable PTP device and stop the overflow check

    :param struct adapter \*adapter:
        board private structure

.. _`cxgb4_ptp_stop.description`:

Description
-----------

Stop the PTP support.

.. This file was automatic generated / don't edit.

