
.. _API-napi-synchronize:

================
napi_synchronize
================

*man napi_synchronize(9)*

*4.6.0-rc1*

wait until NAPI is not running


Synopsis
========

.. c:function:: void napi_synchronize( const struct napi_struct * n )

Arguments
=========

``n``
    NAPI context


Description
===========

Wait until NAPI is done being scheduled on this context. Waits till any outstanding processing completes but does not disable future activations.
