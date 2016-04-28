.. -*- coding: utf-8; mode: rst -*-

.. _API-input-mt-report-finger-count:

============================
input_mt_report_finger_count
============================

*man input_mt_report_finger_count(9)*

*4.6.0-rc5*

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

Reports the contact count via BTN_TOOL_FINGER, BTN_TOOL_DOUBLETAP,
BTN_TOOL_TRIPLETAP and BTN_TOOL_QUADTAP.

The input core ensures only the KEY events already setup for this device
will produce output.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
