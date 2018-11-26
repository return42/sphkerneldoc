.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/assoc_array.c

.. _`assoc_array_iterate`:

assoc_array_iterate
===================

.. c:function:: int assoc_array_iterate(const struct assoc_array *array, int (*iterator)(const void *object, void *iterator_data), void *iterator_data)

    Pass all objects in the array to a callback

    :param array:
        The array to iterate over.
    :type array: const struct assoc_array \*

    :param int (\*iterator)(const void \*object, void \*iterator_data):
        The callback function.

    :param iterator_data:
        Private data for the callback function.
    :type iterator_data: void \*

.. _`assoc_array_iterate.description`:

Description
-----------

Iterate over all the objects in an associative array.  Each one will be
presented to the iterator function.

If the array is being modified concurrently with the iteration then it is
possible that some objects in the array will be passed to the iterator
callback more than once - though every object should be passed at least
once.  If this is undesirable then the caller must lock against modification
for the duration of this function.

The function will return 0 if no objects were in the array or else it will
return the result of the last iterator function called.  Iteration stops
immediately if any call to the iteration function results in a non-zero
return.

The caller should hold the RCU read lock or better if concurrent
modification is possible.

.. _`assoc_array_find`:

assoc_array_find
================

.. c:function:: void *assoc_array_find(const struct assoc_array *array, const struct assoc_array_ops *ops, const void *index_key)

    Find an object by index key

    :param array:
        The associative array to search.
    :type array: const struct assoc_array \*

    :param ops:
        The operations to use.
    :type ops: const struct assoc_array_ops \*

    :param index_key:
        The key to the object.
    :type index_key: const void \*

.. _`assoc_array_find.description`:

Description
-----------

Find an object in an associative array by walking through the internal tree
to the node that should contain the object and then searching the leaves
there.  NULL is returned if the requested object was not found in the array.

The caller must hold the RCU read lock or better.

.. _`assoc_array_destroy`:

assoc_array_destroy
===================

.. c:function:: void assoc_array_destroy(struct assoc_array *array, const struct assoc_array_ops *ops)

    Destroy an associative array

    :param array:
        The array to destroy.
    :type array: struct assoc_array \*

    :param ops:
        The operations to use.
    :type ops: const struct assoc_array_ops \*

.. _`assoc_array_destroy.description`:

Description
-----------

Discard all metadata and free all objects in an associative array.  The
array will be empty and ready to use again upon completion.  This function
cannot fail.

The caller must prevent all other accesses whilst this takes place as no
attempt is made to adjust pointers gracefully to permit RCU readlock-holding
accesses to continue.  On the other hand, no memory allocation is required.

.. _`assoc_array_insert`:

assoc_array_insert
==================

.. c:function:: struct assoc_array_edit *assoc_array_insert(struct assoc_array *array, const struct assoc_array_ops *ops, const void *index_key, void *object)

    Script insertion of an object into an associative array

    :param array:
        The array to insert into.
    :type array: struct assoc_array \*

    :param ops:
        The operations to use.
    :type ops: const struct assoc_array_ops \*

    :param index_key:
        The key to insert at.
    :type index_key: const void \*

    :param object:
        The object to insert.
    :type object: void \*

.. _`assoc_array_insert.description`:

Description
-----------

Precalculate and preallocate a script for the insertion or replacement of an
object in an associative array.  This results in an edit script that can
either be applied or cancelled.

The function returns a pointer to an edit script or -ENOMEM.

The caller should lock against other modifications and must continue to hold
the lock until \ :c:func:`assoc_array_apply_edit`\  has been called.

Accesses to the tree may take place concurrently with this function,
provided they hold the RCU read lock.

.. _`assoc_array_insert_set_object`:

assoc_array_insert_set_object
=============================

.. c:function:: void assoc_array_insert_set_object(struct assoc_array_edit *edit, void *object)

    Set the new object pointer in an edit script

    :param edit:
        The edit script to modify.
    :type edit: struct assoc_array_edit \*

    :param object:
        The object pointer to set.
    :type object: void \*

.. _`assoc_array_insert_set_object.description`:

Description
-----------

Change the object to be inserted in an edit script.  The object pointed to
by the old object is not freed.  This must be done prior to applying the
script.

.. _`assoc_array_delete`:

assoc_array_delete
==================

.. c:function:: struct assoc_array_edit *assoc_array_delete(struct assoc_array *array, const struct assoc_array_ops *ops, const void *index_key)

    Script deletion of an object from an associative array

    :param array:
        The array to search.
    :type array: struct assoc_array \*

    :param ops:
        The operations to use.
    :type ops: const struct assoc_array_ops \*

    :param index_key:
        The key to the object.
    :type index_key: const void \*

.. _`assoc_array_delete.description`:

Description
-----------

Precalculate and preallocate a script for the deletion of an object from an
associative array.  This results in an edit script that can either be
applied or cancelled.

The function returns a pointer to an edit script if the object was found,
NULL if the object was not found or -ENOMEM.

The caller should lock against other modifications and must continue to hold
the lock until \ :c:func:`assoc_array_apply_edit`\  has been called.

Accesses to the tree may take place concurrently with this function,
provided they hold the RCU read lock.

.. _`assoc_array_clear`:

assoc_array_clear
=================

.. c:function:: struct assoc_array_edit *assoc_array_clear(struct assoc_array *array, const struct assoc_array_ops *ops)

    Script deletion of all objects from an associative array

    :param array:
        The array to clear.
    :type array: struct assoc_array \*

    :param ops:
        The operations to use.
    :type ops: const struct assoc_array_ops \*

.. _`assoc_array_clear.description`:

Description
-----------

Precalculate and preallocate a script for the deletion of all the objects
from an associative array.  This results in an edit script that can either
be applied or cancelled.

The function returns a pointer to an edit script if there are objects to be
deleted, NULL if there are no objects in the array or -ENOMEM.

The caller should lock against other modifications and must continue to hold
the lock until \ :c:func:`assoc_array_apply_edit`\  has been called.

Accesses to the tree may take place concurrently with this function,
provided they hold the RCU read lock.

.. _`assoc_array_apply_edit`:

assoc_array_apply_edit
======================

.. c:function:: void assoc_array_apply_edit(struct assoc_array_edit *edit)

    Apply an edit script to an associative array

    :param edit:
        The script to apply.
    :type edit: struct assoc_array_edit \*

.. _`assoc_array_apply_edit.description`:

Description
-----------

Apply an edit script to an associative array to effect an insertion,
deletion or clearance.  As the edit script includes preallocated memory,
this is guaranteed not to fail.

The edit script, dead objects and dead metadata will be scheduled for
destruction after an RCU grace period to permit those doing read-only
accesses on the array to continue to do so under the RCU read lock whilst
the edit is taking place.

.. _`assoc_array_cancel_edit`:

assoc_array_cancel_edit
=======================

.. c:function:: void assoc_array_cancel_edit(struct assoc_array_edit *edit)

    Discard an edit script.

    :param edit:
        The script to discard.
    :type edit: struct assoc_array_edit \*

.. _`assoc_array_cancel_edit.description`:

Description
-----------

Free an edit script and all the preallocated data it holds without making
any changes to the associative array it was intended for.

NOTE!  In the case of an insertion script, this does \_not\_ release the leaf
that was to be inserted.  That is left to the caller.

.. _`assoc_array_gc`:

assoc_array_gc
==============

.. c:function:: int assoc_array_gc(struct assoc_array *array, const struct assoc_array_ops *ops, bool (*iterator)(void *object, void *iterator_data), void *iterator_data)

    Garbage collect an associative array.

    :param array:
        The array to clean.
    :type array: struct assoc_array \*

    :param ops:
        The operations to use.
    :type ops: const struct assoc_array_ops \*

    :param bool (\*iterator)(void \*object, void \*iterator_data):
        A callback function to pass judgement on each object.

    :param iterator_data:
        Private data for the callback function.
    :type iterator_data: void \*

.. _`assoc_array_gc.description`:

Description
-----------

Collect garbage from an associative array and pack down the internal tree to
save memory.

The iterator function is asked to pass judgement upon each object in the
array.  If it returns false, the object is discard and if it returns true,
the object is kept.  If it returns true, it must increment the object's
usage count (or whatever it needs to do to retain it) before returning.

This function returns 0 if successful or -ENOMEM if out of memory.  In the
latter case, the array is not changed.

The caller should lock against other modifications and must continue to hold
the lock until \ :c:func:`assoc_array_apply_edit`\  has been called.

Accesses to the tree may take place concurrently with this function,
provided they hold the RCU read lock.

.. This file was automatic generated / don't edit.

