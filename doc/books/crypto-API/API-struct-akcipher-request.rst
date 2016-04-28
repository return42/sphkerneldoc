.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-akcipher-request:

=======================
struct akcipher_request
=======================

*man struct akcipher_request(9)*

*4.6.0-rc5*

public key request


Synopsis
========

.. code-block:: c

    struct akcipher_request {
      struct crypto_async_request base;
      struct scatterlist * src;
      struct scatterlist * dst;
      unsigned int src_len;
      unsigned int dst_len;
      void * __ctx[];
    };


Members
=======

base
    Common attributes for async crypto requests

src
    Source data

dst
    Destination data

src_len
    Size of the input buffer

dst_len
    Size of the output buffer. It needs to be at least as big as the
    expected result depending on the operation After operation it will
    be updated with the actual size of the result. In case of error
    where the dst sgl size was insufficient, it will be updated to the
    size required for the operation.

__ctx[]
    Start of private context data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
