.. -*- coding: utf-8; mode: rst -*-

.. _buffer-and-memory:

============================
Buffer and Memory Management
============================


.. _buffer-and-memory-buffer-types:

Buffer Types
============

ALSA provides several different buffer allocation functions depending on
the bus and the architecture. All these have a consistent API. The
allocation of physically-contiguous pages is done via
``snd_malloc_xxx_pages()`` function, where xxx is the bus type.

The allocation of pages with fallback is
``snd_malloc_xxx_pages_fallback()``. This function tries to allocate the
specified pages but if the pages are not available, it tries to reduce
the page sizes until enough space is found.

The release the pages, call ``snd_free_xxx_pages()`` function.

Usually, ALSA drivers try to allocate and reserve a large contiguous
physical space at the time the module is loaded for the later use. This
is called “pre-allocation”. As already written, you can call the
following function at pcm instance construction time (in the case of PCI
bus).


.. code-block:: c

      snd_pcm_lib_preallocate_pages_for_all(pcm, SNDRV_DMA_TYPE_DEV,
                                            snd_dma_pci_data(pci), size, max);

where ``size`` is the byte size to be pre-allocated and the ``max`` is
the maximum size to be changed via the ``prealloc`` proc file. The
allocator will try to get an area as large as possible within the given
size.

The second argument (type) and the third argument (device pointer) are
dependent on the bus. In the case of the ISA bus, pass
``snd_dma_isa_data()`` as the third argument with ``SNDRV_DMA_TYPE_DEV``
type. For the continuous buffer unrelated to the bus can be
pre-allocated with ``SNDRV_DMA_TYPE_CONTINUOUS`` type and the
``snd_dma_continuous_data(GFP_KERNEL)`` device pointer, where
``GFP_KERNEL`` is the kernel allocation flag to use. For the PCI
scatter-gather buffers, use ``SNDRV_DMA_TYPE_DEV_SG`` with
``snd_dma_pci_data(pci)`` (see the
:ref:`Non-Contiguous Buffers <buffer-and-memory-non-contiguous>`
section).

Once the buffer is pre-allocated, you can use the allocator in the
``hw_params`` callback:


.. code-block:: c

      snd_pcm_lib_malloc_pages(substream, size);

Note that you have to pre-allocate to use this function.


.. _buffer-and-memory-external-hardware:

External Hardware Buffers
=========================

Some chips have their own hardware buffers and the DMA transfer from the
host memory is not available. In such a case, you need to either 1)
copy/set the audio data directly to the external hardware buffer, or 2)
make an intermediate buffer and copy/set the data from it to the
external hardware buffer in interrupts (or in tasklets, preferably).

The first case works fine if the external hardware buffer is large
enough. This method doesn't need any extra buffers and thus is more
effective. You need to define the ``copy`` and ``silence`` callbacks for
the data transfer. However, there is a drawback: it cannot be mmapped.
The examples are GUS's GF1 PCM or emu8000's wavetable PCM.

The second case allows for mmap on the buffer, although you have to
handle an interrupt or a tasklet to transfer the data from the
intermediate buffer to the hardware buffer. You can find an example in
the vxpocket driver.

Another case is when the chip uses a PCI memory-map region for the
buffer instead of the host memory. In this case, mmap is available only
on certain architectures like the Intel one. In non-mmap mode, the data
cannot be transferred as in the normal way. Thus you need to define the
``copy`` and ``silence`` callbacks as well, as in the cases above. The
examples are found in ``rme32.c`` and ``rme96.c``.

The implementation of the ``copy`` and ``silence`` callbacks depends
upon whether the hardware supports interleaved or non-interleaved
samples. The ``copy`` callback is defined like below, a bit differently
depending whether the direction is playback or capture:


.. code-block:: c

      static int playback_copy(struct snd_pcm_substream *substream, int channel,
                   snd_pcm_uframes_t pos, void *src, snd_pcm_uframes_t count);
      static int capture_copy(struct snd_pcm_substream *substream, int channel,
                   snd_pcm_uframes_t pos, void *dst, snd_pcm_uframes_t count);

In the case of interleaved samples, the second argument (``channel``) is
not used. The third argument (``pos``) points the current position
offset in frames.

The meaning of the fourth argument is different between playback and
capture. For playback, it holds the source data pointer, and for
capture, it's the destination data pointer.

The last argument is the number of frames to be copied.

What you have to do in this callback is again different between playback
and capture directions. In the playback case, you copy the given amount
of data (``count``) at the specified pointer (``src``) to the specified
offset (``pos``) on the hardware buffer. When coded like memcpy-like
way, the copy would be like:


.. code-block:: c

      my_memcpy(my_buffer + frames_to_bytes(runtime, pos), src,
                frames_to_bytes(runtime, count));

For the capture direction, you copy the given amount of data (``count``)
at the specified offset (``pos``) on the hardware buffer to the
specified pointer (``dst``).


.. code-block:: c

      my_memcpy(dst, my_buffer + frames_to_bytes(runtime, pos),
                frames_to_bytes(runtime, count));

Note that both the position and the amount of data are given in frames.

In the case of non-interleaved samples, the implementation will be a bit
more complicated.

You need to check the channel argument, and if it's -1, copy the whole
channels. Otherwise, you have to copy only the specified channel. Please
check ``isa/gus/gus_pcm.c`` as an example.

The ``silence`` callback is also implemented in a similar way.


.. code-block:: c

      static int silence(struct snd_pcm_substream *substream, int channel,
                         snd_pcm_uframes_t pos, snd_pcm_uframes_t count);

The meanings of arguments are the same as in the ``copy`` callback,
although there is no ``src/dst`` argument. In the case of interleaved
samples, the channel argument has no meaning, as well as on ``copy``
callback.

The role of ``silence`` callback is to set the given amount (``count``)
of silence data at the specified offset (``pos``) on the hardware
buffer. Suppose that the data format is signed (that is, the silent-data
is 0), and the implementation using a memset-like function would be
like:


.. code-block:: c

      my_memcpy(my_buffer + frames_to_bytes(runtime, pos), 0,
                frames_to_bytes(runtime, count));

In the case of non-interleaved samples, again, the implementation
becomes a bit more complicated. See, for example, ``isa/gus/gus_pcm.c``.


.. _buffer-and-memory-non-contiguous:

Non-Contiguous Buffers
======================

If your hardware supports the page table as in emu10k1 or the buffer
descriptors as in via82xx, you can use the scatter-gather (SG) DMA. ALSA
provides an interface for handling SG-buffers. The API is provided in
``<sound/pcm.h>``.

For creating the SG-buffer handler, call
``snd_pcm_lib_preallocate_pages()`` or
``snd_pcm_lib_preallocate_pages_for_all()`` with
``SNDRV_DMA_TYPE_DEV_SG`` in the PCM constructor like other PCI
pre-allocator. You need to pass ``snd_dma_pci_data(pci)``, where pci is
the struct ``pci_dev`` pointer of the chip as well. The
``struct snd_sg_buf`` instance is created as substream->dma_private.
You can cast the pointer like:


.. code-block:: c

      struct snd_sg_buf *sgbuf = (struct snd_sg_buf *)substream->dma_private;

Then call ``snd_pcm_lib_malloc_pages()`` in the ``hw_params`` callback
as well as in the case of normal PCI buffer. The SG-buffer handler will
allocate the non-contiguous kernel pages of the given size and map them
onto the virtually contiguous memory. The virtual pointer is addressed
in runtime->dma_area. The physical address (runtime->dma_addr) is set
to zero, because the buffer is physically non-contiguous. The physical
address table is set up in sgbuf->table. You can get the physical
address at a certain offset via ``snd_pcm_sgbuf_get_addr()``.

When a SG-handler is used, you need to set ``snd_pcm_sgbuf_ops_page`` as
the ``page`` callback. (See
:ref:`page callback section <pcm-interface-operators-page-callback>`.)

To release the data, call ``snd_pcm_lib_free_pages()`` in the
``hw_free`` callback as usual.


.. _buffer-and-memory-vmalloced:

Vmalloc'ed Buffers
==================

It's possible to use a buffer allocated via ``vmalloc``, for example,
for an intermediate buffer. Since the allocated pages are not
contiguous, you need to set the ``page`` callback to obtain the physical
address at every offset.

The implementation of ``page`` callback would be like this:


.. code-block:: c

      #include <linux/vmalloc.h>

      /* get the physical page pointer on the given offset */
      static struct page *mychip_page(struct snd_pcm_substream *substream,
                                      unsigned long offset)
      {
              void *pageptr = substream->runtime->dma_area + offset;
              return vmalloc_to_page(pageptr);
      }




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
