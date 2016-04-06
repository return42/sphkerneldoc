
.. _API-struct-akcipher-alg:

===================
struct akcipher_alg
===================

*man struct akcipher_alg(9)*

*4.6.0-rc1*

generic public key algorithm


Synopsis
========

.. code-block:: c

    struct akcipher_alg {
      int (* sign) (struct akcipher_request *req);
      int (* verify) (struct akcipher_request *req);
      int (* encrypt) (struct akcipher_request *req);
      int (* decrypt) (struct akcipher_request *req);
      int (* set_pub_key) (struct crypto_akcipher *tfm, const void *key,unsigned int keylen);
      int (* set_priv_key) (struct crypto_akcipher *tfm, const void *key,unsigned int keylen);
      int (* max_size) (struct crypto_akcipher *tfm);
      int (* init) (struct crypto_akcipher *tfm);
      void (* exit) (struct crypto_akcipher *tfm);
      unsigned int reqsize;
      struct crypto_alg base;
    };


Members
=======

sign
    Function performs a sign operation as defined by public key algorithm. In case of error, where the dst_len was insufficient, the req->dst_len will be updated to the size
    required for the operation

verify
    Function performs a sign operation as defined by public key algorithm. In case of error, where the dst_len was insufficient, the req->dst_len will be updated to the size
    required for the operation

encrypt
    Function performs an encrypt operation as defined by public key algorithm. In case of error, where the dst_len was insufficient, the req->dst_len will be updated to the size
    required for the operation

decrypt
    Function performs a decrypt operation as defined by public key algorithm. In case of error, where the dst_len was insufficient, the req->dst_len will be updated to the size
    required for the operation

set_pub_key
    Function invokes the algorithm specific set public key function, which knows how to decode and interpret the BER encoded public key

set_priv_key
    Function invokes the algorithm specific set private key function, which knows how to decode and interpret the BER encoded private key

max_size
    Function returns dest buffer size required for a given key.

init
    Initialize the cryptographic transformation object. This function is used to initialize the cryptographic transformation object. This function is called only once at the
    instantiation time, right after the transformation context was allocated. In case the cryptographic hardware has some special requirements which need to be handled by software,
    this function shall check for the precise requirement of the transformation and put any software fallbacks in place.

exit
    Deinitialize the cryptographic transformation object. This is a counterpart to ``init``, used to remove various changes set in ``init``.

reqsize
    Request context size required by algorithm implementation

base
    Common crypto API algorithm data structure
