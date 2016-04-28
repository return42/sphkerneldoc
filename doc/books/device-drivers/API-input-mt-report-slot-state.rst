.. -*- coding: utf-8; mode: rst -*-

.. _API-input-mt-report-slot-state:

==========================
input_mt_report_slot_state
==========================

*man input_mt_report_slot_state(9)*

*4.6.0-rc5*

report contact state


Synopsis
========

.. c:function:: void input_mt_report_slot_state( struct input_dev * dev, unsigned int tool_type, bool active )

Arguments
=========

``dev``
    input device with allocated MT slots

``tool_type``
    the tool type to use in this slot

``active``
    true if contact is active, false otherwise


Description
===========

Reports a contact via ABS_MT_TRACKING_ID, and optionally
ABS_MT_TOOL_TYPE. If active is true and the slot is currently
inactive, or if the tool type is changed, a new tracking id is assigned
to the slot. The tool type is only reported if the corresponding absbit
field is set.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
