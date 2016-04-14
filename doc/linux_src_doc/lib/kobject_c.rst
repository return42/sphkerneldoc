.. -*- coding: utf-8; mode: rst -*-

=========
kobject.c
=========

.. _`kobject_namespace`:

kobject_namespace
=================

.. c:function:: const void *kobject_namespace (struct kobject *kobj)

    return @kobj's namespace tag

    :param struct kobject \*kobj:
        kobject in question


.. _`kobject_namespace.description`:

Description
-----------

Returns namespace tag of ``kobj`` if its parent has namespace ops enabled
and thus ``kobj`` should have a namespace tag associated with it.  Returns
``NULL`` otherwise.


.. _`kobject_get_path`:

kobject_get_path
================

.. c:function:: char *kobject_get_path (struct kobject *kobj, gfp_t gfp_mask)

    generate and return the path associated with a given kobj and kset pair.

    :param struct kobject \*kobj:
        kobject in question, with which to build the path

    :param gfp_t gfp_mask:
        the allocation type used to allocate the path


.. _`kobject_get_path.description`:

Description
-----------

The result must be freed by the caller with :c:func:`kfree`.


.. _`kobject_set_name_vargs`:

kobject_set_name_vargs
======================

.. c:function:: int kobject_set_name_vargs (struct kobject *kobj, const char *fmt, va_list vargs)

    Set the name of an kobject

    :param struct kobject \*kobj:
        struct kobject to set the name of

    :param const char \*fmt:
        format string used to build the name

    :param va_list vargs:
        vargs to format the string.


.. _`kobject_set_name`:

kobject_set_name
================

.. c:function:: int kobject_set_name (struct kobject *kobj, const char *fmt,  ...)

    Set the name of a kobject

    :param struct kobject \*kobj:
        struct kobject to set the name of

    :param const char \*fmt:
        format string used to build the name

    :param ...:
        variable arguments


.. _`kobject_set_name.description`:

Description
-----------

This sets the name of the kobject.  If you have already added the
kobject to the system, you must call :c:func:`kobject_rename` in order to
change the name of the kobject.


.. _`kobject_init`:

kobject_init
============

.. c:function:: void kobject_init (struct kobject *kobj, struct kobj_type *ktype)

    initialize a kobject structure

    :param struct kobject \*kobj:
        pointer to the kobject to initialize

    :param struct kobj_type \*ktype:
        pointer to the ktype for this kobject.


.. _`kobject_init.description`:

Description
-----------

This function will properly initialize a kobject such that it can then
be passed to the :c:func:`kobject_add` call.

After this function is called, the kobject MUST be cleaned up by a call
to :c:func:`kobject_put`, not by a call to kfree directly to ensure that all of
the memory is cleaned up properly.


.. _`kobject_add`:

kobject_add
===========

.. c:function:: int kobject_add (struct kobject *kobj, struct kobject *parent, const char *fmt,  ...)

    the main kobject add function

    :param struct kobject \*kobj:
        the kobject to add

    :param struct kobject \*parent:
        pointer to the parent of the kobject.

    :param const char \*fmt:
        format to name the kobject with.

    :param ...:
        variable arguments


.. _`kobject_add.description`:

Description
-----------

The kobject name is set and added to the kobject hierarchy in this
function.

If ``parent`` is set, then the parent of the ``kobj`` will be set to it.
If ``parent`` is NULL, then the parent of the ``kobj`` will be set to the
kobject associated with the kset assigned to this kobject.  If no kset
is assigned to the kobject, then the kobject will be located in the
root of the sysfs tree.

If this function returns an error, :c:func:`kobject_put` must be called to
properly clean up the memory associated with the object.
Under no instance should the kobject that is passed to this function
be directly freed with a call to :c:func:`kfree`, that can leak memory.

Note, no "add" uevent will be created with this call, the caller should set
up all of the necessary sysfs files for the object and then call
:c:func:`kobject_uevent` with the UEVENT_ADD parameter to ensure that
userspace is properly notified of this kobject's creation.


.. _`kobject_init_and_add`:

kobject_init_and_add
====================

.. c:function:: int kobject_init_and_add (struct kobject *kobj, struct kobj_type *ktype, struct kobject *parent, const char *fmt,  ...)

    initialize a kobject structure and add it to the kobject hierarchy

    :param struct kobject \*kobj:
        pointer to the kobject to initialize

    :param struct kobj_type \*ktype:
        pointer to the ktype for this kobject.

    :param struct kobject \*parent:
        pointer to the parent of this kobject.

    :param const char \*fmt:
        the name of the kobject.

    :param ...:
        variable arguments


.. _`kobject_init_and_add.description`:

Description
-----------

This function combines the call to :c:func:`kobject_init` and
:c:func:`kobject_add`.  The same type of error handling after a call to
:c:func:`kobject_add` and kobject lifetime rules are the same here.


.. _`kobject_rename`:

kobject_rename
==============

.. c:function:: int kobject_rename (struct kobject *kobj, const char *new_name)

    change the name of an object

    :param struct kobject \*kobj:
        object in question.

    :param const char \*new_name:
        object's new name


.. _`kobject_rename.description`:

Description
-----------

It is the responsibility of the caller to provide mutual
exclusion between two different calls of kobject_rename
on the same kobject and to ensure that new_name is valid and
won't conflict with other kobjects.


.. _`kobject_move`:

kobject_move
============

.. c:function:: int kobject_move (struct kobject *kobj, struct kobject *new_parent)

    move object to another parent

    :param struct kobject \*kobj:
        object in question.

    :param struct kobject \*new_parent:
        object's new parent (can be NULL)


.. _`kobject_del`:

kobject_del
===========

.. c:function:: void kobject_del (struct kobject *kobj)

    unlink kobject from hierarchy.

    :param struct kobject \*kobj:
        object.


.. _`kobject_get`:

kobject_get
===========

.. c:function:: struct kobject *kobject_get (struct kobject *kobj)

    increment refcount for object.

    :param struct kobject \*kobj:
        object.


.. _`kobject_put`:

kobject_put
===========

.. c:function:: void kobject_put (struct kobject *kobj)

    decrement refcount for object.

    :param struct kobject \*kobj:
        object.


.. _`kobject_put.description`:

Description
-----------

Decrement the refcount, and if 0, call :c:func:`kobject_cleanup`.


.. _`kobject_create`:

kobject_create
==============

.. c:function:: struct kobject *kobject_create ( void)

    create a struct kobject dynamically

    :param void:
        no arguments


.. _`kobject_create.description`:

Description
-----------


This function creates a kobject structure dynamically and sets it up
to be a "dynamic" kobject with a default release function set up.

If the kobject was not able to be created, NULL will be returned.
The kobject structure returned from here must be cleaned up with a
call to :c:func:`kobject_put` and not :c:func:`kfree`, as :c:func:`kobject_init` has
already been called on this structure.


.. _`kobject_create_and_add`:

kobject_create_and_add
======================

.. c:function:: struct kobject *kobject_create_and_add (const char *name, struct kobject *parent)

    create a struct kobject dynamically and register it with sysfs

    :param const char \*name:
        the name for the kobject

    :param struct kobject \*parent:
        the parent kobject of this kobject, if any.


.. _`kobject_create_and_add.description`:

Description
-----------

This function creates a kobject structure dynamically and registers it
with sysfs.  When you are finished with this structure, call
:c:func:`kobject_put` and the structure will be dynamically freed when
it is no longer being used.

If the kobject was not able to be created, NULL will be returned.


.. _`kset_init`:

kset_init
=========

.. c:function:: void kset_init (struct kset *k)

    initialize a kset for use

    :param struct kset \*k:
        kset


.. _`kset_register`:

kset_register
=============

.. c:function:: int kset_register (struct kset *k)

    initialize and add a kset.

    :param struct kset \*k:
        kset.


.. _`kset_unregister`:

kset_unregister
===============

.. c:function:: void kset_unregister (struct kset *k)

    remove a kset.

    :param struct kset \*k:
        kset.


.. _`kset_find_obj`:

kset_find_obj
=============

.. c:function:: struct kobject *kset_find_obj (struct kset *kset, const char *name)

    search for object in kset.

    :param struct kset \*kset:
        kset we're looking in.

    :param const char \*name:
        object's name.


.. _`kset_find_obj.description`:

Description
-----------

Lock kset via ``kset``\ ->subsys, and iterate over ``kset``\ ->list,
looking for a matching kobject. If matching object is found
take a reference and return the object.


.. _`kset_create`:

kset_create
===========

.. c:function:: struct kset *kset_create (const char *name, const struct kset_uevent_ops *uevent_ops, struct kobject *parent_kobj)

    create a struct kset dynamically

    :param const char \*name:
        the name for the kset

    :param const struct kset_uevent_ops \*uevent_ops:
        a struct kset_uevent_ops for the kset

    :param struct kobject \*parent_kobj:
        the parent kobject of this kset, if any.


.. _`kset_create.description`:

Description
-----------

This function creates a kset structure dynamically.  This structure can
then be registered with the system and show up in sysfs with a call to
:c:func:`kset_register`.  When you are finished with this structure, if
:c:func:`kset_register` has been called, call :c:func:`kset_unregister` and the
structure will be dynamically freed when it is no longer being used.

If the kset was not able to be created, NULL will be returned.


.. _`kset_create_and_add`:

kset_create_and_add
===================

.. c:function:: struct kset *kset_create_and_add (const char *name, const struct kset_uevent_ops *uevent_ops, struct kobject *parent_kobj)

    create a struct kset dynamically and add it to sysfs

    :param const char \*name:
        the name for the kset

    :param const struct kset_uevent_ops \*uevent_ops:
        a struct kset_uevent_ops for the kset

    :param struct kobject \*parent_kobj:
        the parent kobject of this kset, if any.


.. _`kset_create_and_add.description`:

Description
-----------

This function creates a kset structure dynamically and registers it
with sysfs.  When you are finished with this structure, call
:c:func:`kset_unregister` and the structure will be dynamically freed when it
is no longer being used.

If the kset was not able to be created, NULL will be returned.

