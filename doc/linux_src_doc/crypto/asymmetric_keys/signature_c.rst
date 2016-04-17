.. -*- coding: utf-8; mode: rst -*-

===========
signature.c
===========


.. _`verify_signature`:

verify_signature
================

.. c:function:: int verify_signature (const struct key *key, const struct public_key_signature *sig)

    Initiate the use of an asymmetric key to verify a signature

    :param const struct key \*key:
        The asymmetric key to verify against

    :param const struct public_key_signature \*sig:
        The signature to check



.. _`verify_signature.description`:

Description
-----------

Returns 0 if successful or else an error.

