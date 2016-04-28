.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-aead-request:

===================
struct aead_request
===================

*man struct aead_request(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
