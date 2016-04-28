.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-unregister:

====================
regulator_unregister
====================

*man regulator_unregister(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
