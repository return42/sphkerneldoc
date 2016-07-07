.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/ntp.c

.. _`pps_clear`:

pps_clear
=========

.. c:function:: void pps_clear( void)

    Clears the PPS state variables

    :param  void:
        no arguments

.. _`ntp_synced`:

ntp_synced
==========

.. c:function:: int ntp_synced( void)

    Returns 1 if the NTP status is not UNSYNC

    :param  void:
        no arguments

.. _`ntp_clear`:

ntp_clear
=========

.. c:function:: void ntp_clear( void)

    Clears the NTP state variables

    :param  void:
        no arguments

.. _`ntp_get_next_leap`:

ntp_get_next_leap
=================

.. c:function:: ktime_t ntp_get_next_leap( void)

    Returns the next leapsecond in CLOCK_REALTIME ktime_t

    :param  void:
        no arguments

.. _`ntp_get_next_leap.description`:

Description
-----------

Provides the time of the next leapsecond against CLOCK_REALTIME in
a ktime_t format. Returns KTIME_MAX if no leapsecond is pending.

.. _`ntp_validate_timex`:

ntp_validate_timex
==================

.. c:function:: int ntp_validate_timex(struct timex *txc)

    Ensures the timex is ok for use in do_adjtimex

    :param struct timex \*txc:
        *undescribed*

.. This file was automatic generated / don't edit.

