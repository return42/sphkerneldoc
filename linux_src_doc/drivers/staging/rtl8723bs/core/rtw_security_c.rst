.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8723bs/core/rtw_security.c

.. _`rijndaelkeysetupenc`:

rijndaelKeySetupEnc
===================

.. c:function:: void rijndaelKeySetupEnc(u32 rk, const u8 cipherKey)

    :param rk:
        *undescribed*
    :type rk: u32

    :param cipherKey:
        *undescribed*
    :type cipherKey: const u8

.. _`rijndaelkeysetupenc.description`:

Description
-----------

\ ``return``\       the number of rounds for the given cipher key size.

.. _`omac1_aes_128_vector`:

omac1_aes_128_vector
====================

.. c:function:: int omac1_aes_128_vector(u8 *key, size_t num_elem, u8  *addr, size_t *len, u8 *mac)

    One-Key CBC MAC (OMAC1) hash with AES-128

    :param key:
        128-bit key for the hash operation
    :type key: u8 \*

    :param num_elem:
        Number of elements in the data vector
    :type num_elem: size_t

    :param addr:
        Pointers to the data areas
    :type addr: u8  \*

    :param len:
        Lengths of the data blocks
    :type len: size_t \*

    :param mac:
        Buffer for MAC (128 bits, i.e., 16 bytes)
    :type mac: u8 \*

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

    :param key:
        128-bit key for the hash operation
    :type key: u8 \*

    :param data:
        Data buffer for which a MAC is determined
    :type data: u8 \*

    :param data_len:
        Length of data buffer in bytes
    :type data_len: size_t

    :param mac:
        Buffer for MAC (128 bits, i.e., 16 bytes)
    :type mac: u8 \*

.. _`omac1_aes_128.return`:

Return
------

0 on success, -1 on failure

This is a mode for using block cipher (AES in this case) for authentication.
OMAC1 was standardized with the name CMAC by NIST in a Special Publication
(SP) 800-38B.

.. This file was automatic generated / don't edit.

