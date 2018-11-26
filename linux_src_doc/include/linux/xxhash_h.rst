.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/xxhash.h

.. _`xxh32`:

xxh32
=====

.. c:function:: uint32_t xxh32(const void *input, size_t length, uint32_t seed)

    calculate the 32-bit hash of the input with a given seed.

    :param input:
        The data to hash.
    :type input: const void \*

    :param length:
        The length of the data to hash.
    :type length: size_t

    :param seed:
        The seed can be used to alter the result predictably.
    :type seed: uint32_t

.. _`xxh32.description`:

Description
-----------

Speed on Core 2 Duo \ ````\  3 GHz (single thread, SMHasher benchmark) : 5.4 GB/s

.. _`xxh32.return`:

Return
------

The 32-bit hash of the data.

.. _`xxh64`:

xxh64
=====

.. c:function:: uint64_t xxh64(const void *input, size_t length, uint64_t seed)

    calculate the 64-bit hash of the input with a given seed.

    :param input:
        The data to hash.
    :type input: const void \*

    :param length:
        The length of the data to hash.
    :type length: size_t

    :param seed:
        The seed can be used to alter the result predictably.
    :type seed: uint64_t

.. _`xxh64.description`:

Description
-----------

This function runs 2x faster on 64-bit systems, but slower on 32-bit systems.

.. _`xxh64.return`:

Return
------

The 64-bit hash of the data.

.. _`xxh32_state`:

struct xxh32_state
==================

.. c:type:: struct xxh32_state

    private xxh32 state, do not use members directly

.. _`xxh32_state.definition`:

Definition
----------

.. code-block:: c

    struct xxh32_state {
        uint32_t total_len_32;
        uint32_t large_len;
        uint32_t v1;
        uint32_t v2;
        uint32_t v3;
        uint32_t v4;
        uint32_t mem32[4];
        uint32_t memsize;
    }

.. _`xxh32_state.members`:

Members
-------

total_len_32
    *undescribed*

large_len
    *undescribed*

v1
    *undescribed*

v2
    *undescribed*

v3
    *undescribed*

v4
    *undescribed*

mem32
    *undescribed*

memsize
    *undescribed*

.. _`xxh64_state`:

struct xxh64_state
==================

.. c:type:: struct xxh64_state

    private xxh64 state, do not use members directly

.. _`xxh64_state.definition`:

Definition
----------

.. code-block:: c

    struct xxh64_state {
        uint64_t total_len;
        uint64_t v1;
        uint64_t v2;
        uint64_t v3;
        uint64_t v4;
        uint64_t mem64[4];
        uint32_t memsize;
    }

.. _`xxh64_state.members`:

Members
-------

total_len
    *undescribed*

v1
    *undescribed*

v2
    *undescribed*

v3
    *undescribed*

v4
    *undescribed*

mem64
    *undescribed*

memsize
    *undescribed*

.. _`xxh32_reset`:

xxh32_reset
===========

.. c:function:: void xxh32_reset(struct xxh32_state *state, uint32_t seed)

    reset the xxh32 state to start a new hashing operation

    :param state:
        The xxh32 state to reset.
    :type state: struct xxh32_state \*

    :param seed:
        Initialize the hash state with this seed.
    :type seed: uint32_t

.. _`xxh32_reset.description`:

Description
-----------

Call this function on any xxh32_state to prepare for a new hashing operation.

.. _`xxh32_update`:

xxh32_update
============

.. c:function:: int xxh32_update(struct xxh32_state *state, const void *input, size_t length)

    hash the data given and update the xxh32 state

    :param state:
        The xxh32 state to update.
    :type state: struct xxh32_state \*

    :param input:
        The data to hash.
    :type input: const void \*

    :param length:
        The length of the data to hash.
    :type length: size_t

.. _`xxh32_update.description`:

Description
-----------

After calling \ :c:func:`xxh32_reset`\  call \ :c:func:`xxh32_update`\  as many times as necessary.

.. _`xxh32_update.return`:

Return
------

Zero on success, otherwise an error code.

.. _`xxh32_digest`:

xxh32_digest
============

.. c:function:: uint32_t xxh32_digest(const struct xxh32_state *state)

    produce the current xxh32 hash

    :param state:
        Produce the current xxh32 hash of this state.
    :type state: const struct xxh32_state \*

.. _`xxh32_digest.description`:

Description
-----------

A hash value can be produced at any time. It is still possible to continue
inserting input into the hash state after a call to \ :c:func:`xxh32_digest`\ , and
generate new hashes later on, by calling \ :c:func:`xxh32_digest`\  again.

.. _`xxh32_digest.return`:

Return
------

The xxh32 hash stored in the state.

.. _`xxh64_reset`:

xxh64_reset
===========

.. c:function:: void xxh64_reset(struct xxh64_state *state, uint64_t seed)

    reset the xxh64 state to start a new hashing operation

    :param state:
        The xxh64 state to reset.
    :type state: struct xxh64_state \*

    :param seed:
        Initialize the hash state with this seed.
    :type seed: uint64_t

.. _`xxh64_update`:

xxh64_update
============

.. c:function:: int xxh64_update(struct xxh64_state *state, const void *input, size_t length)

    hash the data given and update the xxh64 state

    :param state:
        The xxh64 state to update.
    :type state: struct xxh64_state \*

    :param input:
        The data to hash.
    :type input: const void \*

    :param length:
        The length of the data to hash.
    :type length: size_t

.. _`xxh64_update.description`:

Description
-----------

After calling \ :c:func:`xxh64_reset`\  call \ :c:func:`xxh64_update`\  as many times as necessary.

.. _`xxh64_update.return`:

Return
------

Zero on success, otherwise an error code.

.. _`xxh64_digest`:

xxh64_digest
============

.. c:function:: uint64_t xxh64_digest(const struct xxh64_state *state)

    produce the current xxh64 hash

    :param state:
        Produce the current xxh64 hash of this state.
    :type state: const struct xxh64_state \*

.. _`xxh64_digest.description`:

Description
-----------

A hash value can be produced at any time. It is still possible to continue
inserting input into the hash state after a call to \ :c:func:`xxh64_digest`\ , and
generate new hashes later on, by calling \ :c:func:`xxh64_digest`\  again.

.. _`xxh64_digest.return`:

Return
------

The xxh64 hash stored in the state.

.. _`xxh32_copy_state`:

xxh32_copy_state
================

.. c:function:: void xxh32_copy_state(struct xxh32_state *dst, const struct xxh32_state *src)

    copy the source state into the destination state

    :param dst:
        The destination xxh32 state.
    :type dst: struct xxh32_state \*

    :param src:
        The source xxh32 state.
    :type src: const struct xxh32_state \*

.. _`xxh64_copy_state`:

xxh64_copy_state
================

.. c:function:: void xxh64_copy_state(struct xxh64_state *dst, const struct xxh64_state *src)

    copy the source state into the destination state

    :param dst:
        The destination xxh64 state.
    :type dst: struct xxh64_state \*

    :param src:
        The source xxh64 state.
    :type src: const struct xxh64_state \*

.. This file was automatic generated / don't edit.

