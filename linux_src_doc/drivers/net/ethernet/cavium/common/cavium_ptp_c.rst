.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/cavium/common/cavium_ptp.c

.. _`cavium_ptp_adjfine`:

cavium_ptp_adjfine
==================

.. c:function:: int cavium_ptp_adjfine(struct ptp_clock_info *ptp_info, long scaled_ppm)

    Adjust ptp frequency

    :param struct ptp_clock_info \*ptp_info:
        *undescribed*

    :param long scaled_ppm:
        how much to adjust by, in parts per million, but with a
        16 bit binary fractional field

.. _`cavium_ptp_adjtime`:

cavium_ptp_adjtime
==================

.. c:function:: int cavium_ptp_adjtime(struct ptp_clock_info *ptp_info, s64 delta)

    Adjust ptp time

    :param struct ptp_clock_info \*ptp_info:
        *undescribed*

    :param s64 delta:
        how much to adjust by, in nanosecs

.. _`cavium_ptp_gettime`:

cavium_ptp_gettime
==================

.. c:function:: int cavium_ptp_gettime(struct ptp_clock_info *ptp_info, struct timespec64 *ts)

    Get hardware clock time with adjustment

    :param struct ptp_clock_info \*ptp_info:
        *undescribed*

    :param struct timespec64 \*ts:
        timespec

.. _`cavium_ptp_settime`:

cavium_ptp_settime
==================

.. c:function:: int cavium_ptp_settime(struct ptp_clock_info *ptp_info, const struct timespec64 *ts)

    Set hardware clock time. Reset adjustment

    :param struct ptp_clock_info \*ptp_info:
        *undescribed*

    :param const struct timespec64 \*ts:
        timespec

.. _`cavium_ptp_enable`:

cavium_ptp_enable
=================

.. c:function:: int cavium_ptp_enable(struct ptp_clock_info *ptp_info, struct ptp_clock_request *rq, int on)

    Request to enable or disable an ancillary feature.

    :param struct ptp_clock_info \*ptp_info:
        *undescribed*

    :param struct ptp_clock_request \*rq:
        request

    :param int on:
        is it on

.. This file was automatic generated / don't edit.

