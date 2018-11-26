.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/ccp/ccp-crypto-main.c

.. _`ccp_crypto_enqueue_request`:

ccp_crypto_enqueue_request
==========================

.. c:function:: int ccp_crypto_enqueue_request(struct crypto_async_request *req, struct ccp_cmd *cmd)

    queue an crypto async request for processing by the CCP

    :param req:
        crypto_async_request struct to be processed
    :type req: struct crypto_async_request \*

    :param cmd:
        ccp_cmd struct to be sent to the CCP
    :type cmd: struct ccp_cmd \*

.. This file was automatic generated / don't edit.

