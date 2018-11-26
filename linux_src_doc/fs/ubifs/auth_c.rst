.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/auth.c

.. _`__ubifs_node_calc_hash`:

\__ubifs_node_calc_hash
=======================

.. c:function:: int __ubifs_node_calc_hash(const struct ubifs_info *c, const void *node, u8 *hash)

    calculate the hash of a UBIFS node

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param node:
        the node to calculate a hash for
    :type node: const void \*

    :param hash:
        the returned hash
    :type hash: u8 \*

.. _`__ubifs_node_calc_hash.description`:

Description
-----------

Returns 0 for success or a negative error code otherwise.

.. _`ubifs_hash_calc_hmac`:

ubifs_hash_calc_hmac
====================

.. c:function:: int ubifs_hash_calc_hmac(const struct ubifs_info *c, const u8 *hash, u8 *hmac)

    calculate a HMAC from a hash

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param hash:
        the node to calculate a HMAC for
    :type hash: const u8 \*

    :param hmac:
        the returned HMAC
    :type hmac: u8 \*

.. _`ubifs_hash_calc_hmac.description`:

Description
-----------

Returns 0 for success or a negative error code otherwise.

.. _`ubifs_prepare_auth_node`:

ubifs_prepare_auth_node
=======================

.. c:function:: int ubifs_prepare_auth_node(struct ubifs_info *c, void *node, struct shash_desc *inhash)

    Prepare an authentication node

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param node:
        the node to calculate a hash for
    :type node: void \*

    :param inhash:
        *undescribed*
    :type inhash: struct shash_desc \*

.. _`ubifs_prepare_auth_node.description`:

Description
-----------

This function prepares an authentication node for writing onto flash.
It creates a HMAC from the given input hash and writes it to the node.

Returns 0 for success or a negative error code otherwise.

.. _`__ubifs_hash_get_desc`:

\__ubifs_hash_get_desc
======================

.. c:function:: struct shash_desc *__ubifs_hash_get_desc(const struct ubifs_info *c)

    get a descriptor suitable for hashing a node

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

.. _`__ubifs_hash_get_desc.description`:

Description
-----------

This function returns a descriptor suitable for hashing a node. Free after use
with kfree.

.. _`__ubifs_shash_final`:

\__ubifs_shash_final
====================

.. c:function:: int __ubifs_shash_final(const struct ubifs_info *c, struct shash_desc *desc, u8 *out)

    finalize shash

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param desc:
        the descriptor
    :type desc: struct shash_desc \*

    :param out:
        the output hash
    :type out: u8 \*

.. _`__ubifs_shash_final.description`:

Description
-----------

Simple wrapper around \ :c:func:`crypto_shash_final`\ , safe to be called with
disabled authentication.

.. _`ubifs_bad_hash`:

ubifs_bad_hash
==============

.. c:function:: void ubifs_bad_hash(const struct ubifs_info *c, const void *node, const u8 *hash, int lnum, int offs)

    Report hash mismatches

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param node:
        the node
    :type node: const void \*

    :param hash:
        the expected hash
    :type hash: const u8 \*

    :param lnum:
        the LEB \ ``node``\  was read from
    :type lnum: int

    :param offs:
        offset in LEB \ ``node``\  was read from
    :type offs: int

.. _`ubifs_bad_hash.description`:

Description
-----------

This function reports a hash mismatch when a node has a different hash than
expected.

.. _`__ubifs_node_check_hash`:

\__ubifs_node_check_hash
========================

.. c:function:: int __ubifs_node_check_hash(const struct ubifs_info *c, const void *node, const u8 *expected)

    check the hash of a node against given hash

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param node:
        the node
    :type node: const void \*

    :param expected:
        the expected hash
    :type expected: const u8 \*

.. _`__ubifs_node_check_hash.description`:

Description
-----------

This function calculates a hash over a node and compares it to the given hash.
Returns 0 if both hashes are equal or authentication is disabled, otherwise a
negative error code is returned.

.. _`ubifs_init_authentication`:

ubifs_init_authentication
=========================

.. c:function:: int ubifs_init_authentication(struct ubifs_info *c)

    initialize UBIFS authentication support

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_init_authentication.description`:

Description
-----------

This function returns 0 for success or a negative error code otherwise.

.. _`__ubifs_exit_authentication`:

\__ubifs_exit_authentication
============================

.. c:function:: void __ubifs_exit_authentication(struct ubifs_info *c)

    release resource

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`__ubifs_exit_authentication.description`:

Description
-----------

This function releases the authentication related resources.

.. _`ubifs_node_calc_hmac`:

ubifs_node_calc_hmac
====================

.. c:function:: int ubifs_node_calc_hmac(const struct ubifs_info *c, const void *node, int len, int ofs_hmac, void *hmac)

    calculate the HMAC of a UBIFS node

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param node:
        the node to insert a HMAC into.
    :type node: const void \*

    :param len:
        the length of the node
    :type len: int

    :param ofs_hmac:
        the offset in the node where the HMAC is inserted
    :type ofs_hmac: int

    :param hmac:
        returned HMAC
    :type hmac: void \*

.. _`ubifs_node_calc_hmac.description`:

Description
-----------

This function calculates a HMAC of a UBIFS node. The HMAC is expected to be
embedded into the node, so this area is not covered by the HMAC. Also not
covered is the UBIFS_NODE_MAGIC and the CRC of the node.

.. _`__ubifs_node_insert_hmac`:

\__ubifs_node_insert_hmac
=========================

.. c:function:: int __ubifs_node_insert_hmac(const struct ubifs_info *c, void *node, int len, int ofs_hmac)

    insert a HMAC into a UBIFS node

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param node:
        the node to insert a HMAC into.
    :type node: void \*

    :param len:
        the length of the node
    :type len: int

    :param ofs_hmac:
        the offset in the node where the HMAC is inserted
    :type ofs_hmac: int

.. _`__ubifs_node_insert_hmac.description`:

Description
-----------

This function inserts a HMAC at offset \ ``ofs_hmac``\  into the node given in
\ ``node``\ .

This function returns 0 for success or a negative error code otherwise.

.. _`__ubifs_node_verify_hmac`:

\__ubifs_node_verify_hmac
=========================

.. c:function:: int __ubifs_node_verify_hmac(const struct ubifs_info *c, const void *node, int len, int ofs_hmac)

    verify the HMAC of UBIFS node

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param node:
        the node to insert a HMAC into.
    :type node: const void \*

    :param len:
        the length of the node
    :type len: int

    :param ofs_hmac:
        the offset in the node where the HMAC is inserted
    :type ofs_hmac: int

.. _`__ubifs_node_verify_hmac.description`:

Description
-----------

This function verifies the HMAC at offset \ ``ofs_hmac``\  of the node given in
\ ``node``\ . Returns 0 if successful or a negative error code otherwise.

.. _`ubifs_hmac_wkm`:

ubifs_hmac_wkm
==============

.. c:function:: int ubifs_hmac_wkm(struct ubifs_info *c, u8 *hmac)

    Create a HMAC of the well known message

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param hmac:
        The HMAC of the well known message
    :type hmac: u8 \*

.. _`ubifs_hmac_wkm.description`:

Description
-----------

This function creates a HMAC of a well known message. This is used
to check if the provided key is suitable to authenticate a UBIFS
image. This is only a convenience to the user to provide a better
error message when the wrong key is provided.

This function returns 0 for success or a negative error code otherwise.

.. This file was automatic generated / don't edit.

