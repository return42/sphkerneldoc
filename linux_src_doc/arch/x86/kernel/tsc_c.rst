.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/tsc.c

.. _`native_calibrate_tsc`:

native_calibrate_tsc
====================

.. c:function:: unsigned long native_calibrate_tsc( void)

    Determine TSC frequency via CPUID, else return 0.

    :param void:
        no arguments
    :type void: 

.. _`native_calibrate_cpu_early`:

native_calibrate_cpu_early
==========================

.. c:function:: unsigned long native_calibrate_cpu_early( void)

    can calibrate the cpu early in boot

    :param void:
        no arguments
    :type void: 

.. _`native_calibrate_cpu`:

native_calibrate_cpu
====================

.. c:function:: unsigned long native_calibrate_cpu( void)

    calibrate the cpu

    :param void:
        no arguments
    :type void: 

.. _`convert_art_ns_to_tsc`:

convert_art_ns_to_tsc
=====================

.. c:function:: struct system_counterval_t convert_art_ns_to_tsc(u64 art_ns)

    Convert ART in nanoseconds to TSC.

    :param art_ns:
        ART (Always Running Timer) in unit of nanoseconds
    :type art_ns: u64

.. _`convert_art_ns_to_tsc.description`:

Description
-----------

PTM requires all timestamps to be in units of nanoseconds. When user
software requests a cross-timestamp, this function converts system timestamp
to TSC.

This is valid when CPU feature flag X86_FEATURE_TSC_KNOWN_FREQ is set
indicating the tsc_khz is derived from CPUID[15H]. Drivers should check
that this flag is set before conversion to TSC is attempted.

.. _`convert_art_ns_to_tsc.return`:

Return
------

struct system_counterval_t - system counter value with the pointer to the
corresponding clocksource

.. _`tsc_refine_calibration_work`:

tsc_refine_calibration_work
===========================

.. c:function:: void tsc_refine_calibration_work(struct work_struct *work)

    Further refine tsc freq calibration \ ``work``\  - ignored.

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`tsc_refine_calibration_work.description`:

Description
-----------

This functions uses delayed work over a period of a
second to further refine the TSC freq value. Since this is
timer based, instead of loop based, we don't block the boot
process while this longer calibration is done.

If there are any calibration anomalies (too many SMIs, etc),
or the refined calibration is off by 1% of the fast early
calibration, we throw out the new calibration and use the
early calibration.

.. This file was automatic generated / don't edit.

