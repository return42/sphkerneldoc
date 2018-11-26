.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/asymmetric_keys/signature.c

.. _`query_asymmetric_key`:

query_asymmetric_key
====================

.. c:function:: int query_asymmetric_key(const struct kernel_pkey_params *params, struct kernel_pkey_query *info)

    Get information about an aymmetric key.

    :param params:
        Various parameters.
    :type params: const struct kernel_pkey_params \*

    :param info:
        Where to put the information.
    :type info: struct kernel_pkey_query \*

.. _`encrypt_blob`:

encrypt_blob
============

.. c:function:: int encrypt_blob(struct kernel_pkey_params *params, const void *data, void *enc)

    Encrypt data using an asymmetric key

    :param params:
        Various parameters
    :type params: struct kernel_pkey_params \*

    :param data:
        Data blob to be encrypted, length params->data_len
    :type data: const void \*

    :param enc:
        Encrypted data buffer, length params->enc_len
    :type enc: void \*

.. _`encrypt_blob.description`:

Description
-----------

Encrypt the specified data blob using the private key specified by
params->key.  The encrypted data is wrapped in an encoding if
params->encoding is specified (eg. "pkcs1").

Returns the length of the data placed in the encrypted data buffer or an
error.

.. _`decrypt_blob`:

decrypt_blob
============

.. c:function:: int decrypt_blob(struct kernel_pkey_params *params, const void *enc, void *data)

    Decrypt data using an asymmetric key

    :param params:
        Various parameters
    :type params: struct kernel_pkey_params \*

    :param enc:
        Encrypted data to be decrypted, length params->enc_len
    :type enc: const void \*

    :param data:
        Decrypted data buffer, length params->data_len
    :type data: void \*

.. _`decrypt_blob.description`:

Description
-----------

Decrypt the specified data blob using the private key specified by
params->key.  The decrypted data is wrapped in an encoding if
params->encoding is specified (eg. "pkcs1").

Returns the length of the data placed in the decrypted data buffer or an
error.

.. _`create_signature`:

create_signature
================

.. c:function:: int create_signature(struct kernel_pkey_params *params, const void *data, void *enc)

    Sign some data using an asymmetric key

    :param params:
        Various parameters
    :type params: struct kernel_pkey_params \*

    :param data:
        Data blob to be signed, length params->data_len
    :type data: const void \*

    :param enc:
        Signature buffer, length params->enc_len
    :type enc: void \*

.. _`create_signature.description`:

Description
-----------

Sign the specified data blob using the private key specified by params->key.
The signature is wrapped in an encoding if params->encoding is specified
(eg. "pkcs1").  If the encoding needs to know the digest type, this can be
passed through params->hash_algo (eg. "sha1").

Returns the length of the data placed in the signature buffer or an error.

.. _`verify_signature`:

verify_signature
================

.. c:function:: int verify_signature(const struct key *key, const struct public_key_signature *sig)

    Initiate the use of an asymmetric key to verify a signature

    :param key:
        The asymmetric key to verify against
    :type key: const struct key \*

    :param sig:
        The signature to check
    :type sig: const struct public_key_signature \*

.. _`verify_signature.description`:

Description
-----------

Returns 0 if successful or else an error.

.. This file was automatic generated / don't edit.

