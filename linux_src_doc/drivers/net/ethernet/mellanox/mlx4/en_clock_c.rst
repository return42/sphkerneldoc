.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/mellanox/mlx4/en_clock.c

.. _`mlx4_en_remove_timestamp`:

mlx4_en_remove_timestamp
========================

.. c:function:: void mlx4_en_remove_timestamp(struct mlx4_en_dev *mdev)

    disable PTP device

    :param mdev:
        board private structure
    :type mdev: struct mlx4_en_dev \*

.. _`mlx4_en_remove_timestamp.description`:

Description
-----------

Stop the PTP support.

.. _`mlx4_en_phc_adjfreq`:

mlx4_en_phc_adjfreq
===================

.. c:function:: int mlx4_en_phc_adjfreq(struct ptp_clock_info *ptp, s32 delta)

    adjust the frequency of the hardware clock

    :param ptp:
        ptp clock structure
    :type ptp: struct ptp_clock_info \*

    :param delta:
        Desired frequency change in parts per billion
    :type delta: s32

.. _`mlx4_en_phc_adjfreq.description`:

Description
-----------

Adjust the frequency of the PHC cycle counter by the indicated delta from
the base frequency.

.. _`mlx4_en_phc_adjtime`:

mlx4_en_phc_adjtime
===================

.. c:function:: int mlx4_en_phc_adjtime(struct ptp_clock_info *ptp, s64 delta)

    Shift the time of the hardware clock

    :param ptp:
        ptp clock structure
    :type ptp: struct ptp_clock_info \*

    :param delta:
        Desired change in nanoseconds
    :type delta: s64

.. _`mlx4_en_phc_adjtime.description`:

Description
-----------

Adjust the timer by resetting the timecounter structure.

.. _`mlx4_en_phc_gettime`:

mlx4_en_phc_gettime
===================

.. c:function:: int mlx4_en_phc_gettime(struct ptp_clock_info *ptp, struct timespec64 *ts)

    Reads the current time from the hardware clock

    :param ptp:
        ptp clock structure
    :type ptp: struct ptp_clock_info \*

    :param ts:
        timespec structure to hold the current time value
    :type ts: struct timespec64 \*

.. _`mlx4_en_phc_gettime.description`:

Description
-----------

Read the timecounter and return the correct value in ns after converting
it into a struct timespec.

.. _`mlx4_en_phc_settime`:

mlx4_en_phc_settime
===================

.. c:function:: int mlx4_en_phc_settime(struct ptp_clock_info *ptp, const struct timespec64 *ts)

    Set the current time on the hardware clock

    :param ptp:
        ptp clock structure
    :type ptp: struct ptp_clock_info \*

    :param ts:
        timespec containing the new time for the cycle counter
    :type ts: const struct timespec64 \*

.. _`mlx4_en_phc_settime.description`:

Description
-----------

Reset the timecounter to use a new base value instead of the kernel
wall timer value.

.. _`mlx4_en_phc_enable`:

mlx4_en_phc_enable
==================

.. c:function:: int mlx4_en_phc_enable(struct ptp_clock_info __always_unused *ptp, struct ptp_clock_request __always_unused *request, int __always_unused on)

    enable or disable an ancillary feature

    :param ptp:
        ptp clock structure
    :type ptp: struct ptp_clock_info __always_unused \*

    :param request:
        Desired resource to enable or disable
    :type request: struct ptp_clock_request __always_unused \*

    :param on:
        Caller passes one to enable or zero to disable
    :type on: int __always_unused

.. _`mlx4_en_phc_enable.description`:

Description
-----------

Enable (or disable) ancillary features of the PHC subsystem.
Currently, no ancillary features are supported.

.. This file was automatic generated / don't edit.

