.. -*- coding: utf-8; mode: rst -*-

==========
random32.c
==========


.. _`prandom_u32_state`:

prandom_u32_state
=================

.. c:function:: u32 prandom_u32_state (struct rnd_state *state)

    seeded pseudo-random number generator.

    :param struct rnd_state \*state:
        pointer to state structure holding seeded state.



.. _`prandom_u32_state.description`:

Description
-----------

This is used for pseudo-randomness with no outside seeding.
For more random results, use :c:func:`prandom_u32`.



.. _`prandom_u32`:

prandom_u32
===========

.. c:function:: u32 prandom_u32 ( void)

    pseudo random number generator

    :param void:
        no arguments



.. _`prandom_u32.description`:

Description
-----------


A 32 bit pseudo-random number is generated using a fast
algorithm suitable for simulation. This algorithm is NOT
considered safe for cryptographic use.



.. _`prandom_bytes_state`:

prandom_bytes_state
===================

.. c:function:: void prandom_bytes_state (struct rnd_state *state, void *buf, size_t bytes)

    get the requested number of pseudo-random bytes

    :param struct rnd_state \*state:
        pointer to state structure holding seeded state.

    :param void \*buf:
        where to copy the pseudo-random bytes to

    :param size_t bytes:
        the requested number of bytes



.. _`prandom_bytes_state.description`:

Description
-----------

This is used for pseudo-randomness with no outside seeding.
For more random results, use :c:func:`prandom_bytes`.



.. _`prandom_bytes`:

prandom_bytes
=============

.. c:function:: void prandom_bytes (void *buf, size_t bytes)

    get the requested number of pseudo-random bytes

    :param void \*buf:
        where to copy the pseudo-random bytes to

    :param size_t bytes:
        the requested number of bytes



.. _`prandom_seed`:

prandom_seed
============

.. c:function:: void prandom_seed (u32 entropy)

    add entropy to pseudo random number generator

    :param u32 entropy:

        *undescribed*



.. _`prandom_seed.description`:

Description
-----------

Add some additional seeding to the prandom pool.

