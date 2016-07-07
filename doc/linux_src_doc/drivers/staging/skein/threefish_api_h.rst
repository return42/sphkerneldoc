.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/skein/threefish_api.h

.. _`threefish_set_key`:

threefish_set_key
=================

.. c:function:: void threefish_set_key(struct threefish_key *key_ctx, enum threefish_size state_size, u64 *key_data, u64 *tweak)

    :param struct threefish_key \*key_ctx:
        *undescribed*

    :param enum threefish_size state_size:
        *undescribed*

    :param u64 \*key_data:
        *undescribed*

    :param u64 \*tweak:
        *undescribed*

.. _`threefish_set_key.description`:

Description
-----------

This function sets the key and tweak data for the Threefish cipher of
the given size. The key data must have the same length (number of bits)
as the state size

\ ``param``\  key_ctx
Pointer to a Threefish key structure.
\ ``param``\  size
Which Skein size to use.
\ ``param``\  key_data
Pointer to the key words (word has 64 bits).
\ ``param``\  tweak
Pointer to the two tweak words (word has 64 bits).

.. _`threefish_encrypt_block_bytes`:

threefish_encrypt_block_bytes
=============================

.. c:function:: void threefish_encrypt_block_bytes(struct threefish_key *key_ctx, u8 *in, u8 *out)

    :param struct threefish_key \*key_ctx:
        *undescribed*

    :param u8 \*in:
        *undescribed*

    :param u8 \*out:
        *undescribed*

.. _`threefish_encrypt_block_bytes.description`:

Description
-----------

The buffer must have at least the same length (number of bits) as the
state size for this key. The function uses the first \ ``c``\  state_size bits
of the input buffer, encrypts them and stores the result in the output
buffer.

\ ``param``\  key_ctx
Pointer to a Threefish key structure.
\ ``param``\  in
Poionter to plaintext data buffer.
\ ``param``\  out
Pointer to cipher buffer.

.. _`threefish_encrypt_block_words`:

threefish_encrypt_block_words
=============================

.. c:function:: void threefish_encrypt_block_words(struct threefish_key *key_ctx, u64 *in, u64 *out)

    :param struct threefish_key \*key_ctx:
        *undescribed*

    :param u64 \*in:
        *undescribed*

    :param u64 \*out:
        *undescribed*

.. _`threefish_encrypt_block_words.description`:

Description
-----------

The buffer must have at least the same length (number of bits) as the
state size for this key. The function uses the first \ ``c``\  state_size bits
of the input buffer, encrypts them and stores the result in the output
buffer.

The wordsize ist set to 64 bits.

\ ``param``\  key_ctx
Pointer to a Threefish key structure.
\ ``param``\  in
Poionter to plaintext data buffer.
\ ``param``\  out
Pointer to cipher buffer.

.. _`threefish_decrypt_block_bytes`:

threefish_decrypt_block_bytes
=============================

.. c:function:: void threefish_decrypt_block_bytes(struct threefish_key *key_ctx, u8 *in, u8 *out)

    :param struct threefish_key \*key_ctx:
        *undescribed*

    :param u8 \*in:
        *undescribed*

    :param u8 \*out:
        *undescribed*

.. _`threefish_decrypt_block_bytes.description`:

Description
-----------

The buffer must have at least the same length (number of bits) as the
state size for this key. The function uses the first \ ``c``\  state_size bits
of the input buffer, decrypts them and stores the result in the output
buffer

\ ``param``\  key_ctx
Pointer to a Threefish key structure.
\ ``param``\  in
Poionter to cipher data buffer.
\ ``param``\  out
Pointer to plaintext buffer.

.. _`threefish_decrypt_block_words`:

threefish_decrypt_block_words
=============================

.. c:function:: void threefish_decrypt_block_words(struct threefish_key *key_ctx, u64 *in, u64 *out)

    :param struct threefish_key \*key_ctx:
        *undescribed*

    :param u64 \*in:
        *undescribed*

    :param u64 \*out:
        *undescribed*

.. _`threefish_decrypt_block_words.description`:

Description
-----------

The buffer must have at least the same length (number of bits) as the
state size for this key. The function uses the first \ ``c``\  state_size bits
of the input buffer, encrypts them and stores the result in the output
buffer.

The wordsize ist set to 64 bits.

\ ``param``\  key_ctx
Pointer to a Threefish key structure.
\ ``param``\  in
Poionter to cipher data buffer.
\ ``param``\  out
Pointer to plaintext buffer.

.. This file was automatic generated / don't edit.

