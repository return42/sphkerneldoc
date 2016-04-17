.. -*- coding: utf-8; mode: rst -*-

==============
pkcs7_verify.c
==============


.. _`pkcs7_verify`:

pkcs7_verify
============

.. c:function:: int pkcs7_verify (struct pkcs7_message *pkcs7, enum key_being_used_for usage)

    Verify a PKCS#7 message

    :param struct pkcs7_message \*pkcs7:
        The PKCS#7 message to be verified

    :param enum key_being_used_for usage:
        The use to which the key is being put



.. _`pkcs7_verify.description`:

Description
-----------

Verify a PKCS#7 message is internally consistent - that is, the data digest
matches the digest in the AuthAttrs and any signature in the message or one
of the X.509 certificates it carries that matches another X.509 cert in the
message can be verified.

This does not look to match the contents of the PKCS#7 message against any
external public keys.

Returns, in order of descending priority::

 (*) -EKEYREJECTED if a key was selected that had a usage restriction at
     odds with the specified usage, or:

 (*) -EKEYREJECTED if a signature failed to match for which we found an
        appropriate X.509 certificate, or:

 (*) -EBADMSG if some part of the message was invalid, or:

 (*) -ENOPKG if none of the signature chains are verifiable because suitable
        crypto modules couldn't be found, or:

 (*) 0 if all the signature chains that don't incur -ENOPKG can be verified
        (note that a signature chain may be of zero length), or:



.. _`pkcs7_supply_detached_data`:

pkcs7_supply_detached_data
==========================

.. c:function:: int pkcs7_supply_detached_data (struct pkcs7_message *pkcs7, const void *data, size_t datalen)

    Supply the data needed to verify a PKCS#7 message

    :param struct pkcs7_message \*pkcs7:
        The PKCS#7 message

    :param const void \*data:
        The data to be verified

    :param size_t datalen:
        The amount of data



.. _`pkcs7_supply_detached_data.description`:

Description
-----------

Supply the detached data needed to verify a PKCS#7 message.  Note that no
attempt to retain/pin the data is made.  That is left to the caller.  The
data will not be modified by :c:func:`pkcs7_verify` and will not be freed when the
PKCS#7 message is freed.

Returns -EINVAL if data is already supplied in the message, 0 otherwise.

