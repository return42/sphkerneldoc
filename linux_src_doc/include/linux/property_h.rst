.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/property.h

.. _`property_entry`:

struct property_entry
=====================

.. c:type:: struct property_entry

    "Built-in" device property representation.

.. _`property_entry.definition`:

Definition
----------

.. code-block:: c

    struct property_entry {
        const char *name;
        size_t length;
        bool is_array;
        enum dev_prop_type type;
        union {
            union {
                const u8 *u8_data;
                const u16 *u16_data;
                const u32 *u32_data;
                const u64 *u64_data;
                const char * const *str;
            } pointer;
            union {
                u8 u8_data;
                u16 u16_data;
                u32 u32_data;
                u64 u64_data;
                const char *str;
            } value;
        } ;
    }

.. _`property_entry.members`:

Members
-------

name
    Name of the property.

length
    Length of data making up the value.

is_array
    True when the property is an array.

type
    Type of the data in unions.

{unnamed_union}
    anonymous

pointer
    Pointer to the property (an array of items of the given type).

value
    Value of the property (when it is a single item of the given type).

.. This file was automatic generated / don't edit.

