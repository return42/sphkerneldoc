
.. _API-mpt-verify-adapter:

==================
mpt_verify_adapter
==================

*man mpt_verify_adapter(9)*

*4.6.0-rc1*

Given IOC identifier, set pointer to its adapter structure.


Synopsis
========

.. c:function:: int mpt_verify_adapter( int iocid, MPT_ADAPTER ** iocpp )

Arguments
=========

``iocid``
    IOC unique identifier (integer)

``iocpp``
    Pointer to pointer to IOC adapter


Description
===========

Given a unique IOC identifier, set pointer to the associated MPT adapter structure.

Returns iocid and sets iocpp if iocid is found. Returns -1 if iocid is not found.
