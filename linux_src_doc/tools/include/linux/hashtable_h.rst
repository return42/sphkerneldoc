.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/include/linux/hashtable.h

.. _`hash_init`:

hash_init
=========

.. c:function::  hash_init( hashtable)

    initialize a hash table

    :param hashtable:
        hashtable to be initialized
    :type hashtable: 

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

    :param hashtable:
        hashtable to add to
    :type hashtable: 

    :param node:
        the \ :c:type:`struct hlist_node <hlist_node>`\  of the object to be added
    :type node: 

    :param key:
        the key of the object to be added
    :type key: 

.. _`hash_hashed`:

hash_hashed
===========

.. c:function:: bool hash_hashed(struct hlist_node *node)

    check whether an object is in any hashtable

    :param node:
        the \ :c:type:`struct hlist_node <hlist_node>`\  of the object to be checked
    :type node: struct hlist_node \*

.. _`hash_empty`:

hash_empty
==========

.. c:function::  hash_empty( hashtable)

    check whether a hashtable is empty

    :param hashtable:
        hashtable to check
    :type hashtable: 

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

    :param node:
        \ :c:type:`struct hlist_node <hlist_node>`\  of the object to remove
    :type node: struct hlist_node \*

.. _`hash_for_each`:

hash_for_each
=============

.. c:function::  hash_for_each( name,  bkt,  obj,  member)

    iterate over a hashtable

    :param name:
        hashtable to iterate
    :type name: 

    :param bkt:
        integer to use as bucket loop cursor
    :type bkt: 

    :param obj:
        the type \* to use as a loop cursor for each entry
    :type obj: 

    :param member:
        the name of the hlist_node within the struct
    :type member: 

.. _`hash_for_each_safe`:

hash_for_each_safe
==================

.. c:function::  hash_for_each_safe( name,  bkt,  tmp,  obj,  member)

    iterate over a hashtable safe against removal of hash entry

    :param name:
        hashtable to iterate
    :type name: 

    :param bkt:
        integer to use as bucket loop cursor
    :type bkt: 

    :param tmp:
        a \ :c:type:`struct used <used>`\  for temporary storage
    :type tmp: 

    :param obj:
        the type \* to use as a loop cursor for each entry
    :type obj: 

    :param member:
        the name of the hlist_node within the struct
    :type member: 

.. _`hash_for_each_possible`:

hash_for_each_possible
======================

.. c:function::  hash_for_each_possible( name,  obj,  member,  key)

    iterate over all possible objects hashing to the same bucket

    :param name:
        hashtable to iterate
    :type name: 

    :param obj:
        the type \* to use as a loop cursor for each entry
    :type obj: 

    :param member:
        the name of the hlist_node within the struct
    :type member: 

    :param key:
        the key of the objects to iterate over
    :type key: 

.. _`hash_for_each_possible_safe`:

hash_for_each_possible_safe
===========================

.. c:function::  hash_for_each_possible_safe( name,  obj,  tmp,  member,  key)

    iterate over all possible objects hashing to the same bucket safe against removals

    :param name:
        hashtable to iterate
    :type name: 

    :param obj:
        the type \* to use as a loop cursor for each entry
    :type obj: 

    :param tmp:
        a \ :c:type:`struct used <used>`\  for temporary storage
    :type tmp: 

    :param member:
        the name of the hlist_node within the struct
    :type member: 

    :param key:
        the key of the objects to iterate over
    :type key: 

.. This file was automatic generated / don't edit.

