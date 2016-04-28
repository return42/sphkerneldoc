.. -*- coding: utf-8; mode: rst -*-

.. _API-check-asym-packing:

==================
check_asym_packing
==================

*man check_asym_packing(9)*

*4.6.0-rc5*

Check to see if the group is packed into the sched doman.


Synopsis
========

.. c:function:: int check_asym_packing( struct lb_env * env, struct sd_lb_stats * sds )

Arguments
=========

``env``
    The load balancing environment.

``sds``
    Statistics of the sched_domain which is to be packed


Description
===========

This is primarily intended to used at the sibling level. Some cores like
POWER7 prefer to use lower numbered SMT threads. In the case of POWER7,
it can move to lower SMT modes only when higher threads are idle. When
in lower SMT modes, the threads will perform better since they share
less core resources. Hence when we have idle threads, we want them to be
the higher ones.

This packing function is run on idle threads. It checks to see if the
busiest CPU in this domain (core in the P7 case) has a higher CPU number
than the packing function is being run on. Here we are assuming lower
CPU number will be equivalent to lower a SMT thread number.


Return
======

1 when packing is required and a task should be moved to this CPU. The
amount of the imbalance is returned in *imbalance.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
