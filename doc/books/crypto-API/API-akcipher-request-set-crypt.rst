
.. _API-akcipher-request-set-crypt:

==========================
akcipher_request_set_crypt
==========================

*man akcipher_request_set_crypt(9)*

*4.6.0-rc1*

Sets request parameters


Synopsis
========

.. c:function:: void akcipher_request_set_crypt( struct akcipher_request * req, struct scatterlist * src, struct scatterlist * dst, unsigned int src_len, unsigned int dst_len )

Arguments
=========

``req``
    public key request

``src``
    ptr to input scatter list

``dst``
    ptr to output scatter list

``src_len``
    size of the src input scatter list to be processed

``dst_len``
    size of the dst output scatter list


Description
===========

Sets parameters required by crypto operation
