.. -*- coding: utf-8; mode: rst -*-

============
flex_array.c
============


.. _`flex_array_alloc`:

flex_array_alloc
================

.. c:function:: struct flex_array *flex_array_alloc (int element_size, unsigned int total, gfp_t flags)

    allocate a new flexible array

    :param int element_size:
        the size of individual elements in the array

    :param unsigned int total:
        total number of elements that this should hold

    :param gfp_t flags:
        page allocation flags to use for base array



.. _`flex_array_alloc.note`:

Note
----

all locking must be provided by the caller.

``total`` is used to size internal structures.  If the user ever
accesses any array indexes >=\ ``total``\ , it will produce errors.



.. _`flex_array_alloc.the-maximum-number-of-elements-is-defined-as`:

The maximum number of elements is defined as
--------------------------------------------

the number of
elements that can be stored in a page times the number of
page pointers that we can fit in the base structure or (using
integer math)::

        (PAGE_SIZE/element_size) * (PAGE_SIZE-8)/sizeof(void *)

Here's a table showing example capacities.  Note that the maximum
index that the get/:c:func:`put` functions is just nr_objects-1.   This
basically means that you get 4MB of storage on 32-bit and 2MB on
64-bit.


Element size | Objects | Objects |
PAGE_SIZE=4k |  32-bit |  64-bit |
---------------------------------|

     1 bytes | 4177920 | 2088960 |
     2 bytes | 2088960 | 1044480 |
     3 bytes | 1392300 |  696150 |
     4 bytes | 1044480 |  522240 |
    32 bytes |  130560 |   65408 |
    33 bytes |  126480 |   63240 |
  2048 bytes |    2040 |    1020 |
  2049 bytes |    1020 |     510 |
      void * | 1044480 |  261120 |

Since 64-bit pointers are twice the size, we lose half the
capacity in the base structure.  Also note that no effort is made
to efficiently pack objects across page boundaries.



.. _`flex_array_free_parts`:

flex_array_free_parts
=====================

.. c:function:: void flex_array_free_parts (struct flex_array *fa)

    just free the second-level pages

    :param struct flex_array \*fa:
        the flex array from which to free parts



.. _`flex_array_free_parts.description`:

Description
-----------

This is to be used in cases where the base 'struct flex_array'
has been statically allocated and should not be free.



.. _`flex_array_put`:

flex_array_put
==============

.. c:function:: int flex_array_put (struct flex_array *fa, unsigned int element_nr, void *src, gfp_t flags)

    copy data into the array at @element_nr

    :param struct flex_array \*fa:
        the flex array to copy data into

    :param unsigned int element_nr:
        index of the position in which to insert
        the new element.

    :param void \*src:
        address of data to copy into the array

    :param gfp_t flags:
        page allocation flags to use for array expansion



.. _`flex_array_put.description`:

Description
-----------


Note that this \*copies\* the contents of ``src`` into
the array.  If you are trying to store an array of
pointers, make sure to pass in :c:type:`struct ptr <ptr>` instead of ptr.
You may instead wish to use the :c:func:`flex_array_put_ptr`
helper function.

Locking must be provided by the caller.



.. _`flex_array_clear`:

flex_array_clear
================

.. c:function:: int flex_array_clear (struct flex_array *fa, unsigned int element_nr)

    clear element in array at @element_nr

    :param struct flex_array \*fa:
        the flex array of the element.

    :param unsigned int element_nr:
        index of the position to clear.



.. _`flex_array_clear.description`:

Description
-----------

Locking must be provided by the caller.



.. _`flex_array_prealloc`:

flex_array_prealloc
===================

.. c:function:: int flex_array_prealloc (struct flex_array *fa, unsigned int start, unsigned int nr_elements, gfp_t flags)

    guarantee that array space exists

    :param struct flex_array \*fa:
        the flex array for which to preallocate parts

    :param unsigned int start:
        index of first array element for which space is allocated

    :param unsigned int nr_elements:
        number of elements for which space is allocated

    :param gfp_t flags:
        page allocation flags



.. _`flex_array_prealloc.description`:

Description
-----------

This will guarantee that no future calls to :c:func:`flex_array_put`
will allocate memory.  It can be used if you are expecting to
be holding a lock or in some atomic context while writing
data into the array.

Locking must be provided by the caller.



.. _`flex_array_get`:

flex_array_get
==============

.. c:function:: void *flex_array_get (struct flex_array *fa, unsigned int element_nr)

    pull data back out of the array

    :param struct flex_array \*fa:
        the flex array from which to extract data

    :param unsigned int element_nr:
        index of the element to fetch from the array



.. _`flex_array_get.description`:

Description
-----------

Returns a pointer to the data at index ``element_nr``\ .  Note
that this is a copy of the data that was passed in.  If you
are using this to store pointers, you'll get back :c:type:`struct ptr <ptr>`.  You
may instead wish to use the flex_array_get_ptr helper.

Locking must be provided by the caller.



.. _`flex_array_get_ptr`:

flex_array_get_ptr
==================

.. c:function:: void *flex_array_get_ptr (struct flex_array *fa, unsigned int element_nr)

    pull a ptr back out of the array

    :param struct flex_array \*fa:
        the flex array from which to extract data

    :param unsigned int element_nr:
        index of the element to fetch from the array



.. _`flex_array_get_ptr.description`:

Description
-----------

Returns the pointer placed in the flex array at element_nr using
:c:func:`flex_array_put_ptr`.  This function should not be called if the
element in question was not set using the :c:func:`_put_ptr` helper.



.. _`flex_array_shrink`:

flex_array_shrink
=================

.. c:function:: int flex_array_shrink (struct flex_array *fa)

    free unused second-level pages

    :param struct flex_array \*fa:
        the flex array to shrink



.. _`flex_array_shrink.description`:

Description
-----------

Frees all second-level pages that consist solely of unused
elements.  Returns the number of pages freed.

Locking must be provided by the caller.

