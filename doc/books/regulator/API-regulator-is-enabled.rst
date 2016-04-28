.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-is-enabled:

====================
regulator_is_enabled
====================

*man regulator_is_enabled(9)*

*4.6.0-rc5*

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

Returns positive if the regulator driver backing the source/client has
requested that the device be enabled, zero if it hasn't, else a negative
errno code.

Note that the device backing this regulator handle can have multiple
users, so it might be enabled even if ``regulator_enable`` was never
called for this particular source.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
