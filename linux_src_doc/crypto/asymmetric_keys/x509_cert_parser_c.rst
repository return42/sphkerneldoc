.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/asymmetric_keys/x509_cert_parser.c

.. _`x509_decode_time`:

x509_decode_time
================

.. c:function:: int x509_decode_time(time64_t *_t, size_t hdrlen, unsigned char tag, const unsigned char *value, size_t vlen)

    Decode an X.509 time ASN.1 object

    :param _t:
        The time to fill in
    :type _t: time64_t \*

    :param hdrlen:
        The length of the object header
    :type hdrlen: size_t

    :param tag:
        The object tag
    :type tag: unsigned char

    :param value:
        The object value
    :type value: const unsigned char \*

    :param vlen:
        The size of the object value
    :type vlen: size_t

.. _`x509_decode_time.description`:

Description
-----------

Decode an ASN.1 universal time or generalised time field into a struct the
kernel can handle and check it for validity.  The time is decoded thus:

[RFC5280 §4.1.2.5]
CAs conforming to this profile MUST always encode certificate validity
dates through the year 2049 as UTCTime; certificate validity dates in
2050 or later MUST be encoded as GeneralizedTime.  Conforming
applications MUST be able to process validity dates that are encoded in
either UTCTime or GeneralizedTime.

.. This file was automatic generated / don't edit.

