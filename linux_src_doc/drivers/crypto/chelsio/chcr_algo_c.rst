.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/chelsio/chcr_algo.c

.. _`create_cipher_wr`:

create_cipher_wr
================

.. c:function:: struct sk_buff *create_cipher_wr(struct cipher_wr_param *wrparam)

    form the WR for cipher operations

    :param struct cipher_wr_param \*wrparam:
        *undescribed*

.. _`create_hash_wr`:

create_hash_wr
==============

.. c:function:: struct sk_buff *create_hash_wr(struct ahash_request *req, struct hash_wr_param *param)

    Create hash work request \ ``req``\  - Cipher req base

    :param struct ahash_request \*req:
        *undescribed*

    :param struct hash_wr_param \*param:
        *undescribed*

.. This file was automatic generated / don't edit.

