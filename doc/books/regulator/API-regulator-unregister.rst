
.. _API-regulator-unregister:

====================
regulator_unregister
====================

*man regulator_unregister(9)*

*4.6.0-rc1*

unregister regulator


Synopsis
========

.. c:function:: void regulator_unregister( struct regulator_dev * rdev )

Arguments
=========

``rdev``
    regulator to unregister


Description
===========

Called by regulator drivers to unregister a regulator.
