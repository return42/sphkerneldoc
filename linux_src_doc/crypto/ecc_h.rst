.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/ecc.h

.. _`ecc_is_key_valid`:

ecc_is_key_valid
================

.. c:function:: int ecc_is_key_valid(unsigned int curve_id, unsigned int ndigits, const u8 *private_key, unsigned int private_key_len)

    Validate a given ECDH private key

    :param unsigned int curve_id:
        id representing the curve to use

    :param unsigned int ndigits:
        curve number of digits

    :param const u8 \*private_key:
        private key to be used for the given curve

    :param unsigned int private_key_len:
        private key len

.. _`ecc_is_key_valid.description`:

Description
-----------

Returns 0 if the key is acceptable, a negative value otherwise

.. _`ecdh_make_pub_key`:

ecdh_make_pub_key
=================

.. c:function:: int ecdh_make_pub_key(const unsigned int curve_id, unsigned int ndigits, const u8 *private_key, unsigned int private_key_len, u8 *public_key, unsigned int public_key_len)

    Compute an ECC public key

    :param const unsigned int curve_id:
        id representing the curve to use

    :param unsigned int ndigits:
        *undescribed*

    :param const u8 \*private_key:
        pregenerated private key for the given curve

    :param unsigned int private_key_len:
        length of private_key

    :param u8 \*public_key:
        buffer for storing the public key generated

    :param unsigned int public_key_len:
        length of the public_key buffer

.. _`ecdh_make_pub_key.description`:

Description
-----------

Returns 0 if the public key was generated successfully, a negative value
if an error occurred.

.. _`crypto_ecdh_shared_secret`:

crypto_ecdh_shared_secret
=========================

.. c:function:: int crypto_ecdh_shared_secret(unsigned int curve_id, unsigned int ndigits, const u8 *private_key, unsigned int private_key_len, const u8 *public_key, unsigned int public_key_len, u8 *secret, unsigned int secret_len)

    Compute a shared secret

    :param unsigned int curve_id:
        id representing the curve to use

    :param unsigned int ndigits:
        *undescribed*

    :param const u8 \*private_key:
        private key of part A

    :param unsigned int private_key_len:
        length of private_key

    :param const u8 \*public_key:
        public key of counterpart B

    :param unsigned int public_key_len:
        length of public_key

    :param u8 \*secret:
        buffer for storing the calculated shared secret

    :param unsigned int secret_len:
        length of the secret buffer

.. _`crypto_ecdh_shared_secret.note`:

Note
----

It is recommended that you hash the result of crypto_ecdh_shared_secret
before using it for symmetric encryption or HMAC.

Returns 0 if the shared secret was generated successfully, a negative value
if an error occurred.

.. This file was automatic generated / don't edit.

