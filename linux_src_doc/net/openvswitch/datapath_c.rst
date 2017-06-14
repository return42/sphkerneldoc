.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/openvswitch/datapath.c

.. _`locking-`:

Locking:
========

All writes e.g. Writes to device state (add/remove datapath, port, set
operations on vports, etc.), Writes to other state (flow table
modifications, set miscellaneous datapath parameters, etc.) are protected
by ovs_lock.

Reads are protected by RCU.

There are a few special cases (mostly stats) that have their own
synchronization but they nest under all of above and don't interact with
each other.

The RTNL lock nests inside ovs_mutex.

.. This file was automatic generated / don't edit.

