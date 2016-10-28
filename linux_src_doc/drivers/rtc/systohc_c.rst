.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rtc/systohc.c

.. _`rtc_set_ntp_time`:

rtc_set_ntp_time
================

.. c:function:: int rtc_set_ntp_time(struct timespec64 now)

    Save NTP synchronized time to the RTC

    :param struct timespec64 now:
        Current time of day

.. _`rtc_set_ntp_time.description`:

Description
-----------

Replacement for the NTP platform function update_persistent_clock64
that stores time for later retrieval by rtc_hctosys.

Returns 0 on successful RTC update, -ENODEV if a RTC update is not
possible at all, and various other -errno for specific temporary failure
cases.

If temporary failure is indicated the caller should try again 'soon'

.. This file was automatic generated / don't edit.

