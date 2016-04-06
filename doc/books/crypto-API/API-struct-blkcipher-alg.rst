
.. _API-struct-blkcipher-alg:

====================
struct blkcipher_alg
====================

*man struct blkcipher_alg(9)*

*4.6.0-rc1*

synchronous block cipher definition


Synopsis
========

.. code-block:: c

    struct blkcipher_alg {
      int (* setkey) (struct crypto_tfm *tfm, const u8 *key,unsigned int keylen);
      int (* encrypt) (struct blkcipher_desc *desc,struct scatterlist *dst, struct scatterlist *src,unsigned int nbytes);
      int (* decrypt) (struct blkcipher_desc *desc,struct scatterlist *dst, struct scatterlist *src,unsigned int nbytes);
      const char * geniv;
      unsigned int min_keysize;
      unsigned int max_keysize;
      unsigned int ivsize;
    };


Members
=======

setkey
    see struct ablkcipher_alg

encrypt
    see struct ablkcipher_alg

decrypt
    see struct ablkcipher_alg

geniv
    see struct ablkcipher_alg

min_keysize
    see struct ablkcipher_alg

max_keysize
    see struct ablkcipher_alg

ivsize
    see struct ablkcipher_alg


Description
===========

All fields except ``geniv`` and ``ivsize`` are mandatory and must be filled.
