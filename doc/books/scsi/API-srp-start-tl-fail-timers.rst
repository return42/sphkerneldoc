
.. _API-srp-start-tl-fail-timers:

========================
srp_start_tl_fail_timers
========================

*man srp_start_tl_fail_timers(9)*

*4.6.0-rc1*

start the transport layer failure timers


Synopsis
========

.. c:function:: void srp_start_tl_fail_timers( struct srp_rport * rport )

Arguments
=========

``rport``
    SRP target port.


Description
===========

Start the transport layer fast I/O failure and device loss timers. Do not modify a timer that was already started.
