.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/qlogic/qede/qede_ptp.c

.. _`qede_ptp_adjfreq`:

qede_ptp_adjfreq
================

.. c:function:: int qede_ptp_adjfreq(struct ptp_clock_info *info, s32 ppb)

    :param struct ptp_clock_info \*info:
        *undescribed*

    :param s32 ppb:
        parts per billion adjustment from base

.. _`qede_ptp_adjfreq.description`:

Description
-----------

Adjust the frequency of the ptp cycle counter by the
indicated ppb from the base frequency.

.. This file was automatic generated / don't edit.

