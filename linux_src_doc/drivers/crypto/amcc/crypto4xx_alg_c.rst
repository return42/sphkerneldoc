.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/amcc/crypto4xx_alg.c

.. _`set_dynamic_sa_command_0`:

set_dynamic_sa_command_0
========================

.. c:function:: void set_dynamic_sa_command_0(struct dynamic_sa_ctl *sa, u32 save_h, u32 save_iv, u32 ld_h, u32 ld_iv, u32 hdr_proc, u32 h, u32 c, u32 pad_type, u32 op_grp, u32 op, u32 dir)

    :param struct dynamic_sa_ctl \*sa:
        *undescribed*

    :param u32 save_h:
        *undescribed*

    :param u32 save_iv:
        *undescribed*

    :param u32 ld_h:
        *undescribed*

    :param u32 ld_iv:
        *undescribed*

    :param u32 hdr_proc:
        *undescribed*

    :param u32 h:
        *undescribed*

    :param u32 c:
        *undescribed*

    :param u32 pad_type:
        *undescribed*

    :param u32 op_grp:
        *undescribed*

    :param u32 op:
        *undescribed*

    :param u32 dir:
        *undescribed*

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

    :param struct crypto_skcipher \*cipher:
        *undescribed*

    :param const u8 \*key:
        *undescribed*

    :param unsigned int keylen:
        *undescribed*

    :param unsigned char cm:
        *undescribed*

    :param u8 fb:
        *undescribed*

.. _`crypto4xx_setkey_aes_ccm`:

crypto4xx_setkey_aes_ccm
========================

.. c:function:: int crypto4xx_setkey_aes_ccm(struct crypto_aead *cipher, const u8 *key, unsigned int keylen)

    CCM Functions

    :param struct crypto_aead \*cipher:
        *undescribed*

    :param const u8 \*key:
        *undescribed*

    :param unsigned int keylen:
        *undescribed*

.. _`crypto4xx_aes_gcm_validate_keylen`:

crypto4xx_aes_gcm_validate_keylen
=================================

.. c:function:: int crypto4xx_aes_gcm_validate_keylen(unsigned int keylen)

    GCM Functions

    :param unsigned int keylen:
        *undescribed*

.. _`crypto4xx_hash_alg_init`:

crypto4xx_hash_alg_init
=======================

.. c:function:: int crypto4xx_hash_alg_init(struct crypto_tfm *tfm, unsigned int sa_len, unsigned char ha, unsigned char hm)

    :param struct crypto_tfm \*tfm:
        *undescribed*

    :param unsigned int sa_len:
        *undescribed*

    :param unsigned char ha:
        *undescribed*

    :param unsigned char hm:
        *undescribed*

.. _`crypto4xx_sha1_alg_init`:

crypto4xx_sha1_alg_init
=======================

.. c:function:: int crypto4xx_sha1_alg_init(struct crypto_tfm *tfm)

    :param struct crypto_tfm \*tfm:
        *undescribed*

.. This file was automatic generated / don't edit.

