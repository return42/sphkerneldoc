.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/internal/aead.h

.. _`crypto_aead_chunksize`:

crypto_aead_chunksize
=====================

.. c:function:: unsigned int crypto_aead_chunksize(struct crypto_aead *tfm)

    obtain chunk size

    :param tfm:
        cipher handle
    :type tfm: struct crypto_aead \*

.. _`crypto_aead_chunksize.description`:

Description
-----------

The block size is set to one for ciphers such as CCM.  However,
you still need to provide incremental updates in multiples of
the underlying block size as the IV does not have sub-block
granularity.  This is known in this API as the chunk size.

.. _`crypto_aead_chunksize.return`:

Return
------

chunk size in bytes

.. This file was automatic generated / don't edit.

