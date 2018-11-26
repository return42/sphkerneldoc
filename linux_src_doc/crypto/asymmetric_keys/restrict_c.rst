.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/asymmetric_keys/restrict.c

.. _`restrict_link_by_signature`:

restrict_link_by_signature
==========================

.. c:function:: int restrict_link_by_signature(struct key *dest_keyring, const struct key_type *type, const union key_payload *payload, struct key *trust_keyring)

    Restrict additions to a ring of public keys

    :param dest_keyring:
        Keyring being linked to.
    :type dest_keyring: struct key \*

    :param type:
        The type of key being added.
    :type type: const struct key_type \*

    :param payload:
        The payload of the new key.
    :type payload: const union key_payload \*

    :param trust_keyring:
        A ring of keys that can be used to vouch for the new cert.
    :type trust_keyring: struct key \*

.. _`restrict_link_by_signature.description`:

Description
-----------

Check the new certificate against the ones in the trust keyring.  If one of
those is the signing key and validates the new certificate, then mark the
new certificate as being trusted.

Returns 0 if the new certificate was accepted, -ENOKEY if we couldn't find a
matching parent certificate in the trusted list, -EKEYREJECTED if the
signature check fails or the key is blacklisted, -ENOPKG if the signature
uses unsupported crypto, or some other error if there is a matching
certificate but the signature check cannot be performed.

.. _`restrict_link_by_key_or_keyring`:

restrict_link_by_key_or_keyring
===============================

.. c:function:: int restrict_link_by_key_or_keyring(struct key *dest_keyring, const struct key_type *type, const union key_payload *payload, struct key *trusted)

    Restrict additions to a ring of public keys using the restrict_key information stored in the ring.

    :param dest_keyring:
        Keyring being linked to.
    :type dest_keyring: struct key \*

    :param type:
        The type of key being added.
    :type type: const struct key_type \*

    :param payload:
        The payload of the new key.
    :type payload: const union key_payload \*

    :param trusted:
        A key or ring of keys that can be used to vouch for the new cert.
    :type trusted: struct key \*

.. _`restrict_link_by_key_or_keyring.description`:

Description
-----------

Check the new certificate only against the key or keys passed in the data
parameter. If one of those is the signing key and validates the new
certificate, then mark the new certificate as being ok to link.

Returns 0 if the new certificate was accepted, -ENOKEY if we
couldn't find a matching parent certificate in the trusted list,
-EKEYREJECTED if the signature check fails, -ENOPKG if the signature uses
unsupported crypto, or some other error if there is a matching certificate
but the signature check cannot be performed.

.. _`restrict_link_by_key_or_keyring_chain`:

restrict_link_by_key_or_keyring_chain
=====================================

.. c:function:: int restrict_link_by_key_or_keyring_chain(struct key *dest_keyring, const struct key_type *type, const union key_payload *payload, struct key *trusted)

    Restrict additions to a ring of public keys using the restrict_key information stored in the ring.

    :param dest_keyring:
        Keyring being linked to.
    :type dest_keyring: struct key \*

    :param type:
        The type of key being added.
    :type type: const struct key_type \*

    :param payload:
        The payload of the new key.
    :type payload: const union key_payload \*

    :param trusted:
        A key or ring of keys that can be used to vouch for the new cert.
    :type trusted: struct key \*

.. _`restrict_link_by_key_or_keyring_chain.description`:

Description
-----------

Check the new certificate only against the key or keys passed in the data
parameter. If one of those is the signing key and validates the new
certificate, then mark the new certificate as being ok to link.

Returns 0 if the new certificate was accepted, -ENOKEY if we
couldn't find a matching parent certificate in the trusted list,
-EKEYREJECTED if the signature check fails, -ENOPKG if the signature uses
unsupported crypto, or some other error if there is a matching certificate
but the signature check cannot be performed.

.. This file was automatic generated / don't edit.

