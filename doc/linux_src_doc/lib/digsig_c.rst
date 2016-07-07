.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/digsig.c

.. _`digsig_verify`:

digsig_verify
=============

.. c:function:: int digsig_verify(struct key *keyring, const char *sig, int siglen, const char *data, int datalen)

    digital signature verification with public key

    :param struct key \*keyring:
        keyring to search key in

    :param const char \*sig:
        digital signature

    :param int siglen:
        length of the signature

    :param const char \*data:
        data

    :param int datalen:
        length of the data

.. _`digsig_verify.description`:

Description
-----------

Returns 0 on success, -EINVAL otherwise

Verifies data integrity against digital signature.
Currently only RSA is supported.
Normally hash of the content is used as a data for this function.

.. This file was automatic generated / don't edit.

