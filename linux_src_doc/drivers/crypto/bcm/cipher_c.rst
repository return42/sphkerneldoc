.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/bcm/cipher.c

.. _`select_channel`:

select_channel
==============

.. c:function:: u8 select_channel( void)

    Select a SPU channel to handle a crypto request. Selects channel in round robin order.

    :param  void:
        no arguments

.. _`select_channel.return`:

Return
------

channel index

.. _`spu_ablkcipher_rx_sg_create`:

spu_ablkcipher_rx_sg_create
===========================

.. c:function:: int spu_ablkcipher_rx_sg_create(struct brcm_message *mssg, struct iproc_reqctx_s *rctx, u8 rx_frag_num, unsigned int chunksize, u32 stat_pad_len)

    Build up the scatterlist of buffers used to receive a SPU response message for an ablkcipher request. Includes buffers to catch SPU message headers and the response data.

    :param struct brcm_message \*mssg:
        mailbox message containing the receive sg

    :param struct iproc_reqctx_s \*rctx:
        crypto request context

    :param u8 rx_frag_num:
        number of scatterlist elements required to hold the
        SPU response message

    :param unsigned int chunksize:
        Number of bytes of response data expected

    :param u32 stat_pad_len:
        Number of bytes required to pad the STAT field to
        a 4-byte boundary

.. _`spu_ablkcipher_rx_sg_create.description`:

Description
-----------

The scatterlist that gets allocated here is freed in \ :c:func:`spu_chunk_cleanup`\ 
when the request completes, whether the request is handled successfully or
there is an error.

.. _`spu_ablkcipher_rx_sg_create.return`:

Return
------

0 if successful
< 0 if an error

.. _`spu_ablkcipher_tx_sg_create`:

spu_ablkcipher_tx_sg_create
===========================

.. c:function:: int spu_ablkcipher_tx_sg_create(struct brcm_message *mssg, struct iproc_reqctx_s *rctx, u8 tx_frag_num, unsigned int chunksize, u32 pad_len)

    Build up the scatterlist of buffers used to send a SPU request message for an ablkcipher request. Includes SPU message headers and the request data.

    :param struct brcm_message \*mssg:
        mailbox message containing the transmit sg

    :param struct iproc_reqctx_s \*rctx:
        crypto request context

    :param u8 tx_frag_num:
        number of scatterlist elements required to construct the
        SPU request message

    :param unsigned int chunksize:
        Number of bytes of request data

    :param u32 pad_len:
        Number of pad bytes

.. _`spu_ablkcipher_tx_sg_create.description`:

Description
-----------

The scatterlist that gets allocated here is freed in \ :c:func:`spu_chunk_cleanup`\ 
when the request completes, whether the request is handled successfully or
there is an error.

.. _`spu_ablkcipher_tx_sg_create.return`:

Return
------

0 if successful
< 0 if an error

.. _`handle_ablkcipher_req`:

handle_ablkcipher_req
=====================

.. c:function:: int handle_ablkcipher_req(struct iproc_reqctx_s *rctx)

    Submit as much of a block cipher request as fits in a single SPU request message, starting at the current position in the request data.

    :param struct iproc_reqctx_s \*rctx:
        Crypto request context

.. _`handle_ablkcipher_req.description`:

Description
-----------

This may be called on the crypto API thread, or, when a request is so large
it must be broken into multiple SPU messages, on the thread used to invoke
the response callback. When requests are broken into multiple SPU
messages, we assume subsequent messages depend on previous results, and
thus always wait for previous results before submitting the next message.
Because requests are submitted in lock step like this, there is no need
to synchronize access to request data structures.

.. _`handle_ablkcipher_req.return`:

Return
------

-EINPROGRESS: request has been accepted and result will be returned
asynchronously
Any other value indicates an error

.. _`handle_ablkcipher_resp`:

handle_ablkcipher_resp
======================

.. c:function:: void handle_ablkcipher_resp(struct iproc_reqctx_s *rctx)

    Process a block cipher SPU response. Updates the total received count for the request and updates global stats.

    :param struct iproc_reqctx_s \*rctx:
        Crypto request context

.. _`spu_ahash_rx_sg_create`:

spu_ahash_rx_sg_create
======================

.. c:function:: int spu_ahash_rx_sg_create(struct brcm_message *mssg, struct iproc_reqctx_s *rctx, u8 rx_frag_num, unsigned int digestsize, u32 stat_pad_len)

    Build up the scatterlist of buffers used to receive a SPU response message for an ahash request.

    :param struct brcm_message \*mssg:
        mailbox message containing the receive sg

    :param struct iproc_reqctx_s \*rctx:
        crypto request context

    :param u8 rx_frag_num:
        number of scatterlist elements required to hold the
        SPU response message

    :param unsigned int digestsize:
        length of hash digest, in bytes

    :param u32 stat_pad_len:
        Number of bytes required to pad the STAT field to
        a 4-byte boundary

.. _`spu_ahash_rx_sg_create.description`:

Description
-----------

The scatterlist that gets allocated here is freed in \ :c:func:`spu_chunk_cleanup`\ 
when the request completes, whether the request is handled successfully or
there is an error.

.. _`spu_ahash_rx_sg_create.return`:

Return
------

0 if successful
< 0 if an error

.. _`spu_ahash_tx_sg_create`:

spu_ahash_tx_sg_create
======================

.. c:function:: int spu_ahash_tx_sg_create(struct brcm_message *mssg, struct iproc_reqctx_s *rctx, u8 tx_frag_num, u32 spu_hdr_len, unsigned int hash_carry_len, unsigned int new_data_len, u32 pad_len)

    Build up the scatterlist of buffers used to send a SPU request message for an ahash request. Includes SPU message headers and the request data.

    :param struct brcm_message \*mssg:
        mailbox message containing the transmit sg

    :param struct iproc_reqctx_s \*rctx:
        crypto request context

    :param u8 tx_frag_num:
        number of scatterlist elements required to construct the
        SPU request message

    :param u32 spu_hdr_len:
        length in bytes of SPU message header

    :param unsigned int hash_carry_len:
        Number of bytes of data carried over from previous req

    :param unsigned int new_data_len:
        Number of bytes of new request data

    :param u32 pad_len:
        Number of pad bytes

.. _`spu_ahash_tx_sg_create.description`:

Description
-----------

The scatterlist that gets allocated here is freed in \ :c:func:`spu_chunk_cleanup`\ 
when the request completes, whether the request is handled successfully or
there is an error.

.. _`spu_ahash_tx_sg_create.return`:

Return
------

0 if successful
< 0 if an error

.. _`handle_ahash_req`:

handle_ahash_req
================

.. c:function:: int handle_ahash_req(struct iproc_reqctx_s *rctx)

    Process an asynchronous hash request from the crypto API.

    :param struct iproc_reqctx_s \*rctx:
        Crypto request context

.. _`handle_ahash_req.description`:

Description
-----------

Builds a SPU request message embedded in a mailbox message and submits the
mailbox message on a selected mailbox channel. The SPU request message is
constructed as a scatterlist, including entries from the crypto API's
src scatterlist to avoid copying the data to be hashed. This function is
called either on the thread from the crypto API, or, in the case that the
crypto API request is too large to fit in a single SPU request message,
on the thread that invokes the receive callback with a response message.
Because some operations require the response from one chunk before the next
chunk can be submitted, we always wait for the response for the previous
chunk before submitting the next chunk. Because requests are submitted in
lock step like this, there is no need to synchronize access to request data
structures.

.. _`handle_ahash_req.return`:

Return
------

-EINPROGRESS: request has been submitted to SPU and response will be
returned asynchronously
-EAGAIN:      non-final request included a small amount of data, which for
efficiency we did not submit to the SPU, but instead stored
to be submitted to the SPU with the next part of the request

.. _`handle_ahash_req.other`:

other
-----

an error code

.. _`spu_hmac_outer_hash`:

spu_hmac_outer_hash
===================

.. c:function:: int spu_hmac_outer_hash(struct ahash_request *req, struct iproc_ctx_s *ctx)

    Request synchonous software compute of the outer hash for an HMAC request.

    :param struct ahash_request \*req:
        The HMAC request from the crypto API

    :param struct iproc_ctx_s \*ctx:
        The session context

.. _`spu_hmac_outer_hash.return`:

Return
------

0 if synchronous hash operation successful
-EINVAL if the hash algo is unrecognized
any other value indicates an error

.. _`ahash_req_done`:

ahash_req_done
==============

.. c:function:: int ahash_req_done(struct iproc_reqctx_s *rctx)

    Process a hash result from the SPU hardware.

    :param struct iproc_reqctx_s \*rctx:
        Crypto request context

.. _`ahash_req_done.return`:

Return
------

0 if successful
< 0 if an error

.. _`handle_ahash_resp`:

handle_ahash_resp
=================

.. c:function:: void handle_ahash_resp(struct iproc_reqctx_s *rctx)

    Process a SPU response message for a hash request. Checks if the entire crypto API request has been processed, and if so, invokes post processing on the result.

    :param struct iproc_reqctx_s \*rctx:
        Crypto request context

.. _`spu_aead_rx_sg_create`:

spu_aead_rx_sg_create
=====================

.. c:function:: int spu_aead_rx_sg_create(struct brcm_message *mssg, struct aead_request *req, struct iproc_reqctx_s *rctx, u8 rx_frag_num, unsigned int assoc_len, u32 ret_iv_len, unsigned int resp_len, unsigned int digestsize, u32 stat_pad_len)

    Build up the scatterlist of buffers used to receive a SPU response message for an AEAD request. Includes buffers to catch SPU message headers and the response data.

    :param struct brcm_message \*mssg:
        mailbox message containing the receive sg

    :param struct aead_request \*req:
        *undescribed*

    :param struct iproc_reqctx_s \*rctx:
        crypto request context

    :param u8 rx_frag_num:
        number of scatterlist elements required to hold the
        SPU response message

    :param unsigned int assoc_len:
        Length of associated data included in the crypto request

    :param u32 ret_iv_len:
        Length of IV returned in response

    :param unsigned int resp_len:
        Number of bytes of response data expected to be written to
        dst buffer from crypto API

    :param unsigned int digestsize:
        Length of hash digest, in bytes

    :param u32 stat_pad_len:
        Number of bytes required to pad the STAT field to
        a 4-byte boundary

.. _`spu_aead_rx_sg_create.description`:

Description
-----------

The scatterlist that gets allocated here is freed in \ :c:func:`spu_chunk_cleanup`\ 
when the request completes, whether the request is handled successfully or
there is an error.

.. _`spu_aead_rx_sg_create.return`:

Return
------

0 if successful
< 0 if an error

.. _`spu_aead_tx_sg_create`:

spu_aead_tx_sg_create
=====================

.. c:function:: int spu_aead_tx_sg_create(struct brcm_message *mssg, struct iproc_reqctx_s *rctx, u8 tx_frag_num, u32 spu_hdr_len, struct scatterlist *assoc, unsigned int assoc_len, int assoc_nents, unsigned int aead_iv_len, unsigned int chunksize, u32 aad_pad_len, u32 pad_len, bool incl_icv)

    Build up the scatterlist of buffers used to send a SPU request message for an AEAD request. Includes SPU message headers and the request data.

    :param struct brcm_message \*mssg:
        mailbox message containing the transmit sg

    :param struct iproc_reqctx_s \*rctx:
        crypto request context

    :param u8 tx_frag_num:
        number of scatterlist elements required to construct the
        SPU request message

    :param u32 spu_hdr_len:
        length of SPU message header in bytes

    :param struct scatterlist \*assoc:
        crypto API associated data scatterlist

    :param unsigned int assoc_len:
        length of associated data

    :param int assoc_nents:
        number of scatterlist entries containing assoc data

    :param unsigned int aead_iv_len:
        length of AEAD IV, if included

    :param unsigned int chunksize:
        Number of bytes of request data

    :param u32 aad_pad_len:
        Number of bytes of padding at end of AAD. For GCM/CCM.

    :param u32 pad_len:
        Number of pad bytes

    :param bool incl_icv:
        If true, write separate ICV buffer after data and
        any padding

.. _`spu_aead_tx_sg_create.description`:

Description
-----------

The scatterlist that gets allocated here is freed in \ :c:func:`spu_chunk_cleanup`\ 
when the request completes, whether the request is handled successfully or
there is an error.

.. _`spu_aead_tx_sg_create.return`:

Return
------

0 if successful
< 0 if an error

.. _`handle_aead_req`:

handle_aead_req
===============

.. c:function:: int handle_aead_req(struct iproc_reqctx_s *rctx)

    Submit a SPU request message for the next chunk of the current AEAD request.

    :param struct iproc_reqctx_s \*rctx:
        Crypto request context

.. _`handle_aead_req.description`:

Description
-----------

Unlike other operation types, we assume the length of the request fits in
a single SPU request message. \ :c:func:`aead_enqueue`\  makes sure this is true.
Comments for other op types regarding threads applies here as well.

Unlike incremental hash ops, where the spu returns the entire hash for
truncated algs like sha-224, the SPU returns just the truncated hash in
response to aead requests. So digestsize is always ctx->digestsize here.

.. _`handle_aead_req.return`:

Return
------

-EINPROGRESS: crypto request has been accepted and result will be
returned asynchronously
Any other value indicates an error

.. _`handle_aead_resp`:

handle_aead_resp
================

.. c:function:: void handle_aead_resp(struct iproc_reqctx_s *rctx)

    Process a SPU response message for an AEAD request.

    :param struct iproc_reqctx_s \*rctx:
        Crypto request context

.. _`spu_chunk_cleanup`:

spu_chunk_cleanup
=================

.. c:function:: void spu_chunk_cleanup(struct iproc_reqctx_s *rctx)

    Do cleanup after processing one chunk of a request

    :param struct iproc_reqctx_s \*rctx:
        request context

.. _`spu_chunk_cleanup.description`:

Description
-----------

Mailbox scatterlists are allocated for each chunk. So free them after
processing each chunk.

.. _`finish_req`:

finish_req
==========

.. c:function:: void finish_req(struct iproc_reqctx_s *rctx, int err)

    Used to invoke the complete callback from the requester when a request has been handled asynchronously.

    :param struct iproc_reqctx_s \*rctx:
        Request context

    :param int err:
        Indicates whether the request was successful or not

.. _`finish_req.description`:

Description
-----------

Ensures that cleanup has been done for request

.. _`spu_rx_callback`:

spu_rx_callback
===============

.. c:function:: void spu_rx_callback(struct mbox_client *cl, void *msg)

    Callback from mailbox framework with a SPU response.

    :param struct mbox_client \*cl:
        mailbox client structure for SPU driver

    :param void \*msg:
        mailbox message containing SPU response

.. _`ablkcipher_enqueue`:

ablkcipher_enqueue
==================

.. c:function:: int ablkcipher_enqueue(struct ablkcipher_request *req, bool encrypt)

    Handle ablkcipher encrypt or decrypt request.

    :param struct ablkcipher_request \*req:
        Crypto API request

    :param bool encrypt:
        true if encrypting; false if decrypting

.. _`ablkcipher_enqueue.return`:

Return
------

-EINPROGRESS if request accepted and result will be returned
asynchronously
< 0 if an error

.. _`spu_no_incr_hash`:

spu_no_incr_hash
================

.. c:function:: bool spu_no_incr_hash(struct iproc_ctx_s *ctx)

    Determine whether incremental hashing is supported.

    :param struct iproc_ctx_s \*ctx:
        Crypto session context

.. _`spu_no_incr_hash.description`:

Description
-----------

SPU-2 does not support incremental hashing (we'll have to revisit and
condition based on chip revision or device tree entry if future versions do
support incremental hash)

SPU-M also doesn't support incremental hashing of AES-XCBC

.. _`spu_no_incr_hash.return`:

Return
------

true if incremental hashing is not supported
false otherwise

.. _`aead_gcm_esp_setkey`:

aead_gcm_esp_setkey
===================

.. c:function:: int aead_gcm_esp_setkey(struct crypto_aead *cipher, const u8 *key, unsigned int keylen)

    \ :c:func:`setkey`\  operation for ESP variant of GCM AES.

    :param struct crypto_aead \*cipher:
        AEAD structure

    :param const u8 \*key:
        Key followed by 4 bytes of salt

    :param unsigned int keylen:
        Length of key plus salt, in bytes

.. _`aead_gcm_esp_setkey.description`:

Description
-----------

Extracts salt from key and stores it to be prepended to IV on each request.
Digest is always 16 bytes

.. _`aead_gcm_esp_setkey.return`:

Return
------

Value from generic gcm setkey.

.. _`rfc4543_gcm_esp_setkey`:

rfc4543_gcm_esp_setkey
======================

.. c:function:: int rfc4543_gcm_esp_setkey(struct crypto_aead *cipher, const u8 *key, unsigned int keylen)

    setkey operation for RFC4543 variant of GCM/GMAC.

    :param struct crypto_aead \*cipher:
        *undescribed*

    :param const u8 \*key:
        *undescribed*

    :param unsigned int keylen:
        *undescribed*

.. _`rfc4543_gcm_esp_setkey.cipher`:

cipher
------

AEAD structure

.. _`rfc4543_gcm_esp_setkey.key`:

key
---

Key followed by 4 bytes of salt

.. _`rfc4543_gcm_esp_setkey.keylen`:

keylen
------

Length of key plus salt, in bytes

Extracts salt from key and stores it to be prepended to IV on each request.
Digest is always 16 bytes

.. _`rfc4543_gcm_esp_setkey.return`:

Return
------

Value from generic gcm setkey.

.. _`aead_ccm_esp_setkey`:

aead_ccm_esp_setkey
===================

.. c:function:: int aead_ccm_esp_setkey(struct crypto_aead *cipher, const u8 *key, unsigned int keylen)

    \ :c:func:`setkey`\  operation for ESP variant of CCM AES.

    :param struct crypto_aead \*cipher:
        AEAD structure

    :param const u8 \*key:
        Key followed by 4 bytes of salt

    :param unsigned int keylen:
        Length of key plus salt, in bytes

.. _`aead_ccm_esp_setkey.description`:

Description
-----------

Extracts salt from key and stores it to be prepended to IV on each request.
Digest is always 16 bytes

.. _`aead_ccm_esp_setkey.return`:

Return
------

Value from generic ccm setkey.

.. _`spu_functions_register`:

spu_functions_register
======================

.. c:function:: void spu_functions_register(struct device *dev, enum spu_spu_type spu_type, enum spu_spu_subtype spu_subtype)

    Specify hardware-specific SPU functions based on SPU type read from device tree.

    :param struct device \*dev:
        device structure

    :param enum spu_spu_type spu_type:
        SPU hardware generation

    :param enum spu_spu_subtype spu_subtype:
        SPU hardware version

.. _`spu_mb_init`:

spu_mb_init
===========

.. c:function:: int spu_mb_init(struct device *dev)

    Initialize mailbox client. Request ownership of a mailbox channel for the SPU being probed.

    :param struct device \*dev:
        SPU driver device structure

.. _`spu_mb_init.return`:

Return
------

0 if successful
< 0 otherwise

.. This file was automatic generated / don't edit.

