.. -*- coding: utf-8; mode: rst -*-

.. _API-dmx-section-cb:

==============
dmx_section_cb
==============

*man dmx_section_cb(9)*

*4.6.0-rc5*

DVB demux TS filter callback function prototype


Synopsis
========

.. c:function:: int dmx_section_cb( const u8 * buffer1, size_t buffer1_len, const u8 * buffer2, size_t buffer2_len, struct dmx_section_filter * source )

Arguments
=========

``buffer1``
    Pointer to the start of the filtered section, e.g. within the
    circular buffer of the demux driver.

``buffer1_len``
    Length of the filtered section data in ``buffer1``, including
    headers and CRC.

``buffer2``
    Pointer to the tail of the filtered section data, or NULL. Useful to
    handle the wrapping of a circular buffer.

``buffer2_len``
    Length of the filtered section data in ``buffer2``, including
    headers and CRC.

``source``
    Indicates which section feed is the source of the callback.


Description
===========

This function callback prototype, provided by the client of the demux
API, is called from the demux code. The function is only called when
filtering of sections has been enabled using the function
``dmx_ts_feed``.\ ``start_filtering``. When the demux driver has
received a complete section that matches at least one section filter,
the client is notified via this callback function. Normally this
function is called for each received section; however, it is also
possible to deliver multiple sections with one callback, for example
when the system load is high. If an error occurs while receiving a
section, this function should be called with the corresponding error
type set in the success field, whether or not there is data to deliver.
The Section Feed implementation should maintain a circular buffer for
received sections. However, this is not necessary if the Section Feed
API is implemented as a client of the TS Feed API, because the TS Feed
implementation then buffers the received data. The size of the circular
buffer can be configured using the ``dmx_ts_feed``.\ ``set`` function in
the Section Feed API. If there is no room in the circular buffer when a
new section is received, the section must be discarded. If this happens,
the value of the success parameter should be DMX_OVERRUN_ERROR on the
next callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
