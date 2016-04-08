
.. _API-regulator-register-notifier:

===========================
regulator_register_notifier
===========================

*man regulator_register_notifier(9)*

*4.6.0-rc1*

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
