.. -*- coding: utf-8; mode: rst -*-

.. _API-calculate-imbalance:

===================
calculate_imbalance
===================

*man calculate_imbalance(9)*

*4.6.0-rc5*

Calculate the amount of imbalance present within the groups of a given
sched_domain during load balance.


Synopsis
========

.. c:function:: void calculate_imbalance( struct lb_env * env, struct sd_lb_stats * sds )

Arguments
=========

``env``
    load balance environment

``sds``
    statistics of the sched_domain whose imbalance is to be calculated.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
