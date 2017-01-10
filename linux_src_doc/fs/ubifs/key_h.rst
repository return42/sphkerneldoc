.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/key.h

.. _`key_mask_hash`:

key_mask_hash
=============

.. c:function:: uint32_t key_mask_hash(uint32_t hash)

    mask a valid hash value.

    :param uint32_t hash:
        *undescribed*

.. _`key_mask_hash.description`:

Description
-----------

We use hash values as offset in directories, so values \ ``0``\  and \ ``1``\  are
reserved for "." and "..". \ ``2``\  is reserved for "end of readdir" marker. This
function makes sure the reserved values are not used.

.. _`key_r5_hash`:

key_r5_hash
===========

.. c:function:: uint32_t key_r5_hash(const char *s, int len)

    R5 hash function (borrowed from reiserfs).

    :param const char \*s:
        direntry name

    :param int len:
        name length

.. _`key_test_hash`:

key_test_hash
=============

.. c:function:: uint32_t key_test_hash(const char *str, int len)

    testing hash function.

    :param const char \*str:
        direntry name

    :param int len:
        name length

.. _`ino_key_init`:

ino_key_init
============

.. c:function:: void ino_key_init(const struct ubifs_info *c, union ubifs_key *key, ino_t inum)

    initialize inode key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        key to initialize

    :param ino_t inum:
        inode number

.. _`ino_key_init_flash`:

ino_key_init_flash
==================

.. c:function:: void ino_key_init_flash(const struct ubifs_info *c, void *k, ino_t inum)

    initialize on-flash inode key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*k:
        key to initialize

    :param ino_t inum:
        inode number

.. _`lowest_ino_key`:

lowest_ino_key
==============

.. c:function:: void lowest_ino_key(const struct ubifs_info *c, union ubifs_key *key, ino_t inum)

    get the lowest possible inode key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        key to initialize

    :param ino_t inum:
        inode number

.. _`highest_ino_key`:

highest_ino_key
===============

.. c:function:: void highest_ino_key(const struct ubifs_info *c, union ubifs_key *key, ino_t inum)

    get the highest possible inode key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        key to initialize

    :param ino_t inum:
        inode number

.. _`dent_key_init`:

dent_key_init
=============

.. c:function:: void dent_key_init(const struct ubifs_info *c, union ubifs_key *key, ino_t inum, const struct fscrypt_name *nm)

    initialize directory entry key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        key to initialize

    :param ino_t inum:
        parent inode number

    :param const struct fscrypt_name \*nm:
        direntry name and length. Not a string when encrypted!

.. _`dent_key_init_hash`:

dent_key_init_hash
==================

.. c:function:: void dent_key_init_hash(const struct ubifs_info *c, union ubifs_key *key, ino_t inum, uint32_t hash)

    initialize directory entry key without re-calculating hash function.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        key to initialize

    :param ino_t inum:
        parent inode number

    :param uint32_t hash:
        direntry name hash

.. _`dent_key_init_flash`:

dent_key_init_flash
===================

.. c:function:: void dent_key_init_flash(const struct ubifs_info *c, void *k, ino_t inum, const struct fscrypt_name *nm)

    initialize on-flash directory entry key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*k:
        key to initialize

    :param ino_t inum:
        parent inode number

    :param const struct fscrypt_name \*nm:
        direntry name and length

.. _`lowest_dent_key`:

lowest_dent_key
===============

.. c:function:: void lowest_dent_key(const struct ubifs_info *c, union ubifs_key *key, ino_t inum)

    get the lowest possible directory entry key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        where to store the lowest key

    :param ino_t inum:
        parent inode number

.. _`xent_key_init`:

xent_key_init
=============

.. c:function:: void xent_key_init(const struct ubifs_info *c, union ubifs_key *key, ino_t inum, const struct fscrypt_name *nm)

    initialize extended attribute entry key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        key to initialize

    :param ino_t inum:
        host inode number

    :param const struct fscrypt_name \*nm:
        extended attribute entry name and length

.. _`xent_key_init_flash`:

xent_key_init_flash
===================

.. c:function:: void xent_key_init_flash(const struct ubifs_info *c, void *k, ino_t inum, const struct fscrypt_name *nm)

    initialize on-flash extended attribute entry key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*k:
        key to initialize

    :param ino_t inum:
        host inode number

    :param const struct fscrypt_name \*nm:
        extended attribute entry name and length

.. _`lowest_xent_key`:

lowest_xent_key
===============

.. c:function:: void lowest_xent_key(const struct ubifs_info *c, union ubifs_key *key, ino_t inum)

    get the lowest possible extended attribute entry key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        where to store the lowest key

    :param ino_t inum:
        host inode number

.. _`data_key_init`:

data_key_init
=============

.. c:function:: void data_key_init(const struct ubifs_info *c, union ubifs_key *key, ino_t inum, unsigned int block)

    initialize data key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        key to initialize

    :param ino_t inum:
        inode number

    :param unsigned int block:
        block number

.. _`highest_data_key`:

highest_data_key
================

.. c:function:: void highest_data_key(const struct ubifs_info *c, union ubifs_key *key, ino_t inum)

    get the highest possible data key for an inode.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        key to initialize

    :param ino_t inum:
        inode number

.. _`trun_key_init`:

trun_key_init
=============

.. c:function:: void trun_key_init(const struct ubifs_info *c, union ubifs_key *key, ino_t inum)

    initialize truncation node key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        key to initialize

    :param ino_t inum:
        inode number

.. _`trun_key_init.description`:

Description
-----------

Note, UBIFS does not have truncation keys on the media and this function is
only used for purposes of replay.

.. _`invalid_key_init`:

invalid_key_init
================

.. c:function:: void invalid_key_init(const struct ubifs_info *c, union ubifs_key *key)

    initialize invalid node key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        key to initialize

.. _`invalid_key_init.description`:

Description
-----------

This is a helper function which marks a \ ``key``\  object as invalid.

.. _`key_type`:

key_type
========

.. c:function:: int key_type(const struct ubifs_info *c, const union ubifs_key *key)

    get key type.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        key to get type of

.. _`key_type_flash`:

key_type_flash
==============

.. c:function:: int key_type_flash(const struct ubifs_info *c, const void *k)

    get type of a on-flash formatted key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const void \*k:
        key to get type of

.. _`key_inum`:

key_inum
========

.. c:function:: ino_t key_inum(const struct ubifs_info *c, const void *k)

    fetch inode number from key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const void \*k:
        key to fetch inode number from

.. _`key_inum_flash`:

key_inum_flash
==============

.. c:function:: ino_t key_inum_flash(const struct ubifs_info *c, const void *k)

    fetch inode number from an on-flash formatted key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const void \*k:
        key to fetch inode number from

.. _`key_hash`:

key_hash
========

.. c:function:: uint32_t key_hash(const struct ubifs_info *c, const union ubifs_key *key)

    get directory entry hash.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        the key to get hash from

.. _`key_hash_flash`:

key_hash_flash
==============

.. c:function:: uint32_t key_hash_flash(const struct ubifs_info *c, const void *k)

    get directory entry hash from an on-flash formatted key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const void \*k:
        the key to get hash from

.. _`key_block`:

key_block
=========

.. c:function:: unsigned int key_block(const struct ubifs_info *c, const union ubifs_key *key)

    get data block number.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        the key to get the block number from

.. _`key_block_flash`:

key_block_flash
===============

.. c:function:: unsigned int key_block_flash(const struct ubifs_info *c, const void *k)

    get data block number from an on-flash formatted key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const void \*k:
        the key to get the block number from

.. _`key_read`:

key_read
========

.. c:function:: void key_read(const struct ubifs_info *c, const void *from, union ubifs_key *to)

    transform a key to in-memory format.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const void \*from:
        the key to transform

    :param union ubifs_key \*to:
        the key to store the result

.. _`key_write`:

key_write
=========

.. c:function:: void key_write(const struct ubifs_info *c, const union ubifs_key *from, void *to)

    transform a key from in-memory format.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*from:
        the key to transform

    :param void \*to:
        the key to store the result

.. _`key_write_idx`:

key_write_idx
=============

.. c:function:: void key_write_idx(const struct ubifs_info *c, const union ubifs_key *from, void *to)

    transform a key from in-memory format for the index.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*from:
        the key to transform

    :param void \*to:
        the key to store the result

.. _`key_copy`:

key_copy
========

.. c:function:: void key_copy(const struct ubifs_info *c, const union ubifs_key *from, union ubifs_key *to)

    copy a key.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*from:
        the key to copy from

    :param union ubifs_key \*to:
        the key to copy to

.. _`keys_cmp`:

keys_cmp
========

.. c:function:: int keys_cmp(const struct ubifs_info *c, const union ubifs_key *key1, const union ubifs_key *key2)

    compare keys.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key1:
        the first key to compare

    :param const union ubifs_key \*key2:
        the second key to compare

.. _`keys_cmp.description`:

Description
-----------

This function compares 2 keys and returns \ ``-1``\  if \ ``key1``\  is less than
\ ``key2``\ , \ ``0``\  if the keys are equivalent and \ ``1``\  if \ ``key1``\  is greater than \ ``key2``\ .

.. _`keys_eq`:

keys_eq
=======

.. c:function:: int keys_eq(const struct ubifs_info *c, const union ubifs_key *key1, const union ubifs_key *key2)

    determine if keys are equivalent.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key1:
        the first key to compare

    :param const union ubifs_key \*key2:
        the second key to compare

.. _`keys_eq.description`:

Description
-----------

This function compares 2 keys and returns \ ``1``\  if \ ``key1``\  is equal to \ ``key2``\  and
\ ``0``\  if not.

.. _`is_hash_key`:

is_hash_key
===========

.. c:function:: int is_hash_key(const struct ubifs_info *c, const union ubifs_key *key)

    is a key vulnerable to hash collisions.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param const union ubifs_key \*key:
        key

.. _`is_hash_key.description`:

Description
-----------

This function returns \ ``1``\  if \ ``key``\  is a hashed key or \ ``0``\  otherwise.

.. _`key_max_inode_size`:

key_max_inode_size
==================

.. c:function:: unsigned long long key_max_inode_size(const struct ubifs_info *c)

    get maximum file size allowed by current key format.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

.. This file was automatic generated / don't edit.

