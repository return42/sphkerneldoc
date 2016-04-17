
.. _sliced:

=========================
Sliced VBI Data Interface
=========================

VBI stands for Vertical Blanking Interval, a gap in the sequence of lines of an analog video signal. During VBI no picture information is transmitted, allowing some time while the
electron beam of a cathode ray tube TV returns to the top of the screen.

Sliced VBI devices use hardware to demodulate data transmitted in the VBI. V4L2 drivers shall *not* do this by software, see also the :ref:`raw VBI interface <raw-vbi>`. The data
is passed as short packets of fixed size, covering one scan line each. The number of packets per video frame is variable.

Sliced VBI capture and output devices are accessed through the same character special files as raw VBI devices. When a driver supports both interfaces, the default function of a
``/dev/vbi`` device is *raw* VBI capturing or output, and the sliced VBI function is only available after calling the :ref:`VIDIOC_S_FMT <vidioc-g-fmt>` ioctl as defined below.
Likewise a ``/dev/video`` device may support the sliced VBI API, however the default function here is video capturing or output. Different file descriptors must be used to pass raw
and sliced VBI data simultaneously, if this is supported by the driver.


Querying Capabilities
=====================

Devices supporting the sliced VBI capturing or output API set the ``V4L2_CAP_SLICED_VBI_CAPTURE`` or ``V4L2_CAP_SLICED_VBI_OUTPUT`` flag respectively, in the ``capabilities`` field
of struct :ref:`v4l2_capability <v4l2-capability>` returned by the :ref:`VIDIOC_QUERYCAP <vidioc-querycap>` ioctl. At least one of the read/write, streaming or asynchronous
:ref:`I/O methods <io>` must be supported. Sliced VBI devices may have a tuner or modulator.


Supplemental Functions
======================

Sliced VBI devices shall support :ref:`video input or output <video>` and :ref:`tuner or modulator <tuner>` ioctls if they have these capabilities, and they may support
:ref:`control <control>` ioctls. The :ref:`video standard <standard>` ioctls provide information vital to program a sliced VBI device, therefore must be supported.


.. _sliced-vbi-format-negotitation:

Sliced VBI Format Negotiation
=============================

To find out which data services are supported by the hardware applications can call the :ref:`VIDIOC_G_SLICED_VBI_CAP <vidioc-g-sliced-vbi-cap>` ioctl. All drivers
implementing the sliced VBI interface must support this ioctl. The results may differ from those of the :ref:`VIDIOC_S_FMT <vidioc-g-fmt>` ioctl when the number of VBI lines
the hardware can capture or output per frame, or the number of services it can identify on a given line are limited. For example on PAL line 16 the hardware may be able to look for
a VPS or Teletext signal, but not both at the same time.

To determine the currently selected services applications set the ``type`` field of struct :ref:`v4l2_format <v4l2-format>` to ``V4L2_BUF_TYPE_SLICED_VBI_CAPTURE`` or
``V4L2_BUF_TYPE_SLICED_VBI_OUTPUT``, and the :ref:`VIDIOC_G_FMT <vidioc-g-fmt>` ioctl fills the ``fmt.sliced`` member, a struct
:ref:`v4l2_sliced_vbi_format <v4l2-sliced-vbi-format>`.

Applications can request different parameters by initializing or modifying the ``fmt.sliced`` member and calling the :ref:`VIDIOC_S_FMT <vidioc-g-fmt>` ioctl with a pointer to
the ``v4l2_format`` structure.

The sliced VBI API is more complicated than the raw VBI API because the hardware must be told which VBI service to expect on each scan line. Not all services may be supported by
the hardware on all lines (this is especially true for VBI output where Teletext is often unsupported and other services can only be inserted in one specific line). In many cases,
however, it is sufficient to just set the ``service_set`` field to the required services and let the driver fill the ``service_lines`` array according to hardware capabilities.
Only if more precise control is needed should the programmer set the ``service_lines`` array explicitly.

The :ref:`VIDIOC_S_FMT <vidioc-g-fmt>` ioctl modifies the parameters according to hardware capabilities. When the driver allocates resources at this point, it may return an
EBUSY error code if the required resources are temporarily unavailable. Other resource allocation points which may return EBUSY can be the
:ref:`VIDIOC_STREAMON <vidioc-streamon>` ioctl and the first :ref:`read() <func-read>`, :ref:`write() <func-write>` and :ref:`select() <func-select>` call.


.. _v4l2-sliced-vbi-format:

struct v4l2_sliced_vbi_format
=============================

::

    TODO ... 


    <table frame="none" pgwide="1" id="v4l2-sliced-vbi-format">
          <title>struct
    <structname>v4l2_sliced_vbi_format</structname></title>
          <tgroup cols="5">
        <colspec colname="c1" colwidth="3⋆"/>
        <colspec colname="c2" colwidth="3⋆"/>
        <colspec colname="c3" colwidth="2⋆"/>
        <colspec colname="c4" colwidth="2⋆"/>
        <colspec colname="c5" colwidth="2⋆"/>
        <spanspec namest="c3" nameend="c5" spanname="hspan"/>
        <tbody valign="top">
          <row>
            <entry>__u32</entry>
            <entry><structfield>service_set</structfield></entry>
            <entry spanname="hspan"><para>If
    <structfield>service_set</structfield> is non-zero when passed with
    <link linkend="vidioc-g-fmt"><constant>VIDIOC_S_FMT</constant></link> or <link linkend="vidioc-g-fmt"><constant>VIDIOC_TRY_FMT</constant></link>, the
    <structfield>service_lines</structfield> array will be filled by the
    driver according to the services specified in this field. For example,
    if <structfield>service_set</structfield> is initialized with
    <constant>V4L2_SLICED_TELETEXT_B | V4L2_SLICED_WSS_625</constant>, a
    driver for the cx25840 video decoder sets lines 7-22 of both
    fields<footnote><para>According to <link linkend="ets300706">ETS 300 706</link> lines 6-22 of the
    first field and lines 5-22 of the second field may carry Teletext
    data.</para></footnote> to <constant>V4L2_SLICED_TELETEXT_B</constant>
    and line 23 of the first field to
    <constant>V4L2_SLICED_WSS_625</constant>. If
    <structfield>service_set</structfield> is set to zero, then the values
    of <structfield>service_lines</structfield> will be used instead.
    </para><para>On return the driver sets this field to the union of all
    elements of the returned <structfield>service_lines</structfield>
    array. It may contain less services than requested, perhaps just one,
    if the hardware cannot handle more services simultaneously. It may be
    empty (zero) if none of the requested services are supported by the
    hardware.</para></entry>
          </row>
          <row>
            <entry>__u16</entry>
            <entry><structfield>service_lines</structfield>[2][24]</entry>
            <entry spanname="hspan"><para>Applications initialize this
    array with sets of data services the driver shall look for or insert
    on the respective scan line. Subject to hardware capabilities drivers
    return the requested set, a subset, which may be just a single
    service, or an empty set. When the hardware cannot handle multiple
    services on the same line the driver shall choose one. No assumptions
    can be made on which service the driver chooses.</para><para>Data
    services are defined in <xref linkend="vbi-services2"/>. Array indices
    map to ITU-R line numbers (see also <xref linkend="vbi-525"/> and <xref linkend="vbi-625"/>) as follows: <!-- No nested
    tables, sigh. --></para></entry>
          </row>
          <row>
            <entry/>
            <entry/>
            <entry>Element</entry>
            <entry>525 line systems</entry>
            <entry>625 line systems</entry>
          </row>
          <row>
            <entry/>
            <entry/>
            <entry><structfield>service_lines</structfield>[0][1]</entry>
            <entry align="center">1</entry>
            <entry align="center">1</entry>
          </row>
          <row>
            <entry/>
            <entry/>
            <entry><structfield>service_lines</structfield>[0][23]</entry>
            <entry align="center">23</entry>
            <entry align="center">23</entry>
          </row>
          <row>
            <entry/>
            <entry/>
            <entry><structfield>service_lines</structfield>[1][1]</entry>
            <entry align="center">264</entry>
            <entry align="center">314</entry>
          </row>
          <row>
            <entry/>
            <entry/>
            <entry><structfield>service_lines</structfield>[1][23]</entry>
            <entry align="center">286</entry>
            <entry align="center">336</entry>
          </row>
          <!-- End of line numbers table. -->
          <row>
            <entry/>
            <entry/>
            <entry spanname="hspan">Drivers must set
    <structfield>service_lines</structfield>[0][0] and
    <structfield>service_lines</structfield>[1][0] to zero.
    The <constant>V4L2_VBI_ITU_525_F1_START</constant>,
    <constant>V4L2_VBI_ITU_525_F2_START</constant>,
    <constant>V4L2_VBI_ITU_625_F1_START</constant> and
    <constant>V4L2_VBI_ITU_625_F2_START</constant> defines give the start
    line numbers for each field for each 525 or 625 line format as a
    convenience.  Don't forget that ITU line numbering starts at 1, not 0.
    </entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>io_size</structfield></entry>
            <entry spanname="hspan">Maximum number of bytes passed by
    one <link linkend="func-read"><function>read()</function></link> or <link linkend="func-write"><function>write()</function></link> call, and the buffer size in bytes for
    the <link linkend="vidioc-qbuf"><constant>VIDIOC_QBUF</constant></link> and <link linkend="vidioc-qbuf"><constant>VIDIOC_DQBUF</constant></link> ioctl. Drivers set this field to
    the size of struct <link linkend="v4l2-sliced-vbi-data">v4l2_sliced_vbi_data</link> times the number of non-zero
    elements in the returned <structfield>service_lines</structfield>
    array (that is the number of lines potentially carrying data).</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>reserved</structfield>[2]</entry>
            <entry spanname="hspan">This array is reserved for future
    extensions. Applications and drivers must set it to zero.</entry>
          </row>
        </tbody>
          </tgroup>
        </table>




.. _vbi-services2:

Sliced VBI services
===================

::

    TODO ... 


    <table frame="none" pgwide="1" id="vbi-services2">
          <title>Sliced VBI services</title>
          <tgroup cols="5">
        <colspec colname="c1" colwidth="2⋆"/>
        <colspec colname="c2" colwidth="1⋆"/>
        <colspec colname="c3" colwidth="1⋆"/>
        <colspec colname="c4" colwidth="2⋆"/>
        <colspec colname="c5" colwidth="2⋆"/>
        <spanspec namest="c3" nameend="c5" spanname="rlp"/>
        <thead>
          <row>
            <entry>Symbol</entry>
            <entry>Value</entry>
            <entry>Reference</entry>
            <entry>Lines, usually</entry>
            <entry>Payload</entry>
          </row>
        </thead>
        <tbody valign="top">
          <row>
            <entry><constant>V4L2_SLICED_TELETEXT_B</constant>
    (Teletext System B)</entry>
            <entry>0x0001</entry>
            <entry><xref linkend="ets300706"/>, <xref linkend="itu653"/></entry>
            <entry>PAL/SECAM line 7-22, 320-335 (second field 7-22)</entry>
            <entry>Last 42 of the 45 byte Teletext packet, that is
    without clock run-in and framing code, lsb first transmitted.</entry>
          </row>
          <row>
            <entry><constant>V4L2_SLICED_VPS</constant></entry>
            <entry>0x0400</entry>
            <entry><xref linkend="ets300231"/></entry>
            <entry>PAL line 16</entry>
            <entry>Byte number 3 to 15 according to Figure 9 of
    ETS 300 231, lsb first transmitted.</entry>
          </row>
          <row>
            <entry><constant>V4L2_SLICED_CAPTION_525</constant></entry>
            <entry>0x1000</entry>
            <entry><xref linkend="cea608"/></entry>
            <entry>NTSC line 21, 284 (second field 21)</entry>
            <entry>Two bytes in transmission order, including parity
    bit, lsb first transmitted.</entry>
          </row>
          <row>
            <entry><constant>V4L2_SLICED_WSS_625</constant></entry>
            <entry>0x4000</entry>
            <entry><xref linkend="itu1119"/>, <xref linkend="en300294"/></entry>
            <entry>PAL/SECAM line 23</entry>
            <entry><screen>
    Byte         0                 1
          msb         lsb  msb           lsb
     Bit  7 6 5 4 3 2 1 0  x x 13 12 11 10 9
    </screen></entry>
          </row>
          <row>
            <entry><constant>V4L2_SLICED_VBI_525</constant></entry>
            <entry>0x1000</entry>
            <entry spanname="rlp">Set of services applicable to 525
    line systems.</entry>
          </row>
          <row>
            <entry><constant>V4L2_SLICED_VBI_625</constant></entry>
            <entry>0x4401</entry>
            <entry spanname="rlp">Set of services applicable to 625
    line systems.</entry>
          </row>
        </tbody>
          </tgroup>
        </table>



Drivers may return an EINVAL error code when applications attempt to read or write data without prior format negotiation, after switching the video standard (which may invalidate
the negotiated VBI parameters) and after switching the video input (which may change the video standard as a side effect). The :ref:`VIDIOC_S_FMT <vidioc-g-fmt>` ioctl may
return an EBUSY error code when applications attempt to change the format while i/o is in progress (between a :ref:`VIDIOC_STREAMON <vidioc-streamon>` and
:ref:`VIDIOC_STREAMOFF <vidioc-streamon>` call, and after the first :ref:`read() <func-read>` or :ref:`write() <func-write>` call).


Reading and writing sliced VBI data
===================================

A single :ref:`read() <func-read>` or :ref:`write() <func-write>` call must pass all data belonging to one video frame. That is an array of ``v4l2_sliced_vbi_data`` structures
with one or more elements and a total size not exceeding ``io_size`` bytes. Likewise in streaming I/O mode one buffer of ``io_size`` bytes must contain data of one video frame. The
``id`` of unused ``v4l2_sliced_vbi_data`` elements must be zero.


.. _v4l2-sliced-vbi-data:

.. table:: struct v4l2_sliced_vbi_data

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                                               | ``id``                 | A flag from :ref:`vbi-services`   identifying the type of data in this packet. Only a      |
    |                                                                     |                        | single bit must be set. When the ``id`` of a captured packet is zero, the packet is empty  |
    |                                                                     |                        | and the contents of other fields are undefined. Applications shall ignore empty packets.   |
    |                                                                     |                        | When the ``id`` of a packet for output is zero the contents of the ``data`` field are      |
    |                                                                     |                        | undefined and the driver must no longer insert data on the requested ``field`` and         |
    |                                                                     |                        | ``line``.                                                                                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                                               | ``field``              | The video field number this data has been captured from, or shall be inserted at. ``0``    |
    |                                                                     |                        | for the first field, ``1`` for the second field.                                           |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                                               | ``line``               | The field (as opposed to frame) line number this data has been captured from, or shall be  |
    |                                                                     |                        | inserted at. See :ref:`vbi-525`   and :ref:`vbi-625`   for valid values. Sliced VBI        |
    |                                                                     |                        | capture devices can set the line number of all packets to ``0`` if the hardware cannot     |
    |                                                                     |                        | reliably identify scan lines. The field number must always be valid.                       |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                                               | ``reserved``           | This field is reserved for future extensions. Applications and drivers must set it to      |
    |                                                                     |                        | zero.                                                                                      |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                                                | ``data``  [48]         | The packet payload. See :ref:`vbi-services`   for the contents and number of bytes passed  |
    |                                                                     |                        | for each data type. The contents of padding bytes at the end of this array are undefined,  |
    |                                                                     |                        | drivers and applications shall ignore them.                                                |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+


Packets are always passed in ascending line number order, without duplicate line numbers. The :ref:`write() <func-write>` function and the :ref:`VIDIOC_QBUF <vidioc-qbuf>`
ioctl must return an EINVAL error code when applications violate this rule. They must also return an EINVAL error code when applications pass an incorrect field or line number, or
a combination of ``field``, ``line`` and ``id`` which has not been negotiated with the :ref:`VIDIOC_G_FMT <vidioc-g-fmt>` or :ref:`VIDIOC_S_FMT <vidioc-g-fmt>` ioctl. When
the line numbers are unknown the driver must pass the packets in transmitted order. The driver can insert empty packets with ``id`` set to zero anywhere in the packet array.

To assure synchronization and to distinguish from frame dropping, when a captured frame does not carry any of the requested data services drivers must pass one or more empty
packets. When an application fails to pass VBI data in time for output, the driver must output the last VPS and WSS packet again, and disable the output of Closed Caption and
Teletext data, or output data which is ignored by Closed Caption and Teletext decoders.

A sliced VBI device may support :ref:`read/write <rw>` and/or streaming (:ref:`memory mapping <mmap>` and/or :ref:`user pointer <userp>`) I/O. The latter bears the
possibility of synchronizing video and VBI data by using buffer timestamps.


Sliced VBI Data in MPEG Streams
===============================

If a device can produce an MPEG output stream, it may be capable of providing :ref:`negotiated sliced VBI services <sliced-vbi-format-negotitation>` as data embedded in the MPEG
stream. Users or applications control this sliced VBI data insertion with the :ref:`V4L2_CID_MPEG_STREAM_VBI_FMT <v4l2-mpeg-stream-vbi-fmt>` control.

If the driver does not provide the :ref:`V4L2_CID_MPEG_STREAM_VBI_FMT <v4l2-mpeg-stream-vbi-fmt>` control, or only allows that control to be set to
:ref:`V4L2_MPEG_STREAM_VBI_FMT_NONE <v4l2-mpeg-stream-vbi-fmt>`, then the device cannot embed sliced VBI data in the MPEG stream.

The :ref:`V4L2_CID_MPEG_STREAM_VBI_FMT <v4l2-mpeg-stream-vbi-fmt>` control does not implicitly set the device driver to capture nor cease capturing sliced VBI data. The
control only indicates to embed sliced VBI data in the MPEG stream, if an application has negotiated sliced VBI service be captured.

It may also be the case that a device can embed sliced VBI data in only certain types of MPEG streams: for example in an MPEG-2 PS but not an MPEG-2 TS. In this situation, if
sliced VBI data insertion is requested, the sliced VBI data will be embedded in MPEG stream types when supported, and silently omitted from MPEG stream types where sliced VBI data
insertion is not supported by the device.

The following subsections specify the format of the embedded sliced VBI data.


MPEG Stream Embedded, Sliced VBI Data Format: NONE
--------------------------------------------------

The :ref:`V4L2_MPEG_STREAM_VBI_FMT_NONE <v4l2-mpeg-stream-vbi-fmt>` embedded sliced VBI format shall be interpreted by drivers as a control to cease embedding sliced VBI
data in MPEG streams. Neither the device nor driver shall insert "empty" embedded sliced VBI data packets in the MPEG stream when this format is set. No MPEG stream data structures
are specified for this format.


MPEG Stream Embedded, Sliced VBI Data Format: IVTV
--------------------------------------------------

The :ref:`V4L2_MPEG_STREAM_VBI_FMT_IVTV <v4l2-mpeg-stream-vbi-fmt>` embedded sliced VBI format, when supported, indicates to the driver to embed up to 36 lines of sliced VBI
data per frame in an MPEG-2 *Private Stream 1 PES* packet encapsulated in an MPEG-2 *Program Pack* in the MPEG stream.

*Historical context*: This format specification originates from a custom, embedded, sliced VBI data format used by the ``ivtv`` driver. This format has already been informally
specified in the kernel sources in the file ``Documentation/video4linux/cx2341x/README.vbi`` . The maximum size of the payload and other aspects of this format are driven by the
CX23415 MPEG decoder's capabilities and limitations with respect to extracting, decoding, and displaying sliced VBI data embedded within an MPEG stream.

This format's use is *not* exclusive to the ``ivtv`` driver *nor* exclusive to CX2341x devices, as the sliced VBI data packet insertion into the MPEG stream is implemented in
driver software. At least the ``cx18`` driver provides sliced VBI data insertion into an MPEG-2 PS in this format as well.

The following definitions specify the payload of the MPEG-2 *Private Stream 1 PES* packets that contain sliced VBI data when
:ref:`V4L2_MPEG_STREAM_VBI_FMT_IVTV <v4l2-mpeg-stream-vbi-fmt>` is set. (The MPEG-2 *Private Stream 1 PES* packet header and encapsulating MPEG-2 *Program Pack* header are
not detailed here. Please refer to the MPEG-2 specifications for details on those packet headers.)

The payload of the MPEG-2 *Private Stream 1 PES* packets that contain sliced VBI data is specified by struct :ref:`v4l2_mpeg_vbi_fmt_ivtv <v4l2-mpeg-vbi-fmt-ivtv>`. The
payload is variable length, depending on the actual number of lines of sliced VBI data present in a video frame. The payload may be padded at the end with unspecified fill bytes to
align the end of the payload to a 4-byte boundary. The payload shall never exceed 1552 bytes (2 fields with 18 lines/field with 43 bytes of data/line and a 4 byte magic number).


.. _v4l2-mpeg-vbi-fmt-ivtv:

struct v4l2_mpeg_vbi_fmt_ivtv
=============================

::

    TODO ... 


    <table frame="none" pgwide="1" id="v4l2-mpeg-vbi-fmt-ivtv">
          <title>struct <structname>v4l2_mpeg_vbi_fmt_ivtv</structname>
          </title>
          <tgroup cols="4">
        <colspec colname="c1" colwidth="1*"/><colspec colname="c2" colwidth="1*"/><colspec colname="c3" colwidth="1*"/><colspec colname="c4" colwidth="2*"/><spanspec spanname="hspan" namest="c1" nameend="c4"/>
        <tbody valign="top">
          <row>
            <entry>__u8</entry>
            <entry><structfield>magic</structfield>[4]</entry>
            <entry/>
            <entry>A "magic" constant from <xref linkend="v4l2-mpeg-vbi-fmt-ivtv-magic"/> that indicates
    this is a valid sliced VBI data payload and also indicates which
    member of the anonymous union, <structfield>itv0</structfield> or
    <structfield>ITV0</structfield>, to use for the payload data.</entry>
          </row>
          <row>
            <entry>union</entry>
            <entry>(anonymous)</entry>
          </row>
          <row>
            <entry/>
            <entry>struct <link linkend="v4l2-mpeg-vbi-itv0">
              <structname>v4l2_mpeg_vbi_itv0</structname></link>
            </entry>
            <entry><structfield>itv0</structfield></entry>
            <entry>The primary form of the sliced VBI data payload
    that contains anywhere from 1 to 35 lines of sliced VBI data.
    Line masks are provided in this form of the payload indicating
    which VBI lines are provided.</entry>
          </row>
          <row>
            <entry/>
            <entry>struct <link linkend="v4l2-mpeg-vbi-itv0-1">
              <structname>v4l2_mpeg_vbi_ITV0</structname></link>
            </entry>
            <entry><structfield>ITV0</structfield></entry>
            <entry>An alternate form of the sliced VBI data payload
    used when 36 lines of sliced VBI data are present.  No line masks are
    provided in this form of the payload; all valid line mask bits are
    implcitly set.</entry>
          </row>
        </tbody>
          </tgroup>
        </table>




.. _v4l2-mpeg-vbi-fmt-ivtv-magic:

Magic Constants for struct v4l2_mpeg_vbi_fmt_ivtv magic field
=============================================================

::

    TODO ... 


    <table frame="none" pgwide="1" id="v4l2-mpeg-vbi-fmt-ivtv-magic">
          <title>Magic Constants for struct <link linkend="v4l2-mpeg-vbi-fmt-ivtv">v4l2_mpeg_vbi_fmt_ivtv</link>
        <structfield>magic</structfield> field</title>
          <tgroup cols="3">
        <colspec colname="c1" colwidth="3*"/><colspec colname="c2" colwidth="1*"/><colspec colname="c3" colwidth="4*"/><spanspec spanname="hspan" namest="c1" nameend="c3"/>
        <thead>
          <row>
            <entry align="left">Defined Symbol</entry>
            <entry align="left">Value</entry>
            <entry align="left">Description</entry>
          </row>
        </thead>
        <tbody valign="top">
          <row>
            <entry><constant>V4L2_MPEG_VBI_IVTV_MAGIC0</constant>
            </entry>
            <entry>"itv0"</entry>
            <entry>Indicates the <structfield>itv0</structfield>
    member of the union in struct <link linkend="v4l2-mpeg-vbi-fmt-ivtv">v4l2_mpeg_vbi_fmt_ivtv</link> is valid.</entry>
          </row>
          <row>
            <entry><constant>V4L2_MPEG_VBI_IVTV_MAGIC1</constant>
            </entry>
            <entry>"ITV0"</entry>
            <entry>Indicates the <structfield>ITV0</structfield>
    member of the union in struct <link linkend="v4l2-mpeg-vbi-fmt-ivtv">v4l2_mpeg_vbi_fmt_ivtv</link> is valid and
    that 36 lines of sliced VBI data are present.</entry>
          </row>
        </tbody>
          </tgroup>
        </table>




.. _v4l2-mpeg-vbi-itv0:

struct v4l2_mpeg_vbi_itv0
=========================

::

    TODO ... 


    <table frame="none" pgwide="1" id="v4l2-mpeg-vbi-itv0">
          <title>struct <structname>v4l2_mpeg_vbi_itv0</structname>
          </title>
          <tgroup cols="3">
        <colspec colname="c1" colwidth="1*"/><colspec colname="c2" colwidth="1*"/><colspec colname="c3" colwidth="2*"/><spanspec spanname="hspan" namest="c1" nameend="c3"/>
        <tbody valign="top">
          <row>
            <entry>__le32</entry>
            <entry><structfield>linemask</structfield>[2]</entry>
            <entry><para>Bitmasks indicating the VBI service lines
    present.  These <structfield>linemask</structfield> values are stored
    in little endian byte order in the MPEG stream.  Some reference
    <structfield>linemask</structfield> bit positions with their
    corresponding VBI line number and video field are given below.
    b<subscript>0</subscript> indicates the least significant bit of a
    <structfield>linemask</structfield> value:<screen>
    <structfield>linemask</structfield>[0] b<subscript>0</subscript>:       line  6     first field
    <structfield>linemask</structfield>[0] b<subscript>17</subscript>:      line 23     first field
    <structfield>linemask</structfield>[0] b<subscript>18</subscript>:      line  6     second field
    <structfield>linemask</structfield>[0] b<subscript>31</subscript>:      line 19     second field
    <structfield>linemask</structfield>[1] b<subscript>0</subscript>:       line 20     second field
    <structfield>linemask</structfield>[1] b<subscript>3</subscript>:       line 23     second field
    <structfield>linemask</structfield>[1] b<subscript>4</subscript>-b<subscript>31</subscript>:    unused and set to 0</screen></para></entry>
          </row>
          <row>
            <entry>struct <link linkend="v4l2-mpeg-vbi-itv0-line">
              <structname>v4l2_mpeg_vbi_itv0_line</structname></link>
            </entry>
            <entry><structfield>line</structfield>[35]</entry>
            <entry>This is a variable length array that holds from 1
    to 35 lines of sliced VBI data.  The sliced VBI data lines present
    correspond to the bits set in the <structfield>linemask</structfield>
    array, starting from b<subscript>0</subscript> of <structfield>
    linemask</structfield>[0] up through b<subscript>31</subscript> of
    <structfield>linemask</structfield>[0], and from b<subscript>0
    </subscript> of <structfield>linemask</structfield>[1] up through b
    <subscript>3</subscript> of <structfield>linemask</structfield>[1].
    <structfield>line</structfield>[0] corresponds to the first bit
    found set in the <structfield>linemask</structfield> array,
    <structfield>line</structfield>[1] corresponds to the second bit
    found set in the <structfield>linemask</structfield> array, etc.
    If no <structfield>linemask</structfield> array bits are set, then
    <structfield>line</structfield>[0] may contain one line of
    unspecified data that should be ignored by applications.</entry>
          </row>
        </tbody>
          </tgroup>
        </table>




.. _v4l2-mpeg-vbi-itv0-1:

.. table:: struct v4l2_mpeg_vbi_ITV0

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct                                        | ``line``\ [36]                                | A fixed length array of 36 lines of sliced VBI data. ``line``\ [0] through ``line``\ [17]  |
    | :ref:`v4l2_mpeg_vbi_itv0_line      <v4l2-mpeg |                                               | correspond to lines 6 through 23 of the first field. ``line``  [18] through ``line``  [35] |
    | -vbi-itv0-line>`                              |                                               | corresponds to lines 6 through 23 of the second field.                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-mpeg-vbi-itv0-line:

struct v4l2_mpeg_vbi_itv0_line
==============================

::

    TODO ... 


    <table frame="none" pgwide="1" id="v4l2-mpeg-vbi-itv0-line">
          <title>struct <structname>v4l2_mpeg_vbi_itv0_line</structname>
          </title>
          <tgroup cols="3">
        <colspec colname="c1" colwidth="1*"/><colspec colname="c2" colwidth="1*"/><colspec colname="c3" colwidth="2*"/><spanspec spanname="hspan" namest="c1" nameend="c3"/>
        <tbody valign="top">
          <row>
            <entry>__u8</entry>
            <entry><structfield>id</structfield></entry>
            <entry>A line identifier value from
    <xref linkend="ITV0-Line-Identifier-Constants"/> that indicates
    the type of sliced VBI data stored on this line.</entry>
          </row>
          <row>
            <entry>__u8</entry>
            <entry><structfield>data</structfield>[42]</entry>
            <entry>The sliced VBI data for the line.</entry>
          </row>
        </tbody>
          </tgroup>
        </table>




.. _ITV0-Line-Identifier-Constants:

.. table:: Line Identifiers for struct v4l2_mpeg_vbi_itv0_line id field

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | Defined Symbol                                                      | Value                  | Description                                                                                |
    +=====================================================================+========================+============================================================================================+
    | ``V4L2_MPEG_VBI_IVTV_TELETEXT_B``                                   | 1                      | Refer to :ref:`Sliced  VBI services <vbi-services2>`  for a description of the line        |
    |                                                                     |                        | payload.                                                                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_MPEG_VBI_IVTV_CAPTION_525``                                  | 4                      | Refer to :ref:`Sliced  VBI services <vbi-services2>`  for a description of the line        |
    |                                                                     |                        | payload.                                                                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_MPEG_VBI_IVTV_WSS_625``                                      | 5                      | Refer to :ref:`Sliced  VBI services <vbi-services2>`  for a description of the line        |
    |                                                                     |                        | payload.                                                                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_MPEG_VBI_IVTV_VPS``                                          | 7                      | Refer to :ref:`Sliced  VBI services <vbi-services2>`  for a description of the line        |
    |                                                                     |                        | payload.                                                                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+


