.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/caam/caamalg_desc.c

.. _`cnstr_shdsc_aead_null_encap`:

cnstr_shdsc_aead_null_encap
===========================

.. c:function:: void cnstr_shdsc_aead_null_encap(u32 * const desc, struct alginfo *adata, unsigned int icvsize)

    IPSec ESP encapsulation shared descriptor (non-protocol) with no (null) encryption.

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*adata:
        pointer to authentication transform definitions. Note that since a
        split key is to be used, the size of the split key itself is
        specified. Valid algorithm values - one of OP_ALG_ALGSEL_{MD5, SHA1,
        SHA224, SHA256, SHA384, SHA512} ANDed with OP_ALG_AAI_HMAC_PRECOMP.

    :param unsigned int icvsize:
        integrity check value (ICV) size (truncated or full)

.. _`cnstr_shdsc_aead_null_encap.note`:

Note
----

Requires an MDHA split key.

.. _`cnstr_shdsc_aead_null_decap`:

cnstr_shdsc_aead_null_decap
===========================

.. c:function:: void cnstr_shdsc_aead_null_decap(u32 * const desc, struct alginfo *adata, unsigned int icvsize)

    IPSec ESP decapsulation shared descriptor (non-protocol) with no (null) decryption.

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*adata:
        pointer to authentication transform definitions. Note that since a
        split key is to be used, the size of the split key itself is
        specified. Valid algorithm values - one of OP_ALG_ALGSEL_{MD5, SHA1,
        SHA224, SHA256, SHA384, SHA512} ANDed with OP_ALG_AAI_HMAC_PRECOMP.

    :param unsigned int icvsize:
        integrity check value (ICV) size (truncated or full)

.. _`cnstr_shdsc_aead_null_decap.note`:

Note
----

Requires an MDHA split key.

.. _`cnstr_shdsc_aead_encap`:

cnstr_shdsc_aead_encap
======================

.. c:function:: void cnstr_shdsc_aead_encap(u32 * const desc, struct alginfo *cdata, struct alginfo *adata, unsigned int ivsize, unsigned int icvsize, const bool is_rfc3686, u32 *nonce, const u32 ctx1_iv_off, const bool is_qi)

    IPSec ESP encapsulation shared descriptor (non-protocol).

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - one of OP_ALG_ALGSEL_{AES, DES, 3DES} ANDed
        with OP_ALG_AAI_CBC or OP_ALG_AAI_CTR_MOD128.

    :param struct alginfo \*adata:
        pointer to authentication transform definitions. Note that since a
        split key is to be used, the size of the split key itself is
        specified. Valid algorithm values - one of OP_ALG_ALGSEL_{MD5, SHA1,
        SHA224, SHA256, SHA384, SHA512} ANDed with OP_ALG_AAI_HMAC_PRECOMP.

    :param unsigned int ivsize:
        initialization vector size

    :param unsigned int icvsize:
        integrity check value (ICV) size (truncated or full)

    :param const bool is_rfc3686:
        true when ctr(aes) is wrapped by rfc3686 template

    :param u32 \*nonce:
        pointer to rfc3686 nonce

    :param const u32 ctx1_iv_off:
        IV offset in CONTEXT1 register

    :param const bool is_qi:
        true when called from caam/qi

.. _`cnstr_shdsc_aead_encap.note`:

Note
----

Requires an MDHA split key.

.. _`cnstr_shdsc_aead_decap`:

cnstr_shdsc_aead_decap
======================

.. c:function:: void cnstr_shdsc_aead_decap(u32 * const desc, struct alginfo *cdata, struct alginfo *adata, unsigned int ivsize, unsigned int icvsize, const bool geniv, const bool is_rfc3686, u32 *nonce, const u32 ctx1_iv_off, const bool is_qi)

    IPSec ESP decapsulation shared descriptor (non-protocol).

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - one of OP_ALG_ALGSEL_{AES, DES, 3DES} ANDed
        with OP_ALG_AAI_CBC or OP_ALG_AAI_CTR_MOD128.

    :param struct alginfo \*adata:
        pointer to authentication transform definitions. Note that since a
        split key is to be used, the size of the split key itself is
        specified. Valid algorithm values - one of OP_ALG_ALGSEL_{MD5, SHA1,
        SHA224, SHA256, SHA384, SHA512} ANDed with OP_ALG_AAI_HMAC_PRECOMP.

    :param unsigned int ivsize:
        initialization vector size

    :param unsigned int icvsize:
        integrity check value (ICV) size (truncated or full)

    :param const bool geniv:
        *undescribed*

    :param const bool is_rfc3686:
        true when ctr(aes) is wrapped by rfc3686 template

    :param u32 \*nonce:
        pointer to rfc3686 nonce

    :param const u32 ctx1_iv_off:
        IV offset in CONTEXT1 register

    :param const bool is_qi:
        true when called from caam/qi

.. _`cnstr_shdsc_aead_decap.note`:

Note
----

Requires an MDHA split key.

.. _`cnstr_shdsc_aead_givencap`:

cnstr_shdsc_aead_givencap
=========================

.. c:function:: void cnstr_shdsc_aead_givencap(u32 * const desc, struct alginfo *cdata, struct alginfo *adata, unsigned int ivsize, unsigned int icvsize, const bool is_rfc3686, u32 *nonce, const u32 ctx1_iv_off, const bool is_qi)

    IPSec ESP encapsulation shared descriptor (non-protocol) with HW-generated initialization vector.

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - one of OP_ALG_ALGSEL_{AES, DES, 3DES} ANDed
        with OP_ALG_AAI_CBC or OP_ALG_AAI_CTR_MOD128.

    :param struct alginfo \*adata:
        pointer to authentication transform definitions. Note that since a
        split key is to be used, the size of the split key itself is
        specified. Valid algorithm values - one of OP_ALG_ALGSEL_{MD5, SHA1,
        SHA224, SHA256, SHA384, SHA512} ANDed with OP_ALG_AAI_HMAC_PRECOMP.

    :param unsigned int ivsize:
        initialization vector size

    :param unsigned int icvsize:
        integrity check value (ICV) size (truncated or full)

    :param const bool is_rfc3686:
        true when ctr(aes) is wrapped by rfc3686 template

    :param u32 \*nonce:
        pointer to rfc3686 nonce

    :param const u32 ctx1_iv_off:
        IV offset in CONTEXT1 register

    :param const bool is_qi:
        true when called from caam/qi

.. _`cnstr_shdsc_aead_givencap.note`:

Note
----

Requires an MDHA split key.

.. _`cnstr_shdsc_gcm_encap`:

cnstr_shdsc_gcm_encap
=====================

.. c:function:: void cnstr_shdsc_gcm_encap(u32 * const desc, struct alginfo *cdata, unsigned int icvsize)

    gcm encapsulation shared descriptor

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_GCM.

    :param unsigned int icvsize:
        integrity check value (ICV) size (truncated or full)

.. _`cnstr_shdsc_gcm_decap`:

cnstr_shdsc_gcm_decap
=====================

.. c:function:: void cnstr_shdsc_gcm_decap(u32 * const desc, struct alginfo *cdata, unsigned int icvsize)

    gcm decapsulation shared descriptor

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_GCM.

    :param unsigned int icvsize:
        integrity check value (ICV) size (truncated or full)

.. _`cnstr_shdsc_rfc4106_encap`:

cnstr_shdsc_rfc4106_encap
=========================

.. c:function:: void cnstr_shdsc_rfc4106_encap(u32 * const desc, struct alginfo *cdata, unsigned int icvsize)

    IPSec ESP gcm encapsulation shared descriptor (non-protocol).

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_GCM.

    :param unsigned int icvsize:
        integrity check value (ICV) size (truncated or full)

.. _`cnstr_shdsc_rfc4106_decap`:

cnstr_shdsc_rfc4106_decap
=========================

.. c:function:: void cnstr_shdsc_rfc4106_decap(u32 * const desc, struct alginfo *cdata, unsigned int icvsize)

    IPSec ESP gcm decapsulation shared descriptor (non-protocol).

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_GCM.

    :param unsigned int icvsize:
        integrity check value (ICV) size (truncated or full)

.. _`cnstr_shdsc_rfc4543_encap`:

cnstr_shdsc_rfc4543_encap
=========================

.. c:function:: void cnstr_shdsc_rfc4543_encap(u32 * const desc, struct alginfo *cdata, unsigned int icvsize)

    IPSec ESP gmac encapsulation shared descriptor (non-protocol).

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_GCM.

    :param unsigned int icvsize:
        integrity check value (ICV) size (truncated or full)

.. _`cnstr_shdsc_rfc4543_decap`:

cnstr_shdsc_rfc4543_decap
=========================

.. c:function:: void cnstr_shdsc_rfc4543_decap(u32 * const desc, struct alginfo *cdata, unsigned int icvsize)

    IPSec ESP gmac decapsulation shared descriptor (non-protocol).

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_GCM.

    :param unsigned int icvsize:
        integrity check value (ICV) size (truncated or full)

.. _`cnstr_shdsc_ablkcipher_encap`:

cnstr_shdsc_ablkcipher_encap
============================

.. c:function:: void cnstr_shdsc_ablkcipher_encap(u32 * const desc, struct alginfo *cdata, unsigned int ivsize, const bool is_rfc3686, const u32 ctx1_iv_off)

    ablkcipher encapsulation shared descriptor

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - one of OP_ALG_ALGSEL_{AES, DES, 3DES} ANDed
        with OP_ALG_AAI_CBC or OP_ALG_AAI_CTR_MOD128.

    :param unsigned int ivsize:
        initialization vector size

    :param const bool is_rfc3686:
        true when ctr(aes) is wrapped by rfc3686 template

    :param const u32 ctx1_iv_off:
        IV offset in CONTEXT1 register

.. _`cnstr_shdsc_ablkcipher_decap`:

cnstr_shdsc_ablkcipher_decap
============================

.. c:function:: void cnstr_shdsc_ablkcipher_decap(u32 * const desc, struct alginfo *cdata, unsigned int ivsize, const bool is_rfc3686, const u32 ctx1_iv_off)

    ablkcipher decapsulation shared descriptor

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - one of OP_ALG_ALGSEL_{AES, DES, 3DES} ANDed
        with OP_ALG_AAI_CBC or OP_ALG_AAI_CTR_MOD128.

    :param unsigned int ivsize:
        initialization vector size

    :param const bool is_rfc3686:
        true when ctr(aes) is wrapped by rfc3686 template

    :param const u32 ctx1_iv_off:
        IV offset in CONTEXT1 register

.. _`cnstr_shdsc_ablkcipher_givencap`:

cnstr_shdsc_ablkcipher_givencap
===============================

.. c:function:: void cnstr_shdsc_ablkcipher_givencap(u32 * const desc, struct alginfo *cdata, unsigned int ivsize, const bool is_rfc3686, const u32 ctx1_iv_off)

    ablkcipher encapsulation shared descriptor with HW-generated initialization vector.

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - one of OP_ALG_ALGSEL_{AES, DES, 3DES} ANDed
        with OP_ALG_AAI_CBC.

    :param unsigned int ivsize:
        initialization vector size

    :param const bool is_rfc3686:
        true when ctr(aes) is wrapped by rfc3686 template

    :param const u32 ctx1_iv_off:
        IV offset in CONTEXT1 register

.. _`cnstr_shdsc_xts_ablkcipher_encap`:

cnstr_shdsc_xts_ablkcipher_encap
================================

.. c:function:: void cnstr_shdsc_xts_ablkcipher_encap(u32 * const desc, struct alginfo *cdata)

    xts ablkcipher encapsulation shared descriptor

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_XTS.

.. _`cnstr_shdsc_xts_ablkcipher_decap`:

cnstr_shdsc_xts_ablkcipher_decap
================================

.. c:function:: void cnstr_shdsc_xts_ablkcipher_decap(u32 * const desc, struct alginfo *cdata)

    xts ablkcipher decapsulation shared descriptor

    :param u32 \* const desc:
        pointer to buffer used for descriptor construction

    :param struct alginfo \*cdata:
        pointer to block cipher transform definitions
        Valid algorithm values - OP_ALG_ALGSEL_AES ANDed with OP_ALG_AAI_XTS.

.. This file was automatic generated / don't edit.

