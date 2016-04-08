
.. _API-regulator-is-enabled:

====================
regulator_is_enabled
====================

*man regulator_is_enabled(9)*

*4.6.0-rc1*

is the regulator output enabled


Synopsis
========

.. c:function:: int regulator_is_enabled( struct regulator * regulator )

Arguments
=========

``regulator``
    regulator source


Description
===========

Returns positive if the regulator driver backing the source/client has requested that the device be enabled, zero if it hasn't, else a negative errno code.

Note that the device backing this regulator handle can have multiple users, so it might be enabled even if ``regulator_enable`` was never called for this particular source.
