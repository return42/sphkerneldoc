
.. _API-struct-clk-notifier-data:

========================
struct clk_notifier_data
========================

*man struct clk_notifier_data(9)*

*4.6.0-rc1*

rate data to pass to the notifier callback


Synopsis
========

.. code-block:: c

    struct clk_notifier_data {
      struct clk * clk;
      unsigned long old_rate;
      unsigned long new_rate;
    };


Members
=======

clk
    struct clk ⋆ being changed

old_rate
    previous rate of this clk

new_rate
    new rate of this clk


Description
===========

For a pre-notifier, old_rate is the clk's rate before this rate change, and new_rate is what the rate will be in the future. For a post-notifier, old_rate and new_rate are both
set to the clk's current rate (this was done to optimize the implementation).
