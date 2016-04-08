
.. _API-napi-complete:

=============
napi_complete
=============

*man napi_complete(9)*

*4.6.0-rc1*

NAPI processing complete


Synopsis
========

.. c:function:: void napi_complete( struct napi_struct * n )

Arguments
=========

``n``
    NAPI context


Description
===========

Mark NAPI processing as complete. Consider using ``napi_complete_done`` instead.
