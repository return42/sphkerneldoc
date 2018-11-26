.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/internal/scompress.h

.. _`scomp_alg`:

struct scomp_alg
================

.. c:type:: struct scomp_alg

    synchronous compression algorithm

.. _`scomp_alg.definition`:

Definition
----------

.. code-block:: c

    struct scomp_alg {
        void *(*alloc_ctx)(struct crypto_scomp *tfm);
        void (*free_ctx)(struct crypto_scomp *tfm, void *ctx);
        int (*compress)(struct crypto_scomp *tfm, const u8 *src,unsigned int slen, u8 *dst, unsigned int *dlen, void *ctx);
        int (*decompress)(struct crypto_scomp *tfm, const u8 *src,unsigned int slen, u8 *dst, unsigned int *dlen, void *ctx);
        struct crypto_alg base;
    }

.. _`scomp_alg.members`:

Members
-------

alloc_ctx
    Function allocates algorithm specific context

free_ctx
    Function frees context allocated with alloc_ctx

compress
    Function performs a compress operation

decompress
    Function performs a de-compress operation

base
    Common crypto API algorithm data structure

.. _`crypto_register_scomp`:

crypto_register_scomp
=====================

.. c:function:: int crypto_register_scomp(struct scomp_alg *alg)

    - Register synchronous compression algorithm

    :param alg:
        algorithm definition
    :type alg: struct scomp_alg \*

.. _`crypto_register_scomp.description`:

Description
-----------

Function registers an implementation of a synchronous
compression algorithm

.. _`crypto_register_scomp.return`:

Return
------

zero on success; error code in case of error

.. _`crypto_unregister_scomp`:

crypto_unregister_scomp
=======================

.. c:function:: int crypto_unregister_scomp(struct scomp_alg *alg)

    - Unregister synchronous compression algorithm

    :param alg:
        algorithm definition
    :type alg: struct scomp_alg \*

.. _`crypto_unregister_scomp.description`:

Description
-----------

Function unregisters an implementation of a synchronous
compression algorithm

.. _`crypto_unregister_scomp.return`:

Return
------

zero on success; error code in case of error

.. This file was automatic generated / don't edit.

