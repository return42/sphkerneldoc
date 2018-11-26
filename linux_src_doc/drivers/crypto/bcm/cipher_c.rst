.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/bcm/cipher.c

.. _`select_channel`:

select_channel
==============

.. c:function:: u8 select_channel( void)

    Select a SPU channel to handle a crypto request. Selects channel in round robin order.

    :param void:
        no arguments
    :type void: 

.. _`select_channel.return`:

Return
------

channel index

.. _`spu_ablkcipher_rx_sg_create`:

spu_ablkcipher_rx_sg_create
===========================

.. c:function:: int spu_ablkcipher_rx_sg_create(struct brcm_message *mssg, struct iproc_reqctx_s *rctx, u8 rx_frag_num, unsigned int chunksize, u32 stat_pad_len)

    Build up the scatterlist of buffers used to receive a SPU response message for an ablkcipher request. Includes buffers to catch SPU message headers and the response data.

    :param mssg:
        mailbox message containing the receive sg
    :type mssg: struct brcm_message \*

    :param rctx:
        crypto request context
    :type rctx: struct iproc_reqctx_s \*

    :param rx_frag_num:
        number of scatterlist elements required to hold the
        SPU response message
    :type rx_frag_num: u8

    :param chunksize:
        Number of bytes of response data expected
    :type chunksize: unsigned int

    :param stat_pad_len:
        Number of bytes required to pad the STAT field to
        a 4-byte boundary
    :type stat_pad_len: u32

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

    :param mssg:
        mailbox message containing the transmit sg
    :type mssg: struct brcm_message \*

    :param rctx:
        crypto request context
    :type rctx: struct iproc_reqctx_s \*

    :param tx_frag_num:
        number of scatterlist elements required to construct the
        SPU request message
    :type tx_frag_num: u8

    :param chunksize:
        Number of bytes of request data
    :type chunksize: unsigned int

    :param pad_len:
        Number of pad bytes
    :type pad_len: u32

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

    :param rctx:
        Crypto request context
    :type rctx: struct iproc_reqctx_s \*

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

    :param rctx:
        Crypto request context
    :type rctx: struct iproc_reqctx_s \*

.. _`spu_ahash_rx_sg_create`:

spu_ahash_rx_sg_create
======================

.. c:function:: int spu_ahash_rx_sg_create(struct brcm_message *mssg, struct iproc_reqctx_s *rctx, u8 rx_frag_num, unsigned int digestsize, u32 stat_pad_len)

    Build up the scatterlist of buffers used to receive a SPU response message for an ahash request.

    :param mssg:
        mailbox message containing the receive sg
    :type mssg: struct brcm_message \*

    :param rctx:
        crypto request context
    :type rctx: struct iproc_reqctx_s \*

    :param rx_frag_num:
        number of scatterlist elements required to hold the
        SPU response message
    :type rx_frag_num: u8

    :param digestsize:
        length of hash digest, in bytes
    :type digestsize: unsigned int

    :param stat_pad_len:
        Number of bytes required to pad the STAT field to
        a 4-byte boundary
    :type stat_pad_len: u32

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

    :param mssg:
        mailbox message containing the transmit sg
    :type mssg: struct brcm_message \*

    :param rctx:
        crypto request context
    :type rctx: struct iproc_reqctx_s \*

    :param tx_frag_num:
        number of scatterlist elements required to construct the
        SPU request message
    :type tx_frag_num: u8

    :param spu_hdr_len:
        length in bytes of SPU message header
    :type spu_hdr_len: u32

    :param hash_carry_len:
        Number of bytes of data carried over from previous req
    :type hash_carry_len: unsigned int

    :param new_data_len:
        Number of bytes of new request data
    :type new_data_len: unsigned int

    :param pad_len:
        Number of pad bytes
    :type pad_len: u32

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

    :param rctx:
        Crypto request context
    :type rctx: struct iproc_reqctx_s \*

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

    :param req:
        The HMAC request from the crypto API
    :type req: struct ahash_request \*

    :param ctx:
        The session context
    :type ctx: struct iproc_ctx_s \*

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

    :param rctx:
        Crypto request context
    :type rctx: struct iproc_reqctx_s \*

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

    :param rctx:
        Crypto request context
    :type rctx: struct iproc_reqctx_s \*

.. _`spu_aead_rx_sg_create`:

spu_aead_rx_sg_create
=====================

.. c:function:: int spu_aead_rx_sg_create(struct brcm_message *mssg, struct aead_request *req, struct iproc_reqctx_s *rctx, u8 rx_frag_num, unsigned int assoc_len, u32 ret_iv_len, unsigned int resp_len, unsigned int digestsize, u32 stat_pad_len)

    Build up the scatterlist of buffers used to receive a SPU response message for an AEAD request. Includes buffers to catch SPU message headers and the response data.

    :param mssg:
        mailbox message containing the receive sg
    :type mssg: struct brcm_message \*

    :param req:
        *undescribed*
    :type req: struct aead_request \*

    :param rctx:
        crypto request context
    :type rctx: struct iproc_reqctx_s \*

    :param rx_frag_num:
        number of scatterlist elements required to hold the
        SPU response message
    :type rx_frag_num: u8

    :param assoc_len:
        Length of associated data included in the crypto request
    :type assoc_len: unsigned int

    :param ret_iv_len:
        Length of IV returned in response
    :type ret_iv_len: u32

    :param resp_len:
        Number of bytes of response data expected to be written to
        dst buffer from crypto API
    :type resp_len: unsigned int

    :param digestsize:
        Length of hash digest, in bytes
    :type digestsize: unsigned int

    :param stat_pad_len:
        Number of bytes required to pad the STAT field to
        a 4-byte boundary
    :type stat_pad_len: u32

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

    :param mssg:
        mailbox message containing the transmit sg
    :type mssg: struct brcm_message \*

    :param rctx:
        crypto request context
    :type rctx: struct iproc_reqctx_s \*

    :param tx_frag_num:
        number of scatterlist elements required to construct the
        SPU request message
    :type tx_frag_num: u8

    :param spu_hdr_len:
        length of SPU message header in bytes
    :type spu_hdr_len: u32

    :param assoc:
        crypto API associated data scatterlist
    :type assoc: struct scatterlist \*

    :param assoc_len:
        length of associated data
    :type assoc_len: unsigned int

    :param assoc_nents:
        number of scatterlist entries containing assoc data
    :type assoc_nents: int

    :param aead_iv_len:
        length of AEAD IV, if included
    :type aead_iv_len: unsigned int

    :param chunksize:
        Number of bytes of request data
    :type chunksize: unsigned int

    :param aad_pad_len:
        Number of bytes of padding at end of AAD. For GCM/CCM.
    :type aad_pad_len: u32

    :param pad_len:
        Number of pad bytes
    :type pad_len: u32

    :param incl_icv:
        If true, write separate ICV buffer after data and
        any padding
    :type incl_icv: bool

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

    :param rctx:
        Crypto request context
    :type rctx: struct iproc_reqctx_s \*

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

    :param rctx:
        Crypto request context
    :type rctx: struct iproc_reqctx_s \*

.. _`spu_chunk_cleanup`:

spu_chunk_cleanup
=================

.. c:function:: void spu_chunk_cleanup(struct iproc_reqctx_s *rctx)

    Do cleanup after processing one chunk of a request

    :param rctx:
        request context
    :type rctx: struct iproc_reqctx_s \*

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

    :param rctx:
        Request context
    :type rctx: struct iproc_reqctx_s \*

    :param err:
        Indicates whether the request was successful or not
    :type err: int

.. _`finish_req.description`:

Description
-----------

Ensures that cleanup has been done for request

.. _`spu_rx_callback`:

spu_rx_callback
===============

.. c:function:: void spu_rx_callback(struct mbox_client *cl, void *msg)

    Callback from mailbox framework with a SPU response.

    :param cl:
        mailbox client structure for SPU driver
    :type cl: struct mbox_client \*

    :param msg:
        mailbox message containing SPU response
    :type msg: void \*

.. _`ablkcipher_enqueue`:

ablkcipher_enqueue
==================

.. c:function:: int ablkcipher_enqueue(struct ablkcipher_request *req, bool encrypt)

    Handle ablkcipher encrypt or decrypt request.

    :param req:
        Crypto API request
    :type req: struct ablkcipher_request \*

    :param encrypt:
        true if encrypting; false if decrypting
    :type encrypt: bool

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

    :param ctx:
        Crypto session context
    :type ctx: struct iproc_ctx_s \*

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

    :param cipher:
        AEAD structure
    :type cipher: struct crypto_aead \*

    :param key:
        Key followed by 4 bytes of salt
    :type key: const u8 \*

    :param keylen:
        Length of key plus salt, in bytes
    :type keylen: unsigned int

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

    :param cipher:
        *undescribed*
    :type cipher: struct crypto_aead \*

    :param key:
        *undescribed*
    :type key: const u8 \*

    :param keylen:
        *undescribed*
    :type keylen: unsigned int

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

    :param cipher:
        AEAD structure
    :type cipher: struct crypto_aead \*

    :param key:
        Key followed by 4 bytes of salt
    :type key: const u8 \*

    :param keylen:
        Length of key plus salt, in bytes
    :type keylen: unsigned int

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

    :param dev:
        device structure
    :type dev: struct device \*

    :param spu_type:
        SPU hardware generation
    :type spu_type: enum spu_spu_type

    :param spu_subtype:
        SPU hardware version
    :type spu_subtype: enum spu_spu_subtype

.. _`spu_mb_init`:

spu_mb_init
===========

.. c:function:: int spu_mb_init(struct device *dev)

    Initialize mailbox client. Request ownership of a mailbox channel for the SPU being probed.

    :param dev:
        SPU driver device structure
    :type dev: struct device \*

.. _`spu_mb_init.return`:

Return
------

0 if successful
< 0 otherwise

.. This file was automatic generated / don't edit.

