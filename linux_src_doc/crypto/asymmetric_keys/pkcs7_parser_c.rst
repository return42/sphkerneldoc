.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/asymmetric_keys/pkcs7_parser.c

.. _`pkcs7_free_message`:

pkcs7_free_message
==================

.. c:function:: void pkcs7_free_message(struct pkcs7_message *pkcs7)

    Free a PKCS#7 message

    :param pkcs7:
        The PKCS#7 message to free
    :type pkcs7: struct pkcs7_message \*

.. _`pkcs7_parse_message`:

pkcs7_parse_message
===================

.. c:function:: struct pkcs7_message *pkcs7_parse_message(const void *data, size_t datalen)

    Parse a PKCS#7 message

    :param data:
        The raw binary ASN.1 encoded message to be parsed
    :type data: const void \*

    :param datalen:
        The size of the encoded message
    :type datalen: size_t

.. _`pkcs7_get_content_data`:

pkcs7_get_content_data
======================

.. c:function:: int pkcs7_get_content_data(const struct pkcs7_message *pkcs7, const void **_data, size_t *_data_len, size_t *_headerlen)

    Get access to the PKCS#7 content

    :param pkcs7:
        The preparsed PKCS#7 message to access
    :type pkcs7: const struct pkcs7_message \*

    :param _data:
        Place to return a pointer to the data
    :type _data: const void \*\*

    :param _data_len:
        Place to return the data length
    :type _data_len: size_t \*

    :param _headerlen:
        Size of ASN.1 header not included in \_data
    :type _headerlen: size_t \*

.. _`pkcs7_get_content_data.description`:

Description
-----------

Get access to the data content of the PKCS#7 message.  The size of the
header of the ASN.1 object that contains it is also provided and can be used
to adjust \*\_data and \*\_data_len to get the entire object.

Returns -ENODATA if the data object was missing from the message.

.. This file was automatic generated / don't edit.

