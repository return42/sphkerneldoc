
.. _API-regulator-suspend-finish:

========================
regulator_suspend_finish
========================

*man regulator_suspend_finish(9)*

*4.6.0-rc1*

resume regulators from system wide suspend


Synopsis
========

.. c:function:: int regulator_suspend_finish( void )

Arguments
=========

``void``
    no arguments


Description
===========

Turn on regulators that might be turned off by regulator_suspend_prepare and that should be turned on according to the regulators properties.
