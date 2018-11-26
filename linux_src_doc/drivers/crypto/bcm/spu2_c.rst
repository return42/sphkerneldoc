.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/bcm/spu2.c

.. _`spu2_cipher_xlate`:

spu2_cipher_xlate
=================

.. c:function:: int spu2_cipher_xlate(enum spu_cipher_alg cipher_alg, enum spu_cipher_mode cipher_mode, enum spu_cipher_type cipher_type, enum spu2_cipher_type *spu2_type, enum spu2_cipher_mode *spu2_mode)

    Convert a cipher {alg/mode/type} triple to a SPU2 cipher type and mode.

    :param cipher_alg:
        [in]  cipher algorithm value from software enumeration
    :type cipher_alg: enum spu_cipher_alg

    :param cipher_mode:
        [in]  cipher mode value from software enumeration
    :type cipher_mode: enum spu_cipher_mode

    :param cipher_type:
        [in]  cipher type value from software enumeration
    :type cipher_type: enum spu_cipher_type

    :param spu2_type:
        [out] cipher type value used by spu2 hardware
    :type spu2_type: enum spu2_cipher_type \*

    :param spu2_mode:
        [out] cipher mode value used by spu2 hardware
    :type spu2_mode: enum spu2_cipher_mode \*

.. _`spu2_cipher_xlate.return`:

Return
------

0 if successful

.. _`spu2_hash_xlate`:

spu2_hash_xlate
===============

.. c:function:: int spu2_hash_xlate(enum hash_alg hash_alg, enum hash_mode hash_mode, enum hash_type hash_type, enum spu_cipher_type ciph_type, enum spu2_hash_type *spu2_type, enum spu2_hash_mode *spu2_mode)

    Convert a hash {alg/mode/type} triple to a SPU2 hash type and mode.

    :param hash_alg:
        [in] hash algorithm value from software enumeration
    :type hash_alg: enum hash_alg

    :param hash_mode:
        [in] hash mode value from software enumeration
    :type hash_mode: enum hash_mode

    :param hash_type:
        [in] hash type value from software enumeration
    :type hash_type: enum hash_type

    :param ciph_type:
        [in] cipher type value from software enumeration
    :type ciph_type: enum spu_cipher_type

    :param spu2_type:
        [out] hash type value used by SPU2 hardware
    :type spu2_type: enum spu2_hash_type \*

    :param spu2_mode:
        [out] hash mode value used by SPU2 hardware
    :type spu2_mode: enum spu2_hash_mode \*

.. _`spu2_hash_xlate.return`:

Return
------

0 if successful

.. _`spu2_fmd_init`:

spu2_fmd_init
=============

.. c:function:: int spu2_fmd_init(struct SPU2_FMD *fmd, enum spu2_cipher_type spu2_type, enum spu2_cipher_mode spu2_mode, u32 cipher_key_len, u32 cipher_iv_len)

    At setkey time, initialize the fixed meta data for subsequent ablkcipher requests for this context.

    :param fmd:
        *undescribed*
    :type fmd: struct SPU2_FMD \*

    :param spu2_type:
        *undescribed*
    :type spu2_type: enum spu2_cipher_type

    :param spu2_mode:
        Cipher mode
    :type spu2_mode: enum spu2_cipher_mode

    :param cipher_key_len:
        Length of cipher key, in bytes
    :type cipher_key_len: u32

    :param cipher_iv_len:
        Length of cipher initialization vector, in bytes
    :type cipher_iv_len: u32

.. _`spu2_fmd_init.return`:

Return
------

0 (success)

.. _`spu2_fmd_ctrl0_write`:

spu2_fmd_ctrl0_write
====================

.. c:function:: void spu2_fmd_ctrl0_write(struct SPU2_FMD *fmd, bool is_inbound, bool auth_first, enum spu2_proto_sel protocol, enum spu2_cipher_type cipher_type, enum spu2_cipher_mode cipher_mode, enum spu2_hash_type auth_type, enum spu2_hash_mode auth_mode)

    Write ctrl0 field in fixed metadata (FMD) field of SPU request packet.

    :param fmd:
        Start of FMD field to be written
    :type fmd: struct SPU2_FMD \*

    :param is_inbound:
        true if decrypting. false if encrypting.
    :type is_inbound: bool

    :param auth_first:
        *undescribed*
    :type auth_first: bool

    :param protocol:
        protocol selector
    :type protocol: enum spu2_proto_sel

    :param cipher_type:
        cipher algorithm
    :type cipher_type: enum spu2_cipher_type

    :param cipher_mode:
        cipher mode
    :type cipher_mode: enum spu2_cipher_mode

    :param auth_type:
        authentication type
    :type auth_type: enum spu2_hash_type

    :param auth_mode:
        authentication mode
    :type auth_mode: enum spu2_hash_mode

.. _`spu2_fmd_ctrl1_write`:

spu2_fmd_ctrl1_write
====================

.. c:function:: void spu2_fmd_ctrl1_write(struct SPU2_FMD *fmd, bool is_inbound, u64 assoc_size, u64 auth_key_len, u64 cipher_key_len, bool gen_iv, bool hash_iv, bool return_iv, u64 ret_iv_len, u64 ret_iv_offset, u64 cipher_iv_len, u64 digest_size, bool return_payload, bool return_md)

    Write ctrl1 field in fixed metadata (FMD) field of SPU request packet.

    :param fmd:
        Start of FMD field to be written
    :type fmd: struct SPU2_FMD \*

    :param is_inbound:
        *undescribed*
    :type is_inbound: bool

    :param assoc_size:
        Length of additional associated data, in bytes
    :type assoc_size: u64

    :param auth_key_len:
        Length of authentication key, in bytes
    :type auth_key_len: u64

    :param cipher_key_len:
        Length of cipher key, in bytes
    :type cipher_key_len: u64

    :param gen_iv:
        If true, hw generates IV and returns in response
    :type gen_iv: bool

    :param hash_iv:
        IV participates in hash. Used for IPSEC and TLS.
    :type hash_iv: bool

    :param return_iv:
        Return IV in output packet before payload
    :type return_iv: bool

    :param ret_iv_len:
        Length of IV returned from SPU, in bytes
    :type ret_iv_len: u64

    :param ret_iv_offset:
        Offset into full IV of start of returned IV
    :type ret_iv_offset: u64

    :param cipher_iv_len:
        Length of input cipher IV, in bytes
    :type cipher_iv_len: u64

    :param digest_size:
        Length of digest (aka, hash tag or ICV), in bytes
    :type digest_size: u64

    :param return_payload:
        Return payload in SPU response
    :type return_payload: bool

    :param return_md:
        return metadata in SPU response
    :type return_md: bool

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

    :param fmd:
        Start of FMD field to be written
    :type fmd: struct SPU2_FMD \*

    :param cipher_offset:
        Number of bytes from Start of Packet (end of FD field) where
        data to be encrypted or decrypted begins
    :type cipher_offset: u64

    :param auth_key_len:
        Length of authentication key, in bytes
    :type auth_key_len: u64

    :param auth_iv_len:
        Length of authentication initialization vector, in bytes
    :type auth_iv_len: u64

    :param cipher_key_len:
        Length of cipher key, in bytes
    :type cipher_key_len: u64

    :param cipher_iv_len:
        Length of cipher IV, in bytes
    :type cipher_iv_len: u64

.. _`spu2_fmd_ctrl3_write`:

spu2_fmd_ctrl3_write
====================

.. c:function:: void spu2_fmd_ctrl3_write(struct SPU2_FMD *fmd, u64 payload_len)

    Set the ctrl3 field in FMD

    :param fmd:
        Fixed meta data. First field in SPU2 msg header.
    :type fmd: struct SPU2_FMD \*

    :param payload_len:
        Length of payload, in bytes
    :type payload_len: u64

.. _`spu2_ctx_max_payload`:

spu2_ctx_max_payload
====================

.. c:function:: u32 spu2_ctx_max_payload(enum spu_cipher_alg cipher_alg, enum spu_cipher_mode cipher_mode, unsigned int blocksize)

    Determine the maximum length of the payload for a SPU message for a given cipher and hash alg context.

    :param cipher_alg:
        The cipher algorithm
    :type cipher_alg: enum spu_cipher_alg

    :param cipher_mode:
        The cipher mode
    :type cipher_mode: enum spu_cipher_mode

    :param blocksize:
        The size of a block of data for this algo
    :type blocksize: unsigned int

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

    :param spu_hdr:
        Start of SPU message header (FMD)
    :type spu_hdr: u8 \*

.. _`spu2_payload_length.return`:

Return
------

payload length, in bytes

.. _`spu2_response_hdr_len`:

spu2_response_hdr_len
=====================

.. c:function:: u16 spu2_response_hdr_len(u16 auth_key_len, u16 enc_key_len, bool is_hash)

    Determine the expected length of a SPU response header.

    :param auth_key_len:
        Length of authentication key, in bytes
    :type auth_key_len: u16

    :param enc_key_len:
        Length of encryption key, in bytes
    :type enc_key_len: u16

    :param is_hash:
        *undescribed*
    :type is_hash: bool

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

    :param hash_alg:
        hash algorithm
    :type hash_alg: enum hash_alg

    :param hash_mode:
        hash mode
    :type hash_mode: enum hash_mode

    :param chunksize:
        length of data, in bytes
    :type chunksize: u32

    :param hash_block_size:
        size of a hash block, in bytes
    :type hash_block_size: u16

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

    :param cipher_mode:
        *undescribed*
    :type cipher_mode: enum spu_cipher_mode

    :param data_size:
        *undescribed*
    :type data_size: unsigned int

.. _`spu2_gcm_ccm_pad_len.return`:

Return
------

0. Unlike SPU-M, SPU2 hardware does any GCM/CCM padding required.

.. _`spu2_assoc_resp_len`:

spu2_assoc_resp_len
===================

.. c:function:: u32 spu2_assoc_resp_len(enum spu_cipher_mode cipher_mode, unsigned int assoc_len, unsigned int iv_len, bool is_encrypt)

    Determine the size of the AAD2 buffer needed to catch associated data in a SPU2 output packet.

    :param cipher_mode:
        cipher mode
    :type cipher_mode: enum spu_cipher_mode

    :param assoc_len:
        length of additional associated data, in bytes
    :type assoc_len: unsigned int

    :param iv_len:
        length of initialization vector, in bytes
    :type iv_len: unsigned int

    :param is_encrypt:
        true if encrypting. false if decrypt.
    :type is_encrypt: bool

.. _`spu2_assoc_resp_len.return`:

Return
------

Length of buffer to catch associated data in response

.. _`spu2_hash_type`:

spu2_hash_type
==============

.. c:function:: enum hash_type spu2_hash_type(u32 src_sent)

    Determine the type of hash operation.

    :param src_sent:
        The number of bytes in the current request that have already
        been sent to the SPU to be hashed.
    :type src_sent: u32

.. _`spu2_hash_type.description`:

Description
-----------

SPU2 always does a FULL hash operation

.. _`spu2_digest_size`:

spu2_digest_size
================

.. c:function:: u32 spu2_digest_size(u32 alg_digest_size, enum hash_alg alg, enum hash_type htype)

    Determine the size of a hash digest to expect the SPU to return.

    :param alg_digest_size:
        *undescribed*
    :type alg_digest_size: u32

    :param alg:
        *undescribed*
    :type alg: enum hash_alg

    :param htype:
        *undescribed*
    :type htype: enum hash_type

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

    :param spu_hdr:
        Start of buffer where SPU request header is to be written
    :type spu_hdr: u8 \*

    :param req_opts:
        SPU request message options
    :type req_opts: struct spu_request_opts \*

    :param cipher_parms:
        Parameters related to cipher algorithm
    :type cipher_parms: struct spu_cipher_parms \*

    :param hash_parms:
        Parameters related to hash algorithm
    :type hash_parms: struct spu_hash_parms \*

    :param aead_parms:
        Parameters related to AEAD operation
    :type aead_parms: struct spu_aead_parms \*

    :param data_size:
        Length of data to be encrypted or authenticated. If AEAD, does
        not include length of AAD.
    :type data_size: unsigned int

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

    :param spu_hdr:
        Location of start of SPU request (FMD field)
    :type spu_hdr: u8 \*

    :param cipher_parms:
        Parameters describing cipher request
    :type cipher_parms: struct spu_cipher_parms \*

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

    :param spu_hdr:
        Start of the request message header (MH field)
    :type spu_hdr: u8 \*

    :param spu_req_hdr_len:
        Length in bytes of the SPU request header
    :type spu_req_hdr_len: u16

    :param is_inbound:
        *undescribed*
    :type is_inbound: unsigned int

    :param cipher_parms:
        Parameters describing cipher operation to be performed
    :type cipher_parms: struct spu_cipher_parms \*

    :param update_key:
        If true, rewrite the cipher key in SCTX
    :type update_key: bool

    :param data_size:
        Length of the data in the BD field
    :type data_size: unsigned int

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

    :param pad_start:
        Start of buffer where pad bytes are to be written
    :type pad_start: u8 \*

    :param gcm_padding:
        Length of GCM padding, in bytes
    :type gcm_padding: u32

    :param hash_pad_len:
        Number of bytes of padding extend data to full block
    :type hash_pad_len: u32

    :param auth_alg:
        Authentication algorithm
    :type auth_alg: enum hash_alg

    :param auth_mode:
        Authentication mode
    :type auth_mode: enum hash_mode

    :param total_sent:
        Length inserted at end of hash pad
    :type total_sent: unsigned int

    :param status_padding:
        Number of bytes of padding to align STATUS word
    :type status_padding: u32

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

    :param void:
        no arguments
    :type void: 

.. _`spu2_xts_tweak_in_payload.return`:

Return
------

0

.. _`spu2_tx_status_len`:

spu2_tx_status_len
==================

.. c:function:: u8 spu2_tx_status_len( void)

    Return the length of the STATUS field in a SPU response message.

    :param void:
        no arguments
    :type void: 

.. _`spu2_tx_status_len.return`:

Return
------

Length of STATUS field in bytes.

.. _`spu2_rx_status_len`:

spu2_rx_status_len
==================

.. c:function:: u8 spu2_rx_status_len( void)

    Return the length of the STATUS field in a SPU response message.

    :param void:
        no arguments
    :type void: 

.. _`spu2_rx_status_len.return`:

Return
------

Length of STATUS field in bytes.

.. _`spu2_status_process`:

spu2_status_process
===================

.. c:function:: int spu2_status_process(u8 *statp)

    Process the status from a SPU response message.

    :param statp:
        start of STATUS word
    :type statp: u8 \*

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

    :param digestsize:
        Digest size of this request
    :type digestsize: unsigned int

    :param cipher_parms:
        (pointer to) cipher parmaeters, includes IV buf & IV len
    :type cipher_parms: struct spu_cipher_parms \*

    :param assoclen:
        Length of AAD data
    :type assoclen: unsigned int

    :param chunksize:
        length of input data to be sent in this req
    :type chunksize: unsigned int

    :param is_encrypt:
        true if this is an output/encrypt operation
    :type is_encrypt: bool

    :param is_esp:
        true if this is an ESP / RFC4309 operation
    :type is_esp: bool

.. _`spu2_wordalign_padlen`:

spu2_wordalign_padlen
=====================

.. c:function:: u32 spu2_wordalign_padlen(u32 data_size)

    SPU2 does not require padding.

    :param data_size:
        length of data field in bytes
    :type data_size: u32

.. _`spu2_wordalign_padlen.return`:

Return
------

length of status field padding, in bytes (always 0 on SPU2)

.. This file was automatic generated / don't edit.

