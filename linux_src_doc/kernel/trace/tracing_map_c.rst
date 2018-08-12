.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/tracing_map.c

.. _`tracing_map_update_sum`:

tracing_map_update_sum
======================

.. c:function:: void tracing_map_update_sum(struct tracing_map_elt *elt, unsigned int i, u64 n)

    Add a value to a tracing_map_elt's sum field

    :param struct tracing_map_elt \*elt:
        The tracing_map_elt

    :param unsigned int i:
        The index of the given sum associated with the tracing_map_elt

    :param u64 n:
        The value to add to the sum

.. _`tracing_map_update_sum.description`:

Description
-----------

Add n to sum i associated with the specified tracing_map_elt
instance.  The index i is the index returned by the call to
\ :c:func:`tracing_map_add_sum_field`\  when the tracing map was set up.

.. _`tracing_map_read_sum`:

tracing_map_read_sum
====================

.. c:function:: u64 tracing_map_read_sum(struct tracing_map_elt *elt, unsigned int i)

    Return the value of a tracing_map_elt's sum field

    :param struct tracing_map_elt \*elt:
        The tracing_map_elt

    :param unsigned int i:
        The index of the given sum associated with the tracing_map_elt

.. _`tracing_map_read_sum.description`:

Description
-----------

Retrieve the value of the sum i associated with the specified
tracing_map_elt instance.  The index i is the index returned by the
call to \ :c:func:`tracing_map_add_sum_field`\  when the tracing map was set
up.

.. _`tracing_map_read_sum.return`:

Return
------

The sum associated with field i for elt.

.. _`tracing_map_set_var`:

tracing_map_set_var
===================

.. c:function:: void tracing_map_set_var(struct tracing_map_elt *elt, unsigned int i, u64 n)

    Assign a tracing_map_elt's variable field

    :param struct tracing_map_elt \*elt:
        The tracing_map_elt

    :param unsigned int i:
        The index of the given variable associated with the tracing_map_elt

    :param u64 n:
        The value to assign

.. _`tracing_map_set_var.description`:

Description
-----------

Assign n to variable i associated with the specified tracing_map_elt
instance.  The index i is the index returned by the call to
\ :c:func:`tracing_map_add_var`\  when the tracing map was set up.

.. _`tracing_map_var_set`:

tracing_map_var_set
===================

.. c:function:: bool tracing_map_var_set(struct tracing_map_elt *elt, unsigned int i)

    Return whether or not a variable has been set

    :param struct tracing_map_elt \*elt:
        The tracing_map_elt

    :param unsigned int i:
        The index of the given variable associated with the tracing_map_elt

.. _`tracing_map_var_set.description`:

Description
-----------

Return true if the variable has been set, false otherwise.  The
index i is the index returned by the call to \ :c:func:`tracing_map_add_var`\ 
when the tracing map was set up.

.. _`tracing_map_read_var`:

tracing_map_read_var
====================

.. c:function:: u64 tracing_map_read_var(struct tracing_map_elt *elt, unsigned int i)

    Return the value of a tracing_map_elt's variable field

    :param struct tracing_map_elt \*elt:
        The tracing_map_elt

    :param unsigned int i:
        The index of the given variable associated with the tracing_map_elt

.. _`tracing_map_read_var.description`:

Description
-----------

Retrieve the value of the variable i associated with the specified
tracing_map_elt instance.  The index i is the index returned by the
call to \ :c:func:`tracing_map_add_var`\  when the tracing map was set
up.

.. _`tracing_map_read_var.return`:

Return
------

The variable value associated with field i for elt.

.. _`tracing_map_read_var_once`:

tracing_map_read_var_once
=========================

.. c:function:: u64 tracing_map_read_var_once(struct tracing_map_elt *elt, unsigned int i)

    Return and reset a tracing_map_elt's variable field

    :param struct tracing_map_elt \*elt:
        The tracing_map_elt

    :param unsigned int i:
        The index of the given variable associated with the tracing_map_elt

.. _`tracing_map_read_var_once.description`:

Description
-----------

Retrieve the value of the variable i associated with the specified
tracing_map_elt instance, and reset the variable to the 'not set'
state.  The index i is the index returned by the call to
\ :c:func:`tracing_map_add_var`\  when the tracing map was set up.  The reset
essentially makes the variable a read-once variable if it's only
accessed using this function.

.. _`tracing_map_read_var_once.return`:

Return
------

The variable value associated with field i for elt.

.. _`tracing_map_add_sum_field`:

tracing_map_add_sum_field
=========================

.. c:function:: int tracing_map_add_sum_field(struct tracing_map *map)

    Add a field describing a tracing_map sum

    :param struct tracing_map \*map:
        The tracing_map

.. _`tracing_map_add_sum_field.description`:

Description
-----------

Add a sum field to the key and return the index identifying it in
the map and associated tracing_map_elts.  This is the index used
for instance to update a sum for a particular tracing_map_elt using
\ :c:func:`tracing_map_update_sum`\  or reading it via \ :c:func:`tracing_map_read_sum`\ .

.. _`tracing_map_add_sum_field.return`:

Return
------

The index identifying the field in the map and associated
tracing_map_elts, or -EINVAL on error.

.. _`tracing_map_add_var`:

tracing_map_add_var
===================

.. c:function:: int tracing_map_add_var(struct tracing_map *map)

    Add a field describing a tracing_map var

    :param struct tracing_map \*map:
        The tracing_map

.. _`tracing_map_add_var.description`:

Description
-----------

Add a var to the map and return the index identifying it in the map
and associated tracing_map_elts.  This is the index used for
instance to update a var for a particular tracing_map_elt using
\ :c:func:`tracing_map_update_var`\  or reading it via \ :c:func:`tracing_map_read_var`\ .

.. _`tracing_map_add_var.return`:

Return
------

The index identifying the var in the map and associated
tracing_map_elts, or -EINVAL on error.

.. _`tracing_map_add_key_field`:

tracing_map_add_key_field
=========================

.. c:function:: int tracing_map_add_key_field(struct tracing_map *map, unsigned int offset, tracing_map_cmp_fn_t cmp_fn)

    Add a field describing a tracing_map key

    :param struct tracing_map \*map:
        The tracing_map

    :param unsigned int offset:
        The offset within the key

    :param tracing_map_cmp_fn_t cmp_fn:
        The comparison function that will be used to sort on the key

.. _`tracing_map_add_key_field.description`:

Description
-----------

Let the map know there is a key and that if it's used as a sort key
to use cmp_fn.

A key can be a subset of a compound key; for that purpose, the
offset param is used to describe where within the the compound key
the key referenced by this key field resides.

.. _`tracing_map_add_key_field.return`:

Return
------

The index identifying the field in the map and associated
tracing_map_elts, or -EINVAL on error.

.. _`tracing_map_insert`:

tracing_map_insert
==================

.. c:function:: struct tracing_map_elt *tracing_map_insert(struct tracing_map *map, void *key)

    Insert key and/or retrieve val from a tracing_map

    :param struct tracing_map \*map:
        The tracing_map to insert into

    :param void \*key:
        The key to insert

.. _`tracing_map_insert.description`:

Description
-----------

Inserts a key into a tracing_map and creates and returns a new
tracing_map_elt for it, or if the key has already been inserted by
a previous call, returns the tracing_map_elt already associated
with it.  When the map was created, the number of elements to be
allocated for the map was specified (internally maintained as
'max_elts' in struct tracing_map), and that number of
tracing_map_elts was created by \ :c:func:`tracing_map_init`\ .  This is the
pre-allocated pool of tracing_map_elts that \ :c:func:`tracing_map_insert`\ 
will allocate from when adding new keys.  Once that pool is
exhausted, \ :c:func:`tracing_map_insert`\  is useless and will return NULL to
signal that state.  There are two user-visible tracing_map
variables, 'hits' and 'drops', which are updated by this function.
Every time an element is either successfully inserted or retrieved,
the 'hits' value is incrememented.  Every time an element insertion
fails, the 'drops' value is incremented.

This is a lock-free tracing map insertion function implementing a
modified form of Cliff Click's basic insertion algorithm.  It
requires the table size be a power of two.  To prevent any
possibility of an infinite loop we always make the internal table
size double the size of the requested table size (max_elts \* 2).
Likewise, we never reuse a slot or resize or delete elements - when
we've reached max_elts entries, we simply return NULL once we've
run out of entries.  Readers can at any point in time traverse the
tracing map and safely access the key/val pairs.

.. _`tracing_map_insert.return`:

Return
------

the tracing_map_elt pointer val associated with the key.
If this was a newly inserted key, the val will be a newly allocated
and associated tracing_map_elt pointer val.  If the key wasn't
found and the pool of tracing_map_elts has been exhausted, NULL is
returned and no further insertions will succeed.

.. _`tracing_map_lookup`:

tracing_map_lookup
==================

.. c:function:: struct tracing_map_elt *tracing_map_lookup(struct tracing_map *map, void *key)

    Retrieve val from a tracing_map

    :param struct tracing_map \*map:
        The tracing_map to perform the lookup on

    :param void \*key:
        The key to look up

.. _`tracing_map_lookup.description`:

Description
-----------

Looks up key in tracing_map and if found returns the matching
tracing_map_elt.  This is a lock-free lookup; see
\ :c:func:`tracing_map_insert`\  for details on tracing_map and how it works.
Every time an element is retrieved, the 'hits' value is
incrememented.  There is one user-visible tracing_map variable,
'hits', which is updated by this function.  Every time an element
is successfully retrieved, the 'hits' value is incrememented.  The
'drops' value is never updated by this function.

.. _`tracing_map_lookup.return`:

Return
------

the tracing_map_elt pointer val associated with the key.
If the key wasn't found, NULL is returned.

.. _`tracing_map_destroy`:

tracing_map_destroy
===================

.. c:function:: void tracing_map_destroy(struct tracing_map *map)

    Destroy a tracing_map

    :param struct tracing_map \*map:
        The tracing_map to destroy

.. _`tracing_map_destroy.description`:

Description
-----------

Frees a tracing_map along with its associated array of
tracing_map_elts.

Callers should make sure there are no readers or writers actively
reading or inserting into the map before calling this.

.. _`tracing_map_clear`:

tracing_map_clear
=================

.. c:function:: void tracing_map_clear(struct tracing_map *map)

    Clear a tracing_map

    :param struct tracing_map \*map:
        The tracing_map to clear

.. _`tracing_map_clear.description`:

Description
-----------

Resets the tracing map to a cleared or initial state.  The
tracing_map_elts are all cleared, and the array of struct
tracing_map_entry is reset to an initialized state.

Callers should make sure there are no writers actively inserting
into the map before calling this.

.. _`tracing_map_create`:

tracing_map_create
==================

.. c:function:: struct tracing_map *tracing_map_create(unsigned int map_bits, unsigned int key_size, const struct tracing_map_ops *ops, void *private_data)

    Create a lock-free map and element pool

    :param unsigned int map_bits:
        The size of the map (2 \*\* map_bits)

    :param unsigned int key_size:
        The size of the key for the map in bytes

    :param const struct tracing_map_ops \*ops:
        Optional client-defined tracing_map_ops instance

    :param void \*private_data:
        Client data associated with the map

.. _`tracing_map_create.description`:

Description
-----------

Creates and sets up a map to contain 2 \*\* map_bits number of
elements (internally maintained as 'max_elts' in struct
tracing_map).  Before using, map fields should be added to the map
with \ :c:func:`tracing_map_add_sum_field`\  and \ :c:func:`tracing_map_add_key_field`\ .
\ :c:func:`tracing_map_init`\  should then be called to allocate the array of
tracing_map_elts, in order to avoid allocating anything in the map
insertion path.  The user-specified map size reflects the maximum
number of elements that can be contained in the table requested by
the user - internally we double that in order to keep the table
sparse and keep collisions manageable.

A tracing_map is a special-purpose map designed to aggregate or
'sum' one or more values associated with a specific object of type
tracing_map_elt, which is attached by the map to a given key.

\ :c:func:`tracing_map_create`\  sets up the map itself, and provides
operations for inserting tracing_map_elts, but doesn't allocate the
tracing_map_elts themselves, or provide a means for describing the
keys or sums associated with the tracing_map_elts.  All
tracing_map_elts for a given map have the same set of sums and
keys, which are defined by the client using the functions
\ :c:func:`tracing_map_add_key_field`\  and \ :c:func:`tracing_map_add_sum_field`\ .  Once
the fields are defined, the pool of elements allocated for the map
can be created, which occurs when the client code calls
\ :c:func:`tracing_map_init`\ .

When \ :c:func:`tracing_map_init`\  returns, tracing_map_elt elements can be
inserted into the map using \ :c:func:`tracing_map_insert`\ .  When called,
\ :c:func:`tracing_map_insert`\  grabs a free tracing_map_elt from the pool, or
finds an existing match in the map and in either case returns it.
The client can then use \ :c:func:`tracing_map_update_sum`\  and
\ :c:func:`tracing_map_read_sum`\  to update or read a given sum field for the
tracing_map_elt.

The client can at any point retrieve and traverse the current set
of inserted tracing_map_elts in a tracing_map, via
\ :c:func:`tracing_map_sort_entries`\ .  Sorting can be done on any field,
including keys.

See tracing_map.h for a description of tracing_map_ops.

.. _`tracing_map_create.return`:

Return
------

the tracing_map pointer if successful, ERR_PTR if not.

.. _`tracing_map_init`:

tracing_map_init
================

.. c:function:: int tracing_map_init(struct tracing_map *map)

    Allocate and clear a map's tracing_map_elts

    :param struct tracing_map \*map:
        The tracing_map to initialize

.. _`tracing_map_init.description`:

Description
-----------

Allocates a clears a pool of tracing_map_elts equal to the
user-specified size of 2 \*\* map_bits (internally maintained as
'max_elts' in struct tracing_map).  Before using, the map fields
should be added to the map with \ :c:func:`tracing_map_add_sum_field`\  and
\ :c:func:`tracing_map_add_key_field`\ .  \ :c:func:`tracing_map_init`\  should then be
called to allocate the array of tracing_map_elts, in order to avoid
allocating anything in the map insertion path.  The user-specified
map size reflects the max number of elements requested by the user
- internally we double that in order to keep the table sparse and
keep collisions manageable.

See tracing_map.h for a description of tracing_map_ops.

.. _`tracing_map_init.return`:

Return
------

the tracing_map pointer if successful, ERR_PTR if not.

.. _`tracing_map_destroy_sort_entries`:

tracing_map_destroy_sort_entries
================================

.. c:function:: void tracing_map_destroy_sort_entries(struct tracing_map_sort_entry **entries, unsigned int n_entries)

    Destroy an array of sort entries

    :param struct tracing_map_sort_entry \*\*entries:
        The entries to destroy

    :param unsigned int n_entries:
        The number of entries in the array

.. _`tracing_map_destroy_sort_entries.description`:

Description
-----------

Destroy the elements returned by a \ :c:func:`tracing_map_sort_entries`\  call.

.. _`tracing_map_sort_entries`:

tracing_map_sort_entries
========================

.. c:function:: int tracing_map_sort_entries(struct tracing_map *map, struct tracing_map_sort_key *sort_keys, unsigned int n_sort_keys, struct tracing_map_sort_entry ***sort_entries)

    Sort the current set of tracing_map_elts in a map

    :param struct tracing_map \*map:
        The tracing_map

    :param struct tracing_map_sort_key \*sort_keys:
        *undescribed*

    :param unsigned int n_sort_keys:
        *undescribed*

    :param struct tracing_map_sort_entry \*\*\*sort_entries:
        outval: pointer to allocated and sorted array of entries

.. _`tracing_map_sort_entries.description`:

Description
-----------

\ :c:func:`tracing_map_sort_entries`\  sorts the current set of entries in the
map and returns the list of tracing_map_sort_entries containing
them to the client in the sort_entries param.  The client can
access the struct tracing_map_elt element of interest directly as
the 'elt' field of a returned struct tracing_map_sort_entry object.

.. _`tracing_map_sort_entries.the-sort_key-has-only-two-fields`:

The sort_key has only two fields
--------------------------------

idx and descending.  'idx' refers
to the index of the field added via \ :c:func:`tracing_map_add_sum_field`\  or
\ :c:func:`tracing_map_add_key_field`\  when the tracing_map was initialized.
'descending' is a flag that if set reverses the sort order, which
by default is ascending.

The client should not hold on to the returned array but should use
it and call \ :c:func:`tracing_map_destroy_sort_entries`\  when done.

.. _`tracing_map_sort_entries.return`:

Return
------

the number of sort_entries in the struct tracing_map_sort_entry
array, negative on error

.. This file was automatic generated / don't edit.

