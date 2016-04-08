
.. _API-wimax-rfkill:

============
wimax_rfkill
============

*man wimax_rfkill(9)*

*4.6.0-rc1*

Set the software RF switch state for a WiMAX device


Synopsis
========

.. c:function:: int wimax_rfkill( struct wimax_dev * wimax_dev, enum wimax_rf_state state )

Arguments
=========

``wimax_dev``
    WiMAX device descriptor

``state``
    New RF state.


Returns
=======

>= 0 toggle state if ok, < 0 errno code on error. The toggle state is returned as a bitmap, bit 0 being the hardware RF state, bit 1 the software RF state.

0 means disabled (``WIMAX_RF_ON``, radio on), 1 means enabled radio off (``WIMAX_RF_OFF``).


Description
===========

Called by the user when he wants to request the WiMAX radio to be switched on (``WIMAX_RF_ON``) or off (``WIMAX_RF_OFF``). With ``WIMAX_RF_QUERY``, just the current state is
returned.


NOTE
====

This call will block until the operation is complete.
