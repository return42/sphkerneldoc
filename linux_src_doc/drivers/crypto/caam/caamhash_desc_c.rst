.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/caam/caamhash_desc.c

.. _`cnstr_shdsc_ahash`:

cnstr_shdsc_ahash
=================

.. c:function:: void cnstr_shdsc_ahash(u32 * const desc, struct alginfo *adata, u32 state, int digestsize, int ctx_len, bool import_ctx, int era)

    ahash shared descriptor

    :param desc:
        pointer to buffer used for descriptor construction
    :type desc: u32 \* const

    :param adata:
        pointer to authentication transform definitions.
        A split key is required for SEC Era < 6; the size of the split key
        is specified in this case.
        Valid algorithm values - one of OP_ALG_ALGSEL_{MD5, SHA1, SHA224,
        SHA256, SHA384, SHA512}.
    :type adata: struct alginfo \*

    :param state:
        algorithm state OP_ALG_AS_{INIT, FINALIZE, INITFINALIZE, UPDATE}
    :type state: u32

    :param digestsize:
        algorithm's digest size
    :type digestsize: int

    :param ctx_len:
        size of Context Register
    :type ctx_len: int

    :param import_ctx:
        true if previous Context Register needs to be restored
        must be true for ahash update and final
        must be false for for ahash first and digest
    :type import_ctx: bool

    :param era:
        SEC Era
    :type era: int

.. This file was automatic generated / don't edit.

