
.. _API-wimax-report-rfkill-hw:

======================
wimax_report_rfkill_hw
======================

*man wimax_report_rfkill_hw(9)*

*4.6.0-rc1*

Reports changes in the hardware RF switch


Synopsis
========

.. c:function:: void wimax_report_rfkill_hw( struct wimax_dev * wimax_dev, enum wimax_rf_state state )

Arguments
=========

``wimax_dev``
    WiMAX device descriptor

``state``
    New state of the RF Kill switch. ``WIMAX_RF_ON`` radio on, ``WIMAX_RF_OFF`` radio off.


Description
===========

When the device detects a change in the state of thehardware RF switch, it must call this function to let the WiMAX kernel stack know that the state has changed so it can be
properly propagated.

The WiMAX stack caches the state (the driver doesn't need to). As well, as the change is propagated it will come back as a request to change the software state to mirror the
hardware state.

If the device doesn't have a hardware kill switch, just report it on initialization as always on (``WIMAX_RF_ON``, radio on).
