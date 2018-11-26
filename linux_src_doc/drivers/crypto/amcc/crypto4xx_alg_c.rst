.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/amcc/crypto4xx_alg.c

.. _`set_dynamic_sa_command_0`:

set_dynamic_sa_command_0
========================

.. c:function:: void set_dynamic_sa_command_0(struct dynamic_sa_ctl *sa, u32 save_h, u32 save_iv, u32 ld_h, u32 ld_iv, u32 hdr_proc, u32 h, u32 c, u32 pad_type, u32 op_grp, u32 op, u32 dir)

    :param sa:
        *undescribed*
    :type sa: struct dynamic_sa_ctl \*

    :param save_h:
        *undescribed*
    :type save_h: u32

    :param save_iv:
        *undescribed*
    :type save_iv: u32

    :param ld_h:
        *undescribed*
    :type ld_h: u32

    :param ld_iv:
        *undescribed*
    :type ld_iv: u32

    :param hdr_proc:
        *undescribed*
    :type hdr_proc: u32

    :param h:
        *undescribed*
    :type h: u32

    :param c:
        *undescribed*
    :type c: u32

    :param pad_type:
        *undescribed*
    :type pad_type: u32

    :param op_grp:
        *undescribed*
    :type op_grp: u32

    :param op:
        *undescribed*
    :type op: u32

    :param dir:
        *undescribed*
    :type dir: u32

.. _`set_dynamic_sa_command_0.description`:

Description
-----------

Copyright (c) 2008 Applied Micro Circuits Corporation.
All rights reserved. James Hsiao <jhsiao@amcc.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

This file implements the Linux crypto algorithms.

.. _`crypto4xx_setkey_aes`:

crypto4xx_setkey_aes
====================

.. c:function:: int crypto4xx_setkey_aes(struct crypto_skcipher *cipher, const u8 *key, unsigned int keylen, unsigned char cm, u8 fb)

    :param cipher:
        *undescribed*
    :type cipher: struct crypto_skcipher \*

    :param key:
        *undescribed*
    :type key: const u8 \*

    :param keylen:
        *undescribed*
    :type keylen: unsigned int

    :param cm:
        *undescribed*
    :type cm: unsigned char

    :param fb:
        *undescribed*
    :type fb: u8

.. _`crypto4xx_setkey_aes_ccm`:

crypto4xx_setkey_aes_ccm
========================

.. c:function:: int crypto4xx_setkey_aes_ccm(struct crypto_aead *cipher, const u8 *key, unsigned int keylen)

    CCM Functions

    :param cipher:
        *undescribed*
    :type cipher: struct crypto_aead \*

    :param key:
        *undescribed*
    :type key: const u8 \*

    :param keylen:
        *undescribed*
    :type keylen: unsigned int

.. _`crypto4xx_aes_gcm_validate_keylen`:

crypto4xx_aes_gcm_validate_keylen
=================================

.. c:function:: int crypto4xx_aes_gcm_validate_keylen(unsigned int keylen)

    GCM Functions

    :param keylen:
        *undescribed*
    :type keylen: unsigned int

.. _`crypto4xx_hash_alg_init`:

crypto4xx_hash_alg_init
=======================

.. c:function:: int crypto4xx_hash_alg_init(struct crypto_tfm *tfm, unsigned int sa_len, unsigned char ha, unsigned char hm)

    :param tfm:
        *undescribed*
    :type tfm: struct crypto_tfm \*

    :param sa_len:
        *undescribed*
    :type sa_len: unsigned int

    :param ha:
        *undescribed*
    :type ha: unsigned char

    :param hm:
        *undescribed*
    :type hm: unsigned char

.. _`crypto4xx_sha1_alg_init`:

crypto4xx_sha1_alg_init
=======================

.. c:function:: int crypto4xx_sha1_alg_init(struct crypto_tfm *tfm)

    :param tfm:
        *undescribed*
    :type tfm: struct crypto_tfm \*

.. This file was automatic generated / don't edit.

