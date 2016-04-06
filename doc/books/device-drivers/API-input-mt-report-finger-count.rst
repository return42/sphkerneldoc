
.. _API-input-mt-report-finger-count:

============================
input_mt_report_finger_count
============================

*man input_mt_report_finger_count(9)*

*4.6.0-rc1*

report contact count


Synopsis
========

.. c:function:: void input_mt_report_finger_count( struct input_dev * dev, int count )

Arguments
=========

``dev``
    input device with allocated MT slots

``count``
    the number of contacts


Description
===========

Reports the contact count via BTN_TOOL_FINGER, BTN_TOOL_DOUBLETAP, BTN_TOOL_TRIPLETAP and BTN_TOOL_QUADTAP.

The input core ensures only the KEY events already setup for this device will produce output.
