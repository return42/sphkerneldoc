
.. _API-struct-rng-alg:

==============
struct rng_alg
==============

*man struct rng_alg(9)*

*4.6.0-rc1*

random number generator definition


Synopsis
========

.. code-block:: c

    struct rng_alg {
      int (* generate) (struct crypto_rng *tfm,const u8 *src, unsigned int slen,u8 *dst, unsigned int dlen);
      int (* seed) (struct crypto_rng *tfm, const u8 *seed, unsigned int slen);
      void (* set_ent) (struct crypto_rng *tfm, const u8 *data,unsigned int len);
      unsigned int seedsize;
      struct crypto_alg base;
    };


Members
=======

generate
    The function defined by this variable obtains a random number. The random number generator transform must generate the random number out of the context provided with this call,
    plus any additional data if provided to the call.

seed
    Seed or reseed the random number generator. With the invocation of this function call, the random number generator shall become ready for generation. If the random number
    generator requires a seed for setting up a new state, the seed must be provided by the consumer while invoking this function. The required size of the seed is defined with
    ``seedsize`` .

set_ent
    Set entropy that would otherwise be obtained from entropy source. Internal use only.

seedsize
    The seed size required for a random number generator initialization defined with this variable. Some random number generators does not require a seed as the seeding is
    implemented internally without the need of support by the consumer. In this case, the seed size is set to zero.

base
    Common crypto API algorithm data structure.
