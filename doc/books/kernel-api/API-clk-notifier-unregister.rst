
.. _API-clk-notifier-unregister:

=======================
clk_notifier_unregister
=======================

*man clk_notifier_unregister(9)*

*4.6.0-rc1*

change notifier callback


Synopsis
========

.. c:function:: int clk_notifier_unregister( struct clk * clk, struct notifier_block * nb )

Arguments
=========

``clk``
    clock whose rate we are no longer interested in

``nb``
    notifier block which will be unregistered
