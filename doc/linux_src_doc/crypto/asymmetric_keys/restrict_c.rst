.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/asymmetric_keys/restrict.c

.. _`restrict_link_by_signature`:

restrict_link_by_signature
==========================

.. c:function:: int restrict_link_by_signature(struct key *trust_keyring, const struct key_type *type, const union key_payload *payload)

    Restrict additions to a ring of public keys

    :param struct key \*trust_keyring:
        A ring of keys that can be used to vouch for the new cert.

    :param const struct key_type \*type:
        The type of key being added.

    :param const union key_payload \*payload:
        The payload of the new key.

.. _`restrict_link_by_signature.description`:

Description
-----------

Check the new certificate against the ones in the trust keyring.  If one of
those is the signing key and validates the new certificate, then mark the
new certificate as being trusted.

Returns 0 if the new certificate was accepted, -ENOKEY if we couldn't find a
matching parent certificate in the trusted list, -EKEYREJECTED if the
signature check fails or the key is blacklisted and some other error if
there is a matching certificate but the signature check cannot be performed.

.. This file was automatic generated / don't edit.

