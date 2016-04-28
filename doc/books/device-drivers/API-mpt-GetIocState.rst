.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-GetIocState:

===============
mpt_GetIocState
===============

*man mpt_GetIocState(9)*

*4.6.0-rc5*

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

Returns all IOC Doorbell register bits if cooked==0, else just the
Doorbell bits in MPI_IOC_STATE_MASK.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
