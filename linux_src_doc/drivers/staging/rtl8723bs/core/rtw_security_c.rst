.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8723bs/core/rtw_security.c

.. _`rijndaelkeysetupenc`:

rijndaelKeySetupEnc
===================

.. c:function:: void rijndaelKeySetupEnc(u32 rk, const u8 cipherKey)

    :param u32 rk:
        *undescribed*

    :param const u8 cipherKey:
        *undescribed*

.. _`rijndaelkeysetupenc.description`:

Description
-----------

\ ``return``\       the number of rounds for the given cipher key size.

.. _`omac1_aes_128_vector`:

omac1_aes_128_vector
====================

.. c:function:: int omac1_aes_128_vector(u8 *key, size_t num_elem, u8  *addr, size_t *len, u8 *mac)

    One-Key CBC MAC (OMAC1) hash with AES-128

    :param u8 \*key:
        128-bit key for the hash operation

    :param size_t num_elem:
        Number of elements in the data vector

    :param u8  \*addr:
        Pointers to the data areas

    :param size_t \*len:
        Lengths of the data blocks

    :param u8 \*mac:
        Buffer for MAC (128 bits, i.e., 16 bytes)

.. _`omac1_aes_128_vector.return`:

Return
------

0 on success, -1 on failure

This is a mode for using block cipher (AES in this case) for authentication.
OMAC1 was standardized with the name CMAC by NIST in a Special Publication
(SP) 800-38B.

.. _`omac1_aes_128`:

omac1_aes_128
=============

.. c:function:: int omac1_aes_128(u8 *key, u8 *data, size_t data_len, u8 *mac)

    One-Key CBC MAC (OMAC1) hash with AES-128 (aka AES-CMAC)

    :param u8 \*key:
        128-bit key for the hash operation

    :param u8 \*data:
        Data buffer for which a MAC is determined

    :param size_t data_len:
        Length of data buffer in bytes

    :param u8 \*mac:
        Buffer for MAC (128 bits, i.e., 16 bytes)

.. _`omac1_aes_128.return`:

Return
------

0 on success, -1 on failure

This is a mode for using block cipher (AES in this case) for authentication.
OMAC1 was standardized with the name CMAC by NIST in a Special Publication
(SP) 800-38B.

.. This file was automatic generated / don't edit.

