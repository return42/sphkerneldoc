.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/include/linux/hashtable.h

.. _`hash_init`:

hash_init
=========

.. c:function::  hash_init( hashtable)

    initialize a hash table

    :param  hashtable:
        hashtable to be initialized

.. _`hash_init.description`:

Description
-----------

Calculates the size of the hashtable from the given parameter, otherwise
same as hash_init_size.

This has to be a macro since \ :c:func:`HASH_BITS`\  will not work on pointers since
it calculates the size during preprocessing.

.. _`hash_add`:

hash_add
========

.. c:function::  hash_add( hashtable,  node,  key)

    add an object to a hashtable

    :param  hashtable:
        hashtable to add to

    :param  node:
        the \ :c:type:`struct hlist_node <hlist_node>`\  of the object to be added

    :param  key:
        the key of the object to be added

.. _`hash_hashed`:

hash_hashed
===========

.. c:function:: bool hash_hashed(struct hlist_node *node)

    check whether an object is in any hashtable

    :param struct hlist_node \*node:
        the \ :c:type:`struct hlist_node <hlist_node>`\  of the object to be checked

.. _`hash_empty`:

hash_empty
==========

.. c:function::  hash_empty( hashtable)

    check whether a hashtable is empty

    :param  hashtable:
        hashtable to check

.. _`hash_empty.description`:

Description
-----------

This has to be a macro since \ :c:func:`HASH_BITS`\  will not work on pointers since
it calculates the size during preprocessing.

.. _`hash_del`:

hash_del
========

.. c:function:: void hash_del(struct hlist_node *node)

    remove an object from a hashtable

    :param struct hlist_node \*node:
        &struct hlist_node of the object to remove

.. _`hash_for_each`:

hash_for_each
=============

.. c:function::  hash_for_each( name,  bkt,  obj,  member)

    iterate over a hashtable

    :param  name:
        hashtable to iterate

    :param  bkt:
        integer to use as bucket loop cursor

    :param  obj:
        the type \* to use as a loop cursor for each entry

    :param  member:
        the name of the hlist_node within the struct

.. _`hash_for_each_safe`:

hash_for_each_safe
==================

.. c:function::  hash_for_each_safe( name,  bkt,  tmp,  obj,  member)

    iterate over a hashtable safe against removal of hash entry

    :param  name:
        hashtable to iterate

    :param  bkt:
        integer to use as bucket loop cursor

    :param  tmp:
        a \ :c:type:`struct used <used>`\  for temporary storage

    :param  obj:
        the type \* to use as a loop cursor for each entry

    :param  member:
        the name of the hlist_node within the struct

.. _`hash_for_each_possible`:

hash_for_each_possible
======================

.. c:function::  hash_for_each_possible( name,  obj,  member,  key)

    iterate over all possible objects hashing to the same bucket

    :param  name:
        hashtable to iterate

    :param  obj:
        the type \* to use as a loop cursor for each entry

    :param  member:
        the name of the hlist_node within the struct

    :param  key:
        the key of the objects to iterate over

.. _`hash_for_each_possible_safe`:

hash_for_each_possible_safe
===========================

.. c:function::  hash_for_each_possible_safe( name,  obj,  tmp,  member,  key)

    iterate over all possible objects hashing to the same bucket safe against removals

    :param  name:
        hashtable to iterate

    :param  obj:
        the type \* to use as a loop cursor for each entry

    :param  tmp:
        a \ :c:type:`struct used <used>`\  for temporary storage

    :param  member:
        the name of the hlist_node within the struct

    :param  key:
        the key of the objects to iterate over

.. This file was automatic generated / don't edit.

