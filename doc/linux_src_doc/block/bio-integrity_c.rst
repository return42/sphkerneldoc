.. -*- coding: utf-8; mode: rst -*-

===============
bio-integrity.c
===============


.. _`bio_integrity_alloc`:

bio_integrity_alloc
===================

.. c:function:: struct bio_integrity_payload *bio_integrity_alloc (struct bio *bio, gfp_t gfp_mask, unsigned int nr_vecs)

    Allocate integrity payload and attach it to bio

    :param struct bio \*bio:
        bio to attach integrity metadata to

    :param gfp_t gfp_mask:
        Memory allocation mask

    :param unsigned int nr_vecs:
        Number of integrity metadata scatter-gather elements



.. _`bio_integrity_alloc.description`:

Description
-----------

This function prepares a bio for attaching integrity
metadata.  nr_vecs specifies the maximum number of pages containing
integrity metadata that can be attached.



.. _`bio_integrity_free`:

bio_integrity_free
==================

.. c:function:: void bio_integrity_free (struct bio *bio)

    Free bio integrity payload

    :param struct bio \*bio:
        bio containing bip to be freed



.. _`bio_integrity_free.description`:

Description
-----------

Used to free the integrity portion of a bio. Usually
called from :c:func:`bio_free`.



.. _`bio_integrity_add_page`:

bio_integrity_add_page
======================

.. c:function:: int bio_integrity_add_page (struct bio *bio, struct page *page, unsigned int len, unsigned int offset)

    Attach integrity metadata

    :param struct bio \*bio:
        bio to update

    :param struct page \*page:
        page containing integrity metadata

    :param unsigned int len:
        number of bytes of integrity metadata in page

    :param unsigned int offset:
        start offset within page



.. _`bio_integrity_add_page.description`:

Description
-----------

Attach a page containing integrity metadata to bio.



.. _`bio_integrity_enabled`:

bio_integrity_enabled
=====================

.. c:function:: bool bio_integrity_enabled (struct bio *bio)

    Check whether integrity can be passed

    :param struct bio \*bio:
        bio to check



.. _`bio_integrity_enabled.description`:

Description
-----------

Determines whether :c:func:`bio_integrity_prep` can be called
on this bio or not.        bio data direction and target device must be
set prior to calling.  The functions honors the write_generate and
read_verify flags in sysfs.



.. _`bio_integrity_intervals`:

bio_integrity_intervals
=======================

.. c:function:: unsigned int bio_integrity_intervals (struct blk_integrity *bi, unsigned int sectors)

    Return number of integrity intervals for a bio

    :param struct blk_integrity \*bi:
        blk_integrity profile for device

    :param unsigned int sectors:
        Size of the bio in 512-byte sectors



.. _`bio_integrity_intervals.description`:

Description
-----------

The block layer calculates everything in 512 byte
sectors but integrity metadata is done in terms of the data integrity
interval size of the storage device.  Convert the block layer sectors
to the appropriate number of integrity intervals.



.. _`bio_integrity_process`:

bio_integrity_process
=====================

.. c:function:: int bio_integrity_process (struct bio *bio, integrity_processing_fn *proc_fn)

    Process integrity metadata for a bio

    :param struct bio \*bio:
        bio to generate/verify integrity metadata for

    :param integrity_processing_fn \*proc_fn:
        Pointer to the relevant processing function



.. _`bio_integrity_prep`:

bio_integrity_prep
==================

.. c:function:: int bio_integrity_prep (struct bio *bio)

    Prepare bio for integrity I/O

    :param struct bio \*bio:
        bio to prepare



.. _`bio_integrity_prep.description`:

Description
-----------

Allocates a buffer for integrity metadata, maps the
pages and attaches them to a bio.  The bio must have data
direction, target device and start sector set priot to calling.  In
the WRITE case, integrity metadata will be generated using the
block device's integrity function.  In the READ case, the buffer
will be prepared for DMA and a suitable end_io handler set up.



.. _`bio_integrity_verify_fn`:

bio_integrity_verify_fn
=======================

.. c:function:: void bio_integrity_verify_fn (struct work_struct *work)

    Integrity I/O completion worker

    :param struct work_struct \*work:
        Work struct stored in bio to be verified



.. _`bio_integrity_verify_fn.description`:

Description
-----------

This workqueue function is called to complete a READ
request.  The function verifies the transferred integrity metadata
and then calls the original bio end_io function.



.. _`bio_integrity_endio`:

bio_integrity_endio
===================

.. c:function:: void bio_integrity_endio (struct bio *bio)

    Integrity I/O completion function

    :param struct bio \*bio:
        Protected bio



.. _`bio_integrity_endio.description`:

Description
-----------

Completion for integrity I/O

Normally I/O completion is done in interrupt context.  However,
verifying I/O integrity is a time-consuming task which must be run
in process context.        This function postpones completion
accordingly.



.. _`bio_integrity_advance`:

bio_integrity_advance
=====================

.. c:function:: void bio_integrity_advance (struct bio *bio, unsigned int bytes_done)

    Advance integrity vector

    :param struct bio \*bio:
        bio whose integrity vector to update

    :param unsigned int bytes_done:
        number of data bytes that have been completed



.. _`bio_integrity_advance.description`:

Description
-----------

This function calculates how many integrity bytes the
number of completed data bytes correspond to and advances the
integrity vector accordingly.



.. _`bio_integrity_trim`:

bio_integrity_trim
==================

.. c:function:: void bio_integrity_trim (struct bio *bio, unsigned int offset, unsigned int sectors)

    Trim integrity vector

    :param struct bio \*bio:
        bio whose integrity vector to update

    :param unsigned int offset:
        offset to first data sector

    :param unsigned int sectors:
        number of data sectors



.. _`bio_integrity_trim.description`:

Description
-----------

Used to trim the integrity vector in a cloned bio.
The ivec will be advanced corresponding to 'offset' data sectors
and the length will be truncated corresponding to 'len' data
sectors.



.. _`bio_integrity_clone`:

bio_integrity_clone
===================

.. c:function:: int bio_integrity_clone (struct bio *bio, struct bio *bio_src, gfp_t gfp_mask)

    Callback for cloning bios with integrity metadata

    :param struct bio \*bio:
        New bio

    :param struct bio \*bio_src:
        Original bio

    :param gfp_t gfp_mask:
        Memory allocation mask



.. _`bio_integrity_clone.description`:

Description
-----------

Called to allocate a bip when cloning a bio

