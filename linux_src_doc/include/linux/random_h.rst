.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/random.h

.. _`prandom_u32_max`:

prandom_u32_max
===============

.. c:function:: u32 prandom_u32_max(u32 ep_ro)

    returns a pseudo-random number in interval [0, ep_ro)

    :param u32 ep_ro:
        right open interval endpoint

.. _`prandom_u32_max.description`:

Description
-----------

Returns a pseudo-random number that is in interval [0, ep_ro). Note
that the result depends on PRNG being well distributed in [0, ~0U]
u32 space. Here we use maximally equidistributed combined Tausworthe
generator, that is, \ :c:func:`prandom_u32`\ . This is useful when requesting a
random index of an array containing ep_ro elements, for example.

.. _`prandom_u32_max.return`:

Return
------

pseudo-random number in interval [0, ep_ro)

.. _`prandom_seed_state`:

prandom_seed_state
==================

.. c:function:: void prandom_seed_state(struct rnd_state *state, u64 seed)

    set seed for \ :c:func:`prandom_u32_state`\ .

    :param struct rnd_state \*state:
        pointer to state structure to receive the seed.

    :param u64 seed:
        arbitrary 64-bit value to use as a seed.

.. This file was automatic generated / don't edit.

