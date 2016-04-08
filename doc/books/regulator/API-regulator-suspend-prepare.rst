
.. _API-regulator-suspend-prepare:

=========================
regulator_suspend_prepare
=========================

*man regulator_suspend_prepare(9)*

*4.6.0-rc1*

prepare regulators for system wide suspend


Synopsis
========

.. c:function:: int regulator_suspend_prepare( suspend_state_t state )

Arguments
=========

``state``
    system suspend state


Description
===========

Configure each regulator with it's suspend operating parameters for state. This will usually be called by machine suspend code prior to supending.
