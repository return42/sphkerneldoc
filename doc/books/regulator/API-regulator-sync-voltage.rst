.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-sync-voltage:

======================
regulator_sync_voltage
======================

*man regulator_sync_voltage(9)*

*4.6.0-rc5*

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

Re-apply the last configured voltage. This is intended to be used where
some external control source the consumer is cooperating with has caused
the configured voltage to change.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
