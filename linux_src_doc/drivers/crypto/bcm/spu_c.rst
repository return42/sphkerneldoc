.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/bcm/spu.c

.. _`spum_ns2_ctx_max_payload`:

spum_ns2_ctx_max_payload
========================

.. c:function:: u32 spum_ns2_ctx_max_payload(enum spu_cipher_alg cipher_alg, enum spu_cipher_mode cipher_mode, unsigned int blocksize)

    Determine the max length of the payload for a SPU message for a given cipher and hash alg context.

    :param enum spu_cipher_alg cipher_alg:
        The cipher algorithm

    :param enum spu_cipher_mode cipher_mode:
        The cipher mode

    :param unsigned int blocksize:
        The size of a block of data for this algo

.. _`spum_ns2_ctx_max_payload.description`:

Description
-----------

The max payload must be a multiple of the blocksize so that if a request is
too large to fit in a single SPU message, the request can be broken into
max_payload sized chunks. Each chunk must be a multiple of blocksize.

.. _`spum_ns2_ctx_max_payload.return`:

Return
------

Max payload length in bytes

.. _`spum_nsp_ctx_max_payload`:

spum_nsp_ctx_max_payload
========================

.. c:function:: u32 spum_nsp_ctx_max_payload(enum spu_cipher_alg cipher_alg, enum spu_cipher_mode cipher_mode, unsigned int blocksize)

    Determine the max length of the payload for a SPU message for a given cipher and hash alg context.

    :param enum spu_cipher_alg cipher_alg:
        The cipher algorithm

    :param enum spu_cipher_mode cipher_mode:
        The cipher mode

    :param unsigned int blocksize:
        The size of a block of data for this algo

.. _`spum_nsp_ctx_max_payload.description`:

Description
-----------

The max payload must be a multiple of the blocksize so that if a request is
too large to fit in a single SPU message, the request can be broken into
max_payload sized chunks. Each chunk must be a multiple of blocksize.

.. _`spum_nsp_ctx_max_payload.return`:

Return
------

Max payload length in bytes

.. _`spum_response_hdr_len`:

spum_response_hdr_len
=====================

.. c:function:: u16 spum_response_hdr_len(u16 auth_key_len, u16 enc_key_len, bool is_hash)

    Given the length of the hash key and encryption key, determine the expected length of a SPU response header.

    :param u16 auth_key_len:
        authentication key length (bytes)

    :param u16 enc_key_len:
        encryption key length (bytes)

    :param bool is_hash:
        true if response message is for a hash operation

.. _`spum_response_hdr_len.return`:

Return
------

length of SPU response header (bytes)

.. _`spum_hash_pad_len`:

spum_hash_pad_len
=================

.. c:function:: u16 spum_hash_pad_len(enum hash_alg hash_alg, enum hash_mode hash_mode, u32 chunksize, u16 hash_block_size)

    Calculate the length of hash padding required to extend data to a full block size.

    :param enum hash_alg hash_alg:
        hash algorithm

    :param enum hash_mode hash_mode:
        hash mode

    :param u32 chunksize:
        length of data, in bytes

    :param u16 hash_block_size:
        size of a block of data for hash algorithm

.. _`spum_hash_pad_len.description`:

Description
-----------

Reserve space for 1 byte (0x80) start of pad and the total length as u64

.. _`spum_hash_pad_len.return`:

Return
------

length of hash pad in bytes

.. _`spum_gcm_ccm_pad_len`:

spum_gcm_ccm_pad_len
====================

.. c:function:: u32 spum_gcm_ccm_pad_len(enum spu_cipher_mode cipher_mode, unsigned int data_size)

    Determine the required length of GCM or CCM padding.

    :param enum spu_cipher_mode cipher_mode:
        Algo type

    :param unsigned int data_size:
        Length of plaintext (bytes)

.. _`spum_assoc_resp_len`:

spum_assoc_resp_len
===================

.. c:function:: u32 spum_assoc_resp_len(enum spu_cipher_mode cipher_mode, unsigned int assoc_len, unsigned int iv_len, bool is_encrypt)

    Determine the size of the receive buffer required to catch associated data.

    :param enum spu_cipher_mode cipher_mode:
        cipher mode

    :param unsigned int assoc_len:
        length of associated data (bytes)

    :param unsigned int iv_len:
        length of IV (bytes)

    :param bool is_encrypt:
        true if encrypting. false if decrypting.

.. _`spum_assoc_resp_len.return`:

Return
------

length of associated data in response message (bytes)

.. _`spum_aead_ivlen`:

spum_aead_ivlen
===============

.. c:function:: u8 spum_aead_ivlen(enum spu_cipher_mode cipher_mode, u16 iv_len)

    Calculate the length of the AEAD IV to be included in a SPU request after the AAD and before the payload.

    :param enum spu_cipher_mode cipher_mode:
        cipher mode

    :param u16 iv_len:
        *undescribed*

.. _`spum_aead_ivlen.description`:

Description
-----------

In Linux ~4.2 and later, the assoc_data sg includes the IV. So no need
to include the IV as a separate field in the SPU request msg.

.. _`spum_aead_ivlen.return`:

Return
------

Length of AEAD IV in bytes

.. _`spum_hash_type`:

spum_hash_type
==============

.. c:function:: enum hash_type spum_hash_type(u32 src_sent)

    Determine the type of hash operation.

    :param u32 src_sent:
        The number of bytes in the current request that have already
        been sent to the SPU to be hashed.

.. _`spum_hash_type.description`:

Description
-----------

We do not use HASH_TYPE_FULL for requests that fit in a single SPU message.
Using FULL causes failures (such as when the string to be hashed is empty).
For similar reasons, we never use HASH_TYPE_FIN. Instead, submit messages
as INIT or UPDT and do the hash padding in sw.

.. _`spum_digest_size`:

spum_digest_size
================

.. c:function:: u32 spum_digest_size(u32 alg_digest_size, enum hash_alg alg, enum hash_type htype)

    Determine the size of a hash digest to expect the SPU to return.

    :param u32 alg_digest_size:
        *undescribed*

    :param enum hash_alg alg:
        *undescribed*

    :param enum hash_type htype:
        *undescribed*

.. _`spum_digest_size.alg_digest_size`:

alg_digest_size
---------------

Number of bytes in the final digest for the given algo

.. _`spum_digest_size.alg`:

alg
---

The hash algorithm

.. _`spum_digest_size.htype`:

htype
-----

Type of hash operation (init, update, full, etc)

When doing incremental hashing for an algorithm with a truncated hash
(e.g., SHA224), the SPU returns the full digest so that it can be fed back as
a partial result for the next chunk.

.. _`spum_create_request`:

spum_create_request
===================

.. c:function:: u32 spum_create_request(u8 *spu_hdr, struct spu_request_opts *req_opts, struct spu_cipher_parms *cipher_parms, struct spu_hash_parms *hash_parms, struct spu_aead_parms *aead_parms, unsigned int data_size)

    Build a SPU request message header, up to and including the BD header. Construct the message starting at spu_hdr. Caller should allocate this buffer in DMA-able memory at least SPU_HEADER_ALLOC_LEN bytes long.

    :param u8 \*spu_hdr:
        Start of buffer where SPU request header is to be written

    :param struct spu_request_opts \*req_opts:
        SPU request message options

    :param struct spu_cipher_parms \*cipher_parms:
        Parameters related to cipher algorithm

    :param struct spu_hash_parms \*hash_parms:
        Parameters related to hash algorithm

    :param struct spu_aead_parms \*aead_parms:
        Parameters related to AEAD operation

    :param unsigned int data_size:
        Length of data to be encrypted or authenticated. If AEAD, does
        not include length of AAD.

.. _`spum_create_request.return`:

Return
------

the length of the SPU header in bytes. 0 if an error occurs.

.. _`spum_cipher_req_init`:

spum_cipher_req_init
====================

.. c:function:: u16 spum_cipher_req_init(u8 *spu_hdr, struct spu_cipher_parms *cipher_parms)

    Build a SPU request message header, up to and including the BD header.

    :param u8 \*spu_hdr:
        Start of SPU request header (MH)

    :param struct spu_cipher_parms \*cipher_parms:
        Parameters that describe the cipher request

.. _`spum_cipher_req_init.description`:

Description
-----------

Construct the message starting at spu_hdr. Caller should allocate this buffer
in DMA-able memory at least SPU_HEADER_ALLOC_LEN bytes long.

.. _`spum_cipher_req_init.return`:

Return
------

the length of the SPU header in bytes. 0 if an error occurs.

.. _`spum_cipher_req_finish`:

spum_cipher_req_finish
======================

.. c:function:: void spum_cipher_req_finish(u8 *spu_hdr, u16 spu_req_hdr_len, unsigned int is_inbound, struct spu_cipher_parms *cipher_parms, bool update_key, unsigned int data_size)

    Finish building a SPU request message header for a block cipher request. Assumes much of the header was already filled in at \ :c:func:`setkey`\  time in \ :c:func:`spu_cipher_req_init`\ .

    :param u8 \*spu_hdr:
        Start of the request message header (MH field)

    :param u16 spu_req_hdr_len:
        Length in bytes of the SPU request header

    :param unsigned int is_inbound:
        *undescribed*

    :param struct spu_cipher_parms \*cipher_parms:
        Parameters describing cipher operation to be performed

    :param bool update_key:
        If true, rewrite the cipher key in SCTX

    :param unsigned int data_size:
        Length of the data in the BD field

.. _`spum_cipher_req_finish.description`:

Description
-----------

Assumes much of the header was already filled in at \ :c:func:`setkey`\  time in
\ :c:func:`spum_cipher_req_init`\ .
\ :c:func:`spum_cipher_req_init`\  fills in the encryption key. For RC4, when submitting
a request for a non-first chunk, we use the 260-byte SUPDT field from the
previous response as the key. update_key is true for this case. Unused in all
other cases.

.. _`spum_request_pad`:

spum_request_pad
================

.. c:function:: void spum_request_pad(u8 *pad_start, u32 gcm_ccm_padding, u32 hash_pad_len, enum hash_alg auth_alg, enum hash_mode auth_mode, unsigned int total_sent, u32 status_padding)

    Create pad bytes at the end of the data.

    :param u8 \*pad_start:
        Start of buffer where pad bytes are to be written

    :param u32 gcm_ccm_padding:
        length of GCM/CCM padding, in bytes

    :param u32 hash_pad_len:
        Number of bytes of padding extend data to full block

    :param enum hash_alg auth_alg:
        authentication algorithm

    :param enum hash_mode auth_mode:
        authentication mode

    :param unsigned int total_sent:
        length inserted at end of hash pad

    :param u32 status_padding:
        Number of bytes of padding to align STATUS word

.. _`spum_request_pad.there-may-be-three-forms-of-pad`:

There may be three forms of pad
-------------------------------

1. GCM/CCM pad - for GCM/CCM mode ciphers, pad to 16-byte alignment
2. hash pad - pad to a block length, with 0x80 data terminator and
size at the end
3. STAT pad - to ensure the STAT field is 4-byte aligned

.. _`spum_xts_tweak_in_payload`:

spum_xts_tweak_in_payload
=========================

.. c:function:: u8 spum_xts_tweak_in_payload( void)

    Indicate that SPUM DOES place the XTS tweak field in the packet payload (rather than using IV)

    :param  void:
        no arguments

.. _`spum_xts_tweak_in_payload.return`:

Return
------

1

.. _`spum_tx_status_len`:

spum_tx_status_len
==================

.. c:function:: u8 spum_tx_status_len( void)

    Return the length of the STATUS field in a SPU response message.

    :param  void:
        no arguments

.. _`spum_tx_status_len.return`:

Return
------

Length of STATUS field in bytes.

.. _`spum_rx_status_len`:

spum_rx_status_len
==================

.. c:function:: u8 spum_rx_status_len( void)

    Return the length of the STATUS field in a SPU response message.

    :param  void:
        no arguments

.. _`spum_rx_status_len.return`:

Return
------

Length of STATUS field in bytes.

.. _`spum_status_process`:

spum_status_process
===================

.. c:function:: int spum_status_process(u8 *statp)

    Process the status from a SPU response message.

    :param u8 \*statp:
        start of STATUS word

.. _`spum_status_process.return`:

Return
------

0 - if status is good and response should be processed
!0 - status indicates an error and response is invalid

.. _`spum_ccm_update_iv`:

spum_ccm_update_iv
==================

.. c:function:: void spum_ccm_update_iv(unsigned int digestsize, struct spu_cipher_parms *cipher_parms, unsigned int assoclen, unsigned int chunksize, bool is_encrypt, bool is_esp)

    Update the IV as per the requirements for CCM mode.

    :param unsigned int digestsize:
        Digest size of this request

    :param struct spu_cipher_parms \*cipher_parms:
        (pointer to) cipher parmaeters, includes IV buf & IV len

    :param unsigned int assoclen:
        Length of AAD data

    :param unsigned int chunksize:
        length of input data to be sent in this req

    :param bool is_encrypt:
        true if this is an output/encrypt operation

    :param bool is_esp:
        true if this is an ESP / RFC4309 operation

.. _`spum_wordalign_padlen`:

spum_wordalign_padlen
=====================

.. c:function:: u32 spum_wordalign_padlen(u32 data_size)

    Given the length of a data field, determine the padding required to align the data following this field on a 4-byte boundary.

    :param u32 data_size:
        length of data field in bytes

.. _`spum_wordalign_padlen.return`:

Return
------

length of status field padding, in bytes

.. This file was automatic generated / don't edit.

