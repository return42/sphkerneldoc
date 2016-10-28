.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/e1000e/ptp.c

.. _`e1000e_phc_adjfreq`:

e1000e_phc_adjfreq
==================

.. c:function:: int e1000e_phc_adjfreq(struct ptp_clock_info *ptp, s32 delta)

    adjust the frequency of the hardware clock

    :param struct ptp_clock_info \*ptp:
        ptp clock structure

    :param s32 delta:
        Desired frequency change in parts per billion

.. _`e1000e_phc_adjfreq.description`:

Description
-----------

Adjust the frequency of the PHC cycle counter by the indicated delta from
the base frequency.

.. _`e1000e_phc_adjtime`:

e1000e_phc_adjtime
==================

.. c:function:: int e1000e_phc_adjtime(struct ptp_clock_info *ptp, s64 delta)

    Shift the time of the hardware clock

    :param struct ptp_clock_info \*ptp:
        ptp clock structure

    :param s64 delta:
        Desired change in nanoseconds

.. _`e1000e_phc_adjtime.description`:

Description
-----------

Adjust the timer by resetting the timecounter structure.

.. _`e1000e_phc_get_syncdevicetime`:

e1000e_phc_get_syncdevicetime
=============================

.. c:function:: int e1000e_phc_get_syncdevicetime(ktime_t *device, struct system_counterval_t *system, void *ctx)

    Callback given to timekeeping code reads system/device registers

    :param ktime_t \*device:
        current device time

    :param struct system_counterval_t \*system:
        system counter value read synchronously with device time

    :param void \*ctx:
        context provided by timekeeping code

.. _`e1000e_phc_get_syncdevicetime.description`:

Description
-----------

Read device and system (ART) clock simultaneously and return the corrected
clock values in ns.

.. _`e1000e_phc_getcrosststamp`:

e1000e_phc_getcrosststamp
=========================

.. c:function:: int e1000e_phc_getcrosststamp(struct ptp_clock_info *ptp, struct system_device_crosststamp *xtstamp)

    Reads the current system/device cross timestamp

    :param struct ptp_clock_info \*ptp:
        ptp clock structure

    :param struct system_device_crosststamp \*xtstamp:
        *undescribed*

.. _`e1000e_phc_getcrosststamp.description`:

Description
-----------

Read device and system (ART) clock simultaneously and return the scaled
clock values in ns.

.. _`e1000e_phc_gettime`:

e1000e_phc_gettime
==================

.. c:function:: int e1000e_phc_gettime(struct ptp_clock_info *ptp, struct timespec64 *ts)

    Reads the current time from the hardware clock

    :param struct ptp_clock_info \*ptp:
        ptp clock structure

    :param struct timespec64 \*ts:
        timespec structure to hold the current time value

.. _`e1000e_phc_gettime.description`:

Description
-----------

Read the timecounter and return the correct value in ns after converting
it into a struct timespec.

.. _`e1000e_phc_settime`:

e1000e_phc_settime
==================

.. c:function:: int e1000e_phc_settime(struct ptp_clock_info *ptp, const struct timespec64 *ts)

    Set the current time on the hardware clock

    :param struct ptp_clock_info \*ptp:
        ptp clock structure

    :param const struct timespec64 \*ts:
        timespec containing the new time for the cycle counter

.. _`e1000e_phc_settime.description`:

Description
-----------

Reset the timecounter to use a new base value instead of the kernel
wall timer value.

.. _`e1000e_phc_enable`:

e1000e_phc_enable
=================

.. c:function:: int e1000e_phc_enable(struct ptp_clock_info __always_unused *ptp, struct ptp_clock_request __always_unused *request, int __always_unused on)

    enable or disable an ancillary feature

    :param struct ptp_clock_info __always_unused \*ptp:
        ptp clock structure

    :param struct ptp_clock_request __always_unused \*request:
        Desired resource to enable or disable

    :param int __always_unused on:
        Caller passes one to enable or zero to disable

.. _`e1000e_phc_enable.description`:

Description
-----------

Enable (or disable) ancillary features of the PHC subsystem.
Currently, no ancillary features are supported.

.. _`e1000e_ptp_init`:

e1000e_ptp_init
===============

.. c:function:: void e1000e_ptp_init(struct e1000_adapter *adapter)

    initialize PTP for devices which support it

    :param struct e1000_adapter \*adapter:
        board private structure

.. _`e1000e_ptp_init.description`:

Description
-----------

This function performs the required steps for enabling PTP support.
If PTP support has already been loaded it simply calls the cyclecounter
init routine and exits.

.. _`e1000e_ptp_remove`:

e1000e_ptp_remove
=================

.. c:function:: void e1000e_ptp_remove(struct e1000_adapter *adapter)

    disable PTP device and stop the overflow check

    :param struct e1000_adapter \*adapter:
        board private structure

.. _`e1000e_ptp_remove.description`:

Description
-----------

Stop the PTP support, and cancel the delayed work.

.. This file was automatic generated / don't edit.

