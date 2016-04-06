
.. _API-get-sd-load-idx:

===============
get_sd_load_idx
===============

*man get_sd_load_idx(9)*

*4.6.0-rc1*

Obtain the load index for a given sched domain.


Synopsis
========

.. c:function:: int get_sd_load_idx( struct sched_domain * sd, enum cpu_idle_type idle )

Arguments
=========

``sd``
    The sched_domain whose load_idx is to be obtained.

``idle``
    The idle status of the CPU for whose sd load_idx is obtained.


Return
======

The load index.
