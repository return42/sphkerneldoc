.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/android/ashmem.c

.. _`ashmem_area`:

struct ashmem_area
==================

.. c:type:: struct ashmem_area

    The anonymous shared memory area

.. _`ashmem_area.definition`:

Definition
----------

.. code-block:: c

    struct ashmem_area {
        char name[ASHMEM_FULL_NAME_LEN];
        struct list_head unpinned_list;
        struct file *file;
        size_t size;
        unsigned long prot_mask;
    }

.. _`ashmem_area.members`:

Members
-------

name
    The optional name in /proc/pid/maps

unpinned_list
    The list of all ashmem areas

file
    The shmem-based backing file

size
    The size of the mapping, in bytes

prot_mask
    The allowed protection bits, as vm_flags

.. _`ashmem_area.description`:

Description
-----------

The lifecycle of this structure is from our parent file's \ :c:func:`open`\  until
its \ :c:func:`release`\ . It is also protected by 'ashmem_mutex'

.. _`ashmem_area.warning`:

Warning
-------

Mappings do NOT pin this structure; It dies on \ :c:func:`close`\ 

.. _`ashmem_range`:

struct ashmem_range
===================

.. c:type:: struct ashmem_range

    A range of unpinned/evictable pages

.. _`ashmem_range.definition`:

Definition
----------

.. code-block:: c

    struct ashmem_range {
        struct list_head lru;
        struct list_head unpinned;
        struct ashmem_area *asma;
        size_t pgstart;
        size_t pgend;
        unsigned int purged;
    }

.. _`ashmem_range.members`:

Members
-------

lru
    The entry in the LRU list

unpinned
    The entry in its area's unpinned list

asma
    The associated anonymous shared memory area.

pgstart
    The starting page (inclusive)

pgend
    The ending page (inclusive)

purged
    The purge status (ASHMEM_NOT or ASHMEM_WAS_PURGED)

.. _`ashmem_range.description`:

Description
-----------

The lifecycle of this structure is from unpin to pin.
It is protected by 'ashmem_mutex'

.. _`lru_add`:

lru_add
=======

.. c:function:: void lru_add(struct ashmem_range *range)

    Adds a range of memory to the LRU list

    :param range:
        The memory range being added.
    :type range: struct ashmem_range \*

.. _`lru_add.description`:

Description
-----------

The range is first added to the end (tail) of the LRU list.
After this, the size of the range is added to \ ``lru_count``\ 

.. _`lru_del`:

lru_del
=======

.. c:function:: void lru_del(struct ashmem_range *range)

    Removes a range of memory from the LRU list

    :param range:
        The memory range being removed
    :type range: struct ashmem_range \*

.. _`lru_del.description`:

Description
-----------

The range is first deleted from the LRU list.
After this, the size of the range is removed from \ ``lru_count``\ 

.. _`range_alloc`:

range_alloc
===========

.. c:function:: int range_alloc(struct ashmem_area *asma, struct ashmem_range *prev_range, unsigned int purged, size_t start, size_t end)

    Allocates and initializes a new ashmem_range structure

    :param asma:
        The associated ashmem_area
    :type asma: struct ashmem_area \*

    :param prev_range:
        The previous ashmem_range in the sorted asma->unpinned list
    :type prev_range: struct ashmem_range \*

    :param purged:
        Initial purge status (ASMEM_NOT_PURGED or ASHMEM_WAS_PURGED)
    :type purged: unsigned int

    :param start:
        The starting page (inclusive)
    :type start: size_t

    :param end:
        The ending page (inclusive)
    :type end: size_t

.. _`range_alloc.description`:

Description
-----------

This function is protected by ashmem_mutex.

.. _`range_alloc.return`:

Return
------

0 if successful, or -ENOMEM if there is an error

.. _`range_del`:

range_del
=========

.. c:function:: void range_del(struct ashmem_range *range)

    Deletes and dealloctes an ashmem_range structure

    :param range:
        The associated ashmem_range that has previously been allocated
    :type range: struct ashmem_range \*

.. _`range_shrink`:

range_shrink
============

.. c:function:: void range_shrink(struct ashmem_range *range, size_t start, size_t end)

    Shrinks an ashmem_range

    :param range:
        The associated ashmem_range being shrunk
    :type range: struct ashmem_range \*

    :param start:
        The starting byte of the new range
    :type start: size_t

    :param end:
        The ending byte of the new range
    :type end: size_t

.. _`range_shrink.description`:

Description
-----------

This does not modify the data inside the existing range in any way - It
simply shrinks the boundaries of the range.

Theoretically, with a little tweaking, this could eventually be changed
to range_resize, and expand the lru_count if the new range is larger.

.. _`ashmem_open`:

ashmem_open
===========

.. c:function:: int ashmem_open(struct inode *inode, struct file *file)

    Opens an Anonymous Shared Memory structure

    :param inode:
        The backing file's index node(?)
    :type inode: struct inode \*

    :param file:
        The backing file
    :type file: struct file \*

.. _`ashmem_open.description`:

Description
-----------

Please note that the ashmem_area is not returned by this function - It is
instead written to "file->private_data".

.. _`ashmem_open.return`:

Return
------

0 if successful, or another code if unsuccessful.

.. _`ashmem_release`:

ashmem_release
==============

.. c:function:: int ashmem_release(struct inode *ignored, struct file *file)

    Releases an Anonymous Shared Memory structure

    :param ignored:
        The backing file's Index Node(?) - It is ignored here.
    :type ignored: struct inode \*

    :param file:
        The backing file
    :type file: struct file \*

.. _`ashmem_release.return`:

Return
------

0 if successful. If it is anything else, go have a coffee and
try again.

.. This file was automatic generated / don't edit.

