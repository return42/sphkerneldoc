.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/sha1.c

.. _`sha_transform`:

sha_transform
=============

.. c:function:: void sha_transform(__u32 *digest, const char *data, __u32 *array)

    single block SHA1 transform

    :param digest:
        160 bit digest to update
    :type digest: __u32 \*

    :param data:
        512 bits of data to hash
    :type data: const char \*

    :param array:
        16 words of workspace (see note)
    :type array: __u32 \*

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

.. c:function:: void sha_init(__u32 *buf)

    initialize the vectors for a SHA1 digest

    :param buf:
        vector to initialize
    :type buf: __u32 \*

.. This file was automatic generated / don't edit.

