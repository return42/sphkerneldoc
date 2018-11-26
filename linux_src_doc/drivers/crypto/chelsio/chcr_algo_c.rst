.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/chelsio/chcr_algo.c

.. _`create_cipher_wr`:

create_cipher_wr
================

.. c:function:: struct sk_buff *create_cipher_wr(struct cipher_wr_param *wrparam)

    form the WR for cipher operations

    :param wrparam:
        *undescribed*
    :type wrparam: struct cipher_wr_param \*

.. _`create_hash_wr`:

create_hash_wr
==============

.. c:function:: struct sk_buff *create_hash_wr(struct ahash_request *req, struct hash_wr_param *param)

    Create hash work request \ ``req``\  - Cipher req base

    :param req:
        *undescribed*
    :type req: struct ahash_request \*

    :param param:
        *undescribed*
    :type param: struct hash_wr_param \*

.. This file was automatic generated / don't edit.

