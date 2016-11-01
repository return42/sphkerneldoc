.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/chelsio/chcr_algo.c

.. _`create_cipher_wr`:

create_cipher_wr
================

.. c:function:: struct sk_buff *create_cipher_wr(struct crypto_async_request *req_base, struct chcr_context *ctx, unsigned short qid, unsigned short op_type)

    form the WR for cipher operations

    :param struct crypto_async_request \*req_base:
        *undescribed*

    :param struct chcr_context \*ctx:
        crypto driver context of the request.

    :param unsigned short qid:
        ingress qid where response of this WR should be received.

    :param unsigned short op_type:
        encryption or decryption

.. _`create_final_hash_wr`:

create_final_hash_wr
====================

.. c:function:: struct sk_buff *create_final_hash_wr(struct ahash_request *req, struct hash_wr_param *param)

    Create hash work request \ ``req``\  - Cipher req base

    :param struct ahash_request \*req:
        *undescribed*

    :param struct hash_wr_param \*param:
        *undescribed*

.. This file was automatic generated / don't edit.

