.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/caam/caamalg_desc.c

.. _`cnstr_shdsc_aead_null_encap`:

cnstr_shdsc_aead_null_encap
===========================

.. c:function:: void cnstr_shdsc_aead_null_encap(u32 * const desc, struct alginfo *adata, unsigned int icvsize, int era)

    IPSec ESP encapsulation shared descriptor (non-protocol) with no (null) encryption.

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param adata:
        pointer to authentication transform definitions.
        A split key is required for SEC Era < 6; the size of the split key
        is specified in this case. Valid algorithm values - one of
        OP_ALG_ALGSEL_{MD5, SHA1, SHA224, SHA256, SHA384, SHA512} ANDed
        with OP_ALG_AAI_HMAC_PRECOMP.
    :type adata: struct alginfo \*

    :param icvsize:
        integrity check value (ICV) size (truncated or full)
    :type icvsize: unsigned int

    :param era:
        SEC Era
    :type era: int

.. _`cnstr_shdsc_aead_null_decap`:

cnstr_shdsc_aead_null_decap
===========================

.. c:function:: void cnstr_shdsc_aead_null_decap(u32 * const desc, struct alginfo *adata, unsigned int icvsize, int era)

    IPSec ESP decapsulation shared descriptor (non-protocol) with no (null) decryption.

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param adata:
        pointer to authentication transform definitions.
        A split key is required for SEC Era < 6; the size of the split key
        is specified in this case. Valid algorithm values - one of
        OP_ALG_ALGSEL_{MD5, SHA1, SHA224, SHA256, SHA384, SHA512} ANDed
        with OP_ALG_AAI_HMAC_PRECOMP.
    :type adata: struct alginfo \*

    :param icvsize:
        integrity check value (ICV) size (truncated or full)
    :type icvsize: unsigned int

    :param era:
        SEC Era
    :type era: int

.. _`cnstr_shdsc_aead_encap`:

cnstr_shdsc_aead_encap
======================

.. c:function:: void cnstr_shdsc_aead_encap(u32 * const desc, struct alginfo *cdata, struct alginfo *adata, unsigned int ivsize, unsigned int icvsize, const bool is_rfc3686, u32 *nonce, const u32 ctx1_iv_off, const bool is_qi, int era)

    IPSec ESP encapsulation shared descriptor (non-protocol).

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - one of OP_ALG_ALGSEL_{AES, DES, 3DES} ANDed
        with OP_ALG_AAI_CBC or OP_ALG_AAI_CTR_MOD128.
    :type cdata: struct alginfo \*

    :param adata:
        pointer to authentication transform definitions.
        A split key is required for SEC Era < 6; the size of the split key
        is specified in this case. Valid algorithm values - one of
        OP_ALG_ALGSEL_{MD5, SHA1, SHA224, SHA256, SHA384, SHA512} ANDed
        with OP_ALG_AAI_HMAC_PRECOMP.
    :type adata: struct alginfo \*

    :param ivsize:
        initialization vector size
    :type ivsize: unsigned int

    :param icvsize:
        integrity check value (ICV) size (truncated or full)
    :type icvsize: unsigned int

    :param is_rfc3686:
        true when ctr(aes) is wrapped by rfc3686 template
    :type is_rfc3686: const bool

    :param nonce:
        pointer to rfc3686 nonce
    :type nonce: u32 \*

    :param ctx1_iv_off:
        IV offset in CONTEXT1 register
    :type ctx1_iv_off: const u32

    :param is_qi:
        true when called from caam/qi
    :type is_qi: const bool

    :param era:
        SEC Era
    :type era: int

.. _`cnstr_shdsc_aead_decap`:

cnstr_shdsc_aead_decap
======================

.. c:function:: void cnstr_shdsc_aead_decap(u32 * const desc, struct alginfo *cdata, struct alginfo *adata, unsigned int ivsize, unsigned int icvsize, const bool geniv, const bool is_rfc3686, u32 *nonce, const u32 ctx1_iv_off, const bool is_qi, int era)

    IPSec ESP decapsulation shared descriptor (non-protocol).

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - one of OP_ALG_ALGSEL_{AES, DES, 3DES} ANDed
        with OP_ALG_AAI_CBC or OP_ALG_AAI_CTR_MOD128.
    :type cdata: struct alginfo \*

    :param adata:
        pointer to authentication transform definitions.
        A split key is required for SEC Era < 6; the size of the split key
        is specified in this case. Valid algorithm values - one of
        OP_ALG_ALGSEL_{MD5, SHA1, SHA224, SHA256, SHA384, SHA512} ANDed
        with OP_ALG_AAI_HMAC_PRECOMP.
    :type adata: struct alginfo \*

    :param ivsize:
        initialization vector size
    :type ivsize: unsigned int

    :param icvsize:
        integrity check value (ICV) size (truncated or full)
    :type icvsize: unsigned int

    :param geniv:
        *undescribed*
    :type geniv: const bool

    :param is_rfc3686:
        true when ctr(aes) is wrapped by rfc3686 template
    :type is_rfc3686: const bool

    :param nonce:
        pointer to rfc3686 nonce
    :type nonce: u32 \*

    :param ctx1_iv_off:
        IV offset in CONTEXT1 register
    :type ctx1_iv_off: const u32

    :param is_qi:
        true when called from caam/qi
    :type is_qi: const bool

    :param era:
        SEC Era
    :type era: int

.. _`cnstr_shdsc_aead_givencap`:

cnstr_shdsc_aead_givencap
=========================

.. c:function:: void cnstr_shdsc_aead_givencap(u32 * const desc, struct alginfo *cdata, struct alginfo *adata, unsigned int ivsize, unsigned int icvsize, const bool is_rfc3686, u32 *nonce, const u32 ctx1_iv_off, const bool is_qi, int era)

    IPSec ESP encapsulation shared descriptor (non-protocol) with HW-generated initialization vector.

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - one of OP_ALG_ALGSEL_{AES, DES, 3DES} ANDed
        with OP_ALG_AAI_CBC or OP_ALG_AAI_CTR_MOD128.
    :type cdata: struct alginfo \*

    :param adata:
        pointer to authentication transform definitions.
        A split key is required for SEC Era < 6; the size of the split key
        is specified in this case. Valid algorithm values - one of
        OP_ALG_ALGSEL_{MD5, SHA1, SHA224, SHA256, SHA384, SHA512} ANDed
        with OP_ALG_AAI_HMAC_PRECOMP.
    :type adata: struct alginfo \*

    :param ivsize:
        initialization vector size
    :type ivsize: unsigned int

    :param icvsize:
        integrity check value (ICV) size (truncated or full)
    :type icvsize: unsigned int

    :param is_rfc3686:
        true when ctr(aes) is wrapped by rfc3686 template
    :type is_rfc3686: const bool

    :param nonce:
        pointer to rfc3686 nonce
    :type nonce: u32 \*

    :param ctx1_iv_off:
        IV offset in CONTEXT1 register
    :type ctx1_iv_off: const u32

    :param is_qi:
        true when called from caam/qi
    :type is_qi: const bool

    :param era:
        SEC Era
    :type era: int

.. _`cnstr_shdsc_gcm_encap`:

cnstr_shdsc_gcm_encap
=====================

.. c:function:: void cnstr_shdsc_gcm_encap(u32 * const desc, struct alginfo *cdata, unsigned int ivsize, unsigned int icvsize, const bool is_qi)

    gcm encapsulation shared descriptor

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_GCM.
    :type cdata: struct alginfo \*

    :param ivsize:
        initialization vector size
    :type ivsize: unsigned int

    :param icvsize:
        integrity check value (ICV) size (truncated or full)
    :type icvsize: unsigned int

    :param is_qi:
        true when called from caam/qi
    :type is_qi: const bool

.. _`cnstr_shdsc_gcm_decap`:

cnstr_shdsc_gcm_decap
=====================

.. c:function:: void cnstr_shdsc_gcm_decap(u32 * const desc, struct alginfo *cdata, unsigned int ivsize, unsigned int icvsize, const bool is_qi)

    gcm decapsulation shared descriptor

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_GCM.
    :type cdata: struct alginfo \*

    :param ivsize:
        initialization vector size
    :type ivsize: unsigned int

    :param icvsize:
        integrity check value (ICV) size (truncated or full)
    :type icvsize: unsigned int

    :param is_qi:
        true when called from caam/qi
    :type is_qi: const bool

.. _`cnstr_shdsc_rfc4106_encap`:

cnstr_shdsc_rfc4106_encap
=========================

.. c:function:: void cnstr_shdsc_rfc4106_encap(u32 * const desc, struct alginfo *cdata, unsigned int ivsize, unsigned int icvsize, const bool is_qi)

    IPSec ESP gcm encapsulation shared descriptor (non-protocol).

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_GCM.
    :type cdata: struct alginfo \*

    :param ivsize:
        initialization vector size
    :type ivsize: unsigned int

    :param icvsize:
        integrity check value (ICV) size (truncated or full)
    :type icvsize: unsigned int

    :param is_qi:
        true when called from caam/qi
    :type is_qi: const bool

.. _`cnstr_shdsc_rfc4106_decap`:

cnstr_shdsc_rfc4106_decap
=========================

.. c:function:: void cnstr_shdsc_rfc4106_decap(u32 * const desc, struct alginfo *cdata, unsigned int ivsize, unsigned int icvsize, const bool is_qi)

    IPSec ESP gcm decapsulation shared descriptor (non-protocol).

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_GCM.
    :type cdata: struct alginfo \*

    :param ivsize:
        initialization vector size
    :type ivsize: unsigned int

    :param icvsize:
        integrity check value (ICV) size (truncated or full)
    :type icvsize: unsigned int

    :param is_qi:
        true when called from caam/qi
    :type is_qi: const bool

.. _`cnstr_shdsc_rfc4543_encap`:

cnstr_shdsc_rfc4543_encap
=========================

.. c:function:: void cnstr_shdsc_rfc4543_encap(u32 * const desc, struct alginfo *cdata, unsigned int ivsize, unsigned int icvsize, const bool is_qi)

    IPSec ESP gmac encapsulation shared descriptor (non-protocol).

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_GCM.
    :type cdata: struct alginfo \*

    :param ivsize:
        initialization vector size
    :type ivsize: unsigned int

    :param icvsize:
        integrity check value (ICV) size (truncated or full)
    :type icvsize: unsigned int

    :param is_qi:
        true when called from caam/qi
    :type is_qi: const bool

.. _`cnstr_shdsc_rfc4543_decap`:

cnstr_shdsc_rfc4543_decap
=========================

.. c:function:: void cnstr_shdsc_rfc4543_decap(u32 * const desc, struct alginfo *cdata, unsigned int ivsize, unsigned int icvsize, const bool is_qi)

    IPSec ESP gmac decapsulation shared descriptor (non-protocol).

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_GCM.
    :type cdata: struct alginfo \*

    :param ivsize:
        initialization vector size
    :type ivsize: unsigned int

    :param icvsize:
        integrity check value (ICV) size (truncated or full)
    :type icvsize: unsigned int

    :param is_qi:
        true when called from caam/qi
    :type is_qi: const bool

.. _`cnstr_shdsc_skcipher_encap`:

cnstr_shdsc_skcipher_encap
==========================

.. c:function:: void cnstr_shdsc_skcipher_encap(u32 * const desc, struct alginfo *cdata, unsigned int ivsize, const bool is_rfc3686, const u32 ctx1_iv_off)

    skcipher encapsulation shared descriptor

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - one of OP_ALG_ALGSEL_{AES, DES, 3DES} ANDed
        with OP_ALG_AAI_CBC or OP_ALG_AAI_CTR_MOD128.
    :type cdata: struct alginfo \*

    :param ivsize:
        initialization vector size
    :type ivsize: unsigned int

    :param is_rfc3686:
        true when ctr(aes) is wrapped by rfc3686 template
    :type is_rfc3686: const bool

    :param ctx1_iv_off:
        IV offset in CONTEXT1 register
    :type ctx1_iv_off: const u32

.. _`cnstr_shdsc_skcipher_decap`:

cnstr_shdsc_skcipher_decap
==========================

.. c:function:: void cnstr_shdsc_skcipher_decap(u32 * const desc, struct alginfo *cdata, unsigned int ivsize, const bool is_rfc3686, const u32 ctx1_iv_off)

    skcipher decapsulation shared descriptor

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - one of OP_ALG_ALGSEL_{AES, DES, 3DES} ANDed
        with OP_ALG_AAI_CBC or OP_ALG_AAI_CTR_MOD128.
    :type cdata: struct alginfo \*

    :param ivsize:
        initialization vector size
    :type ivsize: unsigned int

    :param is_rfc3686:
        true when ctr(aes) is wrapped by rfc3686 template
    :type is_rfc3686: const bool

    :param ctx1_iv_off:
        IV offset in CONTEXT1 register
    :type ctx1_iv_off: const u32

.. _`cnstr_shdsc_xts_skcipher_encap`:

cnstr_shdsc_xts_skcipher_encap
==============================

.. c:function:: void cnstr_shdsc_xts_skcipher_encap(u32 * const desc, struct alginfo *cdata)

    xts skcipher encapsulation shared descriptor

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_XTS.
    :type cdata: struct alginfo \*

.. _`cnstr_shdsc_xts_skcipher_decap`:

cnstr_shdsc_xts_skcipher_decap
==============================

.. c:function:: void cnstr_shdsc_xts_skcipher_decap(u32 * const desc, struct alginfo *cdata)

    xts skcipher decapsulation shared descriptor

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_XTS.
    :type cdata: struct alginfo \*

.. This file was automatic generated / don't edit.

