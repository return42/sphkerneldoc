
==============================
Single-planar format structure
==============================


.. _v4l2-pix-format:

struct v4l2_pix_format
======================

::

    TODO ... 


    <table pgwide="1" frame="none" id="v4l2-pix-format">
        <title>struct <structname>v4l2_pix_format</structname></title>
        <tgroup cols="3">
          <colspec colname="c1" colwidth="1*"/><colspec colname="c2" colwidth="1*"/><colspec colname="c3" colwidth="2*"/><spanspec spanname="hspan" namest="c1" nameend="c3"/>
          <tbody valign="top">
        <row>
          <entry>__u32</entry>
          <entry><structfield>width</structfield></entry>
          <entry>Image width in pixels.</entry>
        </row>
        <row>
          <entry>__u32</entry>
          <entry><structfield>height</structfield></entry>
          <entry>Image height in pixels. If <structfield>field</structfield> is
          one of <constant>V4L2_FIELD_TOP</constant>, <constant>V4L2_FIELD_BOTTOM</constant>
          or <constant>V4L2_FIELD_ALTERNATE</constant> then height refers to the
          number of lines in the field, otherwise it refers to the number of
          lines in the frame (which is twice the field height for interlaced
          formats).</entry>
        </row>
        <row>
          <entry spanname="hspan">Applications set these fields to
    request an image size, drivers return the closest possible values. In
    case of planar formats the <structfield>width</structfield> and
    <structfield>height</structfield> applies to the largest plane. To
    avoid ambiguities drivers must return values rounded up to a multiple
    of the scale factor of any smaller planes. For example when the image
    format is YUV 4:2:0, <structfield>width</structfield> and
    <structfield>height</structfield> must be multiples of two.</entry>
        </row>
        <row>
          <entry>__u32</entry>
          <entry><structfield>pixelformat</structfield></entry>
          <entry>The pixel format or type of compression, set by the
    application. This is a little endian <link linkend="v4l2-fourcc">four character code</link>. V4L2 defines
    standard RGB formats in <xref linkend="rgb-formats"/>, YUV formats in <xref linkend="yuv-formats"/>, and reserved codes in <xref linkend="reserved-formats"/></entry>
        </row>
        <row>
          <entry>enum <link linkend="v4l2-field">v4l2_field</link></entry>
          <entry><structfield>field</structfield></entry>
          <entry>Video images are typically interlaced. Applications
    can request to capture or output only the top or bottom field, or both
    fields interlaced or sequentially stored in one buffer or alternating
    in separate buffers. Drivers return the actual field order selected.
    For more details on fields see <xref linkend="field-order"/>.</entry>
        </row>
        <row>
          <entry>__u32</entry>
          <entry><structfield>bytesperline</structfield></entry>
          <entry>Distance in bytes between the leftmost pixels in two
    adjacent lines.</entry>
        </row>
        <row>
          <entry spanname="hspan"><para>Both applications and drivers
    can set this field to request padding bytes at the end of each line.
    Drivers however may ignore the value requested by the application,
    returning <structfield>width</structfield> times bytes per pixel or a
    larger value required by the hardware. That implies applications can
    just set this field to zero to get a reasonable
    default.</para><para>Video hardware may access padding bytes,
    therefore they must reside in accessible memory. Consider cases where
    padding bytes after the last line of an image cross a system page
    boundary. Input devices may write padding bytes, the value is
    undefined. Output devices ignore the contents of padding
    bytes.</para><para>When the image format is planar the
    <structfield>bytesperline</structfield> value applies to the first
    plane and is divided by the same factor as the
    <structfield>width</structfield> field for the other planes. For
    example the Cb and Cr planes of a YUV 4:2:0 image have half as many
    padding bytes following each line as the Y plane. To avoid ambiguities
    drivers must return a <structfield>bytesperline</structfield> value
    rounded up to a multiple of the scale factor.</para>
    <para>For compressed formats the <structfield>bytesperline</structfield>
    value makes no sense. Applications and drivers must set this to 0 in
    that case.</para></entry>
        </row>
        <row>
          <entry>__u32</entry>
          <entry><structfield>sizeimage</structfield></entry>
          <entry>Size in bytes of the buffer to hold a complete image,
    set by the driver. Usually this is
    <structfield>bytesperline</structfield> times
    <structfield>height</structfield>. When the image consists of variable
    length compressed data this is the maximum number of bytes required to
    hold an image.</entry>
        </row>
        <row>
          <entry>enum <link linkend="v4l2-colorspace">v4l2_colorspace</link></entry>
          <entry><structfield>colorspace</structfield></entry>
          <entry>This information supplements the
    <structfield>pixelformat</structfield> and must be set by the driver for
    capture streams and by the application for output streams,
    see <xref linkend="colorspaces"/>.</entry>
        </row>
        <row>
          <entry>__u32</entry>
          <entry><structfield>priv</structfield></entry>
          <entry><para>This field indicates whether the remaining fields of the
    <structname>v4l2_pix_format</structname> structure, also called the extended
    fields, are valid. When set to <constant>V4L2_PIX_FMT_PRIV_MAGIC</constant>, it
    indicates that the extended fields have been correctly initialized. When set to
    any other value it indicates that the extended fields contain undefined values.
    </para>
    <para>Applications that wish to use the pixel format extended fields must first
    ensure that the feature is supported by querying the device for the
    <link linkend="querycap"><constant>V4L2_CAP_EXT_PIX_FORMAT</constant></link>
    capability. If the capability isn't set the pixel format extended fields are not
    supported and using the extended fields will lead to undefined results.</para>
    <para>To use the extended fields, applications must set the
    <structfield>priv</structfield> field to
    <constant>V4L2_PIX_FMT_PRIV_MAGIC</constant>, initialize all the extended fields
    and zero the unused bytes of the <structname>v4l2_format</structname>
    <structfield>raw_data</structfield> field.</para>
    <para>When the <structfield>priv</structfield> field isn't set to
    <constant>V4L2_PIX_FMT_PRIV_MAGIC</constant> drivers must act as if all the
    extended fields were set to zero. On return drivers must set the
    <structfield>priv</structfield> field to
    <constant>V4L2_PIX_FMT_PRIV_MAGIC</constant> and all the extended fields to
    applicable values.</para></entry>
        </row>
        <row>
          <entry>__u32</entry>
          <entry><structfield>flags</structfield></entry>
          <entry>Flags set by the application or driver, see <xref linkend="format-flags"/>.</entry>
        </row>
        <row>
          <entry>enum <link linkend="v4l2-ycbcr-encoding">v4l2_ycbcr_encoding</link></entry>
          <entry><structfield>ycbcr_enc</structfield></entry>
          <entry>This information supplements the
    <structfield>colorspace</structfield> and must be set by the driver for
    capture streams and by the application for output streams,
    see <xref linkend="colorspaces"/>.</entry>
        </row>
        <row>
          <entry>enum <link linkend="v4l2-quantization">v4l2_quantization</link></entry>
          <entry><structfield>quantization</structfield></entry>
          <entry>This information supplements the
    <structfield>colorspace</structfield> and must be set by the driver for
    capture streams and by the application for output streams,
    see <xref linkend="colorspaces"/>.</entry>
        </row>
        <row>
          <entry>enum <link linkend="v4l2-xfer-func">v4l2_xfer_func</link></entry>
          <entry><structfield>xfer_func</structfield></entry>
          <entry>This information supplements the
    <structfield>colorspace</structfield> and must be set by the driver for
    capture streams and by the application for output streams,
    see <xref linkend="colorspaces"/>.</entry>
        </row>
          </tbody>
        </tgroup>
      </table>


