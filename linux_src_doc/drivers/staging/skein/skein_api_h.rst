.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/skein/skein_api.h

.. _`skein_ctx_prepare`:

skein_ctx_prepare
=================

.. c:function:: int skein_ctx_prepare(struct skein_ctx *ctx, enum skein_size size)

    :param struct skein_ctx \*ctx:
        *undescribed*

    :param enum skein_size size:
        *undescribed*

.. _`skein_ctx_prepare.description`:

Description
-----------

An application must call this function before it can use the Skein
context. The functions clears memory and initializes size dependent
variables.

\ ``param``\  ctx
Pointer to a Skein context.
\ ``param``\  size
Which Skein size to use.
\ ``return``\ 
SKEIN_SUCCESS of SKEIN_FAIL

.. _`skein_init`:

skein_init
==========

.. c:function:: int skein_init(struct skein_ctx *ctx, size_t hash_bit_len)

    :param struct skein_ctx \*ctx:
        *undescribed*

    :param size_t hash_bit_len:
        *undescribed*

.. _`skein_init.description`:

Description
-----------

Initializes the context with this data and saves the resulting Skein
state variables for further use.

\ ``param``\  ctx
Pointer to a Skein context.
\ ``param``\  hash_bit_len
Number of MAC hash bits to compute
\ ``return``\ 
SKEIN_SUCCESS of SKEIN_FAIL
\ ``see``\  skein_reset

.. _`skein_reset`:

skein_reset
===========

.. c:function:: void skein_reset(struct skein_ctx *ctx)

    :param struct skein_ctx \*ctx:
        *undescribed*

.. _`skein_reset.description`:

Description
-----------

Restores the saved chaining variables to reset the Skein context.
Thus applications can reuse the same setup to  process several
messages. This saves a complete Skein initialization cycle.

\ ``param``\  ctx
Pointer to a pre-initialized Skein MAC context

.. _`skein_mac_init`:

skein_mac_init
==============

.. c:function:: int skein_mac_init(struct skein_ctx *ctx, const u8 *key, size_t key_len, size_t hash_bit_len)

    :param struct skein_ctx \*ctx:
        *undescribed*

    :param const u8 \*key:
        *undescribed*

    :param size_t key_len:
        *undescribed*

    :param size_t hash_bit_len:
        *undescribed*

.. _`skein_mac_init.description`:

Description
-----------

Initializes the context with this data and saves the resulting Skein
state variables for further use.

Applications call the normal Skein functions to update the MAC and
get the final result.

\ ``param``\  ctx
Pointer to an empty or preinitialized Skein MAC context
\ ``param``\  key
Pointer to key bytes or NULL
\ ``param``\  key_len
Length of the key in bytes or zero
\ ``param``\  hash_bit_len
Number of MAC hash bits to compute
\ ``return``\ 
SKEIN_SUCCESS of SKEIN_FAIL

.. _`skein_update`:

skein_update
============

.. c:function:: int skein_update(struct skein_ctx *ctx, const u8 *msg, size_t msg_byte_cnt)

    :param struct skein_ctx \*ctx:
        *undescribed*

    :param const u8 \*msg:
        *undescribed*

    :param size_t msg_byte_cnt:
        *undescribed*

.. _`skein_update.description`:

Description
-----------

@param ctx
Pointer to initialized Skein context
\ ``param``\  msg
Pointer to the message.
\ ``param``\  msg_byte_cnt
Length of the message in \ ``b``\  bytes
\ ``return``\ 
Success or error code.

.. _`skein_update_bits`:

skein_update_bits
=================

.. c:function:: int skein_update_bits(struct skein_ctx *ctx, const u8 *msg, size_t msg_bit_cnt)

    :param struct skein_ctx \*ctx:
        *undescribed*

    :param const u8 \*msg:
        *undescribed*

    :param size_t msg_bit_cnt:
        *undescribed*

.. _`skein_update_bits.description`:

Description
-----------

Skein can handle data not only as bytes but also as bit strings of
arbitrary length (up to its maximum design size).

\ ``param``\  ctx
Pointer to initialized Skein context
\ ``param``\  msg
Pointer to the message.
\ ``param``\  msg_bit_cnt
Length of the message in \ ``b``\  bits.

.. _`skein_final`:

skein_final
===========

.. c:function:: int skein_final(struct skein_ctx *ctx, u8 *hash)

    :param struct skein_ctx \*ctx:
        *undescribed*

    :param u8 \*hash:
        *undescribed*

.. _`skein_final.description`:

Description
-----------

Before an application can reuse a Skein setup the application must
reset the Skein context.

\ ``param``\  ctx
Pointer to initialized Skein context
\ ``param``\  hash
Pointer to buffer that receives the hash. The buffer must be large
enough to store \ ``c``\  hash_bit_len bits.
\ ``return``\ 
Success or error code.
\ ``see``\  skein_reset

.. This file was automatic generated / don't edit.

