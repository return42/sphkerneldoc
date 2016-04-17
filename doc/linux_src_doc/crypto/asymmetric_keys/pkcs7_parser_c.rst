.. -*- coding: utf-8; mode: rst -*-

==============
pkcs7_parser.c
==============


.. _`pkcs7_free_message`:

pkcs7_free_message
==================

.. c:function:: void pkcs7_free_message (struct pkcs7_message *pkcs7)

    Free a PKCS#7 message

    :param struct pkcs7_message \*pkcs7:
        The PKCS#7 message to free



.. _`pkcs7_parse_message`:

pkcs7_parse_message
===================

.. c:function:: struct pkcs7_message *pkcs7_parse_message (const void *data, size_t datalen)

    Parse a PKCS#7 message

    :param const void \*data:
        The raw binary ASN.1 encoded message to be parsed

    :param size_t datalen:
        The size of the encoded message



.. _`pkcs7_get_content_data`:

pkcs7_get_content_data
======================

.. c:function:: int pkcs7_get_content_data (const struct pkcs7_message *pkcs7, const void **_data, size_t *_data_len, bool want_wrapper)

    Get access to the PKCS#7 content

    :param const struct pkcs7_message \*pkcs7:
        The preparsed PKCS#7 message to access

    :param const void \*\*_data:
        Place to return a pointer to the data

    :param size_t \*_data_len:
        Place to return the data length

    :param bool want_wrapper:
        True if the ASN.1 object header should be included in the data



.. _`pkcs7_get_content_data.description`:

Description
-----------

Get access to the data content of the PKCS#7 message, including, optionally,
the header of the ASN.1 object that contains it.  Returns -ENODATA if the
data object was missing from the message.

