
.. _API-ablkcipher-request-set-crypt:

============================
ablkcipher_request_set_crypt
============================

*man ablkcipher_request_set_crypt(9)*

*4.6.0-rc1*

set data buffers


Synopsis
========

.. c:function:: void ablkcipher_request_set_crypt( struct ablkcipher_request * req, struct scatterlist * src, struct scatterlist * dst, unsigned int nbytes, void * iv )

Arguments
=========

``req``
    request handle

``src``
    source scatter / gather list

``dst``
    destination scatter / gather list

``nbytes``
    number of bytes to process from ``src``

``iv``
    IV for the cipher operation which must comply with the IV size defined by crypto_ablkcipher_ivsize


Description
===========

This function allows setting of the source data and destination data scatter / gather lists.

For encryption, the source is treated as the plaintext and the destination is the ciphertext. For a decryption operation, the use is reversed - the source is the ciphertext and the
destination is the plaintext.
