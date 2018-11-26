.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/digsig.c

.. _`digsig_verify`:

digsig_verify
=============

.. c:function:: int digsig_verify(struct key *keyring, const char *sig, int siglen, const char *data, int datalen)

    digital signature verification with public key

    :param keyring:
        keyring to search key in
    :type keyring: struct key \*

    :param sig:
        digital signature
    :type sig: const char \*

    :param siglen:
        length of the signature
    :type siglen: int

    :param data:
        data
    :type data: const char \*

    :param datalen:
        length of the data
    :type datalen: int

.. _`digsig_verify.description`:

Description
-----------

Returns 0 on success, -EINVAL otherwise

Verifies data integrity against digital signature.
Currently only RSA is supported.
Normally hash of the content is used as a data for this function.

.. This file was automatic generated / don't edit.

