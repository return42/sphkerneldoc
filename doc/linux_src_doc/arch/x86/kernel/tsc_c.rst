.. -*- coding: utf-8; mode: rst -*-

=====
tsc.c
=====


.. _`native_calibrate_tsc`:

native_calibrate_tsc
====================

.. c:function:: unsigned long native_calibrate_tsc ( void)

    calibrate the tsc on boot

    :param void:
        no arguments



.. _`tsc_refine_calibration_work`:

tsc_refine_calibration_work
===========================

.. c:function:: void tsc_refine_calibration_work (struct work_struct *work)

    Further refine tsc freq calibration @work - ignored.

    :param struct work_struct \*work:

        *undescribed*



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

