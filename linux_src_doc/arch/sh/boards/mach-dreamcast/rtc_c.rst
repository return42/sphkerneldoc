.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/boards/mach-dreamcast/rtc.c

.. _`aica_rtc_gettimeofday`:

aica_rtc_gettimeofday
=====================

.. c:function:: void aica_rtc_gettimeofday(struct timespec *ts)

    Get the time from the AICA RTC

    :param ts:
        pointer to resulting timespec
    :type ts: struct timespec \*

.. _`aica_rtc_gettimeofday.description`:

Description
-----------

Grabs the current RTC seconds counter and adjusts it to the Unix Epoch.

.. _`aica_rtc_settimeofday`:

aica_rtc_settimeofday
=====================

.. c:function:: int aica_rtc_settimeofday(const time_t secs)

    Set the AICA RTC to the current time

    :param secs:
        contains the time_t to set
    :type secs: const time_t

.. _`aica_rtc_settimeofday.description`:

Description
-----------

Adjusts the given \ ``tv``\  to the AICA Epoch and sets the RTC seconds counter.

.. This file was automatic generated / don't edit.

