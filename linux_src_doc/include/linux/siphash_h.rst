.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/siphash.h

.. _`siphash`:

siphash
=======

.. c:function:: u64 siphash(const void *data, size_t len, const siphash_key_t *key)

    compute 64-bit siphash PRF value

    :param data:
        buffer to hash
    :type data: const void \*

    :param len:
        *undescribed*
    :type len: size_t

    :param key:
        the siphash key
    :type key: const siphash_key_t \*

.. _`hsiphash`:

hsiphash
========

.. c:function:: u32 hsiphash(const void *data, size_t len, const hsiphash_key_t *key)

    compute 32-bit hsiphash PRF value

    :param data:
        buffer to hash
    :type data: const void \*

    :param len:
        *undescribed*
    :type len: size_t

    :param key:
        the hsiphash key
    :type key: const hsiphash_key_t \*

.. This file was automatic generated / don't edit.

