
.. _API-struct-aead-request:

===================
struct aead_request
===================

*man struct aead_request(9)*

*4.6.0-rc1*

AEAD request


Synopsis
========

.. code-block:: c

    struct aead_request {
      struct crypto_async_request base;
      unsigned int assoclen;
      unsigned int cryptlen;
      u8 * iv;
      struct scatterlist * src;
      struct scatterlist * dst;
      void * __ctx[];
    };


Members
=======

base
    Common attributes for async crypto requests

assoclen
    Length in bytes of associated data for authentication

cryptlen
    Length of data to be encrypted or decrypted

iv
    Initialisation vector

src
    Source data

dst
    Destination data

__ctx[]
    Start of private context data
