.. -*- coding: utf-8; mode: rst -*-

=========
fsl_dma.c
=========


.. _`fsl_dma_abort_stream`:

fsl_dma_abort_stream
====================

.. c:function:: void fsl_dma_abort_stream (struct snd_pcm_substream *substream)

    :param struct snd_pcm_substream \*substream:

        *undescribed*



.. _`fsl_dma_abort_stream.description`:

Description
-----------


This function should be called by the ISR whenever the DMA controller
halts data transfer.



.. _`fsl_dma_update_pointers`:

fsl_dma_update_pointers
=======================

.. c:function:: void fsl_dma_update_pointers (struct fsl_dma_private *dma_private)

    update LD pointers to point to the next period

    :param struct fsl_dma_private \*dma_private:

        *undescribed*



.. _`fsl_dma_update_pointers.description`:

Description
-----------


As each period is completed, this function changes the the link
descriptor pointers for that period to point to the next period.



.. _`fsl_dma_isr`:

fsl_dma_isr
===========

.. c:function:: irqreturn_t fsl_dma_isr (int irq, void *dev_id)

    :param int irq:
        IRQ of the DMA channel

    :param void \*dev_id:
        pointer to the dma_private structure for this DMA channel



.. _`fsl_dma_new`:

fsl_dma_new
===========

.. c:function:: int fsl_dma_new (struct snd_soc_pcm_runtime *rtd)

    :param struct snd_soc_pcm_runtime \*rtd:

        *undescribed*



.. _`fsl_dma_new.description`:

Description
-----------


This function is called when the codec driver calls :c:func:`snd_soc_new_pcms`,
once for each .dai_link in the machine driver's snd_soc_card
structure.

:c:func:`snd_dma_alloc_pages` is just a front-end to :c:func:`dma_alloc_coherent`, which
(currently) always allocates the DMA buffer in lowmem, even if GFP_HIGHMEM
is specified. Therefore, any DMA buffers we allocate will always be in low
memory, but we support for 36-bit physical addresses anyway.

Regardless of where the memory is actually allocated, since the device can
technically DMA to any 36-bit address, we do need to set the DMA mask to 36.



.. _`fsl_dma_open`:

fsl_dma_open
============

.. c:function:: int fsl_dma_open (struct snd_pcm_substream *substream)

    :param struct snd_pcm_substream \*substream:

        *undescribed*



.. _`fsl_dma_open.description`:

Description
-----------


Each substream has its own DMA buffer.

ALSA divides the DMA buffer into N periods.  We create NUM_DMA_LINKS link
descriptors that ping-pong from one period to the next.  For example, if
there are six periods and two link descriptors, this is how they look



.. _`fsl_dma_open.before-playback-starts`:

before playback starts
----------------------


The last link descriptor
____________  points back to the first
|            |
V            |
___    ___   |

|   |->|   |->|
|___|  |___|
|      |
|      |
V      V
_________________________________________

|      |      |      |      |      |      |  The DMA buffer is
|      |      |      |      |      |      |    divided into 6 parts
|______|______|______|______|______|______|

and here's how they look after the first period is finished playing::

  ____________
 |            |
 V            |
 ___    ___   |

|   |->|   |->|
|___|  |___|
|      |
|______________
|       |
V       V
_________________________________________

|      |      |      |      |      |      |
|      |      |      |      |      |      |
|______|______|______|______|______|______|

The first link descriptor now points to the third period.  The DMA
controller is currently playing the second period.  When it finishes, it
will jump back to the first descriptor and play the third period.



.. _`fsl_dma_open.there-are-four-reasons-we-do-this`:

There are four reasons we do this
---------------------------------


1. The only way to get the DMA controller to automatically restart the

   transfer when it gets to the end of the buffer is to use chaining
   mode.  Basic direct mode doesn't offer that feature.

2. We need to receive an interrupt at the end of every period.  The DMA

   controller can generate an interrupt at the end of every link transfer
   (aka segment).  Making each period into a DMA segment will give us the
   interrupts we need.

3. By creating only two link descriptors, regardless of the number of

   periods, we do not need to reallocate the link descriptors if the
   number of periods changes.

4. All of the audio data is still stored in a single, contiguous DMA

   buffer, which is what ALSA expects.  We're just dividing it into
   contiguous parts, and creating a link descriptor for each one.



.. _`fsl_dma_hw_params`:

fsl_dma_hw_params
=================

.. c:function:: int fsl_dma_hw_params (struct snd_pcm_substream *substream, struct snd_pcm_hw_params *hw_params)

    :param struct snd_pcm_substream \*substream:

        *undescribed*

    :param struct snd_pcm_hw_params \*hw_params:

        *undescribed*



.. _`fsl_dma_hw_params.description`:

Description
-----------


This function obtains hardware parameters about the opened stream and
programs the DMA controller accordingly.

One drawback of big-endian is that when copying integers of different
sizes to a fixed-sized register, the address to which the integer must be
copied is dependent on the size of the integer.

For example, if P is the address of a 32-bit register, and X is a 32-bit
integer, then X should be copied to address P.  However, if X is a 16-bit
integer, then it should be copied to P+2.  If X is an 8-bit register,
then it should be copied to P+3.

So for playback of 8-bit samples, the DMA controller must transfer single
bytes from the DMA buffer to the last byte of the STX0 register, i.e.
offset by 3 bytes. For 16-bit samples, the offset is two bytes.

For 24-bit samples, the offset is 1 byte.  However, the DMA controller
does not support 3-byte copies (the DAHTS register supports only 1, 2, 4,
and 8 bytes at a time).  So we do not support packed 24-bit samples.
24-bit data must be padded to 32 bits.



.. _`fsl_dma_pointer`:

fsl_dma_pointer
===============

.. c:function:: snd_pcm_uframes_t fsl_dma_pointer (struct snd_pcm_substream *substream)

    :param struct snd_pcm_substream \*substream:

        *undescribed*



.. _`fsl_dma_pointer.description`:

Description
-----------


This function is called by ALSA when ALSA wants to know where in the
stream buffer the hardware currently is.

For playback, the SAR register contains the physical address of the most
recent DMA transfer.  For capture, the value is in the DAR register.

The base address of the buffer is stored in the source_addr field of the
first link descriptor.



.. _`fsl_dma_hw_free`:

fsl_dma_hw_free
===============

.. c:function:: int fsl_dma_hw_free (struct snd_pcm_substream *substream)

    :param struct snd_pcm_substream \*substream:

        *undescribed*



.. _`fsl_dma_hw_free.description`:

Description
-----------


Release the resources allocated in :c:func:`fsl_dma_hw_params` and de-program the
registers.

This function can be called multiple times.



.. _`fsl_dma_close`:

fsl_dma_close
=============

.. c:function:: int fsl_dma_close (struct snd_pcm_substream *substream)

    :param struct snd_pcm_substream \*substream:

        *undescribed*



.. _`find_ssi_node`:

find_ssi_node
=============

.. c:function:: struct device_node *find_ssi_node (struct device_node *dma_channel_np)

    - returns the SSI node that points to its DMA channel node

    :param struct device_node \*dma_channel_np:

        *undescribed*



.. _`find_ssi_node.description`:

Description
-----------


Although this DMA driver attempts to operate independently of the other
devices, it still needs to determine some information about the SSI device
that it's working with.  Unfortunately, the device tree does not contain
a pointer from the DMA channel node to the SSI node -- the pointer goes the
other way.  So we need to scan the device tree for SSI nodes until we find
the one that points to the given DMA channel node.  It's ugly, but at least
it's contained in this one function.

