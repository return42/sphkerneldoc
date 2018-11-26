.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/hda/patch_ca0132.c

.. _`dspio_scp`:

dspio_scp
=========

.. c:function:: int dspio_scp(struct hda_codec *codec, int mod_id, int src_id, int req, int dir, const void *data, unsigned int len, void *reply, unsigned int *reply_len)

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param mod_id:
        ID of the DSP module to send the command
    :type mod_id: int

    :param src_id:
        *undescribed*
    :type src_id: int

    :param req:
        ID of request to send to the DSP module
    :type req: int

    :param dir:
        SET or GET
    :type dir: int

    :param data:
        pointer to the data to send with the request, request specific
    :type data: const void \*

    :param len:
        length of the data, in bytes
    :type len: unsigned int

    :param reply:
        point to the buffer to hold data returned for a reply
    :type reply: void \*

    :param reply_len:
        length of the reply buffer returned from GET
    :type reply_len: unsigned int \*

.. _`dspio_scp.description`:

Description
-----------

Returns zero or a negative error code.

.. _`dsp_allocate_router_ports`:

dsp_allocate_router_ports
=========================

.. c:function:: int dsp_allocate_router_ports(struct hda_codec *codec, unsigned int num_chans, unsigned int ports_per_channel, unsigned int start_device, unsigned int *port_map)

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param num_chans:
        number of channels in the stream
    :type num_chans: unsigned int

    :param ports_per_channel:
        number of ports per channel
    :type ports_per_channel: unsigned int

    :param start_device:
        start device
    :type start_device: unsigned int

    :param port_map:
        pointer to the port list to hold the allocated ports
    :type port_map: unsigned int \*

.. _`dsp_allocate_router_ports.description`:

Description
-----------

Returns zero or a negative error code.

.. _`dspxfr_one_seg`:

dspxfr_one_seg
==============

.. c:function:: int dspxfr_one_seg(struct hda_codec *codec, const struct dsp_image_seg *fls, unsigned int reloc, struct dma_engine *dma_engine, unsigned int dma_chan, unsigned int port_map_mask, bool ovly)

    allocated DMA engine.

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param fls:
        pointer to a fast load image
    :type fls: const struct dsp_image_seg \*

    :param reloc:
        Relocation address for loading single-segment overlays, or 0 for
        no relocation
    :type reloc: unsigned int

    :param dma_engine:
        pointer to DMA engine to be used for DSP download
    :type dma_engine: struct dma_engine \*

    :param dma_chan:
        The number of DMA channels used for DSP download
    :type dma_chan: unsigned int

    :param port_map_mask:
        port mapping
    :type port_map_mask: unsigned int

    :param ovly:
        TRUE if overlay format is required
    :type ovly: bool

.. _`dspxfr_one_seg.description`:

Description
-----------

Returns zero or a negative error code.

.. _`dspxfr_image`:

dspxfr_image
============

.. c:function:: int dspxfr_image(struct hda_codec *codec, const struct dsp_image_seg *fls_data, unsigned int reloc, unsigned int sample_rate, unsigned short channels, bool ovly)

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param fls_data:
        pointer to a fast load image
    :type fls_data: const struct dsp_image_seg \*

    :param reloc:
        Relocation address for loading single-segment overlays, or 0 for
        no relocation
    :type reloc: unsigned int

    :param sample_rate:
        sampling rate of the stream used for DSP download
    :type sample_rate: unsigned int

    :param channels:
        channels of the stream used for DSP download
    :type channels: unsigned short

    :param ovly:
        TRUE if overlay format is required
    :type ovly: bool

.. _`dspxfr_image.description`:

Description
-----------

Returns zero or a negative error code.

.. _`dspload_image`:

dspload_image
=============

.. c:function:: int dspload_image(struct hda_codec *codec, const struct dsp_image_seg *fls, bool ovly, unsigned int reloc, bool autostart, int router_chans)

    Download DSP from a DSP Image Fast Load structure.

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param fls:
        pointer to a fast load image
    :type fls: const struct dsp_image_seg \*

    :param ovly:
        TRUE if overlay format is required
    :type ovly: bool

    :param reloc:
        Relocation address for loading single-segment overlays, or 0 for
        no relocation
    :type reloc: unsigned int

    :param autostart:
        TRUE if DSP starts after loading; ignored if ovly is TRUE
    :type autostart: bool

    :param router_chans:
        number of audio router channels to be allocated (0 means use
        internal defaults; max is 32)
    :type router_chans: int

.. _`dspload_image.description`:

Description
-----------

Download DSP from a DSP Image Fast Load structure. This structure is a
linear, non-constant sized element array of structures, each of which
contain the count of the data to be loaded, the data itself, and the
corresponding starting chip address of the starting data location.
Returns zero or a negative error code.

.. This file was automatic generated / don't edit.

