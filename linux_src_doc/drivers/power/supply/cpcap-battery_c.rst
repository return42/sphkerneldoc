.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/power/supply/cpcap-battery.c

.. _`cpcap_battery_cc_raw_div`:

cpcap_battery_cc_raw_div
========================

.. c:function:: int cpcap_battery_cc_raw_div(struct cpcap_battery_ddata *ddata, u32 sample, s32 accumulator, s16 offset, u32 divider)

    calculate and divide coulomb counter μAms values

    :param ddata:
        device driver data
    :type ddata: struct cpcap_battery_ddata \*

    :param sample:
        coulomb counter sample value
    :type sample: u32

    :param accumulator:
        coulomb counter integrator value
    :type accumulator: s32

    :param offset:
        coulomb counter offset value
    :type offset: s16

    :param divider:
        conversion divider
    :type divider: u32

.. _`cpcap_battery_cc_raw_div.description`:

Description
-----------

Note that cc_lsb and cc_dur values are from Motorola Linux kernel
function \ :c:func:`data_get_avg_curr_ua`\  and seem to be based on measured test
results. It also has the following comment:

Adjustment factors are applied here as a temp solution per the test
results. Need to work out a formal solution for this adjustment.

A coulomb counter for similar hardware seems to be documented in
"TWL6030 Gas Gauging Basics (Rev. A)" swca095a.pdf in chapter
"10 Calculating Accumulated Current". We however follow what the
Motorola mapphone Linux kernel is doing as there may be either a
TI or ST coulomb counter in the PMIC.

.. _`cpcap_battery_read_accumulated`:

cpcap_battery_read_accumulated
==============================

.. c:function:: int cpcap_battery_read_accumulated(struct cpcap_battery_ddata *ddata, struct cpcap_coulomb_counter_data *ccd)

    reads cpcap coulomb counter

    :param ddata:
        device driver data
    :type ddata: struct cpcap_battery_ddata \*

    :param ccd:
        *undescribed*
    :type ccd: struct cpcap_coulomb_counter_data \*

.. _`cpcap_battery_read_accumulated.description`:

Description
-----------

Based on Motorola mapphone kernel function \ :c:func:`data_read_regs`\ .
Looking at the registers, the coulomb counter seems similar to
the coulomb counter in TWL6030. See "TWL6030 Gas Gauging Basics
(Rev. A) swca095a.pdf for "10 Calculating Accumulated Current".

Note that swca095a.pdf instructs to stop the coulomb counter
before reading to avoid values changing. Motorola mapphone
Linux kernel does not do it, so let's assume they've verified
the data produced is correct.

.. _`cpcap_battery_cc_get_avg_current`:

cpcap_battery_cc_get_avg_current
================================

.. c:function:: int cpcap_battery_cc_get_avg_current(struct cpcap_battery_ddata *ddata)

    read cpcap coulumb counter

    :param ddata:
        cpcap battery driver device data
    :type ddata: struct cpcap_battery_ddata \*

.. This file was automatic generated / don't edit.

