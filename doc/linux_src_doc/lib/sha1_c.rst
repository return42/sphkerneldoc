.. -*- coding: utf-8; mode: rst -*-

======
sha1.c
======


.. _`sha_transform`:

sha_transform
=============

.. c:function:: void sha_transform (__u32 *digest, const char *data, __u32 *array)

    single block SHA1 transform

    :param __u32 \*digest:
        160 bit digest to update

    :param const char \*data:
        512 bits of data to hash

    :param __u32 \*array:
        16 words of workspace (see note)



.. _`sha_transform.description`:

Description
-----------

This function generates a SHA1 digest for a single 512-bit block.
Be warned, it does not handle padding and message digest, do not
confuse it with the full FIPS 180-1 digest algorithm for variable
length messages.



.. _`sha_transform.note`:

Note
----

If the hash is security sensitive, the caller should be sure
to clear the workspace. This is left to the caller to avoid
unnecessary clears between chained hashing operations.



.. _`sha_init`:

sha_init
========

.. c:function:: void sha_init (__u32 *buf)

    initialize the vectors for a SHA1 digest

    :param __u32 \*buf:
        vector to initialize

