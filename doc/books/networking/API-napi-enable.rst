
.. _API-napi-enable:

===========
napi_enable
===========

*man napi_enable(9)*

*4.6.0-rc1*

enable NAPI scheduling


Synopsis
========

.. c:function:: void napi_enable( struct napi_struct * n )

Arguments
=========

``n``
    NAPI context


Description
===========

Resume NAPI from being scheduled on this context. Must be paired with napi_disable.
