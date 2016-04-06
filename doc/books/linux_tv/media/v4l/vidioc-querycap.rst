
.. _vidioc-querycap:

=====================
ioctl VIDIOC_QUERYCAP
=====================

*man VIDIOC_QUERYCAP(2)*

Query device capabilities


Synopsis
========

.. c:function:: int ioctl( int fd, int request, struct v4l2_capability *argp )

Arguments
=========

``fd``
    File descriptor returned by :ref:`open() <func-open>`.

``request``
    VIDIOC_QUERYCAP

``argp``


Description
===========

All V4L2 devices support the ``VIDIOC_QUERYCAP`` ioctl. It is used to identify kernel devices compatible with this specification and to obtain information about driver and hardware
capabilities. The ioctl takes a pointer to a struct :ref:`v4l2_capability <v4l2-capability>` which is filled by the driver. When the driver is not compatible with this
specification the ioctl returns an EINVAL error code.


.. _v4l2-capability:

struct v4l2_capability
======================

::

    TODO ... 


    <table pgwide="1" frame="none" id="v4l2-capability">
          <title>struct <structname>v4l2_capability</structname></title>
          <tgroup cols="3">
        <colspec colname="c1" colwidth="1*"/><colspec colname="c2" colwidth="1*"/><colspec colname="c3" colwidth="2*"/><spanspec spanname="hspan" namest="c1" nameend="c3"/>
        <tbody valign="top">
          <row>
            <entry>__u8</entry>
            <entry><structfield>driver</structfield>[16]</entry>
            <entry><para>Name of the driver, a unique NUL-terminated
    ASCII string. For example: "bttv". Driver specific applications can
    use this information to verify the driver identity. It is also useful
    to work around known bugs, or to identify drivers in error reports.</para>
    <para>Storing strings in fixed sized arrays is bad
    practice but unavoidable here. Drivers and applications should take
    precautions to never read or write beyond the end of the array and to
    make sure the strings are properly NUL-terminated.</para></entry>
          </row>
          <row>
            <entry>__u8</entry>
            <entry><structfield>card</structfield>[32]</entry>
            <entry>Name of the device, a NUL-terminated UTF-8 string.
    For example: "Yoyodyne TV/FM". One driver may support different brands
    or models of video hardware. This information is intended for users,
    for example in a menu of available devices. Since multiple TV cards of
    the same brand may be installed which are supported by the same
    driver, this name should be combined with the character device file
    name (e. g. <filename>/dev/video2</filename>) or the
    <structfield>bus_info</structfield> string to avoid
    ambiguities.</entry>
          </row>
          <row>
            <entry>__u8</entry>
            <entry><structfield>bus_info</structfield>[32]</entry>
            <entry>Location of the device in the system, a
    NUL-terminated ASCII string. For example: "PCI:0000:05:06.0". This
    information is intended for users, to distinguish multiple
    identical devices. If no such information is available the field must
    simply count the devices controlled by the driver ("platform:vivi-000").
    The bus_info must start with "PCI:" for PCI boards, "PCIe:" for PCI Express boards,
    "usb-" for USB devices, "I2C:" for i2c devices, "ISA:" for ISA devices,
    "parport" for parallel port devices and "platform:" for platform devices.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>version</structfield></entry>
            <entry><para>Version number of the driver.</para>
    <para>Starting with kernel 3.1, the version reported is provided by the
    V4L2 subsystem following the kernel numbering scheme. However, it
    may not always return the same version as the kernel if, for example,
    a stable or distribution-modified kernel uses the V4L2 stack from a
    newer kernel.</para>
    <para>The version number is formatted using the
    <constant>KERNEL_VERSION()</constant> macro:</para></entry>
          </row>
          <row>
            <entry spanname="hspan"><para>
    <programlisting>
    #define KERNEL_VERSION(a,b,c) (((a) &lt;&lt; 16) + ((b) &lt;&lt; 8) + (c))

    __u32 version = KERNEL_VERSION(0, 8, 1);

    printf ("Version: %u.%u.%u\\n",
        (version &gt;&gt; 16) &amp; 0xFF,
        (version &gt;&gt; 8) &amp; 0xFF,
         version &amp; 0xFF);
    </programlisting></para></entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>capabilities</structfield></entry>
            <entry>Available capabilities of the physical device as a whole, see <xref linkend="device-capabilities"/>. The same physical device can export
            multiple devices in /dev (e.g. /dev/videoX, /dev/vbiY and /dev/radioZ).
            The <structfield>capabilities</structfield> field should contain a union
            of all capabilities available around the several V4L2 devices exported
            to userspace.
            For all those devices the <structfield>capabilities</structfield> field
            returns the same set of capabilities. This allows applications to open
            just one of the devices (typically the video device) and discover whether
            video, vbi and/or radio are also supported.
            </entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>device_caps</structfield></entry>
            <entry>Device capabilities of the opened device, see <xref linkend="device-capabilities"/>. Should contain the available capabilities
            of that specific device node. So, for example, <structfield>device_caps</structfield>
            of a radio device will only contain radio related capabilities and
            no video or vbi capabilities. This field is only set if the <structfield>capabilities</structfield>
            field contains the <constant>V4L2_CAP_DEVICE_CAPS</constant> capability.
            Only the <structfield>capabilities</structfield> field can have the
            <constant>V4L2_CAP_DEVICE_CAPS</constant> capability, <structfield>device_caps</structfield>
            will never set <constant>V4L2_CAP_DEVICE_CAPS</constant>.
            </entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>reserved</structfield>[3]</entry>
            <entry>Reserved for future extensions. Drivers must set
    this array to zero.</entry>
          </row>
        </tbody>
          </tgroup>
        </table>




.. _device-capabilities:

.. table:: Device Capabilities Flags

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_VIDEO_CAPTURE``                                          | 0x00000001             | The device supports the single-planar API through the :ref:`Video  Capture <capture>`      |
    |                                                                     |                        | interface.                                                                                 |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_VIDEO_CAPTURE_MPLANE``                                   | 0x00001000             | The device supports the :ref:`multi-planar  API <planar-apis>`  through the                |
    |                                                                     |                        | :ref:`Video  Capture <capture>`  interface.                                                |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_VIDEO_OUTPUT``                                           | 0x00000002             | The device supports the single-planar API through the :ref:`Video  Output <output>`        |
    |                                                                     |                        | interface.                                                                                 |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_VIDEO_OUTPUT_MPLANE``                                    | 0x00002000             | The device supports the :ref:`multi-planar  API <planar-apis>`  through the                |
    |                                                                     |                        | :ref:`Video  Output <output>`  interface.                                                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_VIDEO_M2M``                                              | 0x00004000             | The device supports the single-planar API through the Video Memory-To-Memory interface.    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_VIDEO_M2M_MPLANE``                                       | 0x00008000             | The device supports the :ref:`multi-planar  API <planar-apis>`  through the Video          |
    |                                                                     |                        | Memory-To-Memory interface.                                                                |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_VIDEO_OVERLAY``                                          | 0x00000004             | The device supports the :ref:`Video  Overlay <overlay>`  interface. A video overlay device |
    |                                                                     |                        | typically stores captured images directly in the video memory of a graphics card, with     |
    |                                                                     |                        | hardware clipping and scaling.                                                             |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_VBI_CAPTURE``                                            | 0x00000010             | The device supports the :ref:`Raw  VBI Capture <raw-vbi>`  interface, providing Teletext   |
    |                                                                     |                        | and Closed Caption data.                                                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_VBI_OUTPUT``                                             | 0x00000020             | The device supports the :ref:`Raw  VBI Output <raw-vbi>`  interface.                       |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_SLICED_VBI_CAPTURE``                                     | 0x00000040             | The device supports the :ref:`Sliced  VBI Capture <sliced>`  interface.                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_SLICED_VBI_OUTPUT``                                      | 0x00000080             | The device supports the :ref:`Sliced  VBI Output <sliced>`  interface.                     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_RDS_CAPTURE``                                            | 0x00000100             | The device supports the :ref:`RDS  <rds>`  capture interface.                              |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_VIDEO_OUTPUT_OVERLAY``                                   | 0x00000200             | The device supports the :ref:`Video  Output Overlay <osd>`  (OSD) interface. Unlike the    |
    |                                                                     |                        | *Video Overlay* interface, this is a secondary function of video output devices and        |
    |                                                                     |                        | overlays an image onto an outgoing video signal. When the driver sets this flag, it must   |
    |                                                                     |                        | clear the ``V4L2_CAP_VIDEO_OVERLAY`` flag and vice versa. [1]_                             |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_HW_FREQ_SEEK``                                           | 0x00000400             | The device supports the :ref:`VIDIOC_S_HW_FREQ_SEEK      <vidioc-s-hw-freq-seek>`  ioctl   |
    |                                                                     |                        | for hardware frequency seeking.                                                            |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_RDS_OUTPUT``                                             | 0x00000800             | The device supports the :ref:`RDS  <rds>`  output interface.                               |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_TUNER``                                                  | 0x00010000             | The device has some sort of tuner to receive RF-modulated video signals. For more          |
    |                                                                     |                        | information about tuner programming see :ref:`tuner`.                                      |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_AUDIO``                                                  | 0x00020000             | The device has audio inputs or outputs. It may or may not support audio recording or       |
    |                                                                     |                        | playback, in PCM or compressed formats. PCM audio support must be implemented as ALSA or   |
    |                                                                     |                        | OSS interface. For more information on audio inputs and outputs see :ref:`audio`.          |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_RADIO``                                                  | 0x00040000             | This is a radio receiver.                                                                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_MODULATOR``                                              | 0x00080000             | The device has some sort of modulator to emit RF-modulated video/audio signals. For more   |
    |                                                                     |                        | information about modulator programming see :ref:`tuner`.                                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_SDR_CAPTURE``                                            | 0x00100000             | The device supports the :ref:`SDR  Capture <sdr>`  interface.                              |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_EXT_PIX_FORMAT``                                         | 0x00200000             | The device supports the struct :ref:`v4l2_pix_format    <v4l2-pix-format>`  extended       |
    |                                                                     |                        | fields.                                                                                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_SDR_OUTPUT``                                             | 0x00400000             | The device supports the :ref:`SDR  Output <sdr>`  interface.                               |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_READWRITE``                                              | 0x01000000             | The device supports the :ref:`read()  <rw>`  and/or :ref:`write()  <rw>`  I/O methods.     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_ASYNCIO``                                                | 0x02000000             | The device supports the :ref:`asynchronous  <async>`  I/O methods.                         |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_STREAMING``                                              | 0x04000000             | The device supports the :ref:`streaming  <mmap>`  I/O method.                              |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_CAP_DEVICE_CAPS``                                            | 0x80000000             | The driver fills the ``device_caps`` field. This capability can only appear in the         |
    |                                                                     |                        | ``capabilities`` field and never in the ``device_caps`` field.                             |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



Return Value
============

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.

.. [1]
   The struct :ref:`v4l2_framebuffer <v4l2-framebuffer>` lacks an enum :ref:`v4l2_buf_type <v4l2-buf-type>` field, therefore the type of overlay is implied by the driver
   capabilities.
