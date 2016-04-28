.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-suspend-finish:

========================
regulator_suspend_finish
========================

*man regulator_suspend_finish(9)*

*4.6.0-rc5*

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

Turn on regulators that might be turned off by
regulator_suspend_prepare and that should be turned on according to
the regulators properties.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
