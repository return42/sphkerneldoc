.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ahash-alg:

================
struct ahash_alg
================

*man struct ahash_alg(9)*

*4.6.0-rc5*

asynchronous message digest definition


Synopsis
========

.. code-block:: c

    struct ahash_alg {
      int (* init) (struct ahash_request *req);
      int (* update) (struct ahash_request *req);
      int (* final) (struct ahash_request *req);
      int (* finup) (struct ahash_request *req);
      int (* digest) (struct ahash_request *req);
      int (* export) (struct ahash_request *req, void *out);
      int (* import) (struct ahash_request *req, const void *in);
      int (* setkey) (struct crypto_ahash *tfm, const u8 *key,unsigned int keylen);
      struct hash_alg_common halg;
    };


Members
=======

init
    Initialize the transformation context. Intended only to initialize
    the state of the HASH transformation at the beginning. This shall
    fill in the internal structures used during the entire duration of
    the whole transformation. No data processing happens at this point.

update
    Push a chunk of data into the driver for transformation. This
    function actually pushes blocks of data from upper layers into the
    driver, which then passes those to the hardware as seen fit. This
    function must not finalize the HASH transformation by calculating
    the final message digest as this only adds more data into the
    transformation. This function shall not modify the transformation
    context, as this function may be called in parallel with the same
    transformation object. Data processing can happen synchronously
    [SHASH] or asynchronously [AHASH] at this point.

final
    Retrieve result from the driver. This function finalizes the
    transformation and retrieves the resulting hash from the driver and
    pushes it back to upper layers. No data processing happens at this
    point.

finup
    Combination of ``update`` and ``final``. This function is
    effectively a combination of ``update`` and ``final`` calls issued
    in sequence. As some hardware cannot do ``update`` and ``final``
    separately, this callback was added to allow such hardware to be
    used at least by IPsec. Data processing can happen synchronously
    [SHASH] or asynchronously [AHASH] at this point.

digest
    Combination of ``init`` and ``update`` and ``final``. This function
    effectively behaves as the entire chain of operations, ``init``,
    ``update`` and ``final`` issued in sequence. Just like ``finup``,
    this was added for hardware which cannot do even the ``finup``, but
    can only do the whole transformation in one run. Data processing can
    happen synchronously [SHASH] or asynchronously [AHASH] at this
    point.

export
    Export partial state of the transformation. This function dumps the
    entire state of the ongoing transformation into a provided block of
    data so it can be ``import`` 'ed back later on. This is useful in
    case you want to save partial result of the transformation after
    processing certain amount of data and reload this partial result
    multiple times later on for multiple re-use. No data processing
    happens at this point.

import
    Import partial state of the transformation. This function loads the
    entire state of the ongoing transformation from a provided block of
    data so the transformation can continue from this point onward. No
    data processing happens at this point.

setkey
    Set optional key used by the hashing algorithm. Intended to push
    optional key used by the hashing algorithm from upper layers into
    the driver. This function can store the key in the transformation
    context or can outright program it into the hardware. In the former
    case, one must be careful to program the key into the hardware at
    appropriate time and one must be careful that .\ ``setkey`` can be
    called multiple times during the existence of the transformation
    object. Not all hashing algorithms do implement this function as it
    is only needed for keyed message digests. SHAx/MDx/CRCx do NOT
    implement this function. HMAC(MDx)/HMAC(SHAx)/CMAC(AES) do implement
    this function. This function must be called before any other of the
    ``init``, ``update``, ``final``, ``finup``, ``digest`` is called. No
    data processing happens at this point.

halg
    see struct hash_alg_common


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
