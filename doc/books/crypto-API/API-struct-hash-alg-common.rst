
.. _API-struct-hash-alg-common:

======================
struct hash_alg_common
======================

*man struct hash_alg_common(9)*

*4.6.0-rc1*

define properties of message digest


Synopsis
========

.. code-block:: c

    struct hash_alg_common {
      unsigned int digestsize;
      unsigned int statesize;
      struct crypto_alg base;
    };


Members
=======

digestsize
    Size of the result of the transformation. A buffer of this size must be available to the ``final`` and ``finup`` calls, so they can store the resulting hash into it. For
    various predefined sizes, search include/crypto/ using git grep _DIGEST_SIZE include/crypto.

statesize
    Size of the block for partial state of the transformation. A buffer of this size must be passed to the ``export`` function as it will save the partial state of the
    transformation into it. On the other side, the ``import`` function will load the state from a buffer of this size as well.

base
    Start of data structure of cipher algorithm. The common data structure of crypto_alg contains information common to all ciphers. The hash_alg_common data structure now adds
    the hash-specific information.
