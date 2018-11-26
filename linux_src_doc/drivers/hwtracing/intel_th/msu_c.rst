.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/intel_th/msu.c

.. _`msc_block`:

struct msc_block
================

.. c:type:: struct msc_block

    multiblock mode block descriptor

.. _`msc_block.definition`:

Definition
----------

.. code-block:: c

    struct msc_block {
        struct msc_block_desc *bdesc;
        dma_addr_t addr;
    }

.. _`msc_block.members`:

Members
-------

bdesc
    pointer to hardware descriptor (beginning of the block)

addr
    physical address of the block

.. _`msc_window`:

struct msc_window
=================

.. c:type:: struct msc_window

    multiblock mode window descriptor

.. _`msc_window.definition`:

Definition
----------

.. code-block:: c

    struct msc_window {
        struct list_head entry;
        unsigned long pgoff;
        unsigned int nr_blocks;
        struct msc *msc;
        struct msc_block block[0];
    }

.. _`msc_window.members`:

Members
-------

entry
    window list linkage (msc::win_list)

pgoff
    page offset into the buffer that this window starts at

nr_blocks
    number of blocks (pages) in this window

msc
    *undescribed*

block
    array of block descriptors

.. _`msc_iter`:

struct msc_iter
===============

.. c:type:: struct msc_iter

    iterator for msc buffer

.. _`msc_iter.definition`:

Definition
----------

.. code-block:: c

    struct msc_iter {
        struct list_head entry;
        struct msc *msc;
        struct msc_window *start_win;
        struct msc_window *win;
        unsigned long offset;
        int start_block;
        int block;
        unsigned int block_off;
        unsigned int wrap_count;
        unsigned int eof;
    }

.. _`msc_iter.members`:

Members
-------

entry
    msc::iter_list linkage

msc
    pointer to the MSC device

start_win
    oldest window

win
    current window

offset
    current logical offset into the buffer

start_block
    oldest block in the window

block
    block number in the window

block_off
    offset into current block

wrap_count
    block wrapping handling

eof
    end of buffer reached

.. _`msc`:

struct msc
==========

.. c:type:: struct msc

    MSC device representation

.. _`msc.definition`:

Definition
----------

.. code-block:: c

    struct msc {
        void __iomem *reg_base;
        struct intel_th_device *thdev;
        struct list_head win_list;
        unsigned long nr_pages;
        unsigned long single_sz;
        unsigned int single_wrap : 1;
        void *base;
        dma_addr_t base_addr;
        atomic_t user_count;
        atomic_t mmap_count;
        struct mutex buf_mutex;
        struct list_head iter_list;
        unsigned int enabled : 1, wrap : 1;
        unsigned int mode;
        unsigned int burst_len;
        unsigned int index;
    }

.. _`msc.members`:

Members
-------

reg_base
    register window base address

thdev
    intel_th_device pointer

win_list
    list of windows in multiblock mode

nr_pages
    total number of pages allocated for this buffer

single_sz
    amount of data in single mode

single_wrap
    single mode wrap occurred

base
    buffer's base pointer

base_addr
    buffer's base address

user_count
    number of users of the buffer

mmap_count
    number of mappings

buf_mutex
    mutex to serialize access to buffer-related bits

iter_list
    *undescribed*

enabled
    MSC is enabled

wrap
    wrapping is enabled

mode
    MSC operating mode

burst_len
    write burst length

index
    number of this MSC in the MSU

.. _`msc_oldest_window`:

msc_oldest_window
=================

.. c:function:: struct msc_window *msc_oldest_window(struct msc *msc)

    locate the window with oldest data

    :param msc:
        MSC device
    :type msc: struct msc \*

.. _`msc_oldest_window.description`:

Description
-----------

This should only be used in multiblock mode. Caller should hold the
msc::user_count reference.

.. _`msc_oldest_window.return`:

Return
------

the oldest window with valid data

.. _`msc_win_oldest_block`:

msc_win_oldest_block
====================

.. c:function:: unsigned int msc_win_oldest_block(struct msc_window *win)

    locate the oldest block in a given window

    :param win:
        window to look at
    :type win: struct msc_window \*

.. _`msc_win_oldest_block.return`:

Return
------

index of the block with the oldest data

.. _`msc_is_last_win`:

msc_is_last_win
===============

.. c:function:: bool msc_is_last_win(struct msc_window *win)

    check if a window is the last one for a given MSC

    :param win:
        window
    :type win: struct msc_window \*

.. _`msc_is_last_win.return`:

Return
------

true if \ ``win``\  is the last window in MSC's multiblock buffer

.. _`msc_next_window`:

msc_next_window
===============

.. c:function:: struct msc_window *msc_next_window(struct msc_window *win)

    return next window in the multiblock buffer

    :param win:
        current window
    :type win: struct msc_window \*

.. _`msc_next_window.return`:

Return
------

window following the current one

.. _`msc_buffer_iterate`:

msc_buffer_iterate
==================

.. c:function:: ssize_t msc_buffer_iterate(struct msc_iter *iter, size_t size, void *data, unsigned long (*fn)(void *, void *, size_t))

    go through multiblock buffer's data

    :param iter:
        iterator structure
    :type iter: struct msc_iter \*

    :param size:
        amount of data to scan
    :type size: size_t

    :param data:
        callback's private data
    :type data: void \*

    :param unsigned long (\*fn)(void \*, void \*, size_t):
        iterator callback

.. _`msc_buffer_iterate.description`:

Description
-----------

This will start at the window which will be written to next (containing
the oldest data) and work its way to the current window, calling \ ``fn``\ 
for each chunk of data as it goes.

Caller should have msc::user_count reference to make sure the buffer
doesn't disappear from under us.

.. _`msc_buffer_iterate.return`:

Return
------

amount of data actually scanned.

.. _`msc_buffer_clear_hw_header`:

msc_buffer_clear_hw_header
==========================

.. c:function:: void msc_buffer_clear_hw_header(struct msc *msc)

    clear hw header for multiblock

    :param msc:
        MSC device
    :type msc: struct msc \*

.. _`msc_configure`:

msc_configure
=============

.. c:function:: int msc_configure(struct msc *msc)

    set up MSC hardware

    :param msc:
        the MSC device to configure
    :type msc: struct msc \*

.. _`msc_configure.description`:

Description
-----------

Program storage mode, wrapping, burst length and trace buffer address
into a given MSC. Then, enable tracing and set msc::enabled.
The latter is serialized on msc::buf_mutex, so make sure to hold it.

.. _`msc_disable`:

msc_disable
===========

.. c:function:: void msc_disable(struct msc *msc)

    disable MSC hardware

    :param msc:
        MSC device to disable
    :type msc: struct msc \*

.. _`msc_disable.description`:

Description
-----------

If \ ``msc``\  is enabled, disable tracing on the switch and then disable MSC
storage. Caller must hold msc::buf_mutex.

.. _`msc_buffer_contig_alloc`:

msc_buffer_contig_alloc
=======================

.. c:function:: int msc_buffer_contig_alloc(struct msc *msc, unsigned long size)

    allocate a contiguous buffer for SINGLE mode

    :param msc:
        MSC device
    :type msc: struct msc \*

    :param size:
        allocation size in bytes
    :type size: unsigned long

.. _`msc_buffer_contig_alloc.description`:

Description
-----------

This modifies msc::base, which requires msc::buf_mutex to serialize, so the
caller is expected to hold it.

.. _`msc_buffer_contig_alloc.return`:

Return
------

0 on success, -errno otherwise.

.. _`msc_buffer_contig_free`:

msc_buffer_contig_free
======================

.. c:function:: void msc_buffer_contig_free(struct msc *msc)

    free a contiguous buffer

    :param msc:
        MSC configured in SINGLE mode
    :type msc: struct msc \*

.. _`msc_buffer_contig_get_page`:

msc_buffer_contig_get_page
==========================

.. c:function:: struct page *msc_buffer_contig_get_page(struct msc *msc, unsigned long pgoff)

    find a page at a given offset

    :param msc:
        MSC configured in SINGLE mode
    :type msc: struct msc \*

    :param pgoff:
        page offset
    :type pgoff: unsigned long

.. _`msc_buffer_contig_get_page.return`:

Return
------

page, if \ ``pgoff``\  is within the range, NULL otherwise.

.. _`msc_buffer_win_alloc`:

msc_buffer_win_alloc
====================

.. c:function:: int msc_buffer_win_alloc(struct msc *msc, unsigned int nr_blocks)

    alloc a window for a multiblock mode

    :param msc:
        MSC device
    :type msc: struct msc \*

    :param nr_blocks:
        number of pages in this window
    :type nr_blocks: unsigned int

.. _`msc_buffer_win_alloc.description`:

Description
-----------

This modifies msc::win_list and msc::base, which requires msc::buf_mutex
to serialize, so the caller is expected to hold it.

.. _`msc_buffer_win_alloc.return`:

Return
------

0 on success, -errno otherwise.

.. _`msc_buffer_win_free`:

msc_buffer_win_free
===================

.. c:function:: void msc_buffer_win_free(struct msc *msc, struct msc_window *win)

    free a window from MSC's window list

    :param msc:
        MSC device
    :type msc: struct msc \*

    :param win:
        window to free
    :type win: struct msc_window \*

.. _`msc_buffer_win_free.description`:

Description
-----------

This modifies msc::win_list and msc::base, which requires msc::buf_mutex
to serialize, so the caller is expected to hold it.

.. _`msc_buffer_relink`:

msc_buffer_relink
=================

.. c:function:: void msc_buffer_relink(struct msc *msc)

    set up block descriptors for multiblock mode

    :param msc:
        MSC device
    :type msc: struct msc \*

.. _`msc_buffer_relink.description`:

Description
-----------

This traverses msc::win_list, which requires msc::buf_mutex to serialize,
so the caller is expected to hold it.

.. _`msc_buffer_free`:

msc_buffer_free
===============

.. c:function:: void msc_buffer_free(struct msc *msc)

    free buffers for MSC

    :param msc:
        MSC device
    :type msc: struct msc \*

.. _`msc_buffer_free.description`:

Description
-----------

Free MSC's storage buffers.

This modifies msc::win_list and msc::base, which requires msc::buf_mutex to
serialize, so the caller is expected to hold it.

.. _`msc_buffer_alloc`:

msc_buffer_alloc
================

.. c:function:: int msc_buffer_alloc(struct msc *msc, unsigned long *nr_pages, unsigned int nr_wins)

    allocate a buffer for MSC

    :param msc:
        MSC device
    :type msc: struct msc \*

    :param nr_pages:
        *undescribed*
    :type nr_pages: unsigned long \*

    :param nr_wins:
        *undescribed*
    :type nr_wins: unsigned int

.. _`msc_buffer_alloc.description`:

Description
-----------

Allocate a storage buffer for MSC, depending on the msc::mode, it will be
either done via \ :c:func:`msc_buffer_contig_alloc`\  for SINGLE operation mode or
\ :c:func:`msc_buffer_win_alloc`\  for multiblock operation. The latter allocates one
window per invocation, so in multiblock mode this can be called multiple
times for the same MSC to allocate multiple windows.

This modifies msc::win_list and msc::base, which requires msc::buf_mutex
to serialize, so the caller is expected to hold it.

.. _`msc_buffer_alloc.return`:

Return
------

0 on success, -errno otherwise.

.. _`msc_buffer_unlocked_free_unless_used`:

msc_buffer_unlocked_free_unless_used
====================================

.. c:function:: int msc_buffer_unlocked_free_unless_used(struct msc *msc)

    free a buffer unless it's in use

    :param msc:
        MSC device
    :type msc: struct msc \*

.. _`msc_buffer_unlocked_free_unless_used.description`:

Description
-----------

This will free MSC buffer unless it is in use or there is no allocated
buffer.
Caller needs to hold msc::buf_mutex.

.. _`msc_buffer_unlocked_free_unless_used.return`:

Return
------

0 on successful deallocation or if there was no buffer to
deallocate, -EBUSY if there are active users.

.. _`msc_buffer_free_unless_used`:

msc_buffer_free_unless_used
===========================

.. c:function:: int msc_buffer_free_unless_used(struct msc *msc)

    free a buffer unless it's in use

    :param msc:
        MSC device
    :type msc: struct msc \*

.. _`msc_buffer_free_unless_used.description`:

Description
-----------

This is a locked version of \ :c:func:`msc_buffer_unlocked_free_unless_used`\ .

.. _`msc_buffer_get_page`:

msc_buffer_get_page
===================

.. c:function:: struct page *msc_buffer_get_page(struct msc *msc, unsigned long pgoff)

    get MSC buffer page at a given offset

    :param msc:
        MSC device
    :type msc: struct msc \*

    :param pgoff:
        page offset into the storage buffer
    :type pgoff: unsigned long

.. _`msc_buffer_get_page.description`:

Description
-----------

This traverses msc::win_list, so holding msc::buf_mutex is expected from
the caller.

.. _`msc_buffer_get_page.return`:

Return
------

page if \ ``pgoff``\  corresponds to a valid buffer page or NULL.

.. _`msc_win_to_user_struct`:

struct msc_win_to_user_struct
=============================

.. c:type:: struct msc_win_to_user_struct

    data for \ :c:func:`copy_to_user`\  callback

.. _`msc_win_to_user_struct.definition`:

Definition
----------

.. code-block:: c

    struct msc_win_to_user_struct {
        char __user *buf;
        unsigned long offset;
    }

.. _`msc_win_to_user_struct.members`:

Members
-------

buf
    userspace buffer to copy data to

offset
    running offset

.. _`msc_win_to_user`:

msc_win_to_user
===============

.. c:function:: unsigned long msc_win_to_user(void *data, void *src, size_t len)

    iterator for \ :c:func:`msc_buffer_iterate`\  to copy data to user

    :param data:
        callback's private data
    :type data: void \*

    :param src:
        source buffer
    :type src: void \*

    :param len:
        amount of data to copy from the source buffer
    :type len: size_t

.. This file was automatic generated / don't edit.

