.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-register-notifier:

===========================
regulator_register_notifier
===========================

*man regulator_register_notifier(9)*

*4.6.0-rc5*

register regulator event notifier


Synopsis
========

.. c:function:: int regulator_register_notifier( struct regulator * regulator, struct notifier_block * nb )

Arguments
=========

``regulator``
    regulator source

``nb``
    notifier block


Description
===========

Register notifier block to receive regulator events.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
