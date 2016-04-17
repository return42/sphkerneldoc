.. -*- coding: utf-8; mode: rst -*-

==============
patch_ca0132.c
==============


.. _`dspio_scp`:

dspio_scp
=========

.. c:function:: int dspio_scp (struct hda_codec *codec, int mod_id, int req, int dir, void *data, unsigned int len, void *reply, unsigned int *reply_len)

    :param struct hda_codec \*codec:
        the HDA codec

    :param int mod_id:
        ID of the DSP module to send the command

    :param int req:
        ID of request to send to the DSP module

    :param int dir:
        SET or GET

    :param void \*data:
        pointer to the data to send with the request, request specific

    :param unsigned int len:
        length of the data, in bytes

    :param void \*reply:
        point to the buffer to hold data returned for a reply

    :param unsigned int \*reply_len:
        length of the reply buffer returned from GET



.. _`dspio_scp.description`:

Description
-----------

Returns zero or a negative error code.



.. _`dsp_allocate_router_ports`:

dsp_allocate_router_ports
=========================

.. c:function:: int dsp_allocate_router_ports (struct hda_codec *codec, unsigned int num_chans, unsigned int ports_per_channel, unsigned int start_device, unsigned int *port_map)

    :param struct hda_codec \*codec:
        the HDA codec

    :param unsigned int num_chans:
        number of channels in the stream

    :param unsigned int ports_per_channel:
        number of ports per channel

    :param unsigned int start_device:
        start device

    :param unsigned int \*port_map:
        pointer to the port list to hold the allocated ports



.. _`dsp_allocate_router_ports.description`:

Description
-----------

Returns zero or a negative error code.



.. _`dspxfr_one_seg`:

dspxfr_one_seg
==============

.. c:function:: int dspxfr_one_seg (struct hda_codec *codec, const struct dsp_image_seg *fls, unsigned int reloc, struct dma_engine *dma_engine, unsigned int dma_chan, unsigned int port_map_mask, bool ovly)

    allocated DMA engine.

    :param struct hda_codec \*codec:
        the HDA codec

    :param const struct dsp_image_seg \*fls:
        pointer to a fast load image

    :param unsigned int reloc:
        Relocation address for loading single-segment overlays, or 0 for
        no relocation

    :param struct dma_engine \*dma_engine:
        pointer to DMA engine to be used for DSP download

    :param unsigned int dma_chan:
        The number of DMA channels used for DSP download

    :param unsigned int port_map_mask:
        port mapping

    :param bool ovly:
        TRUE if overlay format is required



.. _`dspxfr_one_seg.description`:

Description
-----------

Returns zero or a negative error code.



.. _`dspxfr_image`:

dspxfr_image
============

.. c:function:: int dspxfr_image (struct hda_codec *codec, const struct dsp_image_seg *fls_data, unsigned int reloc, unsigned int sample_rate, unsigned short channels, bool ovly)

    :param struct hda_codec \*codec:
        the HDA codec

    :param const struct dsp_image_seg \*fls_data:
        pointer to a fast load image

    :param unsigned int reloc:
        Relocation address for loading single-segment overlays, or 0 for
        no relocation

    :param unsigned int sample_rate:
        sampling rate of the stream used for DSP download

    :param unsigned short channels:
        channels of the stream used for DSP download

    :param bool ovly:
        TRUE if overlay format is required



.. _`dspxfr_image.description`:

Description
-----------

Returns zero or a negative error code.



.. _`dspload_image`:

dspload_image
=============

.. c:function:: int dspload_image (struct hda_codec *codec, const struct dsp_image_seg *fls, bool ovly, unsigned int reloc, bool autostart, int router_chans)

    Download DSP from a DSP Image Fast Load structure.

    :param struct hda_codec \*codec:
        the HDA codec

    :param const struct dsp_image_seg \*fls:
        pointer to a fast load image

    :param bool ovly:
        TRUE if overlay format is required

    :param unsigned int reloc:
        Relocation address for loading single-segment overlays, or 0 for
        no relocation

    :param bool autostart:
        TRUE if DSP starts after loading; ignored if ovly is TRUE

    :param int router_chans:
        number of audio router channels to be allocated (0 means use
        internal defaults; max is 32)



.. _`dspload_image.description`:

Description
-----------

Download DSP from a DSP Image Fast Load structure. This structure is a
linear, non-constant sized element array of structures, each of which
contain the count of the data to be loaded, the data itself, and the
corresponding starting chip address of the starting data location.
Returns zero or a negative error code.

