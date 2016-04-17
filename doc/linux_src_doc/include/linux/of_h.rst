.. -*- coding: utf-8; mode: rst -*-

====
of.h
====


.. _`of_property_count_u8_elems`:

of_property_count_u8_elems
==========================

.. c:function:: int of_property_count_u8_elems (const struct device_node *np, const char *propname)

    Count the number of u8 elements in a property

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.



.. _`of_property_count_u8_elems.description`:

Description
-----------

Search for a property in a device node and count the number of u8 elements
in it. Returns number of elements on sucess, -EINVAL if the property does
not exist or its length does not match a multiple of u8 and -ENODATA if the
property does not have a value.



.. _`of_property_count_u16_elems`:

of_property_count_u16_elems
===========================

.. c:function:: int of_property_count_u16_elems (const struct device_node *np, const char *propname)

    Count the number of u16 elements in a property

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.



.. _`of_property_count_u16_elems.description`:

Description
-----------

Search for a property in a device node and count the number of u16 elements
in it. Returns number of elements on sucess, -EINVAL if the property does
not exist or its length does not match a multiple of u16 and -ENODATA if the
property does not have a value.



.. _`of_property_count_u32_elems`:

of_property_count_u32_elems
===========================

.. c:function:: int of_property_count_u32_elems (const struct device_node *np, const char *propname)

    Count the number of u32 elements in a property

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.



.. _`of_property_count_u32_elems.description`:

Description
-----------

Search for a property in a device node and count the number of u32 elements
in it. Returns number of elements on sucess, -EINVAL if the property does
not exist or its length does not match a multiple of u32 and -ENODATA if the
property does not have a value.



.. _`of_property_count_u64_elems`:

of_property_count_u64_elems
===========================

.. c:function:: int of_property_count_u64_elems (const struct device_node *np, const char *propname)

    Count the number of u64 elements in a property

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.



.. _`of_property_count_u64_elems.description`:

Description
-----------

Search for a property in a device node and count the number of u64 elements
in it. Returns number of elements on sucess, -EINVAL if the property does
not exist or its length does not match a multiple of u64 and -ENODATA if the
property does not have a value.



.. _`of_property_read_string_array`:

of_property_read_string_array
=============================

.. c:function:: int of_property_read_string_array (const struct device_node *np, const char *propname, const char **out_strs, size_t sz)

    Read an array of strings from a multiple strings property.

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.

    :param const char \*\*out_strs:
        output array of string pointers.

    :param size_t sz:
        number of array elements to read.



.. _`of_property_read_string_array.description`:

Description
-----------

Search for a property in a device tree node and retrieve a list of
terminated string values (pointer to data, not a copy) in that property.

If ``out_strs`` is NULL, the number of strings in the property is returned.



.. _`of_property_count_strings`:

of_property_count_strings
=========================

.. c:function:: int of_property_count_strings (const struct device_node *np, const char *propname)

    Find and return the number of strings from a multiple strings property.

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.



.. _`of_property_count_strings.description`:

Description
-----------

Search for a property in a device tree node and retrieve the number of null
terminated string contain in it. Returns the number of strings on
success, -EINVAL if the property does not exist, -ENODATA if property
does not have a value, and -EILSEQ if the string is not null-terminated
within the length of the property data.



.. _`of_property_read_string_index`:

of_property_read_string_index
=============================

.. c:function:: int of_property_read_string_index (const struct device_node *np, const char *propname, int index, const char **output)

    Find and read a string from a multiple strings property.

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.

    :param int index:
        index of the string in the list of strings

    :param const char \*\*output:

        *undescribed*



.. _`of_property_read_string_index.description`:

Description
-----------

Search for a property in a device tree node and retrieve a null
terminated string value (pointer to data, not a copy) in the list of strings
contained in that property.
Returns 0 on success, -EINVAL if the property does not exist, -ENODATA if
property does not have a value, and -EILSEQ if the string is not
null-terminated within the length of the property data.

The out_string pointer is modified only if a valid string can be decoded.



.. _`of_property_read_bool`:

of_property_read_bool
=====================

.. c:function:: bool of_property_read_bool (const struct device_node *np, const char *propname)

    Findfrom a property

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.



.. _`of_property_read_bool.description`:

Description
-----------

Search for a property in a device node.
Returns true if the property exists false otherwise.



.. _`of_changeset_entry`:

struct of_changeset_entry
=========================

.. c:type:: of_changeset_entry

    Holds a changeset entry


.. _`of_changeset_entry.definition`:

Definition
----------

.. code-block:: c

  struct of_changeset_entry {
    struct list_head node;
    unsigned long action;
    struct device_node * np;
    struct property * prop;
    struct property * old_prop;
  };


.. _`of_changeset_entry.members`:

Members
-------

:``node``:
    list_head for the log list

:``action``:
    notifier action

:``np``:
    pointer to the device node affected

:``prop``:
    pointer to the property affected

:``old_prop``:
    hold a pointer to the original property




.. _`of_changeset_entry.description`:

Description
-----------

Every modification of the device tree during a changeset
is held in a list of of_changeset_entry structures.
That way we can recover from a partial application, or we can
revert the changeset



.. _`of_changeset`:

struct of_changeset
===================

.. c:type:: of_changeset

    changeset tracker structure


.. _`of_changeset.definition`:

Definition
----------

.. code-block:: c

  struct of_changeset {
    struct list_head entries;
  };


.. _`of_changeset.members`:

Members
-------

:``entries``:
    list_head for the changeset entries




.. _`of_changeset.description`:

Description
-----------

changesets are a convenient way to apply bulk changes to the
live tree. In case of an error, changes are rolled-back.
changesets live on after initial application, and if not
destroyed after use, they can be reverted in one single call.



.. _`of_device_is_system_power_controller`:

of_device_is_system_power_controller
====================================

.. c:function:: bool of_device_is_system_power_controller (const struct device_node *np)

    Tells if system-power-controller is found for device_node

    :param const struct device_node \*np:
        Pointer to the given device_node



.. _`of_device_is_system_power_controller.description`:

Description
-----------

return true if present false otherwise

