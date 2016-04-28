.. -*- coding: utf-8; mode: rst -*-

.. _API-wimax-report-rfkill-sw:

======================
wimax_report_rfkill_sw
======================

*man wimax_report_rfkill_sw(9)*

*4.6.0-rc5*

Reports changes in the software RF switch


Synopsis
========

.. c:function:: void wimax_report_rfkill_sw( struct wimax_dev * wimax_dev, enum wimax_rf_state state )

Arguments
=========

``wimax_dev``
    WiMAX device descriptor

``state``
    New state of the RF kill switch. ``WIMAX_RF_ON`` radio on,
    ``WIMAX_RF_OFF`` radio off.


Description
===========

Reports changes in the software RF switch state to the WiMAX stack.

The main use is during initialization, so the driver can query the
device for its current software radio kill switch state and feed it to
the system.

On the side, the device does not change the software state by itself. In
practice, this can happen, as the device might decide to switch (in
software) the radio off for different reasons.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
