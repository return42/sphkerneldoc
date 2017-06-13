.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/bcm/spu2.c

.. _`spu2_cipher_xlate`:

spu2_cipher_xlate
=================

.. c:function:: int spu2_cipher_xlate(enum spu_cipher_alg cipher_alg, enum spu_cipher_mode cipher_mode, enum spu_cipher_type cipher_type, enum spu2_cipher_type *spu2_type, enum spu2_cipher_mode *spu2_mode)

    Convert a cipher {alg/mode/type} triple to a SPU2 cipher type and mode.

    :param enum spu_cipher_alg cipher_alg:
        [in]  cipher algorithm value from software enumeration

    :param enum spu_cipher_mode cipher_mode:
        [in]  cipher mode value from software enumeration

    :param enum spu_cipher_type cipher_type:
        [in]  cipher type value from software enumeration

    :param enum spu2_cipher_type \*spu2_type:
        [out] cipher type value used by spu2 hardware

    :param enum spu2_cipher_mode \*spu2_mode:
        [out] cipher mode value used by spu2 hardware

.. _`spu2_cipher_xlate.return`:

Return
------

0 if successful

.. _`spu2_hash_xlate`:

spu2_hash_xlate
===============

.. c:function:: int spu2_hash_xlate(enum hash_alg hash_alg, enum hash_mode hash_mode, enum hash_type hash_type, enum spu_cipher_type ciph_type, enum spu2_hash_type *spu2_type, enum spu2_hash_mode *spu2_mode)

    Convert a hash {alg/mode/type} triple to a SPU2 hash type and mode.

    :param enum hash_alg hash_alg:
        [in] hash algorithm value from software enumeration

    :param enum hash_mode hash_mode:
        [in] hash mode value from software enumeration

    :param enum hash_type hash_type:
        [in] hash type value from software enumeration

    :param enum spu_cipher_type ciph_type:
        [in] cipher type value from software enumeration

    :param enum spu2_hash_type \*spu2_type:
        [out] hash type value used by SPU2 hardware

    :param enum spu2_hash_mode \*spu2_mode:
        [out] hash mode value used by SPU2 hardware

.. _`spu2_hash_xlate.return`:

Return
------

0 if successful

.. _`spu2_fmd_init`:

spu2_fmd_init
=============

.. c:function:: int spu2_fmd_init(struct SPU2_FMD *fmd, enum spu2_cipher_type spu2_type, enum spu2_cipher_mode spu2_mode, u32 cipher_key_len, u32 cipher_iv_len)

    At setkey time, initialize the fixed meta data for subsequent ablkcipher requests for this context.

    :param struct SPU2_FMD \*fmd:
        *undescribed*

    :param enum spu2_cipher_type spu2_type:
        *undescribed*

    :param enum spu2_cipher_mode spu2_mode:
        Cipher mode

    :param u32 cipher_key_len:
        Length of cipher key, in bytes

    :param u32 cipher_iv_len:
        Length of cipher initialization vector, in bytes

.. _`spu2_fmd_init.return`:

Return
------

0 (success)

.. _`spu2_fmd_ctrl0_write`:

spu2_fmd_ctrl0_write
====================

.. c:function:: void spu2_fmd_ctrl0_write(struct SPU2_FMD *fmd, bool is_inbound, bool auth_first, enum spu2_proto_sel protocol, enum spu2_cipher_type cipher_type, enum spu2_cipher_mode cipher_mode, enum spu2_hash_type auth_type, enum spu2_hash_mode auth_mode)

    Write ctrl0 field in fixed metadata (FMD) field of SPU request packet.

    :param struct SPU2_FMD \*fmd:
        Start of FMD field to be written

    :param bool is_inbound:
        true if decrypting. false if encrypting.

    :param bool auth_first:
        *undescribed*

    :param enum spu2_proto_sel protocol:
        protocol selector

    :param enum spu2_cipher_type cipher_type:
        cipher algorithm

    :param enum spu2_cipher_mode cipher_mode:
        cipher mode

    :param enum spu2_hash_type auth_type:
        authentication type

    :param enum spu2_hash_mode auth_mode:
        authentication mode

.. _`spu2_fmd_ctrl1_write`:

spu2_fmd_ctrl1_write
====================

.. c:function:: void spu2_fmd_ctrl1_write(struct SPU2_FMD *fmd, bool is_inbound, u64 assoc_size, u64 auth_key_len, u64 cipher_key_len, bool gen_iv, bool hash_iv, bool return_iv, u64 ret_iv_len, u64 ret_iv_offset, u64 cipher_iv_len, u64 digest_size, bool return_payload, bool return_md)

    Write ctrl1 field in fixed metadata (FMD) field of SPU request packet.

    :param struct SPU2_FMD \*fmd:
        Start of FMD field to be written

    :param bool is_inbound:
        *undescribed*

    :param u64 assoc_size:
        Length of additional associated data, in bytes

    :param u64 auth_key_len:
        Length of authentication key, in bytes

    :param u64 cipher_key_len:
        Length of cipher key, in bytes

    :param bool gen_iv:
        If true, hw generates IV and returns in response

    :param bool hash_iv:
        IV participates in hash. Used for IPSEC and TLS.

    :param bool return_iv:
        Return IV in output packet before payload

    :param u64 ret_iv_len:
        Length of IV returned from SPU, in bytes

    :param u64 ret_iv_offset:
        Offset into full IV of start of returned IV

    :param u64 cipher_iv_len:
        Length of input cipher IV, in bytes

    :param u64 digest_size:
        Length of digest (aka, hash tag or ICV), in bytes

    :param bool return_payload:
        Return payload in SPU response

    :param bool return_md:
        return metadata in SPU response

.. _`spu2_fmd_ctrl1_write.description`:

Description
-----------

Packet can have AAD2 w/o AAD1. For algorithms currently supported,
associated data goes in AAD2.

.. _`spu2_fmd_ctrl2_write`:

spu2_fmd_ctrl2_write
====================

.. c:function:: void spu2_fmd_ctrl2_write(struct SPU2_FMD *fmd, u64 cipher_offset, u64 auth_key_len, u64 auth_iv_len, u64 cipher_key_len, u64 cipher_iv_len)

    Set the ctrl2 field in the fixed metadata field of SPU2 header.

    :param struct SPU2_FMD \*fmd:
        Start of FMD field to be written

    :param u64 cipher_offset:
        Number of bytes from Start of Packet (end of FD field) where
        data to be encrypted or decrypted begins

    :param u64 auth_key_len:
        Length of authentication key, in bytes

    :param u64 auth_iv_len:
        Length of authentication initialization vector, in bytes

    :param u64 cipher_key_len:
        Length of cipher key, in bytes

    :param u64 cipher_iv_len:
        Length of cipher IV, in bytes

.. _`spu2_fmd_ctrl3_write`:

spu2_fmd_ctrl3_write
====================

.. c:function:: void spu2_fmd_ctrl3_write(struct SPU2_FMD *fmd, u64 payload_len)

    Set the ctrl3 field in FMD

    :param struct SPU2_FMD \*fmd:
        Fixed meta data. First field in SPU2 msg header.

    :param u64 payload_len:
        Length of payload, in bytes

.. _`spu2_ctx_max_payload`:

spu2_ctx_max_payload
====================

.. c:function:: u32 spu2_ctx_max_payload(enum spu_cipher_alg cipher_alg, enum spu_cipher_mode cipher_mode, unsigned int blocksize)

    Determine the maximum length of the payload for a SPU message for a given cipher and hash alg context.

    :param enum spu_cipher_alg cipher_alg:
        The cipher algorithm

    :param enum spu_cipher_mode cipher_mode:
        The cipher mode

    :param unsigned int blocksize:
        The size of a block of data for this algo

.. _`spu2_ctx_max_payload.description`:

Description
-----------

For SPU2, the hardware generally ignores the PayloadLen field in ctrl3 of
FMD and just keeps computing until it receives a DMA descriptor with the EOF
flag set. So we consider the max payload to be infinite. AES CCM is an
exception.

.. _`spu2_ctx_max_payload.return`:

Return
------

Max payload length in bytes

.. _`spu2_payload_length`:

spu2_payload_length
===================

.. c:function:: u32 spu2_payload_length(u8 *spu_hdr)

    Given a SPU2 message header, extract the payload length.

    :param u8 \*spu_hdr:
        Start of SPU message header (FMD)

.. _`spu2_payload_length.return`:

Return
------

payload length, in bytes

.. _`spu2_response_hdr_len`:

spu2_response_hdr_len
=====================

.. c:function:: u16 spu2_response_hdr_len(u16 auth_key_len, u16 enc_key_len, bool is_hash)

    Determine the expected length of a SPU response header.

    :param u16 auth_key_len:
        Length of authentication key, in bytes

    :param u16 enc_key_len:
        Length of encryption key, in bytes

    :param bool is_hash:
        *undescribed*

.. _`spu2_response_hdr_len.description`:

Description
-----------

For SPU2, includes just FMD. OMD is never requested.

.. _`spu2_response_hdr_len.return`:

Return
------

Length of FMD, in bytes

.. _`spu2_hash_pad_len`:

spu2_hash_pad_len
=================

.. c:function:: u16 spu2_hash_pad_len(enum hash_alg hash_alg, enum hash_mode hash_mode, u32 chunksize, u16 hash_block_size)

    Calculate the length of hash padding required to extend data to a full block size.

    :param enum hash_alg hash_alg:
        hash algorithm

    :param enum hash_mode hash_mode:
        hash mode

    :param u32 chunksize:
        length of data, in bytes

    :param u16 hash_block_size:
        size of a hash block, in bytes

.. _`spu2_hash_pad_len.description`:

Description
-----------

SPU2 hardware does all hash padding

.. _`spu2_hash_pad_len.return`:

Return
------

length of hash pad in bytes

.. _`spu2_gcm_ccm_pad_len`:

spu2_gcm_ccm_pad_len
====================

.. c:function:: u32 spu2_gcm_ccm_pad_len(enum spu_cipher_mode cipher_mode, unsigned int data_size)

    Determine the length of GCM/CCM padding for either the AAD field or the data.

    :param enum spu_cipher_mode cipher_mode:
        *undescribed*

    :param unsigned int data_size:
        *undescribed*

.. _`spu2_gcm_ccm_pad_len.return`:

Return
------

0. Unlike SPU-M, SPU2 hardware does any GCM/CCM padding required.

.. _`spu2_assoc_resp_len`:

spu2_assoc_resp_len
===================

.. c:function:: u32 spu2_assoc_resp_len(enum spu_cipher_mode cipher_mode, unsigned int assoc_len, unsigned int iv_len, bool is_encrypt)

    Determine the size of the AAD2 buffer needed to catch associated data in a SPU2 output packet.

    :param enum spu_cipher_mode cipher_mode:
        cipher mode

    :param unsigned int assoc_len:
        length of additional associated data, in bytes

    :param unsigned int iv_len:
        length of initialization vector, in bytes

    :param bool is_encrypt:
        true if encrypting. false if decrypt.

.. _`spu2_assoc_resp_len.return`:

Return
------

Length of buffer to catch associated data in response

.. _`spu2_hash_type`:

spu2_hash_type
==============

.. c:function:: enum hash_type spu2_hash_type(u32 src_sent)

    Determine the type of hash operation.

    :param u32 src_sent:
        The number of bytes in the current request that have already
        been sent to the SPU to be hashed.

.. _`spu2_hash_type.description`:

Description
-----------

SPU2 always does a FULL hash operation

.. _`spu2_digest_size`:

spu2_digest_size
================

.. c:function:: u32 spu2_digest_size(u32 alg_digest_size, enum hash_alg alg, enum hash_type htype)

    Determine the size of a hash digest to expect the SPU to return.

    :param u32 alg_digest_size:
        *undescribed*

    :param enum hash_alg alg:
        *undescribed*

    :param enum hash_type htype:
        *undescribed*

.. _`spu2_digest_size.alg_digest_size`:

alg_digest_size
---------------

Number of bytes in the final digest for the given algo

.. _`spu2_digest_size.alg`:

alg
---

The hash algorithm

.. _`spu2_digest_size.htype`:

htype
-----

Type of hash operation (init, update, full, etc)

.. _`spu2_create_request`:

spu2_create_request
===================

.. c:function:: u32 spu2_create_request(u8 *spu_hdr, struct spu_request_opts *req_opts, struct spu_cipher_parms *cipher_parms, struct spu_hash_parms *hash_parms, struct spu_aead_parms *aead_parms, unsigned int data_size)

    Build a SPU2 request message header, includint FMD and OMD.

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

.. _`spu2_create_request.description`:

Description
-----------

Construct the message starting at spu_hdr. Caller should allocate this buffer
in DMA-able memory at least SPU_HEADER_ALLOC_LEN bytes long.

.. _`spu2_create_request.return`:

Return
------

the length of the SPU header in bytes. 0 if an error occurs.

.. _`spu2_cipher_req_init`:

spu2_cipher_req_init
====================

.. c:function:: u16 spu2_cipher_req_init(u8 *spu_hdr, struct spu_cipher_parms *cipher_parms)

    Build an ablkcipher SPU2 request message header, including FMD and OMD.

    :param u8 \*spu_hdr:
        Location of start of SPU request (FMD field)

    :param struct spu_cipher_parms \*cipher_parms:
        Parameters describing cipher request

.. _`spu2_cipher_req_init.description`:

Description
-----------

Called at setkey time to initialize a msg header that can be reused for all
subsequent ablkcipher requests. Construct the message starting at spu_hdr.
Caller should allocate this buffer in DMA-able memory at least
SPU_HEADER_ALLOC_LEN bytes long.

.. _`spu2_cipher_req_init.return`:

Return
------

the total length of the SPU header (FMD and OMD) in bytes. 0 if an
error occurs.

.. _`spu2_cipher_req_finish`:

spu2_cipher_req_finish
======================

.. c:function:: void spu2_cipher_req_finish(u8 *spu_hdr, u16 spu_req_hdr_len, unsigned int is_inbound, struct spu_cipher_parms *cipher_parms, bool update_key, unsigned int data_size)

    Finish building a SPU request message header for a block cipher request.

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

.. _`spu2_cipher_req_finish.description`:

Description
-----------

Assumes much of the header was already filled in at \ :c:func:`setkey`\  time in
\ :c:func:`spu_cipher_req_init`\ .
\ :c:func:`spu_cipher_req_init`\  fills in the encryption key. For RC4, when submitting a
request for a non-first chunk, we use the 260-byte SUPDT field from the
previous response as the key. update_key is true for this case. Unused in all
other cases.

.. _`spu2_request_pad`:

spu2_request_pad
================

.. c:function:: void spu2_request_pad(u8 *pad_start, u32 gcm_padding, u32 hash_pad_len, enum hash_alg auth_alg, enum hash_mode auth_mode, unsigned int total_sent, u32 status_padding)

    Create pad bytes at the end of the data.

    :param u8 \*pad_start:
        Start of buffer where pad bytes are to be written

    :param u32 gcm_padding:
        Length of GCM padding, in bytes

    :param u32 hash_pad_len:
        Number of bytes of padding extend data to full block

    :param enum hash_alg auth_alg:
        Authentication algorithm

    :param enum hash_mode auth_mode:
        Authentication mode

    :param unsigned int total_sent:
        Length inserted at end of hash pad

    :param u32 status_padding:
        Number of bytes of padding to align STATUS word

.. _`spu2_request_pad.there-may-be-three-forms-of-pad`:

There may be three forms of pad
-------------------------------

1. GCM pad - for GCM mode ciphers, pad to 16-byte alignment
2. hash pad - pad to a block length, with 0x80 data terminator and
size at the end
3. STAT pad - to ensure the STAT field is 4-byte aligned

.. _`spu2_xts_tweak_in_payload`:

spu2_xts_tweak_in_payload
=========================

.. c:function:: u8 spu2_xts_tweak_in_payload( void)

    Indicate that SPU2 does NOT place the XTS tweak field in the packet payload (it uses IV instead)

    :param  void:
        no arguments

.. _`spu2_xts_tweak_in_payload.return`:

Return
------

0

.. _`spu2_tx_status_len`:

spu2_tx_status_len
==================

.. c:function:: u8 spu2_tx_status_len( void)

    Return the length of the STATUS field in a SPU response message.

    :param  void:
        no arguments

.. _`spu2_tx_status_len.return`:

Return
------

Length of STATUS field in bytes.

.. _`spu2_rx_status_len`:

spu2_rx_status_len
==================

.. c:function:: u8 spu2_rx_status_len( void)

    Return the length of the STATUS field in a SPU response message.

    :param  void:
        no arguments

.. _`spu2_rx_status_len.return`:

Return
------

Length of STATUS field in bytes.

.. _`spu2_status_process`:

spu2_status_process
===================

.. c:function:: int spu2_status_process(u8 *statp)

    Process the status from a SPU response message.

    :param u8 \*statp:
        start of STATUS word

.. _`spu2_status_process.return`:

Return
------

0 - if status is good and response should be processed
!0 - status indicates an error and response is invalid

.. _`spu2_ccm_update_iv`:

spu2_ccm_update_iv
==================

.. c:function:: void spu2_ccm_update_iv(unsigned int digestsize, struct spu_cipher_parms *cipher_parms, unsigned int assoclen, unsigned int chunksize, bool is_encrypt, bool is_esp)

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

.. _`spu2_wordalign_padlen`:

spu2_wordalign_padlen
=====================

.. c:function:: u32 spu2_wordalign_padlen(u32 data_size)

    SPU2 does not require padding.

    :param u32 data_size:
        length of data field in bytes

.. _`spu2_wordalign_padlen.return`:

Return
------

length of status field padding, in bytes (always 0 on SPU2)

.. This file was automatic generated / don't edit.

