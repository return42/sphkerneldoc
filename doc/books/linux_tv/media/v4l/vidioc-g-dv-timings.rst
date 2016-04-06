
.. _vidioc-g-dv-timings:

==============================================
ioctl VIDIOC_G_DV_TIMINGS, VIDIOC_S_DV_TIMINGS
==============================================

*man VIDIOC_G_DV_TIMINGS(2)*

VIDIOC_S_DV_TIMINGS
VIDIOC_SUBDEV_G_DV_TIMINGS
VIDIOC_SUBDEV_S_DV_TIMINGS
Get or set DV timings for input or output


Synopsis
========

.. c:function:: int ioctl( int fd, int request, struct v4l2_dv_timings *argp )

Arguments
=========

``fd``
    File descriptor returned by :ref:`open() <func-open>`.

``request``
    VIDIOC_G_DV_TIMINGS, VIDIOC_S_DV_TIMINGS, VIDIOC_SUBDEV_G_DV_TIMINGS, VIDIOC_SUBDEV_S_DV_TIMINGS

``argp``


Description
===========

To set DV timings for the input or output, applications use the ``VIDIOC_S_DV_TIMINGS`` ioctl and to get the current timings, applications use the ``VIDIOC_G_DV_TIMINGS`` ioctl.
The detailed timing information is filled in using the structure struct :ref:`v4l2_dv_timings <v4l2-dv-timings>`. These ioctls take a pointer to the struct
:ref:`v4l2_dv_timings <v4l2-dv-timings>` structure as argument. If the ioctl is not supported or the timing values are not correct, the driver returns EINVAL error code.

The ``linux/v4l2-dv-timings.h`` header can be used to get the timings of the formats in the :ref:`cea861` and :ref:`vesadmt` standards. If the current input or output does not
support DV timings (e.g. if :ref:`VIDIOC_ENUMINPUT <vidioc-enuminput>` does not set the ``V4L2_IN_CAP_DV_TIMINGS`` flag), then ENODATA error code is returned.


Return Value
============

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.

EINVAL
    This ioctl is not supported, or the ``VIDIOC_S_DV_TIMINGS`` parameter was unsuitable.

ENODATA
    Digital video timings are not supported for this input or output.

EBUSY
    The device is busy and therefore can not change the timings.


.. _v4l2-bt-timings:

struct v4l2_bt_timings
======================

::

    TODO ... 


    <table pgwide="1" frame="none" id="v4l2-bt-timings">
          <title>struct <structname>v4l2_bt_timings</structname></title>
          <tgroup cols="3">
        <colspec colname="c1" colwidth="1*"/><colspec colname="c2" colwidth="1*"/><colspec colname="c3" colwidth="2*"/><spanspec spanname="hspan" namest="c1" nameend="c3"/>
        <tbody valign="top">
          <row>
            <entry>__u32</entry>
            <entry><structfield>width</structfield></entry>
            <entry>Width of the active video in pixels.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>height</structfield></entry>
            <entry>Height of the active video frame in lines. So for interlaced formats the
            height of the active video in each field is <structfield>height</structfield>/2.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>interlaced</structfield></entry>
            <entry>Progressive (0) or interlaced (1)</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>polarities</structfield></entry>
            <entry>This is a bit mask that defines polarities of sync signals.
    bit 0 (V4L2_DV_VSYNC_POS_POL) is for vertical sync polarity and bit 1 (V4L2_DV_HSYNC_POS_POL) is for horizontal sync polarity. If the bit is set
    (1) it is positive polarity and if is cleared (0), it is negative polarity.</entry>
          </row>
          <row>
            <entry>__u64</entry>
            <entry><structfield>pixelclock</structfield></entry>
            <entry>Pixel clock in Hz. Ex. 74.25MHz-&gt;74250000</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>hfrontporch</structfield></entry>
            <entry>Horizontal front porch in pixels</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>hsync</structfield></entry>
            <entry>Horizontal sync length in pixels</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>hbackporch</structfield></entry>
            <entry>Horizontal back porch in pixels</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>vfrontporch</structfield></entry>
            <entry>Vertical front porch in lines. For interlaced formats this refers to the
            odd field (aka field 1).</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>vsync</structfield></entry>
            <entry>Vertical sync length in lines. For interlaced formats this refers to the
            odd field (aka field 1).</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>vbackporch</structfield></entry>
            <entry>Vertical back porch in lines. For interlaced formats this refers to the
            odd field (aka field 1).</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>il_vfrontporch</structfield></entry>
            <entry>Vertical front porch in lines for the even field (aka field 2) of
            interlaced field formats. Must be 0 for progressive formats.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>il_vsync</structfield></entry>
            <entry>Vertical sync length in lines for the even field (aka field 2) of
            interlaced field formats. Must be 0 for progressive formats.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>il_vbackporch</structfield></entry>
            <entry>Vertical back porch in lines for the even field (aka field 2) of
            interlaced field formats. Must be 0 for progressive formats.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>standards</structfield></entry>
            <entry>The video standard(s) this format belongs to. This will be filled in by
            the driver. Applications must set this to 0. See <xref linkend="dv-bt-standards"/>
            for a list of standards.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>flags</structfield></entry>
            <entry>Several flags giving more information about the format.
            See <xref linkend="dv-bt-flags"/> for a description of the flags.
            </entry>
          </row>
        </tbody>
          </tgroup>
        </table>




.. _v4l2-dv-timings:

.. table:: struct v4l2_dv_timings

    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | __u32                                         | ``type``                                      |                                               | Type of DV timings as listed in               |
    |                                               |                                               |                                               | :ref:`dv-timing-types`.                       |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | union                                         |                                               |                                               |                                               |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    |                                               | struct                                        | ``bt``                                        | Timings defined by BT.656/1120 specifications |
    |                                               | :ref:`v4l2_bt_timings    <v4l2-bt-timings>`   |                                               |                                               |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    |                                               | __u32                                         | ``reserved``  [32]                            |                                               |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+



.. _dv-timing-types:

.. table:: DV Timing types

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Timing type                                   | value                                         | Description                                                                                |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                               |                                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | V4L2_DV_BT_656_1120                           | 0                                             | BT.656/1120 timings                                                                        |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _dv-bt-standards:

.. table:: DV BT Timing standards

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | Timing standard                                                                            | Description                                                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            |                                                                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | V4L2_DV_BT_STD_CEA861                                                                      | The timings follow the CEA-861 Digital TV Profile standard                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | V4L2_DV_BT_STD_DMT                                                                         | The timings follow the VESA Discrete Monitor Timings standard                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | V4L2_DV_BT_STD_CVT                                                                         | The timings follow the VESA Coordinated Video Timings standard                             |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | V4L2_DV_BT_STD_GTF                                                                         | The timings follow the VESA Generalized Timings Formula standard                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _dv-bt-flags:

.. table:: DV BT Timing flags

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | Flag                                                                                       | Description                                                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            |                                                                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | V4L2_DV_FL_REDUCED_BLANKING                                                                | CVT/GTF specific: the timings use reduced blanking (CVT) or the 'Secondary GTF' curve      |
    |                                                                                            | (GTF). In both cases the horizontal and/or vertical blanking intervals are reduced,        |
    |                                                                                            | allowing a higher resolution over the same bandwidth. This is a read-only flag,            |
    |                                                                                            | applications must not set this.                                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | V4L2_DV_FL_CAN_REDUCE_FPS                                                                  | CEA-861 specific: set for CEA-861 formats with a framerate that is a multiple of six.      |
    |                                                                                            | These formats can be optionally played at 1 / 1.001 speed to be compatible with 60 Hz      |
    |                                                                                            | based standards such as NTSC and PAL-M that use a framerate of 29.97 frames per second. If |
    |                                                                                            | the transmitter can't generate such frequencies, then the flag will also be cleared. This  |
    |                                                                                            | is a read-only flag, applications must not set this.                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | V4L2_DV_FL_REDUCED_FPS                                                                     | CEA-861 specific: only valid for video transmitters, the flag is cleared by receivers. It  |
    |                                                                                            | is also only valid for formats with the V4L2_DV_FL_CAN_REDUCE_FPS      flag set, for other |
    |                                                                                            | formats the flag will be cleared by the driver. If the application sets this flag, then    |
    |                                                                                            | the pixelclock used to set up the transmitter is divided by 1.001 to make it compatible    |
    |                                                                                            | with NTSC framerates. If the transmitter can't generate such frequencies, then the flag    |
    |                                                                                            | will also be cleared.                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | V4L2_DV_FL_HALF_LINE                                                                       | Specific to interlaced formats: if set, then the vertical frontporch of field 1 (aka the   |
    |                                                                                            | odd field) is really one half-line longer and the vertical backporch of field 2 (aka the   |
    |                                                                                            | even field) is really one half-line shorter, so each field has exactly the same number of  |
    |                                                                                            | half-lines. Whether half-lines can be detected or used depends on the hardware.            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | V4L2_DV_FL_IS_CE_VIDEO                                                                     | If set, then this is a Consumer Electronics (CE) video format. Such formats differ from    |
    |                                                                                            | other formats (commonly called IT formats) in that if R'G'B' encoding is used then by      |
    |                                                                                            | default the R'G'B' values use limited range (i.e. 16-235) as opposed to full range (i.e.   |
    |                                                                                            | 0-255). All formats defined in CEA-861 except for the 640x480p59.94 format are CE formats. |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


