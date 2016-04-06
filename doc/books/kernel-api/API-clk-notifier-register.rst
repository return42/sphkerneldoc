
.. _API-clk-notifier-register:

=====================
clk_notifier_register
=====================

*man clk_notifier_register(9)*

*4.6.0-rc1*

change notifier callback


Synopsis
========

.. c:function:: int clk_notifier_register( struct clk * clk, struct notifier_block * nb )

Arguments
=========

``clk``
    clock whose rate we are interested in

``nb``
    notifier block with callback function pointer


ProTip
======

debugging across notifier chains can be frustrating. Make sure that your notifier callback function prints a nice big warning in case of failure.
