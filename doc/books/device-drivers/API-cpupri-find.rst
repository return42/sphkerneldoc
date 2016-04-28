.. -*- coding: utf-8; mode: rst -*-

.. _API-cpupri-find:

===========
cpupri_find
===========

*man cpupri_find(9)*

*4.6.0-rc5*

find the best (lowest-pri) CPU in the system


Synopsis
========

.. c:function:: int cpupri_find( struct cpupri * cp, struct task_struct * p, struct cpumask * lowest_mask )

Arguments
=========

``cp``
    The cpupri context

``p``
    The task

``lowest_mask``
    A mask to fill in with selected CPUs (or NULL)


Note
====

This function returns the recommended CPUs as calculated during the
current invocation. By the time the call returns, the CPUs may have in
fact changed priorities any number of times. While not ideal, it is not
an issue of correctness since the normal rebalancer logic will correct
any discrepancies created by racing against the uncertainty of the
current priority configuration.


Return
======

(int)bool - CPUs were found


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
