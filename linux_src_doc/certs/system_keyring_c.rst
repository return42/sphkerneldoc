.. -*- coding: utf-8; mode: rst -*-
.. src-file: certs/system_keyring.c

.. _`restrict_link_by_builtin_trusted`:

restrict_link_by_builtin_trusted
================================

.. c:function:: int restrict_link_by_builtin_trusted(struct key *dest_keyring, const struct key_type *type, const union key_payload *payload, struct key *restriction_key)

    Restrict keyring addition by built in CA

    :param dest_keyring:
        *undescribed*
    :type dest_keyring: struct key \*

    :param type:
        *undescribed*
    :type type: const struct key_type \*

    :param payload:
        *undescribed*
    :type payload: const union key_payload \*

    :param restriction_key:
        *undescribed*
    :type restriction_key: struct key \*

.. _`restrict_link_by_builtin_trusted.description`:

Description
-----------

Restrict the addition of keys into a keyring based on the key-to-be-added
being vouched for by a key in the built in system keyring.

.. _`restrict_link_by_builtin_and_secondary_trusted`:

restrict_link_by_builtin_and_secondary_trusted
==============================================

.. c:function:: int restrict_link_by_builtin_and_secondary_trusted(struct key *dest_keyring, const struct key_type *type, const union key_payload *payload, struct key *restrict_key)

    Restrict keyring addition by both builtin and secondary keyrings

    :param dest_keyring:
        *undescribed*
    :type dest_keyring: struct key \*

    :param type:
        *undescribed*
    :type type: const struct key_type \*

    :param payload:
        *undescribed*
    :type payload: const union key_payload \*

    :param restrict_key:
        *undescribed*
    :type restrict_key: struct key \*

.. _`restrict_link_by_builtin_and_secondary_trusted.description`:

Description
-----------

Restrict the addition of keys into a keyring based on the key-to-be-added
being vouched for by a key in either the built-in or the secondary system
keyrings.

.. _`get_builtin_and_secondary_restriction`:

get_builtin_and_secondary_restriction
=====================================

.. c:function:: struct key_restriction *get_builtin_and_secondary_restriction( void)

    keyring. Only for use in \ :c:func:`system_trusted_keyring_init`\ .

    :param void:
        no arguments
    :type void: 

.. _`verify_pkcs7_signature`:

verify_pkcs7_signature
======================

.. c:function:: int verify_pkcs7_signature(const void *data, size_t len, const void *raw_pkcs7, size_t pkcs7_len, struct key *trusted_keys, enum key_being_used_for usage, int (*view_content)(void *ctx, const void *data, size_t len, size_t asn1hdrlen), void *ctx)

    Verify a PKCS#7-based signature on system data.

    :param data:
        The data to be verified (NULL if expecting internal data).
    :type data: const void \*

    :param len:
        Size of \ ``data``\ .
    :type len: size_t

    :param raw_pkcs7:
        The PKCS#7 message that is the signature.
    :type raw_pkcs7: const void \*

    :param pkcs7_len:
        The size of \ ``raw_pkcs7``\ .
    :type pkcs7_len: size_t

    :param trusted_keys:
        Trusted keys to use (NULL for builtin trusted keys only,
        (void \*)1UL for all trusted keys).
    :type trusted_keys: struct key \*

    :param usage:
        The use to which the key is being put.
    :type usage: enum key_being_used_for

    :param int (\*view_content)(void \*ctx, const void \*data, size_t len, size_t asn1hdrlen):
        Callback to gain access to content.

    :param ctx:
        Context for callback.
    :type ctx: void \*

.. This file was automatic generated / don't edit.

