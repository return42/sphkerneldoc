.. -*- coding: utf-8; mode: rst -*-

==========
property.h
==========


.. _`property_entry`:

struct property_entry
=====================

.. c:type:: property_entry

    "Built-in" device property representation.


.. _`property_entry.definition`:

Definition
----------

.. code-block:: c

  struct property_entry {
    const char * name;
    size_t length;
    bool is_array;
    bool is_string;
    union {unnamed_union};
  };


.. _`property_entry.members`:

Members
-------

:``name``:
    Name of the property.

:``length``:
    Length of data making up the value.

:``is_array``:
    True when the property is an array.

:``is_string``:
    True when property is a string.

:``{unnamed_union}``:
    anonymous




.. _`property_set`:

struct property_set
===================

.. c:type:: property_set

    Collection of "built-in" device properties.


.. _`property_set.definition`:

Definition
----------

.. code-block:: c

  struct property_set {
    struct fwnode_handle fwnode;
    struct property_entry * properties;
  };


.. _`property_set.members`:

Members
-------

:``fwnode``:
    Handle to be pointed to by the fwnode field of struct device.

:``properties``:
    Array of properties terminated with a null entry.


