.. -*- coding: utf-8; mode: rst -*-
.. src-file: certs/blacklist.c

.. _`mark_hash_blacklisted`:

mark_hash_blacklisted
=====================

.. c:function:: int mark_hash_blacklisted(const char *hash)

    Add a hash to the system blacklist

    :param const char \*hash:
        23aa429783")

.. _`is_hash_blacklisted`:

is_hash_blacklisted
===================

.. c:function:: int is_hash_blacklisted(const u8 *hash, size_t hash_len, const char *type)

    Determine if a hash is blacklisted

    :param const u8 \*hash:
        The hash to be checked as a binary blob

    :param size_t hash_len:
        The length of the binary hash

    :param const char \*type:
        Type of hash

.. This file was automatic generated / don't edit.

