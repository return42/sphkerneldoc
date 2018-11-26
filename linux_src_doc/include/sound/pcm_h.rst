.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/pcm.h

.. _`snd_pcm_stream_linked`:

snd_pcm_stream_linked
=====================

.. c:function:: int snd_pcm_stream_linked(struct snd_pcm_substream *substream)

    Check whether the substream is linked with others

    :param substream:
        substream to check
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_stream_linked.description`:

Description
-----------

Returns true if the given substream is being linked with others.

.. _`snd_pcm_stream_lock_irqsave`:

snd_pcm_stream_lock_irqsave
===========================

.. c:function::  snd_pcm_stream_lock_irqsave( substream,  flags)

    Lock the PCM stream

    :param substream:
        PCM substream
    :type substream: 

    :param flags:
        irq flags
    :type flags: 

.. _`snd_pcm_stream_lock_irqsave.description`:

Description
-----------

This locks the PCM stream like \ :c:func:`snd_pcm_stream_lock`\  but with the local
IRQ (only when nonatomic is false).  In nonatomic case, this is identical
as \ :c:func:`snd_pcm_stream_lock`\ .

.. _`snd_pcm_group_for_each_entry`:

snd_pcm_group_for_each_entry
============================

.. c:function::  snd_pcm_group_for_each_entry( s,  substream)

    iterate over the linked substreams

    :param s:
        the iterator
    :type s: 

    :param substream:
        the substream
    :type substream: 

.. _`snd_pcm_group_for_each_entry.description`:

Description
-----------

Iterate over the all linked substreams to the given \ ``substream``\ .
When \ ``substream``\  isn't linked with any others, this gives returns \ ``substream``\ 
itself once.

.. _`snd_pcm_running`:

snd_pcm_running
===============

.. c:function:: int snd_pcm_running(struct snd_pcm_substream *substream)

    Check whether the substream is in a running state

    :param substream:
        substream to check
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_running.description`:

Description
-----------

Returns true if the given substream is in the state RUNNING, or in the
state DRAINING for playback.

.. _`bytes_to_samples`:

bytes_to_samples
================

.. c:function:: ssize_t bytes_to_samples(struct snd_pcm_runtime *runtime, ssize_t size)

    Unit conversion of the size from bytes to samples

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param size:
        size in bytes
    :type size: ssize_t

.. _`bytes_to_frames`:

bytes_to_frames
===============

.. c:function:: snd_pcm_sframes_t bytes_to_frames(struct snd_pcm_runtime *runtime, ssize_t size)

    Unit conversion of the size from bytes to frames

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param size:
        size in bytes
    :type size: ssize_t

.. _`samples_to_bytes`:

samples_to_bytes
================

.. c:function:: ssize_t samples_to_bytes(struct snd_pcm_runtime *runtime, ssize_t size)

    Unit conversion of the size from samples to bytes

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param size:
        size in samples
    :type size: ssize_t

.. _`frames_to_bytes`:

frames_to_bytes
===============

.. c:function:: ssize_t frames_to_bytes(struct snd_pcm_runtime *runtime, snd_pcm_sframes_t size)

    Unit conversion of the size from frames to bytes

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param size:
        size in frames
    :type size: snd_pcm_sframes_t

.. _`frame_aligned`:

frame_aligned
=============

.. c:function:: int frame_aligned(struct snd_pcm_runtime *runtime, ssize_t bytes)

    Check whether the byte size is aligned to frames

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param bytes:
        size in bytes
    :type bytes: ssize_t

.. _`snd_pcm_lib_buffer_bytes`:

snd_pcm_lib_buffer_bytes
========================

.. c:function:: size_t snd_pcm_lib_buffer_bytes(struct snd_pcm_substream *substream)

    Get the buffer size of the current PCM in bytes

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_lib_period_bytes`:

snd_pcm_lib_period_bytes
========================

.. c:function:: size_t snd_pcm_lib_period_bytes(struct snd_pcm_substream *substream)

    Get the period size of the current PCM in bytes

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_playback_avail`:

snd_pcm_playback_avail
======================

.. c:function:: snd_pcm_uframes_t snd_pcm_playback_avail(struct snd_pcm_runtime *runtime)

    Get the available (writable) space for playback

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

.. _`snd_pcm_playback_avail.description`:

Description
-----------

Result is between 0 ... (boundary - 1)

.. _`snd_pcm_capture_avail`:

snd_pcm_capture_avail
=====================

.. c:function:: snd_pcm_uframes_t snd_pcm_capture_avail(struct snd_pcm_runtime *runtime)

    Get the available (readable) space for capture

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

.. _`snd_pcm_capture_avail.description`:

Description
-----------

Result is between 0 ... (boundary - 1)

.. _`snd_pcm_playback_hw_avail`:

snd_pcm_playback_hw_avail
=========================

.. c:function:: snd_pcm_sframes_t snd_pcm_playback_hw_avail(struct snd_pcm_runtime *runtime)

    Get the queued space for playback

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

.. _`snd_pcm_capture_hw_avail`:

snd_pcm_capture_hw_avail
========================

.. c:function:: snd_pcm_sframes_t snd_pcm_capture_hw_avail(struct snd_pcm_runtime *runtime)

    Get the free space for capture

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

.. _`snd_pcm_playback_ready`:

snd_pcm_playback_ready
======================

.. c:function:: int snd_pcm_playback_ready(struct snd_pcm_substream *substream)

    check whether the playback buffer is available

    :param substream:
        the pcm substream instance
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_playback_ready.description`:

Description
-----------

Checks whether enough free space is available on the playback buffer.

.. _`snd_pcm_playback_ready.return`:

Return
------

Non-zero if available, or zero if not.

.. _`snd_pcm_capture_ready`:

snd_pcm_capture_ready
=====================

.. c:function:: int snd_pcm_capture_ready(struct snd_pcm_substream *substream)

    check whether the capture buffer is available

    :param substream:
        the pcm substream instance
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_capture_ready.description`:

Description
-----------

Checks whether enough capture data is available on the capture buffer.

.. _`snd_pcm_capture_ready.return`:

Return
------

Non-zero if available, or zero if not.

.. _`snd_pcm_playback_data`:

snd_pcm_playback_data
=====================

.. c:function:: int snd_pcm_playback_data(struct snd_pcm_substream *substream)

    check whether any data exists on the playback buffer

    :param substream:
        the pcm substream instance
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_playback_data.description`:

Description
-----------

Checks whether any data exists on the playback buffer.

.. _`snd_pcm_playback_data.return`:

Return
------

Non-zero if any data exists, or zero if not. If stop_threshold
is bigger or equal to boundary, then this function returns always non-zero.

.. _`snd_pcm_playback_empty`:

snd_pcm_playback_empty
======================

.. c:function:: int snd_pcm_playback_empty(struct snd_pcm_substream *substream)

    check whether the playback buffer is empty

    :param substream:
        the pcm substream instance
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_playback_empty.description`:

Description
-----------

Checks whether the playback buffer is empty.

.. _`snd_pcm_playback_empty.return`:

Return
------

Non-zero if empty, or zero if not.

.. _`snd_pcm_capture_empty`:

snd_pcm_capture_empty
=====================

.. c:function:: int snd_pcm_capture_empty(struct snd_pcm_substream *substream)

    check whether the capture buffer is empty

    :param substream:
        the pcm substream instance
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_capture_empty.description`:

Description
-----------

Checks whether the capture buffer is empty.

.. _`snd_pcm_capture_empty.return`:

Return
------

Non-zero if empty, or zero if not.

.. _`snd_pcm_trigger_done`:

snd_pcm_trigger_done
====================

.. c:function:: void snd_pcm_trigger_done(struct snd_pcm_substream *substream, struct snd_pcm_substream *master)

    Mark the master substream

    :param substream:
        the pcm substream instance
    :type substream: struct snd_pcm_substream \*

    :param master:
        the linked master substream
    :type master: struct snd_pcm_substream \*

.. _`snd_pcm_trigger_done.description`:

Description
-----------

When multiple substreams of the same card are linked and the hardware
supports the single-shot operation, the driver calls this in the loop
in \ :c:func:`snd_pcm_group_for_each_entry`\  for marking the substream as "done".
Then most of trigger operations are performed only to the given master
substream.

The trigger_master mark is cleared at timestamp updates at the end
of trigger operations.

.. _`params_channels`:

params_channels
===============

.. c:function:: unsigned int params_channels(const struct snd_pcm_hw_params *p)

    Get the number of channels from the hw params

    :param p:
        hw params
    :type p: const struct snd_pcm_hw_params \*

.. _`params_rate`:

params_rate
===========

.. c:function:: unsigned int params_rate(const struct snd_pcm_hw_params *p)

    Get the sample rate from the hw params

    :param p:
        hw params
    :type p: const struct snd_pcm_hw_params \*

.. _`params_period_size`:

params_period_size
==================

.. c:function:: unsigned int params_period_size(const struct snd_pcm_hw_params *p)

    Get the period size (in frames) from the hw params

    :param p:
        hw params
    :type p: const struct snd_pcm_hw_params \*

.. _`params_periods`:

params_periods
==============

.. c:function:: unsigned int params_periods(const struct snd_pcm_hw_params *p)

    Get the number of periods from the hw params

    :param p:
        hw params
    :type p: const struct snd_pcm_hw_params \*

.. _`params_buffer_size`:

params_buffer_size
==================

.. c:function:: unsigned int params_buffer_size(const struct snd_pcm_hw_params *p)

    Get the buffer size (in frames) from the hw params

    :param p:
        hw params
    :type p: const struct snd_pcm_hw_params \*

.. _`params_buffer_bytes`:

params_buffer_bytes
===================

.. c:function:: unsigned int params_buffer_bytes(const struct snd_pcm_hw_params *p)

    Get the buffer size (in bytes) from the hw params

    :param p:
        hw params
    :type p: const struct snd_pcm_hw_params \*

.. _`snd_pcm_hw_constraint_single`:

snd_pcm_hw_constraint_single
============================

.. c:function:: int snd_pcm_hw_constraint_single(struct snd_pcm_runtime *runtime, snd_pcm_hw_param_t var, unsigned int val)

    Constrain parameter to a single value

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param var:
        The hw_params variable to constrain
    :type var: snd_pcm_hw_param_t

    :param val:
        The value to constrain to
    :type val: unsigned int

.. _`snd_pcm_hw_constraint_single.return`:

Return
------

Positive if the value is changed, zero if it's not changed, or a
negative error code.

.. _`snd_pcm_format_cpu_endian`:

snd_pcm_format_cpu_endian
=========================

.. c:function:: int snd_pcm_format_cpu_endian(snd_pcm_format_t format)

    Check the PCM format is CPU-endian

    :param format:
        the format to check
    :type format: snd_pcm_format_t

.. _`snd_pcm_format_cpu_endian.return`:

Return
------

1 if the given PCM format is CPU-endian, 0 if
opposite, or a negative error code if endian not specified.

.. _`snd_pcm_set_runtime_buffer`:

snd_pcm_set_runtime_buffer
==========================

.. c:function:: void snd_pcm_set_runtime_buffer(struct snd_pcm_substream *substream, struct snd_dma_buffer *bufp)

    Set the PCM runtime buffer

    :param substream:
        PCM substream to set
    :type substream: struct snd_pcm_substream \*

    :param bufp:
        the buffer information, NULL to clear
    :type bufp: struct snd_dma_buffer \*

.. _`snd_pcm_set_runtime_buffer.description`:

Description
-----------

Copy the buffer information to runtime->dma_buffer when \ ``bufp``\  is non-NULL.
Otherwise it clears the current buffer information.

.. _`snd_pcm_gettime`:

snd_pcm_gettime
===============

.. c:function:: void snd_pcm_gettime(struct snd_pcm_runtime *runtime, struct timespec *tv)

    Fill the timespec depending on the timestamp mode

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param tv:
        timespec to fill
    :type tv: struct timespec \*

.. _`snd_pcm_lib_alloc_vmalloc_buffer`:

snd_pcm_lib_alloc_vmalloc_buffer
================================

.. c:function:: int snd_pcm_lib_alloc_vmalloc_buffer(struct snd_pcm_substream *substream, size_t size)

    allocate virtual DMA buffer

    :param substream:
        the substream to allocate the buffer to
    :type substream: struct snd_pcm_substream \*

    :param size:
        the requested buffer size, in bytes
    :type size: size_t

.. _`snd_pcm_lib_alloc_vmalloc_buffer.description`:

Description
-----------

Allocates the PCM substream buffer using \ :c:func:`vmalloc`\ , i.e., the memory is
contiguous in kernel virtual space, but not in physical memory.  Use this
if the buffer is accessed by kernel code but not by device DMA.

.. _`snd_pcm_lib_alloc_vmalloc_buffer.return`:

Return
------

1 if the buffer was changed, 0 if not changed, or a negative error
code.

.. _`snd_pcm_lib_alloc_vmalloc_32_buffer`:

snd_pcm_lib_alloc_vmalloc_32_buffer
===================================

.. c:function:: int snd_pcm_lib_alloc_vmalloc_32_buffer(struct snd_pcm_substream *substream, size_t size)

    allocate 32-bit-addressable buffer

    :param substream:
        the substream to allocate the buffer to
    :type substream: struct snd_pcm_substream \*

    :param size:
        the requested buffer size, in bytes
    :type size: size_t

.. _`snd_pcm_lib_alloc_vmalloc_32_buffer.description`:

Description
-----------

This function works like \ :c:func:`snd_pcm_lib_alloc_vmalloc_buffer`\ , but uses
\ :c:func:`vmalloc_32`\ , i.e., the pages are allocated from 32-bit-addressable memory.

.. _`snd_pcm_lib_alloc_vmalloc_32_buffer.return`:

Return
------

1 if the buffer was changed, 0 if not changed, or a negative error
code.

.. _`snd_pcm_sgbuf_get_addr`:

snd_pcm_sgbuf_get_addr
======================

.. c:function:: dma_addr_t snd_pcm_sgbuf_get_addr(struct snd_pcm_substream *substream, unsigned int ofs)

    Get the DMA address at the corresponding offset

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

    :param ofs:
        byte offset
    :type ofs: unsigned int

.. _`snd_pcm_sgbuf_get_ptr`:

snd_pcm_sgbuf_get_ptr
=====================

.. c:function:: void *snd_pcm_sgbuf_get_ptr(struct snd_pcm_substream *substream, unsigned int ofs)

    Get the virtual address at the corresponding offset

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

    :param ofs:
        byte offset
    :type ofs: unsigned int

.. _`snd_pcm_sgbuf_get_chunk_size`:

snd_pcm_sgbuf_get_chunk_size
============================

.. c:function:: unsigned int snd_pcm_sgbuf_get_chunk_size(struct snd_pcm_substream *substream, unsigned int ofs, unsigned int size)

    Compute the max size that fits within the contig. page from the given size

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

    :param ofs:
        byte offset
    :type ofs: unsigned int

    :param size:
        byte size to examine
    :type size: unsigned int

.. _`snd_pcm_mmap_data_open`:

snd_pcm_mmap_data_open
======================

.. c:function:: void snd_pcm_mmap_data_open(struct vm_area_struct *area)

    increase the mmap counter

    :param area:
        VMA
    :type area: struct vm_area_struct \*

.. _`snd_pcm_mmap_data_open.description`:

Description
-----------

PCM mmap callback should handle this counter properly

.. _`snd_pcm_mmap_data_close`:

snd_pcm_mmap_data_close
=======================

.. c:function:: void snd_pcm_mmap_data_close(struct vm_area_struct *area)

    decrease the mmap counter

    :param area:
        VMA
    :type area: struct vm_area_struct \*

.. _`snd_pcm_mmap_data_close.description`:

Description
-----------

PCM mmap callback should handle this counter properly

.. _`snd_pcm_limit_isa_dma_size`:

snd_pcm_limit_isa_dma_size
==========================

.. c:function:: void snd_pcm_limit_isa_dma_size(int dma, size_t *max)

    Get the max size fitting with ISA DMA transfer

    :param dma:
        DMA number
    :type dma: int

    :param max:
        pointer to store the max size
    :type max: size_t \*

.. _`snd_pcm_stream_str`:

snd_pcm_stream_str
==================

.. c:function:: const char *snd_pcm_stream_str(struct snd_pcm_substream *substream)

    Get a string naming the direction of a stream

    :param substream:
        the pcm substream instance
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_stream_str.return`:

Return
------

A string naming the direction of the stream.

.. _`snd_pcm_chmap_substream`:

snd_pcm_chmap_substream
=======================

.. c:function:: struct snd_pcm_substream *snd_pcm_chmap_substream(struct snd_pcm_chmap *info, unsigned int idx)

    get the PCM substream assigned to the given chmap info

    :param info:
        chmap information
    :type info: struct snd_pcm_chmap \*

    :param idx:
        the substream number index
    :type idx: unsigned int

.. _`pcm_format_to_bits`:

pcm_format_to_bits
==================

.. c:function:: u64 pcm_format_to_bits(snd_pcm_format_t pcm_format)

    Strong-typed conversion of pcm_format to bitwise

    :param pcm_format:
        PCM format
    :type pcm_format: snd_pcm_format_t

.. This file was automatic generated / don't edit.

