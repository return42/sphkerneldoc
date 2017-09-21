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
        bool is_string;
        union pointer;
        union value;
         };
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

is_string
    True when property is a string.

pointer
    Pointer to the property (an array of items of the given type).

value
    Value of the property (when it is a single item of the given type).

}
    *undescribed*

.. This file was automatic generated / don't edit.

