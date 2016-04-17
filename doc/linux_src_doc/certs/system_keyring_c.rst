.. -*- coding: utf-8; mode: rst -*-

================
system_keyring.c
================


.. _`system_verify_data`:

system_verify_data
==================

.. c:function:: int system_verify_data (const void *data, unsigned long len, const void *raw_pkcs7, size_t pkcs7_len, enum key_being_used_for usage)

    based signature on system data.

    :param const void \*data:
        The data to be verified.

    :param unsigned long len:
        Size of ``data``\ .

    :param const void \*raw_pkcs7:
        The PKCS#7 message that is the signature.

    :param size_t pkcs7_len:
        The size of ``raw_pkcs7``\ .

    :param enum key_being_used_for usage:
        The use to which the key is being put.

