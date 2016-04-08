
.. _API-regulator-sync-voltage:

======================
regulator_sync_voltage
======================

*man regulator_sync_voltage(9)*

*4.6.0-rc1*

re-apply last regulator output voltage


Synopsis
========

.. c:function:: int regulator_sync_voltage( struct regulator * regulator )

Arguments
=========

``regulator``
    regulator source


Description
===========

Re-apply the last configured voltage. This is intended to be used where some external control source the consumer is cooperating with has caused the configured voltage to change.
