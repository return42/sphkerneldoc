.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/include/linux/chash.h

.. _`chash_table`:

struct chash_table
==================

.. c:type:: struct chash_table

    Dynamically allocated closed hash table

.. _`chash_table.definition`:

Definition
----------

.. code-block:: c

    struct chash_table {
        struct __chash_table table;
        unsigned long *data;
    }

.. _`chash_table.members`:

Members
-------

table
    *undescribed*

data
    *undescribed*

.. _`chash_table.description`:

Description
-----------

Use this struct for dynamically allocated hash tables (using
chash_table_alloc and chash_table_free), where the size is
determined at runtime.

.. _`declare_chash_table`:

DECLARE_CHASH_TABLE
===================

.. c:function::  DECLARE_CHASH_TABLE( table,  bts,  key_sz,  val_sz)

    macro to declare a closed hash table

    :param  table:
        name of the declared hash table

    :param  bts:
        Table size will be 2^bits entries

    :param  key_sz:
        Size of hash keys in bytes, 4 or 8

    :param  val_sz:
        Size of data values in bytes, can be 0

.. _`declare_chash_table.description`:

Description
-----------

This declares the hash table variable with a static size.

The closed hash table stores key-value pairs with low memory and
lookup overhead. In operation it performs no dynamic memory
management. The data being stored does not require any
list_heads. The hash table performs best with small \ ``val_sz``\  and as
long as some space (about 50%) is left free in the table. But the
table can still work reasonably efficiently even when filled up to
about 90%. If bigger data items need to be stored and looked up,
store the pointer to it as value in the hash table.

\ ``val_sz``\  may be 0. This can be useful when all the stored
information is contained in the key itself and the fact that it is
in the hash table (or not).

.. _`define_chash_table`:

DEFINE_CHASH_TABLE
==================

.. c:function::  DEFINE_CHASH_TABLE( tbl,  bts,  key_sz,  val_sz)

    macro to define and initialize a closed hash table

    :param  tbl:
        name of the declared hash table

    :param  bts:
        Table size will be 2^bits entries

    :param  key_sz:
        Size of hash keys in bytes, 4 or 8

    :param  val_sz:
        Size of data values in bytes, can be 0

.. _`define_chash_table.note`:

Note
----

the macro can be used for global and local hash table variables.

.. _`init_chash_table`:

INIT_CHASH_TABLE
================

.. c:function::  INIT_CHASH_TABLE( tbl,  bts,  key_sz,  val_sz)

    Initialize a hash table declared by DECLARE_CHASH_TABLE

    :param  tbl:
        name of the declared hash table

    :param  bts:
        Table size will be 2^bits entries

    :param  key_sz:
        Size of hash keys in bytes, 4 or 8

    :param  val_sz:
        Size of data values in bytes, can be 0

.. _`chash_table_dump_stats`:

chash_table_dump_stats
======================

.. c:function::  chash_table_dump_stats( tbl)

    Dump statistics of a closed hash table

    :param  tbl:
        Pointer to the table structure

.. _`chash_table_dump_stats.description`:

Description
-----------

Dumps some performance statistics of the table gathered in operation
in the kernel log using pr_debug. If CONFIG_DYNAMIC_DEBUG is enabled,
user must turn on messages for chash.c (file chash.c +p).

.. _`chash_table_reset_stats`:

chash_table_reset_stats
=======================

.. c:function::  chash_table_reset_stats( tbl)

    Reset statistics of a closed hash table

    :param  tbl:
        Pointer to the table structure

.. _`chash_table_copy_in`:

chash_table_copy_in
===================

.. c:function::  chash_table_copy_in( tbl,  key,  value)

    Copy a new value into the hash table

    :param  tbl:
        Pointer to the table structure

    :param  key:
        Key of the entry to add or update

    :param  value:
        Pointer to value to copy, may be NULL

.. _`chash_table_copy_in.description`:

Description
-----------

If \ ``key``\  already has an entry, its value is replaced. Otherwise a
new entry is added. If \ ``value``\  is NULL, the value is left unchanged
or uninitialized. Returns 1 if an entry already existed, 0 if a new
entry was added or \ ``-ENOMEM``\  if there was no free space in the
table.

.. _`chash_table_copy_out`:

chash_table_copy_out
====================

.. c:function::  chash_table_copy_out( tbl,  key,  value)

    Copy a value out of the hash table

    :param  tbl:
        Pointer to the table structure

    :param  key:
        Key of the entry to find

    :param  value:
        Pointer to value to copy, may be NULL

.. _`chash_table_copy_out.description`:

Description
-----------

If \ ``value``\  is not NULL and the table has a non-0 value_size, the
value at \ ``key``\  is copied to \ ``value``\ . Returns the slot index of the
entry or \ ``-EINVAL``\  if \ ``key``\  was not found.

.. _`chash_table_remove`:

chash_table_remove
==================

.. c:function::  chash_table_remove( tbl,  key,  value)

    Remove an entry from the hash table

    :param  tbl:
        Pointer to the table structure

    :param  key:
        Key of the entry to find

    :param  value:
        Pointer to value to copy, may be NULL

.. _`chash_table_remove.description`:

Description
-----------

If \ ``value``\  is not NULL and the table has a non-0 value_size, the
value at \ ``key``\  is copied to \ ``value``\ . The entry is removed from the
table. Returns the slot index of the removed entry or \ ``-EINVAL``\  if
\ ``key``\  was not found.

.. _`chash_iter_init`:

CHASH_ITER_INIT
===============

.. c:function::  CHASH_ITER_INIT( table,  s)

    Initialize a hash table iterator

    :param  table:
        *undescribed*

    :param  s:
        Initial slot number

.. _`chash_iter_set`:

CHASH_ITER_SET
==============

.. c:function::  CHASH_ITER_SET( iter,  s)

    Set hash table iterator to new slot

    :param  iter:
        Iterator

    :param  s:
        Slot number

.. _`chash_iter_inc`:

CHASH_ITER_INC
==============

.. c:function::  CHASH_ITER_INC( iter)

    Increment hash table iterator

    :param  iter:
        *undescribed*

.. _`chash_iter_inc.description`:

Description
-----------

Wraps around at the end.

.. This file was automatic generated / don't edit.

