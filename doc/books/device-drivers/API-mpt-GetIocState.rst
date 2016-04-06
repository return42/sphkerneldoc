
.. _API-mpt-GetIocState:

===============
mpt_GetIocState
===============

*man mpt_GetIocState(9)*

*4.6.0-rc1*

Get the current state of a MPT adapter.


Synopsis
========

.. c:function:: u32 mpt_GetIocState( MPT_ADAPTER * ioc, int cooked )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``cooked``
    Request raw or cooked IOC state


Description
===========

Returns all IOC Doorbell register bits if cooked==0, else just the Doorbell bits in MPI_IOC_STATE_MASK.
