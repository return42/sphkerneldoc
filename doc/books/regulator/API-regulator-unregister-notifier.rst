.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-unregister-notifier:

=============================
regulator_unregister_notifier
=============================

*man regulator_unregister_notifier(9)*

*4.6.0-rc5*

unregister regulator event notifier


Synopsis
========

.. c:function:: int regulator_unregister_notifier( struct regulator * regulator, struct notifier_block * nb )

Arguments
=========

``regulator``
    regulator source

``nb``
    notifier block


Description
===========

Unregister regulator event notifier block.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
