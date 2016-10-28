.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/rng.h

.. _`rng_alg`:

struct rng_alg
==============

.. c:type:: struct rng_alg

    random number generator definition

.. _`rng_alg.definition`:

Definition
----------

.. code-block:: c

    struct rng_alg {
        int (*generate)(struct crypto_rng *tfm,const u8 *src, unsigned int slen,u8 *dst, unsigned int dlen);
        int (*seed)(struct crypto_rng *tfm, const u8 *seed, unsigned int slen);
        void (*set_ent)(struct crypto_rng *tfm, const u8 *data,unsigned int len);
        unsigned int seedsize;
        struct crypto_alg base;
    }

.. _`rng_alg.members`:

Members
-------

generate
    The function defined by this variable obtains a
    random number. The random number generator transform
    must generate the random number out of the context
    provided with this call, plus any additional data
    if provided to the call.

seed
    Seed or reseed the random number generator.  With the
    invocation of this function call, the random number
    generator shall become ready for generation.  If the
    random number generator requires a seed for setting
    up a new state, the seed must be provided by the
    consumer while invoking this function. The required
    size of the seed is defined with \ ``seedsize``\  .

set_ent
    Set entropy that would otherwise be obtained from
    entropy source.  Internal use only.

seedsize
    The seed size required for a random number generator
    initialization defined with this variable. Some
    random number generators does not require a seed
    as the seeding is implemented internally without
    the need of support by the consumer. In this case,
    the seed size is set to zero.

base
    Common crypto API algorithm data structure.

.. _`crypto_alloc_rng`:

crypto_alloc_rng
================

.. c:function:: struct crypto_rng *crypto_alloc_rng(const char *alg_name, u32 type, u32 mask)

    - allocate RNG handle

    :param const char \*alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        message digest cipher

    :param u32 type:
        specifies the type of the cipher

    :param u32 mask:
        specifies the mask for the cipher

.. _`crypto_alloc_rng.description`:

Description
-----------

Allocate a cipher handle for a random number generator. The returned struct
crypto_rng is the cipher handle that is required for any subsequent
API invocation for that random number generator.

For all random number generators, this call creates a new private copy of
the random number generator that does not share a state with other
instances. The only exception is the "krng" random number generator which
is a kernel crypto API use case for the \ :c:func:`get_random_bytes`\  function of the
/dev/random driver.

.. _`crypto_alloc_rng.return`:

Return
------

allocated cipher handle in case of success; \ :c:func:`IS_ERR`\  is true in case
of an error, \ :c:func:`PTR_ERR`\  returns the error code.

.. _`crypto_rng_alg`:

crypto_rng_alg
==============

.. c:function:: struct rng_alg *crypto_rng_alg(struct crypto_rng *tfm)

    obtain name of RNG

    :param struct crypto_rng \*tfm:
        cipher handle

.. _`crypto_rng_alg.description`:

Description
-----------

Return the generic name (cra_name) of the initialized random number generator

.. _`crypto_rng_alg.return`:

Return
------

generic name string

.. _`crypto_free_rng`:

crypto_free_rng
===============

.. c:function:: void crypto_free_rng(struct crypto_rng *tfm)

    zeroize and free RNG handle

    :param struct crypto_rng \*tfm:
        cipher handle to be freed

.. _`crypto_rng_generate`:

crypto_rng_generate
===================

.. c:function:: int crypto_rng_generate(struct crypto_rng *tfm, const u8 *src, unsigned int slen, u8 *dst, unsigned int dlen)

    get random number

    :param struct crypto_rng \*tfm:
        cipher handle

    :param const u8 \*src:
        Input buffer holding additional data, may be NULL

    :param unsigned int slen:
        Length of additional data

    :param u8 \*dst:
        output buffer holding the random numbers

    :param unsigned int dlen:
        length of the output buffer

.. _`crypto_rng_generate.description`:

Description
-----------

This function fills the caller-allocated buffer with random
numbers using the random number generator referenced by the
cipher handle.

.. _`crypto_rng_generate.return`:

Return
------

0 function was successful; < 0 if an error occurred

.. _`crypto_rng_get_bytes`:

crypto_rng_get_bytes
====================

.. c:function:: int crypto_rng_get_bytes(struct crypto_rng *tfm, u8 *rdata, unsigned int dlen)

    get random number

    :param struct crypto_rng \*tfm:
        cipher handle

    :param u8 \*rdata:
        output buffer holding the random numbers

    :param unsigned int dlen:
        length of the output buffer

.. _`crypto_rng_get_bytes.description`:

Description
-----------

This function fills the caller-allocated buffer with random numbers using the
random number generator referenced by the cipher handle.

.. _`crypto_rng_get_bytes.return`:

Return
------

0 function was successful; < 0 if an error occurred

.. _`crypto_rng_reset`:

crypto_rng_reset
================

.. c:function:: int crypto_rng_reset(struct crypto_rng *tfm, const u8 *seed, unsigned int slen)

    re-initialize the RNG

    :param struct crypto_rng \*tfm:
        cipher handle

    :param const u8 \*seed:
        seed input data

    :param unsigned int slen:
        length of the seed input data

.. _`crypto_rng_reset.description`:

Description
-----------

The reset function completely re-initializes the random number generator
referenced by the cipher handle by clearing the current state. The new state
is initialized with the caller provided seed or automatically, depending
on the random number generator type (the ANSI X9.31 RNG requires
caller-provided seed, the SP800-90A DRBGs perform an automatic seeding).
The seed is provided as a parameter to this function call. The provided seed
should have the length of the seed size defined for the random number
generator as defined by crypto_rng_seedsize.

.. _`crypto_rng_reset.return`:

Return
------

0 if the setting of the key was successful; < 0 if an error occurred

.. _`crypto_rng_seedsize`:

crypto_rng_seedsize
===================

.. c:function:: int crypto_rng_seedsize(struct crypto_rng *tfm)

    obtain seed size of RNG

    :param struct crypto_rng \*tfm:
        cipher handle

.. _`crypto_rng_seedsize.description`:

Description
-----------

The function returns the seed size for the random number generator
referenced by the cipher handle. This value may be zero if the random
number generator does not implement or require a reseeding. For example,
the SP800-90A DRBGs implement an automated reseeding after reaching a
pre-defined threshold.

.. _`crypto_rng_seedsize.return`:

Return
------

seed size for the random number generator

.. This file was automatic generated / don't edit.

