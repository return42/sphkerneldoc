
.. _API-napi-schedule:

=============
napi_schedule
=============

*man napi_schedule(9)*

*4.6.0-rc1*

schedule NAPI poll


Synopsis
========

.. c:function:: void napi_schedule( struct napi_struct * n )

Arguments
=========

``n``
    NAPI context


Description
===========

Schedule NAPI poll routine to be called if it is not already running.
