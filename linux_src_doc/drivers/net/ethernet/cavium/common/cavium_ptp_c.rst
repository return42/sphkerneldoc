.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/cavium/common/cavium_ptp.c

.. _`cavium_ptp_adjfine`:

cavium_ptp_adjfine
==================

.. c:function:: int cavium_ptp_adjfine(struct ptp_clock_info *ptp_info, long scaled_ppm)

    Adjust ptp frequency

    :param ptp_info:
        *undescribed*
    :type ptp_info: struct ptp_clock_info \*

    :param scaled_ppm:
        how much to adjust by, in parts per million, but with a
        16 bit binary fractional field
    :type scaled_ppm: long

.. _`cavium_ptp_adjtime`:

cavium_ptp_adjtime
==================

.. c:function:: int cavium_ptp_adjtime(struct ptp_clock_info *ptp_info, s64 delta)

    Adjust ptp time

    :param ptp_info:
        *undescribed*
    :type ptp_info: struct ptp_clock_info \*

    :param delta:
        how much to adjust by, in nanosecs
    :type delta: s64

.. _`cavium_ptp_gettime`:

cavium_ptp_gettime
==================

.. c:function:: int cavium_ptp_gettime(struct ptp_clock_info *ptp_info, struct timespec64 *ts)

    Get hardware clock time with adjustment

    :param ptp_info:
        *undescribed*
    :type ptp_info: struct ptp_clock_info \*

    :param ts:
        timespec
    :type ts: struct timespec64 \*

.. _`cavium_ptp_settime`:

cavium_ptp_settime
==================

.. c:function:: int cavium_ptp_settime(struct ptp_clock_info *ptp_info, const struct timespec64 *ts)

    Set hardware clock time. Reset adjustment

    :param ptp_info:
        *undescribed*
    :type ptp_info: struct ptp_clock_info \*

    :param ts:
        timespec
    :type ts: const struct timespec64 \*

.. _`cavium_ptp_enable`:

cavium_ptp_enable
=================

.. c:function:: int cavium_ptp_enable(struct ptp_clock_info *ptp_info, struct ptp_clock_request *rq, int on)

    Request to enable or disable an ancillary feature.

    :param ptp_info:
        *undescribed*
    :type ptp_info: struct ptp_clock_info \*

    :param rq:
        request
    :type rq: struct ptp_clock_request \*

    :param on:
        is it on
    :type on: int

.. This file was automatic generated / don't edit.

