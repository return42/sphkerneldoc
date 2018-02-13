.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/caam/key_gen.h

.. _`split_key_len`:

split_key_len
=============

.. c:function:: u32 split_key_len(u32 hash)

    Compute MDHA split key length for a given algorithm

    :param u32 hash:
        Hashing algorithm selection, one of OP_ALG_ALGSEL\_\* - MD5, SHA1,
        SHA224, SHA384, SHA512.

.. _`split_key_len.return`:

Return
------

MDHA split key length

.. _`split_key_pad_len`:

split_key_pad_len
=================

.. c:function:: u32 split_key_pad_len(u32 hash)

    Compute MDHA split key pad length for a given algorithm

    :param u32 hash:
        Hashing algorithm selection, one of OP_ALG_ALGSEL\_\* - MD5, SHA1,
        SHA224, SHA384, SHA512.

.. _`split_key_pad_len.return`:

Return
------

MDHA split key pad length

.. This file was automatic generated / don't edit.

