.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/asymmetric_keys/pkcs7_trust.c

.. _`pkcs7_validate_trust_one`:

pkcs7_validate_trust_one
========================

.. c:function:: int pkcs7_validate_trust_one(struct pkcs7_message *pkcs7, struct pkcs7_signed_info *sinfo, struct key *trust_keyring)

    :param pkcs7:
        *undescribed*
    :type pkcs7: struct pkcs7_message \*

    :param sinfo:
        *undescribed*
    :type sinfo: struct pkcs7_signed_info \*

    :param trust_keyring:
        *undescribed*
    :type trust_keyring: struct key \*

.. _`pkcs7_validate_trust`:

pkcs7_validate_trust
====================

.. c:function:: int pkcs7_validate_trust(struct pkcs7_message *pkcs7, struct key *trust_keyring)

    Validate PKCS#7 trust chain

    :param pkcs7:
        The PKCS#7 certificate to validate
    :type pkcs7: struct pkcs7_message \*

    :param trust_keyring:
        Signing certificates to use as starting points
    :type trust_keyring: struct key \*

.. _`pkcs7_validate_trust.description`:

Description
-----------

Validate that the certificate chain inside the PKCS#7 message intersects
keys we already know and trust.

Returns, in order of descending priority:

(\*) -EKEYREJECTED if a signature failed to match for which we have a valid
key, or:

(\*) 0 if at least one signature chain intersects with the keys in the trust
keyring, or:

(\*) -ENOPKG if a suitable crypto module couldn't be found for a check on a
chain.

(\*) -ENOKEY if we couldn't find a match for any of the signature chains in
the message.

May also return -ENOMEM.

.. This file was automatic generated / don't edit.

