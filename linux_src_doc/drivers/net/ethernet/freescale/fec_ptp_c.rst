.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/freescale/fec_ptp.c

.. _`fec_ptp_enable_pps`:

fec_ptp_enable_pps
==================

.. c:function:: int fec_ptp_enable_pps(struct fec_enet_private *fep, uint enable)

    :param struct fec_enet_private \*fep:
        the fec_enet_private structure handle

    :param uint enable:
        enable the channel pps output

.. _`fec_ptp_enable_pps.description`:

Description
-----------

This function enble the PPS ouput on the timer channel.

.. _`fec_ptp_read`:

fec_ptp_read
============

.. c:function:: u64 fec_ptp_read(const struct cyclecounter *cc)

    read raw cycle counter (to be used by time counter)

    :param const struct cyclecounter \*cc:
        the cyclecounter structure

.. _`fec_ptp_read.description`:

Description
-----------

this function reads the cyclecounter registers and is called by the
cyclecounter structure used to construct a ns counter from the
arbitrary fixed point registers

.. _`fec_ptp_start_cyclecounter`:

fec_ptp_start_cyclecounter
==========================

.. c:function:: void fec_ptp_start_cyclecounter(struct net_device *ndev)

    create the cycle counter from hw

    :param struct net_device \*ndev:
        network device

.. _`fec_ptp_start_cyclecounter.description`:

Description
-----------

this function initializes the timecounter and cyclecounter
structures for use in generated a ns counter from the arbitrary
fixed point cycles registers in the hardware.

.. _`fec_ptp_adjfreq`:

fec_ptp_adjfreq
===============

.. c:function:: int fec_ptp_adjfreq(struct ptp_clock_info *ptp, s32 ppb)

    adjust ptp cycle frequency

    :param struct ptp_clock_info \*ptp:
        the ptp clock structure

    :param s32 ppb:
        parts per billion adjustment from base

.. _`fec_ptp_adjfreq.description`:

Description
-----------

Adjust the frequency of the ptp cycle counter by the
indicated ppb from the base frequency.

Because ENET hardware frequency adjust is complex,
using software method to do that.

.. _`fec_ptp_adjtime`:

fec_ptp_adjtime
===============

.. c:function:: int fec_ptp_adjtime(struct ptp_clock_info *ptp, s64 delta)

    :param struct ptp_clock_info \*ptp:
        the ptp clock structure

    :param s64 delta:
        offset to adjust the cycle counter by

.. _`fec_ptp_adjtime.description`:

Description
-----------

adjust the timer by resetting the timecounter structure.

.. _`fec_ptp_gettime`:

fec_ptp_gettime
===============

.. c:function:: int fec_ptp_gettime(struct ptp_clock_info *ptp, struct timespec64 *ts)

    :param struct ptp_clock_info \*ptp:
        the ptp clock structure

    :param struct timespec64 \*ts:
        timespec structure to hold the current time value

.. _`fec_ptp_gettime.description`:

Description
-----------

read the timecounter and return the correct value on ns,
after converting it into a struct timespec.

.. _`fec_ptp_settime`:

fec_ptp_settime
===============

.. c:function:: int fec_ptp_settime(struct ptp_clock_info *ptp, const struct timespec64 *ts)

    :param struct ptp_clock_info \*ptp:
        the ptp clock structure

    :param const struct timespec64 \*ts:
        the timespec containing the new time for the cycle counter

.. _`fec_ptp_settime.description`:

Description
-----------

reset the timecounter to use a new base value instead of the kernel
wall timer value.

.. _`fec_ptp_enable`:

fec_ptp_enable
==============

.. c:function:: int fec_ptp_enable(struct ptp_clock_info *ptp, struct ptp_clock_request *rq, int on)

    :param struct ptp_clock_info \*ptp:
        the ptp clock structure

    :param struct ptp_clock_request \*rq:
        the requested feature to change

    :param int on:
        whether to enable or disable the feature

.. _`fec_time_keep`:

fec_time_keep
=============

.. c:function:: void fec_time_keep(struct work_struct *work)

    call timecounter_read every second to avoid timer overrun because ENET just support 32bit counter, will timeout in 4s

    :param struct work_struct \*work:
        *undescribed*

.. _`fec_ptp_init`:

fec_ptp_init
============

.. c:function:: void fec_ptp_init(struct platform_device *pdev, int irq_idx)

    :param struct platform_device \*pdev:
        *undescribed*

    :param int irq_idx:
        *undescribed*

.. _`fec_ptp_init.description`:

Description
-----------

This function performs the required steps for enabling ptp
support. If ptp support has already been loaded it simply calls the
cyclecounter init routine and exits.

.. This file was automatic generated / don't edit.

