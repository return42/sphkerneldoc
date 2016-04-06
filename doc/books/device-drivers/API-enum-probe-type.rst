
.. _API-enum-probe-type:

===============
enum probe_type
===============

*man enum probe_type(9)*

*4.6.0-rc1*

device driver probe type to try Device drivers may opt in for special handling of their respective probe routines. This tells the core what to expect and prefer.


Synopsis
========

.. code-block:: c

    enum probe_type {
      PROBE_DEFAULT_STRATEGY,
      PROBE_PREFER_ASYNCHRONOUS,
      PROBE_FORCE_SYNCHRONOUS
    };


Constants
=========

PROBE_DEFAULT_STRATEGY
    Used by drivers that work equally well whether probed synchronously or asynchronously.

PROBE_PREFER_ASYNCHRONOUS
    Drivers for “slow” devices which probing order is not essential for booting the system may opt into executing their probes asynchronously.

PROBE_FORCE_SYNCHRONOUS
    Use this to annotate drivers that need their probe routines to run synchronously with driver and device registration (with the exception of -EPROBE_DEFER handling - re-probing
    always ends up being done asynchronously).


Description
===========

Note that the end goal is to switch the kernel to use asynchronous probing by default, so annotating drivers with ``PROBE_PREFER_ASYNCHRONOUS`` is a temporary measure that allows
us to speed up boot process while we are validating the rest of the drivers.
