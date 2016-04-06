
.. _API-mpt-event-register:

==================
mpt_event_register
==================

*man mpt_event_register(9)*

*4.6.0-rc1*

Register protocol-specific event callback handler.


Synopsis
========

.. c:function:: int mpt_event_register( u8 cb_idx, MPT_EVHANDLER ev_cbfunc )

Arguments
=========

``cb_idx``
    previously registered (via mpt_register) callback handle

``ev_cbfunc``
    callback function


Description
===========

This routine can be called by one or more protocol-specific drivers if/when they choose to be notified of MPT events.

Returns 0 for success.
