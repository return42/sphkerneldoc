
.. _API-input-mt-report-pointer-emulation:

=================================
input_mt_report_pointer_emulation
=================================

*man input_mt_report_pointer_emulation(9)*

*4.6.0-rc1*

common pointer emulation


Synopsis
========

.. c:function:: void input_mt_report_pointer_emulation( struct input_dev * dev, bool use_count )

Arguments
=========

``dev``
    input device with allocated MT slots

``use_count``
    report number of active contacts as finger count


Description
===========

Performs legacy pointer emulation via BTN_TOUCH, ABS_X, ABS_Y and ABS_PRESSURE. Touchpad finger count is emulated if use_count is true.

The input core ensures only the KEY and ABS axes already setup for this device will produce output.
