.. -*- coding: utf-8; mode: rst -*-

.. _API-clk-notifier-register:

=====================
clk_notifier_register
=====================

*man clk_notifier_register(9)*

*4.6.0-rc5*

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

debugging across notifier chains can be frustrating. Make sure that your
notifier callback function prints a nice big warning in case of failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
