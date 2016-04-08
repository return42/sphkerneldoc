
.. _API-xdr-terminate-string:

====================
xdr_terminate_string
====================

*man xdr_terminate_string(9)*

*4.6.0-rc1*

'0'-terminate a string residing in an xdr_buf


Synopsis
========

.. c:function:: void xdr_terminate_string( struct xdr_buf * buf, const u32 len )

Arguments
=========

``buf``
    XDR buffer where string resides

``len``
    length of string, in bytes
