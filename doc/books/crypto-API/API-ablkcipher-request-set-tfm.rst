
.. _API-ablkcipher-request-set-tfm:

==========================
ablkcipher_request_set_tfm
==========================

*man ablkcipher_request_set_tfm(9)*

*4.6.0-rc1*

update cipher handle reference in request


Synopsis
========

.. c:function:: void ablkcipher_request_set_tfm( struct ablkcipher_request * req, struct crypto_ablkcipher * tfm )

Arguments
=========

``req``
    request handle to be modified

``tfm``
    cipher handle that shall be added to the request handle


Description
===========

Allow the caller to replace the existing ablkcipher handle in the request data structure with a different one.
