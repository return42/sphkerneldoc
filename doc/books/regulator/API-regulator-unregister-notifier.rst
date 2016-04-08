
.. _API-regulator-unregister-notifier:

=============================
regulator_unregister_notifier
=============================

*man regulator_unregister_notifier(9)*

*4.6.0-rc1*

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
