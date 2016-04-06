
.. _vidioc-g-sliced-vbi-cap:

=============================
ioctl VIDIOC_G_SLICED_VBI_CAP
=============================

*man VIDIOC_G_SLICED_VBI_CAP(2)*

Query sliced VBI capabilities


Synopsis
========

.. c:function:: int ioctl( int fd, int request, struct v4l2_sliced_vbi_cap *argp )

Arguments
=========

``fd``
    File descriptor returned by :ref:`open() <func-open>`.

``request``
    VIDIOC_G_SLICED_VBI_CAP

``argp``


Description
===========

To find out which data services are supported by a sliced VBI capture or output device, applications initialize the ``type`` field of a struct
:ref:`v4l2_sliced_vbi_cap <v4l2-sliced-vbi-cap>`, clear the ``reserved`` array and call the ``VIDIOC_G_SLICED_VBI_CAP`` ioctl. The driver fills in the remaining fields or
returns an EINVAL error code if the sliced VBI API is unsupported or ``type`` is invalid.

Note the ``type`` field was added, and the ioctl changed from read-only to write-read, in Linux 2.6.19.


.. _v4l2-sliced-vbi-cap:

.. table:: struct v4l2_sliced_vbi_cap

    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+
    | __u16                                         | ``service_set``                               | A set of all data services     |                                |                                |
    |                                               |                                               | supported by the driver. Equal |                                |                                |
    |                                               |                                               | to the union of all elements   |                                |                                |
    |                                               |                                               | of the ``service_lines``       |                                |                                |
    |                                               |                                               | array.                         |                                |                                |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+
    | __u16                                         | ``service_lines``  [2][24]                    | Each element of this array     |                                |                                |
    |                                               |                                               | contains a set of data         |                                |                                |
    |                                               |                                               | services the hardware can look |                                |                                |
    |                                               |                                               | for or insert into a           |                                |                                |
    |                                               |                                               | particular scan line. Data     |                                |                                |
    |                                               |                                               | services are defined in        |                                |                                |
    |                                               |                                               | :ref:`vbi-services`.   Array   |                                |                                |
    |                                               |                                               | indices map to ITU-R line      |                                |                                |
    |                                               |                                               | numbers (see also              |                                |                                |
    |                                               |                                               | :ref:`vbi-525`   and           |                                |                                |
    |                                               |                                               | :ref:`vbi-625`)   as follows:  |                                |                                |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+
    |                                               |                                               | Element                        | 525 line systems               | 625 line systems               |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+
    |                                               |                                               | ``service_lines``\ [0][1]      | 1                              | 1                              |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+
    |                                               |                                               | ``service_lines``\ [0][23]     | 23                             | 23                             |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+
    |                                               |                                               | ``service_lines``\ [1][1]      | 264                            | 314                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+
    |                                               |                                               | ``service_lines``\ [1][23]     | 286                            | 336                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+
    |                                               |                                               |                                |                                |                                |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+
    |                                               |                                               | The number of VBI lines the    |                                |                                |
    |                                               |                                               | hardware can capture or output |                                |                                |
    |                                               |                                               | per frame, or the number of    |                                |                                |
    |                                               |                                               | services it can identify on a  |                                |                                |
    |                                               |                                               | given line may be limited. For |                                |                                |
    |                                               |                                               | example on PAL line 16 the     |                                |                                |
    |                                               |                                               | hardware may be able to look   |                                |                                |
    |                                               |                                               | for a VPS or Teletext signal,  |                                |                                |
    |                                               |                                               | but not both at the same time. |                                |                                |
    |                                               |                                               | Applications can learn about   |                                |                                |
    |                                               |                                               | these limits using the         |                                |                                |
    |                                               |                                               | :ref:`VIDIOC_S_FMT    <vidioc- |                                |                                |
    |                                               |                                               | g-fmt>`                        |                                |                                |
    |                                               |                                               | ioctl as described in          |                                |                                |
    |                                               |                                               | :ref:`sliced`.                 |                                |                                |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+
    |                                               |                                               |                                |                                |                                |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+
    |                                               |                                               | Drivers must set               |                                |                                |
    |                                               |                                               | ``service_lines``\ [0][0] and  |                                |                                |
    |                                               |                                               | ``service_lines``\ [1][0] to   |                                |                                |
    |                                               |                                               | zero.                          |                                |                                |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+
    | __u32                                         | ``type``                                      | Type of the data stream, see   |                                |                                |
    |                                               |                                               | :ref:`v4l2-buf-type`.   Should |                                |                                |
    |                                               |                                               | be                             |                                |                                |
    |                                               |                                               | ``V4L2_BUF_TYPE_SLICED_VBI_CAP |                                |                                |
    |                                               |                                               | TURE``                         |                                |                                |
    |                                               |                                               | or                             |                                |                                |
    |                                               |                                               | ``V4L2_BUF_TYPE_SLICED_VBI_OUT |                                |                                |
    |                                               |                                               | PUT``.                         |                                |                                |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+
    | __u32                                         | ``reserved``  [3]                             | This array is reserved for     |                                |                                |
    |                                               |                                               | future extensions.             |                                |                                |
    |                                               |                                               | Applications and drivers must  |                                |                                |
    |                                               |                                               | set it to zero.                |                                |                                |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------+--------------------------------+--------------------------------+



.. _vbi-services:

Sliced VBI services
===================

::

    TODO ... 


    <table pgwide="1" frame="none" id="vbi-services">
          <title>Sliced VBI services</title>
          <tgroup cols="5">
        <colspec colname="c1" colwidth="2⋆"/>
        <colspec colname="c2" colwidth="1⋆"/>
        <colspec colname="c3" colwidth="1⋆"/>
        <colspec colname="c4" colwidth="2⋆"/>
        <colspec colname="c5" colwidth="2⋆"/>
        <spanspec spanname="rlp" namest="c3" nameend="c5"/>
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
            <entry><constant>V4L2_SLICED_TELETEXT_B</constant> (Teletext
    System B)</entry>
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
            <entry><xref linkend="en300294"/>, <xref linkend="itu1119"/></entry>
            <entry>PAL/SECAM line 23</entry>
            <entry><screen>
    Byte        0                 1
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




Return Value
============

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.

EINVAL
    The value in the ``type`` field is wrong.
