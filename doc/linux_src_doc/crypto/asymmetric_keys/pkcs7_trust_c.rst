.. -*- coding: utf-8; mode: rst -*-

=============
pkcs7_trust.c
=============


.. _`pkcs7_validate_trust_one`:

pkcs7_validate_trust_one
========================

.. c:function:: int pkcs7_validate_trust_one (struct pkcs7_message *pkcs7, struct pkcs7_signed_info *sinfo, struct key *trust_keyring)

    :param struct pkcs7_message \*pkcs7:

        *undescribed*

    :param struct pkcs7_signed_info \*sinfo:

        *undescribed*

    :param struct key \*trust_keyring:

        *undescribed*



.. _`pkcs7_validate_trust`:

pkcs7_validate_trust
====================

.. c:function:: int pkcs7_validate_trust (struct pkcs7_message *pkcs7, struct key *trust_keyring, bool *_trusted)

    Validate PKCS#7 trust chain

    :param struct pkcs7_message \*pkcs7:
        The PKCS#7 certificate to validate

    :param struct key \*trust_keyring:
        Signing certificates to use as starting points

    :param bool \*_trusted:
        Set to true if trustworth, false otherwise



.. _`pkcs7_validate_trust.description`:

Description
-----------

Validate that the certificate chain inside the PKCS#7 message intersects
keys we already know and trust.

Returns, in order of descending priority::

 (*) -EKEYREJECTED if a signature failed to match for which we have a valid
        key, or:

 (*) 0 if at least one signature chain intersects with the keys in the trust
        keyring, or:

 (*) -ENOPKG if a suitable crypto module couldn't be found for a check on a
        chain.

 (*) -ENOKEY if we couldn't find a match for any of the signature chains in
        the message.

May also return -ENOMEM.

