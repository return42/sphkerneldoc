.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/power/swap.c

.. _`alloc_swapdev_block`:

alloc_swapdev_block
===================

.. c:function:: sector_t alloc_swapdev_block(int swap)

    allocate a swap page and register that it has been allocated, so that it can be freed in case of an error.

    :param int swap:
        *undescribed*

.. _`free_all_swap_pages`:

free_all_swap_pages
===================

.. c:function:: void free_all_swap_pages(int swap)

    free swap pages allocated for saving image data. It also frees the extents used to register which swap entries had been allocated.

    :param int swap:
        *undescribed*

.. _`swsusp_swap_check`:

swsusp_swap_check
=================

.. c:function:: int swsusp_swap_check( void)

    check if the resume device is a swap device and get its index (if so)

    :param  void:
        no arguments

.. _`swsusp_swap_check.description`:

Description
-----------

This is called before saving image

.. _`write_page`:

write_page
==========

.. c:function:: int write_page(void *buf, sector_t offset, struct hib_bio_batch *hb)

    Write one page to given swap location.

    :param void \*buf:
        Address we're writing.

    :param sector_t offset:
        Offset of the swap page we're writing to.

    :param struct hib_bio_batch \*hb:
        bio completion batch

.. _`save_image`:

save_image
==========

.. c:function:: int save_image(struct swap_map_handle *handle, struct snapshot_handle *snapshot, unsigned int nr_to_write)

    save the suspend image data

    :param struct swap_map_handle \*handle:
        *undescribed*

    :param struct snapshot_handle \*snapshot:
        *undescribed*

    :param unsigned int nr_to_write:
        *undescribed*

.. _`crc32_threadfn`:

crc32_threadfn
==============

.. c:function:: int crc32_threadfn(void *data)

    :param void \*data:
        *undescribed*

.. _`lzo_compress_threadfn`:

lzo_compress_threadfn
=====================

.. c:function:: int lzo_compress_threadfn(void *data)

    :param void \*data:
        *undescribed*

.. _`save_image_lzo`:

save_image_lzo
==============

.. c:function:: int save_image_lzo(struct swap_map_handle *handle, struct snapshot_handle *snapshot, unsigned int nr_to_write)

    Save the suspend image data compressed with LZO.

    :param struct swap_map_handle \*handle:
        Swap map handle to use for saving the image.

    :param struct snapshot_handle \*snapshot:
        Image to read data from.

    :param unsigned int nr_to_write:
        Number of pages to save.

.. _`enough_swap`:

enough_swap
===========

.. c:function:: int enough_swap(unsigned int nr_pages, unsigned int flags)

    Make sure we have enough swap to save the image.

    :param unsigned int nr_pages:
        *undescribed*

    :param unsigned int flags:
        *undescribed*

.. _`enough_swap.description`:

Description
-----------

Returns TRUE or FALSE after checking the total amount of swap
space avaiable from the resume partition.

.. _`swsusp_write`:

swsusp_write
============

.. c:function:: int swsusp_write(unsigned int flags)

    Write entire image and metadata.

    :param unsigned int flags:
        flags to pass to the "boot" kernel in the image header

.. _`swsusp_write.description`:

Description
-----------

It is important \_NOT\_ to umount filesystems at this point. We want
them synced (in case something goes wrong) but we DO not want to mark

.. _`swsusp_write.filesystem-clean`:

filesystem clean
----------------

it is not. (And it does not matter, if we resume
correctly, we'll mark system clean, anyway.)

.. _`release_swap_reader`:

release_swap_reader
===================

.. c:function:: void release_swap_reader(struct swap_map_handle *handle)

    in a file-alike way

    :param struct swap_map_handle \*handle:
        *undescribed*

.. _`load_image`:

load_image
==========

.. c:function:: int load_image(struct swap_map_handle *handle, struct snapshot_handle *snapshot, unsigned int nr_to_read)

    load the image using the swap map handle \ ``handle``\  and the snapshot handle \ ``snapshot``\  (assume there are \ ``nr_pages``\  pages to load)

    :param struct swap_map_handle \*handle:
        *undescribed*

    :param struct snapshot_handle \*snapshot:
        *undescribed*

    :param unsigned int nr_to_read:
        *undescribed*

.. _`lzo_decompress_threadfn`:

lzo_decompress_threadfn
=======================

.. c:function:: int lzo_decompress_threadfn(void *data)

    :param void \*data:
        *undescribed*

.. _`load_image_lzo`:

load_image_lzo
==============

.. c:function:: int load_image_lzo(struct swap_map_handle *handle, struct snapshot_handle *snapshot, unsigned int nr_to_read)

    Load compressed image data and decompress them with LZO.

    :param struct swap_map_handle \*handle:
        Swap map handle to use for loading data.

    :param struct snapshot_handle \*snapshot:
        Image to copy uncompressed data into.

    :param unsigned int nr_to_read:
        Number of pages to load.

.. _`swsusp_read`:

swsusp_read
===========

.. c:function:: int swsusp_read(unsigned int *flags_p)

    read the hibernation image.

    :param unsigned int \*flags_p:
        flags passed by the "frozen" kernel in the image header should
        be written into this memory location

.. _`swsusp_check`:

swsusp_check
============

.. c:function:: int swsusp_check( void)

    Check for swsusp signature in the resume device

    :param  void:
        no arguments

.. _`swsusp_close`:

swsusp_close
============

.. c:function:: void swsusp_close(fmode_t mode)

    close swap device.

    :param fmode_t mode:
        *undescribed*

.. _`swsusp_unmark`:

swsusp_unmark
=============

.. c:function:: int swsusp_unmark( void)

    Unmark swsusp signature in the resume device

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

