.. -*- coding: utf-8; mode: rst -*-

=======
sysfs.h
=======


.. _`sysfs_attr_init`:

sysfs_attr_init
===============

.. c:function:: sysfs_attr_init ( attr)

    initialize a dynamically allocated sysfs attribute

    :param attr:
        struct attribute to initialize



.. _`sysfs_attr_init.description`:

Description
-----------

Initialize a dynamically allocated struct attribute so we can
make lockdep happy.  This is a new requirement for attributes
and initially this is only needed when lockdep is enabled.
Lockdep gives a nice error when your attribute is added to
sysfs if you don't have this.



.. _`attribute_group`:

struct attribute_group
======================

.. c:type:: attribute_group

    data structure used to declare an attribute group.


.. _`attribute_group.definition`:

Definition
----------

.. code-block:: c

  struct attribute_group {
    const char * name;
    umode_t (* is_visible) (struct kobject *,struct attribute *, int);
    struct attribute ** attrs;
    struct bin_attribute ** bin_attrs;
  };


.. _`attribute_group.members`:

Members
-------

:``name``:
    Optional: Attribute group name
    If specified, the attribute group will be created in
    a new subdirectory with this name.

:``is_visible``:
    Optional: Function to return permissions associated with an
    attribute of the group. Will be called repeatedly for each
    non-binary attribute in the group. Only read/write
    permissions as well as SYSFS_PREALLOC are accepted. Must
    return 0 if an attribute is not visible. The returned value
    will replace static permissions defined in struct attribute.

:``attrs``:
    Pointer to NULL terminated list of attributes.

:``bin_attrs``:
    Pointer to NULL terminated list of binary attributes.
    Either attrs or bin_attrs or both must be provided.




.. _`attribute_group.optional`:

Optional
--------

Function to return permissions associated with a
binary attribute of the group. Will be called repeatedly
for each binary attribute in the group. Only read/write
permissions as well as SYSFS_PREALLOC are accepted. Must
return 0 if a binary attribute is not visible. The returned
value will replace static permissions defined in
struct bin_attribute.



.. _`sysfs_prealloc`:

SYSFS_PREALLOC
==============

.. c:function:: SYSFS_PREALLOC ()



.. _`sysfs_prealloc.description`:

Description
-----------

for examples..



.. _`sysfs_bin_attr_init`:

sysfs_bin_attr_init
===================

.. c:function:: sysfs_bin_attr_init ( bin_attr)

    initialize a dynamically allocated bin_attribute

    :param bin_attr:

        *undescribed*



.. _`sysfs_bin_attr_init.description`:

Description
-----------

Initialize a dynamically allocated struct bin_attribute so we
can make lockdep happy.  This is a new requirement for
attributes and initially this is only needed when lockdep is
enabled.  Lockdep gives a nice error when your attribute is
added to sysfs if you don't have this.

