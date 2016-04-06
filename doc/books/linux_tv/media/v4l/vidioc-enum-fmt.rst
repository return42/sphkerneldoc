
.. _vidioc-enum-fmt:

=====================
ioctl VIDIOC_ENUM_FMT
=====================

*man VIDIOC_ENUM_FMT(2)*

Enumerate image formats


Synopsis
========

.. c:function:: int ioctl( int fd, int request, struct v4l2_fmtdesc *argp )

Arguments
=========

``fd``
    File descriptor returned by :ref:`open() <func-open>`.

``request``
    VIDIOC_ENUM_FMT

``argp``


Description
===========

To enumerate image formats applications initialize the ``type`` and ``index`` field of struct :ref:`v4l2_fmtdesc <v4l2-fmtdesc>` and call the ``VIDIOC_ENUM_FMT`` ioctl with a
pointer to this structure. Drivers fill the rest of the structure or return an EINVAL error code. All formats are enumerable by beginning at index zero and incrementing by one
until EINVAL is returned.

Note that after switching input or output the list of enumerated image formats may be different.


.. _v4l2-fmtdesc:

struct v4l2_fmtdesc
===================

::

    TODO ... 


    <table pgwide="1" frame="none" id="v4l2-fmtdesc">
          <title>struct <structname>v4l2_fmtdesc</structname></title>
          <tgroup cols="3">
        <colspec colname="c1" colwidth="1*"/><colspec colname="c2" colwidth="1*"/><colspec colname="c3" colwidth="2*"/><spanspec spanname="hspan" namest="c1" nameend="c3"/>
        <tbody valign="top">
          <row>
            <entry>__u32</entry>
            <entry><structfield>index</structfield></entry>
            <entry>Number of the format in the enumeration, set by
    the application. This is in no way related to the <structfield>
    pixelformat</structfield> field.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>type</structfield></entry>
            <entry>Type of the data stream, set by the application.
    Only these types are valid here:
    <constant>V4L2_BUF_TYPE_VIDEO_CAPTURE</constant>,
    <constant>V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE</constant>,
    <constant>V4L2_BUF_TYPE_VIDEO_OUTPUT</constant>,
    <constant>V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE</constant> and
    <constant>V4L2_BUF_TYPE_VIDEO_OVERLAY</constant>. See <xref linkend="v4l2-buf-type"/>.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>flags</structfield></entry>
            <entry>See <xref linkend="fmtdesc-flags"/></entry>
          </row>
          <row>
            <entry>__u8</entry>
            <entry><structfield>description</structfield>[32]</entry>
            <entry>Description of the format, a NUL-terminated ASCII
    string. This information is intended for the user, for example: "YUV
    4:2:2".</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>pixelformat</structfield></entry>
            <entry>The image format identifier. This is a
    four character code as computed by the v4l2_fourcc()
    macro:</entry>
          </row>
          <row>
            <entry spanname="hspan"><para><programlisting id="v4l2-fourcc">
    #define v4l2_fourcc(a,b,c,d) (((__u32)(a)&lt;&lt;0)|((__u32)(b)&lt;&lt;8)|((__u32)(c)&lt;&lt;16)|((__u32)(d)&lt;&lt;24))
    </programlisting></para><para>Several image formats are already
    defined by this specification in <xref linkend="pixfmt"/>. Note these
    codes are not the same as those used in the Windows world.</para></entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>reserved</structfield>[4]</entry>
            <entry>Reserved for future extensions. Drivers must set
    the array to zero.</entry>
          </row>
        </tbody>
          </tgroup>
        </table>




.. _fmtdesc-flags:

.. table:: Image Format Description Flags

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_FMT_FLAG_COMPRESSED``                                        | 0x0001                 | This is a compressed format.                                                               |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_FMT_FLAG_EMULATED``                                          | 0x0002                 | This format is not native to the device but emulated through software (usually libv4l2),   |
    |                                                                     |                        | where possible try to use a native format instead for better performance.                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



Return Value
============

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.

EINVAL
    The struct :ref:`v4l2_fmtdesc <v4l2-fmtdesc>` ``type`` is not supported or the ``index`` is out of bounds.
