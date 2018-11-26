.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/core/dc.c

.. _`dc_stream_configure_crc`:

dc_stream_configure_crc
=======================

.. c:function:: bool dc_stream_configure_crc(struct dc *dc, struct dc_stream_state *stream, bool enable, bool continuous)

    Configure CRC capture for the given stream.

    :param dc:
        DC Object
    :type dc: struct dc \*

    :param stream:
        The stream to configure CRC on.
    :type stream: struct dc_stream_state \*

    :param enable:
        Enable CRC if true, disable otherwise.
    :type enable: bool

    :param continuous:
        Capture CRC on every frame if true. Otherwise, only capture
        once.
    :type continuous: bool

.. _`dc_stream_configure_crc.description`:

Description
-----------

By default, only CRC0 is configured, and the entire frame is used to
calculate the crc.

.. _`dc_stream_get_crc`:

dc_stream_get_crc
=================

.. c:function:: bool dc_stream_get_crc(struct dc *dc, struct dc_stream_state *stream, uint32_t *r_cr, uint32_t *g_y, uint32_t *b_cb)

    Get CRC values for the given stream.

    :param dc:
        DC object
    :type dc: struct dc \*

    :param stream:
        The DC stream state of the stream to get CRCs from.
    :type stream: struct dc_stream_state \*

    :param r_cr:
        CRC values for the three channels are stored here.
    :type r_cr: uint32_t \*

    :param g_y:
        *undescribed*
    :type g_y: uint32_t \*

    :param b_cb:
        *undescribed*
    :type b_cb: uint32_t \*

.. _`dc_stream_get_crc.description`:

Description
-----------

dc_stream_configure_crc needs to be called beforehand to enable CRCs.
Return false if stream is not found, or if CRCs are not enabled.

.. This file was automatic generated / don't edit.

