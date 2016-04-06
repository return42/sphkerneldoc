
.. _API-relay-switch-subbuf:

===================
relay_switch_subbuf
===================

*man relay_switch_subbuf(9)*

*4.6.0-rc1*

switch to a new sub-buffer


Synopsis
========

.. c:function:: size_t relay_switch_subbuf( struct rchan_buf * buf, size_t length )

Arguments
=========

``buf``
    channel buffer

``length``
    size of current event


Description
===========

Returns either the length passed in or 0 if full.

Performs sub-buffer-switch tasks such as invoking callbacks, updating padding counts, waking up readers, etc.
