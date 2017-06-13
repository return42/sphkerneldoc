.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/flex_array.h

.. _`flex_array_alloc`:

flex_array_alloc
================

.. c:function:: struct flex_array *flex_array_alloc(int element_size, unsigned int total, gfp_t flags)

    Creates a flexible array.

    :param int element_size:
        individual object size.

    :param unsigned int total:
        maximum number of objects which can be stored.

    :param gfp_t flags:
        GFP flags

.. _`flex_array_alloc.return`:

Return
------

Returns an object of structure flex_array.

.. _`flex_array_prealloc`:

flex_array_prealloc
===================

.. c:function:: int flex_array_prealloc(struct flex_array *fa, unsigned int start, unsigned int nr_elements, gfp_t flags)

    Ensures that memory for the elements indexed in the range defined by start and nr_elements has been allocated.

    :param struct flex_array \*fa:
        array to allocate memory to.

    :param unsigned int start:
        start address

    :param unsigned int nr_elements:
        number of elements to be allocated.

    :param gfp_t flags:
        GFP flags

.. _`flex_array_free`:

flex_array_free
===============

.. c:function:: void flex_array_free(struct flex_array *fa)

    Removes all elements of a flexible array.

    :param struct flex_array \*fa:
        array to be freed.

.. _`flex_array_free_parts`:

flex_array_free_parts
=====================

.. c:function:: void flex_array_free_parts(struct flex_array *fa)

    Removes all elements of a flexible array, but leaves the array itself in place.

    :param struct flex_array \*fa:
        array to be emptied.

.. _`flex_array_put`:

flex_array_put
==============

.. c:function:: int flex_array_put(struct flex_array *fa, unsigned int element_nr, void *src, gfp_t flags)

    Stores data into a flexible array.

    :param struct flex_array \*fa:
        array where element is to be stored.

    :param unsigned int element_nr:
        position to copy, must be less than the maximum specified when
        the array was created.

    :param void \*src:
        data source to be copied into the array.

    :param gfp_t flags:
        GFP flags

.. _`flex_array_put.return`:

Return
------

Returns zero on success, a negative error code otherwise.

.. _`flex_array_clear`:

flex_array_clear
================

.. c:function:: int flex_array_clear(struct flex_array *fa, unsigned int element_nr)

    Clears an individual element in the array, sets the given element to FLEX_ARRAY_FREE.

    :param struct flex_array \*fa:
        array to which element to be cleared belongs.

    :param unsigned int element_nr:
        element position to clear.

.. _`flex_array_clear.return`:

Return
------

Returns zero on success, -EINVAL otherwise.

.. _`flex_array_get`:

flex_array_get
==============

.. c:function:: void *flex_array_get(struct flex_array *fa, unsigned int element_nr)

    Retrieves data into a flexible array.

    :param struct flex_array \*fa:
        array from which data is to be retrieved.

    :param unsigned int element_nr:
        Element position to retrieve data from.

.. _`flex_array_get.return`:

Return
------

Returns a pointer to the data element, or NULL if that
             particular element has never been allocated.

.. _`flex_array_shrink`:

flex_array_shrink
=================

.. c:function:: int flex_array_shrink(struct flex_array *fa)

    Reduces the allocated size of an array.

    :param struct flex_array \*fa:
        array to shrink.

.. _`flex_array_shrink.return`:

Return
------

Returns number of pages of memory actually freed.

.. This file was automatic generated / don't edit.

