.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/siphash.h

.. _`siphash`:

siphash
=======

.. c:function:: u64 siphash(const void *data, size_t len, const siphash_key_t *key)

    compute 64-bit siphash PRF value

    :param const void \*data:
        buffer to hash

    :param size_t len:
        *undescribed*

    :param const siphash_key_t \*key:
        the siphash key

.. _`hsiphash`:

hsiphash
========

.. c:function:: u32 hsiphash(const void *data, size_t len, const hsiphash_key_t *key)

    compute 32-bit hsiphash PRF value

    :param const void \*data:
        buffer to hash

    :param size_t len:
        *undescribed*

    :param const hsiphash_key_t \*key:
        the hsiphash key

.. This file was automatic generated / don't edit.

