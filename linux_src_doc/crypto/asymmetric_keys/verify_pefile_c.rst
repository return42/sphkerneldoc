.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/asymmetric_keys/verify_pefile.c

.. _`verify_pefile_signature`:

verify_pefile_signature
=======================

.. c:function:: int verify_pefile_signature(const void *pebuf, unsigned pelen, struct key *trusted_keys, enum key_being_used_for usage)

    Verify the signature on a PE binary image

    :param const void \*pebuf:
        Buffer containing the PE binary image

    :param unsigned pelen:
        Length of the binary image

    :param struct key \*trusted_keys:
        *undescribed*

    :param enum key_being_used_for usage:
        The use to which the key is being put.

.. _`verify_pefile_signature.description`:

Description
-----------

Validate that the certificate chain inside the PKCS#7 message inside the PE
binary image intersects keys we already know and trust.

Returns, in order of descending priority:

(\*) -ELIBBAD if the image cannot be parsed, or:

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

