
.. _pixfmt:

=============
Image Formats
=============

The V4L2 API was primarily designed for devices exchanging image data with applications. The ``v4l2_pix_format`` and ``v4l2_pix_format_mplane`` structures define the format and
layout of an image in memory. The former is used with the single-planar API, while the latter is used with the multi-planar version (see :ref:`planar-apis`). Image formats are
negotiated with the :ref:`VIDIOC_S_FMT <vidioc-g-fmt>` ioctl. (The explanations here focus on video capturing and output, for overlay frame buffer formats see also
:ref:`VIDIOC_G_FBUF <vidioc-g-fbuf>`.)


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


Multi-planar format structures
==============================

The ``v4l2_plane_pix_format`` structures define size and layout for each of the planes in a multi-planar format. The ``v4l2_pix_format_mplane`` structure contains information
common to all planes (such as image width and height) and an array of ``v4l2_plane_pix_format`` structures, describing all planes of that format.


.. _v4l2-plane-pix-format:

.. table:: struct v4l2_plane_pix_format

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``sizeimage``                                 | Maximum size in bytes required for image data in this plane.                               |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``bytesperline``                              | Distance in bytes between the leftmost pixels in two adjacent lines. See struct            |
    |                                               |                                               | :ref:`v4l2_pix_format    <v4l2-pix-format>`.                                               |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u16                                         | ``reserved[6]``                               | Reserved for future extensions. Should be zeroed by drivers and applications.              |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-pix-format-mplane:

.. table:: struct v4l2_pix_format_mplane

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``width``                                     | Image width in pixels. See struct :ref:`v4l2_pix_format    <v4l2-pix-format>`.             |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``height``                                    | Image height in pixels. See struct :ref:`v4l2_pix_format    <v4l2-pix-format>`.            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``pixelformat``                               | The pixel format. Both single- and multi-planar four character codes can be used.          |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | enum :ref:`v4l2_field   <v4l2-field>`         | ``field``                                     | See struct :ref:`v4l2_pix_format    <v4l2-pix-format>`.                                    |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | enum                                          | ``colorspace``                                | See struct :ref:`v4l2_pix_format    <v4l2-pix-format>`.                                    |
    | :ref:`v4l2_colorspace   <v4l2-colorspace>`    |                                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct                                        | ``plane_fmt[VIDEO_MAX_PLANES]``               | An array of structures describing format of each plane this pixel format consists of. The  |
    | :ref:`v4l2_plane_pix_format     <v4l2-plane-p |                                               | number of valid entries in this array has to be put in the ``num_planes`` field.           |
    | ix-format>`                                   |                                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                          | ``num_planes``                                | Number of planes (i.e. separate memory buffers) for this format and the number of valid    |
    |                                               |                                               | entries in the ``plane_fmt`` array.                                                        |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                          | ``flags``                                     | Flags set by the application or driver, see :ref:`format-flags`.                           |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | enum                                          | ``ycbcr_enc``                                 | This information supplements the ``colorspace`` and must be set by the driver for capture  |
    | :ref:`v4l2_ycbcr_encoding    <v4l2-ycbcr-enco |                                               | streams and by the application for output streams, see :ref:`colorspaces`.                 |
    | ding>`                                        |                                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | enum                                          | ``quantization``                              | This information supplements the ``colorspace`` and must be set by the driver for capture  |
    | :ref:`v4l2_quantization   <v4l2-quantization> |                                               | streams and by the application for output streams, see :ref:`colorspaces`.                 |
    | `                                             |                                               |                                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | enum                                          | ``xfer_func``                                 | This information supplements the ``colorspace`` and must be set by the driver for capture  |
    | :ref:`v4l2_xfer_func    <v4l2-xfer-func>`     |                                               | streams and by the application for output streams, see :ref:`colorspaces`.                 |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u8                                          | ``reserved[7]``                               | Reserved for future extensions. Should be zeroed by drivers and applications.              |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



Standard Image Formats
======================

In order to exchange images between drivers and applications, it is necessary to have standard image data formats which both sides will interpret the same way. V4L2 includes
several such formats, and this section is intended to be an unambiguous specification of the standard image data formats in V4L2.

V4L2 drivers are not limited to these formats, however. Driver-specific formats are possible. In that case the application may depend on a codec to convert images to one of the
standard formats when needed. But the data can still be stored and retrieved in the proprietary format. For example, a device may support a proprietary compressed format.
Applications can still capture and save the data in the compressed format, saving much disk space, and later use a codec to convert the images to the X Windows screen format when
the video is to be displayed.

Even so, ultimately, some standard formats are needed, so the V4L2 specification would not be complete without well-defined standard formats.

The V4L2 standard formats are mainly uncompressed formats. The pixels are always arranged in memory from left to right, and from top to bottom. The first byte of data in the image
buffer is always for the leftmost pixel of the topmost row. Following that is the pixel immediately to its right, and so on until the end of the top row of pixels. Following the
rightmost pixel of the row there may be zero or more bytes of padding to guarantee that each row of pixel data has a certain alignment. Following the pad bytes, if any, is data for
the leftmost pixel of the second row from the top, and so on. The last row has just as many pad bytes after it as the other rows.

In V4L2 each format has an identifier which looks like ``PIX_FMT_XXX``, defined in the :ref:`videodev2.h <videodev>` header file. These identifiers represent
:ref:`four character (FourCC) codes <v4l2-fourcc>` which are also listed below, however they are not the same as those used in the Windows world.

For some formats, data is stored in separate, discontiguous memory buffers. Those formats are identified by a separate set of FourCC codes and are referred to as "multi-planar
formats". For example, a YUV422 frame is normally stored in one memory buffer, but it can also be placed in two or three separate buffers, with Y component in one buffer and CbCr
components in another in the 2-planar version or with each component in its own buffer in the 3-planar case. Those sub-buffers are referred to as "planes".


.. _colorspaces:

Colorspaces
===========

'Color' is a very complex concept and depends on physics, chemistry and biology. Just because you have three numbers that describe the 'red', 'green' and 'blue' components of the
color of a pixel does not mean that you can accurately display that color. A colorspace defines what it actually *means* to have an RGB value of e.g. (255, 0, 0). That is, which
color should be reproduced on the screen in a perfectly calibrated environment.

In order to do that we first need to have a good definition of color, i.e. some way to uniquely and unambiguously define a color so that someone else can reproduce it. Human color
vision is trichromatic since the human eye has color receptors that are sensitive to three different wavelengths of light. Hence the need to use three numbers to describe color. Be
glad you are not a mantis shrimp as those are sensitive to 12 different wavelengths, so instead of RGB we would be using the ABCDEFGHIJKL colorspace...

Color exists only in the eye and brain and is the result of how strongly color receptors are stimulated. This is based on the Spectral Power Distribution (SPD) which is a graph
showing the intensity (radiant power) of the light at wavelengths covering the visible spectrum as it enters the eye. The science of colorimetry is about the relationship between
the SPD and color as perceived by the human brain.

Since the human eye has only three color receptors it is perfectly possible that different SPDs will result in the same stimulation of those receptors and are perceived as the same
color, even though the SPD of the light is different.

In the 1920s experiments were devised to determine the relationship between SPDs and the perceived color and that resulted in the CIE 1931 standard that defines spectral weighting
functions that model the perception of color. Specifically that standard defines functions that can take an SPD and calculate the stimulus for each color receptor. After some
further mathematical transforms these stimuli are known as the *CIE XYZ tristimulus* values and these X, Y and Z values describe a color as perceived by a human unambiguously.
These X, Y and Z values are all in the range [0…1].

The Y value in the CIE XYZ colorspace corresponds to luminance. Often the CIE XYZ colorspace is transformed to the normalized CIE xyY colorspace:

x = X / (X + Y + Z)

y = Y / (X + Y + Z)

The x and y values are the chromaticity coordinates and can be used to define a color without the luminance component Y. It is very confusing to have such similar names for these
colorspaces. Just be aware that if colors are specified with lower case 'x' and 'y', then the CIE xyY colorspace is used. Upper case 'X' and 'Y' refer to the CIE XYZ colorspace.
Also, y has nothing to do with luminance. Together x and y specify a color, and Y the luminance. That is really all you need to remember from a practical point of view. At the end
of this section you will find reading resources that go into much more detail if you are interested.

A monitor or TV will reproduce colors by emitting light at three different wavelengths, the combination of which will stimulate the color receptors in the eye and thus cause the
perception of color. Historically these wavelengths were defined by the red, green and blue phosphors used in the displays. These *color primaries* are part of what defines a
colorspace.

Different display devices will have different primaries and some primaries are more suitable for some display technologies than others. This has resulted in a variety of
colorspaces that are used for different display technologies or uses. To define a colorspace you need to define the three color primaries (these are typically defined as x, y
chromaticity coordinates from the CIE xyY colorspace) but also the white reference: that is the color obtained when all three primaries are at maximum power. This determines the
relative power or energy of the primaries. This is usually chosen to be close to daylight which has been defined as the CIE D65 Illuminant.

To recapitulate: the CIE XYZ colorspace uniquely identifies colors. Other colorspaces are defined by three chromaticity coordinates defined in the CIE xyY colorspace. Based on
those a 3x3 matrix can be constructed that transforms CIE XYZ colors to colors in the new colorspace.

Both the CIE XYZ and the RGB colorspace that are derived from the specific chromaticity primaries are linear colorspaces. But neither the eye, nor display technology is linear.
Doubling the values of all components in the linear colorspace will not be perceived as twice the intensity of the color. So each colorspace also defines a transfer function that
takes a linear color component value and transforms it to the non-linear component value, which is a closer match to the non-linear performance of both the eye and displays. Linear
component values are denoted RGB, non-linear are denoted as R'G'B'. In general colors used in graphics are all R'G'B', except in openGL which uses linear RGB. Special care should
be taken when dealing with openGL to provide linear RGB colors or to use the built-in openGL support to apply the inverse transfer function.

The final piece that defines a colorspace is a function that transforms non-linear R'G'B' to non-linear Y'CbCr. This function is determined by the so-called luma coefficients.
There may be multiple possible Y'CbCr encodings allowed for the same colorspace. Many encodings of color prefer to use luma (Y') and chroma (CbCr) instead of R'G'B'. Since the
human eye is more sensitive to differences in luminance than in color this encoding allows one to reduce the amount of color information compared to the luma data. Note that the
luma (Y') is unrelated to the Y in the CIE XYZ colorspace. Also note that Y'CbCr is often called YCbCr or YUV even though these are strictly speaking wrong.

Sometimes people confuse Y'CbCr as being a colorspace. This is not correct, it is just an encoding of an R'G'B' color into luma and chroma values. The underlying colorspace that is
associated with the R'G'B' color is also associated with the Y'CbCr color.

The final step is how the RGB, R'G'B' or Y'CbCr values are quantized. The CIE XYZ colorspace where X, Y and Z are in the range [0…1] describes all colors that humans can perceive,
but the transform to another colorspace will produce colors that are outside the [0…1] range. Once clamped to the [0…1] range those colors can no longer be reproduced in that
colorspace. This clamping is what reduces the extent or gamut of the colorspace. How the range of [0…1] is translated to integer values in the range of [0…255] (or higher,
depending on the color depth) is called the quantization. This is *not* part of the colorspace definition. In practice RGB or R'G'B' values are full range, i.e. they use the full
[0…255] range. Y'CbCr values on the other hand are limited range with Y' using [16…235] and Cb and Cr using [16…240].

Unfortunately, in some cases limited range RGB is also used where the components use the range [16…235]. And full range Y'CbCr also exists using the [0…255] range.

In order to correctly interpret a color you need to know the quantization range, whether it is R'G'B' or Y'CbCr, the used Y'CbCr encoding and the colorspace. From that information
you can calculate the corresponding CIE XYZ color and map that again to whatever colorspace your display device uses.

The colorspace definition itself consists of the three chromaticity primaries, the white reference chromaticity, a transfer function and the luma coefficients needed to transform
R'G'B' to Y'CbCr. While some colorspace standards correctly define all four, quite often the colorspace standard only defines some, and you have to rely on other standards for the
missing pieces. The fact that colorspaces are often a mix of different standards also led to very confusing naming conventions where the name of a standard was used to name a
colorspace when in fact that standard was part of various other colorspaces as well.

If you want to read more about colors and colorspaces, then the following resources are useful: :ref:`poynton` is a good practical book for video engineers, :ref:`colimg` has a
much broader scope and describes many more aspects of color (physics, chemistry, biology, etc.). The http://www.brucelindbloom.com website is an excellent resource, especially with
respect to the mathematics behind colorspace conversions. The wikipedia `CIE 1931 colorspace`_ article is also very useful.


Defining Colorspaces in V4L2
============================

In V4L2 colorspaces are defined by four values. The first is the colorspace identifier (enum :ref:`v4l2_colorspace <v4l2-colorspace>`) which defines the chromaticities, the
default transfer function, the default Y'CbCr encoding and the default quantization method. The second is the transfer function identifier (enum
:ref:`v4l2_xfer_func <v4l2-xfer-func>`) to specify non-standard transfer functions. The third is the Y'CbCr encoding identifier (enum
:ref:`v4l2_ycbcr_encoding <v4l2-ycbcr-encoding>`) to specify non-standard Y'CbCr encodings and the fourth is the quantization identifier (enum
:ref:`v4l2_quantization <v4l2-quantization>`) to specify non-standard quantization methods. Most of the time only the colorspace field of struct
:ref:`v4l2_pix_format <v4l2-pix-format>` or struct :ref:`v4l2_pix_format_mplane <v4l2-pix-format-mplane>` needs to be filled in. Note that the default R'G'B' quantization
is full range for all colorspaces except for BT.2020 which uses limited range R'G'B' quantization.


.. _v4l2-colorspace:

.. table:: V4L2 Colorspaces

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | Identifier                                                                                 | Details                                                                                    |
    +============================================================================================+============================================================================================+
    | ``V4L2_COLORSPACE_DEFAULT``                                                                | The default colorspace. This can be used by applications to let the driver fill in the     |
    |                                                                                            | colorspace.                                                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_COLORSPACE_SMPTE170M``                                                              | See :ref:`col-smpte-170m`.                                                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_COLORSPACE_REC709``                                                                 | See :ref:`col-rec709`.                                                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_COLORSPACE_SRGB``                                                                   | See :ref:`col-srgb`.                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_COLORSPACE_ADOBERGB``                                                               | See :ref:`col-adobergb`.                                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_COLORSPACE_BT2020``                                                                 | See :ref:`col-bt2020`.                                                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_COLORSPACE_DCI_P3``                                                                 | See :ref:`col-dcip3`.                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_COLORSPACE_SMPTE240M``                                                              | See :ref:`col-smpte-240m`.                                                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_COLORSPACE_470_SYSTEM_M``                                                           | See :ref:`col-sysm`.                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_COLORSPACE_470_SYSTEM_BG``                                                          | See :ref:`col-sysbg`.                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_COLORSPACE_JPEG``                                                                   | See :ref:`col-jpeg`.                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_COLORSPACE_RAW``                                                                    | The raw colorspace. This is used for raw image capture where the image is minimally        |
    |                                                                                            | processed and is using the internal colorspace of the device. The software that processes  |
    |                                                                                            | an image using this 'colorspace' will have to know the internals of the capture device.    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-xfer-func:

.. table:: V4L2 Transfer Function

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | Identifier                                                                                 | Details                                                                                    |
    +============================================================================================+============================================================================================+
    | ``V4L2_XFER_FUNC_DEFAULT``                                                                 | Use the default transfer function as defined by the colorspace.                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_XFER_FUNC_709``                                                                     | Use the Rec. 709 transfer function.                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_XFER_FUNC_SRGB``                                                                    | Use the sRGB transfer function.                                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_XFER_FUNC_ADOBERGB``                                                                | Use the AdobeRGB transfer function.                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_XFER_FUNC_SMPTE240M``                                                               | Use the SMPTE 240M transfer function.                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_XFER_FUNC_NONE``                                                                    | Do not use a transfer function (i.e. use linear RGB values).                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_XFER_FUNC_DCI_P3``                                                                  | Use the DCI-P3 transfer function.                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_XFER_FUNC_SMPTE2084``                                                               | Use the SMPTE 2084 transfer function.                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-ycbcr-encoding:

.. table:: V4L2 Y'CbCr Encodings

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | Identifier                                                                                 | Details                                                                                    |
    +============================================================================================+============================================================================================+
    | ``V4L2_YCBCR_ENC_DEFAULT``                                                                 | Use the default Y'CbCr encoding as defined by the colorspace.                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_YCBCR_ENC_601``                                                                     | Use the BT.601 Y'CbCr encoding.                                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_YCBCR_ENC_709``                                                                     | Use the Rec. 709 Y'CbCr encoding.                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_YCBCR_ENC_XV601``                                                                   | Use the extended gamut xvYCC BT.601 encoding.                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_YCBCR_ENC_XV709``                                                                   | Use the extended gamut xvYCC Rec. 709 encoding.                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_YCBCR_ENC_SYCC``                                                                    | Use the extended gamut sYCC encoding.                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_YCBCR_ENC_BT2020``                                                                  | Use the default non-constant luminance BT.2020 Y'CbCr encoding.                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_YCBCR_ENC_BT2020_CONST_LUM``                                                        | Use the constant luminance BT.2020 Yc'CbcCrc encoding.                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-quantization:

.. table:: V4L2 Quantization Methods

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | Identifier                                                                                 | Details                                                                                    |
    +============================================================================================+============================================================================================+
    | ``V4L2_QUANTIZATION_DEFAULT``                                                              | Use the default quantization encoding as defined by the colorspace. This is always full    |
    |                                                                                            | range for R'G'B' (except for the BT.2020 colorspace) and usually limited range for Y'CbCr. |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_QUANTIZATION_FULL_RANGE``                                                           | Use the full range quantization encoding. I.e. the range [0…1] is mapped to [0…255] (with  |
    |                                                                                            | possible clipping to [1…254] to avoid the 0x00 and 0xff values). Cb and Cr are mapped from |
    |                                                                                            | [-0.5…0.5] to [0…255] (with possible clipping to [1…254] to avoid the 0x00 and 0xff        |
    |                                                                                            | values).                                                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_QUANTIZATION_LIM_RANGE``                                                            | Use the limited range quantization encoding. I.e. the range [0…1] is mapped to [16…235].   |
    |                                                                                            | Cb and Cr are mapped from [-0.5…0.5] to [16…240].                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



Detailed Colorspace Descriptions
================================


.. _col-smpte-170m:

Colorspace SMPTE 170M (V4L2_COLORSPACE_SMPTE170M)
=================================================

The :ref:`smpte170m` standard defines the colorspace used by NTSC and PAL and by SDTV in general. The default transfer function is ``V4L2_XFER_FUNC_709``. The default Y'CbCr
encoding is ``V4L2_YCBCR_ENC_601``. The default Y'CbCr quantization is limited range. The chromaticities of the primary colors and the white reference are:



.. table:: SMPTE 170M Chromaticities

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Color                                         | x                                             | y                                                                                          |
    +===============================================+===============================================+============================================================================================+
    | Red                                           | 0.630                                         | 0.340                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Green                                         | 0.310                                         | 0.595                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Blue                                          | 0.155                                         | 0.070                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | White Reference (D65)                         | 0.3127                                        | 0.3290                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+


The red, green and blue chromaticities are also often referred to as the SMPTE C set, so this colorspace is sometimes called SMPTE C as well.

The transfer function defined for SMPTE 170M is the same as the one defined in Rec. 709.
    L' = -1.099(-L):sup:`0.45` + 0.099 for L ≤ -0.018

    L' = 4.5L for -0.018 < L < 0.018

    L' = 1.099L\ :sup:`0.45` - 0.099 for L ≥ 0.018

Inverse Transfer function:
    L = -((L' - 0.099) / -1.099):sup:`1/0.45` for L' ≤ -0.081

    L = L' / 4.5 for -0.081 < L' < 0.081

    L = ((L' + 0.099) / 1.099)\ :sup:`1/0.45` for L' ≥ 0.081

The luminance (Y') and color difference (Cb and Cr) are obtained with the following ``V4L2_YCBCR_ENC_601`` encoding:
    Y' = 0.299R' + 0.587G' + 0.114B'

    Cb = -0.169R' - 0.331G' + 0.5B'

    Cr = 0.5R' - 0.419G' - 0.081B'

Y' is clamped to the range [0…1] and Cb and Cr are clamped to the range [-0.5…0.5]. This conversion to Y'CbCr is identical to the one defined in the :ref:`itu601` standard and
this colorspace is sometimes called BT.601 as well, even though BT.601 does not mention any color primaries.

The default quantization is limited range, but full range is possible although rarely seen.


.. _col-rec709:

Colorspace Rec. 709 (V4L2_COLORSPACE_REC709)
============================================

The :ref:`itu709` standard defines the colorspace used by HDTV in general. The default transfer function is ``V4L2_XFER_FUNC_709``. The default Y'CbCr encoding is
``V4L2_YCBCR_ENC_709``. The default Y'CbCr quantization is limited range. The chromaticities of the primary colors and the white reference are:



.. table:: Rec. 709 Chromaticities

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Color                                         | x                                             | y                                                                                          |
    +===============================================+===============================================+============================================================================================+
    | Red                                           | 0.640                                         | 0.330                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Green                                         | 0.300                                         | 0.600                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Blue                                          | 0.150                                         | 0.060                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | White Reference (D65)                         | 0.3127                                        | 0.3290                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+


The full name of this standard is Rec. ITU-R BT.709-5.

Transfer function. Normally L is in the range [0…1], but for the extended gamut xvYCC encoding values outside that range are allowed.
    L' = -1.099(-L):sup:`0.45` + 0.099 for L ≤ -0.018

    L' = 4.5L for -0.018 < L < 0.018

    L' = 1.099L\ :sup:`0.45` - 0.099 for L ≥ 0.018

Inverse Transfer function:
    L = -((L' - 0.099) / -1.099):sup:`1/0.45` for L' ≤ -0.081

    L = L' / 4.5 for -0.081 < L' < 0.081

    L = ((L' + 0.099) / 1.099)\ :sup:`1/0.45` for L' ≥ 0.081

The luminance (Y') and color difference (Cb and Cr) are obtained with the following ``V4L2_YCBCR_ENC_709`` encoding:
    Y' = 0.2126R' + 0.7152G' + 0.0722B'

    Cb = -0.1146R' - 0.3854G' + 0.5B'

    Cr = 0.5R' - 0.4542G' - 0.0458B'

Y' is clamped to the range [0…1] and Cb and Cr are clamped to the range [-0.5…0.5].

The default quantization is limited range, but full range is possible although rarely seen.

The ``V4L2_YCBCR_ENC_709`` encoding described above is the default for this colorspace, but it can be overridden with ``V4L2_YCBCR_ENC_601``, in which case the BT.601 Y'CbCr
encoding is used.

Two additional extended gamut Y'CbCr encodings are also possible with this colorspace:

The xvYCC 709 encoding (``V4L2_YCBCR_ENC_XV709``, :ref:`xvycc`) is similar to the Rec. 709 encoding, but it allows for R', G' and B' values that are outside the range [0…1]. The
resulting Y', Cb and Cr values are scaled and offset:
    Y' = (219 / 256) ⋆ (0.2126R' + 0.7152G' + 0.0722B') + (16 / 256)

    Cb = (224 / 256) ⋆ (-0.1146R' - 0.3854G' + 0.5B')

    Cr = (224 / 256) ⋆ (0.5R' - 0.4542G' - 0.0458B')

The xvYCC 601 encoding (``V4L2_YCBCR_ENC_XV601``, :ref:`xvycc`) is similar to the BT.601 encoding, but it allows for R', G' and B' values that are outside the range [0…1]. The
resulting Y', Cb and Cr values are scaled and offset:
    Y' = (219 / 256) ⋆ (0.299R' + 0.587G' + 0.114B') + (16 / 256)

    Cb = (224 / 256) ⋆ (-0.169R' - 0.331G' + 0.5B')

    Cr = (224 / 256) ⋆ (0.5R' - 0.419G' - 0.081B')

Y' is clamped to the range [0…1] and Cb and Cr are clamped to the range [-0.5…0.5]. The non-standard xvYCC 709 or xvYCC 601 encodings can be used by selecting
``V4L2_YCBCR_ENC_XV709`` or ``V4L2_YCBCR_ENC_XV601``. The xvYCC encodings always use full range quantization.


.. _col-srgb:

Colorspace sRGB (V4L2_COLORSPACE_SRGB)
======================================

The :ref:`srgb` standard defines the colorspace used by most webcams and computer graphics. The default transfer function is ``V4L2_XFER_FUNC_SRGB``. The default Y'CbCr encoding
is ``V4L2_YCBCR_ENC_SYCC``. The default Y'CbCr quantization is full range. The chromaticities of the primary colors and the white reference are:



.. table:: sRGB Chromaticities

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Color                                         | x                                             | y                                                                                          |
    +===============================================+===============================================+============================================================================================+
    | Red                                           | 0.640                                         | 0.330                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Green                                         | 0.300                                         | 0.600                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Blue                                          | 0.150                                         | 0.060                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | White Reference (D65)                         | 0.3127                                        | 0.3290                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+


These chromaticities are identical to the Rec. 709 colorspace.

Transfer function. Note that negative values for L are only used by the Y'CbCr conversion.
    L' = -1.055(-L):sup:`1/2.4` + 0.055 for L < -0.0031308

    L' = 12.92L for -0.0031308 ≤ L ≤ 0.0031308

    L' = 1.055L\ :sup:`1/2.4` - 0.055 for 0.0031308 < L ≤ 1

Inverse Transfer function:
    L = -((-L' + 0.055) / 1.055)\ :sup:`2.4` for L' < -0.04045

    L = L' / 12.92 for -0.04045 ≤ L' ≤ 0.04045

    L = ((L' + 0.055) / 1.055)\ :sup:`2.4` for L' > 0.04045

The luminance (Y') and color difference (Cb and Cr) are obtained with the following ``V4L2_YCBCR_ENC_SYCC`` encoding as defined by :ref:`sycc`:
    Y' = 0.2990R' + 0.5870G' + 0.1140B'

    Cb = -0.1687R' - 0.3313G' + 0.5B'

    Cr = 0.5R' - 0.4187G' - 0.0813B'

Y' is clamped to the range [0…1] and Cb and Cr are clamped to the range [-0.5…0.5]. The ``V4L2_YCBCR_ENC_SYCC`` quantization is always full range. Although this Y'CbCr encoding
looks very similar to the ``V4L2_YCBCR_ENC_XV601`` encoding, it is not. The ``V4L2_YCBCR_ENC_XV601`` scales and offsets the Y'CbCr values before quantization, but this encoding
does not do that.


.. _col-adobergb:

Colorspace Adobe RGB (V4L2_COLORSPACE_ADOBERGB)
===============================================

The :ref:`adobergb` standard defines the colorspace used by computer graphics that use the AdobeRGB colorspace. This is also known as the :ref:`oprgb` standard. The default
transfer function is ``V4L2_XFER_FUNC_ADOBERGB``. The default Y'CbCr encoding is ``V4L2_YCBCR_ENC_601``. The default Y'CbCr quantization is limited range. The chromaticities of the
primary colors and the white reference are:



.. table:: Adobe RGB Chromaticities

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Color                                         | x                                             | y                                                                                          |
    +===============================================+===============================================+============================================================================================+
    | Red                                           | 0.6400                                        | 0.3300                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Green                                         | 0.2100                                        | 0.7100                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Blue                                          | 0.1500                                        | 0.0600                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | White Reference (D65)                         | 0.3127                                        | 0.3290                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



Transfer function:
    L' = L\ :sup:`1/2.19921875`

Inverse Transfer function:
    L = L'\ :sup:`2.19921875`

The luminance (Y') and color difference (Cb and Cr) are obtained with the following ``V4L2_YCBCR_ENC_601`` encoding:
    Y' = 0.299R' + 0.587G' + 0.114B'

    Cb = -0.169R' - 0.331G' + 0.5B'

    Cr = 0.5R' - 0.419G' - 0.081B'

Y' is clamped to the range [0…1] and Cb and Cr are clamped to the range [-0.5…0.5]. This transform is identical to one defined in SMPTE 170M/BT.601. The Y'CbCr quantization is
limited range.


.. _col-bt2020:

Colorspace BT.2020 (V4L2_COLORSPACE_BT2020)
===========================================

The :ref:`itu2020` standard defines the colorspace used by Ultra-high definition television (UHDTV). The default transfer function is ``V4L2_XFER_FUNC_709``. The default Y'CbCr
encoding is ``V4L2_YCBCR_ENC_BT2020``. The default R'G'B' quantization is limited range (!), and so is the default Y'CbCr quantization. The chromaticities of the primary colors and
the white reference are:



.. table:: BT.2020 Chromaticities

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Color                                         | x                                             | y                                                                                          |
    +===============================================+===============================================+============================================================================================+
    | Red                                           | 0.708                                         | 0.292                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Green                                         | 0.170                                         | 0.797                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Blue                                          | 0.131                                         | 0.046                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | White Reference (D65)                         | 0.3127                                        | 0.3290                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



Transfer function (same as Rec. 709):
    L' = 4.5L for 0 ≤ L < 0.018

    L' = 1.099L\ :sup:`0.45` - 0.099 for 0.018 ≤ L ≤ 1

Inverse Transfer function:
    L = L' / 4.5 for L' < 0.081

    L = ((L' + 0.099) / 1.099)\ :sup:`1/0.45` for L' ≥ 0.081

The luminance (Y') and color difference (Cb and Cr) are obtained with the following ``V4L2_YCBCR_ENC_BT2020`` encoding:
    Y' = 0.2627R' + 0.6780G' + 0.0593B'

    Cb = -0.1396R' - 0.3604G' + 0.5B'

    Cr = 0.5R' - 0.4598G' - 0.0402B'

Y' is clamped to the range [0…1] and Cb and Cr are clamped to the range [-0.5…0.5]. The Y'CbCr quantization is limited range.

There is also an alternate constant luminance R'G'B' to Yc'CbcCrc (``V4L2_YCBCR_ENC_BT2020_CONST_LUM``) encoding:

Luma:
    Yc' = (0.2627R + 0.6780G + 0.0593B)'

B' - Yc' ≤ 0:
    Cbc = (B' - Yc') / 1.9404

B' - Yc' > 0:
    Cbc = (B' - Yc') / 1.5816

R' - Yc' ≤ 0:
    Crc = (R' - Y') / 1.7184

R' - Yc' > 0:
    Crc = (R' - Y') / 0.9936

Yc' is clamped to the range [0…1] and Cbc and Crc are clamped to the range [-0.5…0.5]. The Yc'CbcCrc quantization is limited range.


.. _col-dcip3:

Colorspace DCI-P3 (V4L2_COLORSPACE_DCI_P3)
==========================================

The :ref:`smpte431` standard defines the colorspace used by cinema projectors that use the DCI-P3 colorspace. The default transfer function is ``V4L2_XFER_FUNC_DCI_P3``. The
default Y'CbCr encoding is ``V4L2_YCBCR_ENC_709``. Note that this colorspace does not specify a Y'CbCr encoding since it is not meant to be encoded to Y'CbCr. So this default
Y'CbCr encoding was picked because it is the HDTV encoding. The default Y'CbCr quantization is limited range. The chromaticities of the primary colors and the white reference are:



.. table:: DCI-P3 Chromaticities

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Color                                         | x                                             | y                                                                                          |
    +===============================================+===============================================+============================================================================================+
    | Red                                           | 0.6800                                        | 0.3200                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Green                                         | 0.2650                                        | 0.6900                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Blue                                          | 0.1500                                        | 0.0600                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | White Reference                               | 0.3140                                        | 0.3510                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



Transfer function:
    L' = L\ :sup:`1/2.6`

Inverse Transfer function:
    L = L'\ :sup:`2.6`

Y'CbCr encoding is not specified. V4L2 defaults to Rec. 709.


.. _col-smpte-240m:

Colorspace SMPTE 240M (V4L2_COLORSPACE_SMPTE240M)
=================================================

The :ref:`smpte240m` standard was an interim standard used during the early days of HDTV (1988-1998). It has been superseded by Rec. 709. The default transfer function is
``V4L2_XFER_FUNC_SMPTE240M``. The default Y'CbCr encoding is ``V4L2_YCBCR_ENC_SMPTE240M``. The default Y'CbCr quantization is limited range. The chromaticities of the primary
colors and the white reference are:



.. table:: SMPTE 240M Chromaticities

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Color                                         | x                                             | y                                                                                          |
    +===============================================+===============================================+============================================================================================+
    | Red                                           | 0.630                                         | 0.340                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Green                                         | 0.310                                         | 0.595                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Blue                                          | 0.155                                         | 0.070                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | White Reference (D65)                         | 0.3127                                        | 0.3290                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+


These chromaticities are identical to the SMPTE 170M colorspace.

Transfer function:
    L' = 4L for 0 ≤ L < 0.0228

    L' = 1.1115L\ :sup:`0.45` - 0.1115 for 0.0228 ≤ L ≤ 1

Inverse Transfer function:
    L = L' / 4 for 0 ≤ L' < 0.0913

    L = ((L' + 0.1115) / 1.1115)\ :sup:`1/0.45` for L' ≥ 0.0913

The luminance (Y') and color difference (Cb and Cr) are obtained with the following ``V4L2_YCBCR_ENC_SMPTE240M`` encoding:
    Y' = 0.2122R' + 0.7013G' + 0.0865B'

    Cb = -0.1161R' - 0.3839G' + 0.5B'

    Cr = 0.5R' - 0.4451G' - 0.0549B'

Yc' is clamped to the range [0…1] and Cbc and Crc are clamped to the range [-0.5…0.5]. The Y'CbCr quantization is limited range.


.. _col-sysm:

Colorspace NTSC 1953 (V4L2_COLORSPACE_470_SYSTEM_M)
===================================================

This standard defines the colorspace used by NTSC in 1953. In practice this colorspace is obsolete and SMPTE 170M should be used instead. The default transfer function is
``V4L2_XFER_FUNC_709``. The default Y'CbCr encoding is ``V4L2_YCBCR_ENC_601``. The default Y'CbCr quantization is limited range. The chromaticities of the primary colors and the
white reference are:



.. table:: NTSC 1953 Chromaticities

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Color                                         | x                                             | y                                                                                          |
    +===============================================+===============================================+============================================================================================+
    | Red                                           | 0.67                                          | 0.33                                                                                       |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Green                                         | 0.21                                          | 0.71                                                                                       |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Blue                                          | 0.14                                          | 0.08                                                                                       |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | White Reference (C)                           | 0.310                                         | 0.316                                                                                      |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+


Note that this colorspace uses Illuminant C instead of D65 as the white reference. To correctly convert an image in this colorspace to another that uses D65 you need to apply a
chromatic adaptation algorithm such as the Bradford method.

The transfer function was never properly defined for NTSC 1953. The Rec. 709 transfer function is recommended in the literature:
    L' = 4.5L for 0 ≤ L < 0.018

    L' = 1.099L\ :sup:`0.45` - 0.099 for 0.018 ≤ L ≤ 1

Inverse Transfer function:
    L = L' / 4.5 for L' < 0.081

    L = ((L' + 0.099) / 1.099)\ :sup:`1/0.45` for L' ≥ 0.081

The luminance (Y') and color difference (Cb and Cr) are obtained with the following ``V4L2_YCBCR_ENC_601`` encoding:
    Y' = 0.299R' + 0.587G' + 0.114B'

    Cb = -0.169R' - 0.331G' + 0.5B'

    Cr = 0.5R' - 0.419G' - 0.081B'

Y' is clamped to the range [0…1] and Cb and Cr are clamped to the range [-0.5…0.5]. The Y'CbCr quantization is limited range. This transform is identical to one defined in SMPTE
170M/BT.601.


.. _col-sysbg:

Colorspace EBU Tech. 3213 (V4L2_COLORSPACE_470_SYSTEM_BG)
=========================================================

The :ref:`tech3213` standard defines the colorspace used by PAL/SECAM in 1975. In practice this colorspace is obsolete and SMPTE 170M should be used instead. The default transfer
function is ``V4L2_XFER_FUNC_709``. The default Y'CbCr encoding is ``V4L2_YCBCR_ENC_601``. The default Y'CbCr quantization is limited range. The chromaticities of the primary
colors and the white reference are:



.. table:: EBU Tech. 3213 Chromaticities

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Color                                         | x                                             | y                                                                                          |
    +===============================================+===============================================+============================================================================================+
    | Red                                           | 0.64                                          | 0.33                                                                                       |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Green                                         | 0.29                                          | 0.60                                                                                       |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Blue                                          | 0.15                                          | 0.06                                                                                       |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | White Reference (D65)                         | 0.3127                                        | 0.3290                                                                                     |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



The transfer function was never properly defined for this colorspace. The Rec. 709 transfer function is recommended in the literature:
    L' = 4.5L for 0 ≤ L < 0.018

    L' = 1.099L\ :sup:`0.45` - 0.099 for 0.018 ≤ L ≤ 1

Inverse Transfer function:
    L = L' / 4.5 for L' < 0.081

    L = ((L' + 0.099) / 1.099)\ :sup:`1/0.45` for L' ≥ 0.081

The luminance (Y') and color difference (Cb and Cr) are obtained with the following ``V4L2_YCBCR_ENC_601`` encoding:
    Y' = 0.299R' + 0.587G' + 0.114B'

    Cb = -0.169R' - 0.331G' + 0.5B'

    Cr = 0.5R' - 0.419G' - 0.081B'

Y' is clamped to the range [0…1] and Cb and Cr are clamped to the range [-0.5…0.5]. The Y'CbCr quantization is limited range. This transform is identical to one defined in SMPTE
170M/BT.601.


.. _col-jpeg:

Colorspace JPEG (V4L2_COLORSPACE_JPEG)
======================================

This colorspace defines the colorspace used by most (Motion-)JPEG formats. The chromaticities of the primary colors and the white reference are identical to sRGB. The transfer
function use is ``V4L2_XFER_FUNC_SRGB``. The Y'CbCr encoding is ``V4L2_YCBCR_ENC_601`` with full range quantization where Y' is scaled to [0…255] and Cb/Cr are scaled to [-128…128]
and then clipped to [-128…127].

Note that the JPEG standard does not actually store colorspace information. So if something other than sRGB is used, then the driver will have to set that information explicitly.
Effectively ``V4L2_COLORSPACE_JPEG`` can be considered to be an abbreviation for ``V4L2_COLORSPACE_SRGB``, ``V4L2_YCBCR_ENC_601`` and ``V4L2_QUANTIZATION_FULL_RANGE``.


Detailed Transfer Function Descriptions
=======================================


.. _xf-smpte-2084:

Transfer Function SMPTE 2084 (V4L2_XFER_FUNC_SMPTE2084)
=======================================================

The :ref:`smpte2084` standard defines the transfer function used by High Dynamic Range content.

Constants:
    m1 = (2610 / 4096) / 4

    m2 = (2523 / 4096) ⋆ 128

    c1 = 3424 / 4096

    c2 = (2413 / 4096) ⋆ 32

    c3 = (2392 / 4096) ⋆ 32

Transfer function:
    L' = ((c1 + c2 ⋆ L\ :sup:`m1`) / (1 + c3 ⋆ L\ :sup:`m1`))\ :sup:`m2`

Inverse Transfer function:
    L = (max(L':sup:`1/m2` - c1, 0) / (c2 - c3 ⋆ L'\ :sup:`1/m2`))\ :sup:`1/m1`


.. _pixfmt-indexed:

Indexed Format
==============

::

    TODO ... 


    <section id="pixfmt-indexed">
        <title>Indexed Format</title>

        <para>In this format each pixel is represented by an 8 bit index
    into a 256 entry ARGB palette. It is intended for <link linkend="osd">Video Output Overlays</link> only. There are no ioctls to
    access the palette, this must be done with ioctls of the Linux framebuffer API.</para>

        <table pgwide="0" frame="none">
          <title>Indexed Image Format</title>
          <tgroup cols="37" align="center">
        <colspec colname="id" align="left"/>
        <colspec colname="fourcc"/>
        <colspec colname="bit"/>

        <colspec colnum="4" colname="b07" align="center"/>
        <colspec colnum="5" colname="b06" align="center"/>
        <colspec colnum="6" colname="b05" align="center"/>
        <colspec colnum="7" colname="b04" align="center"/>
        <colspec colnum="8" colname="b03" align="center"/>
        <colspec colnum="9" colname="b02" align="center"/>
        <colspec colnum="10" colname="b01" align="center"/>
        <colspec colnum="11" colname="b00" align="center"/>

        <spanspec namest="b07" nameend="b00" spanname="b0"/>
        <spanspec namest="b17" nameend="b10" spanname="b1"/>
        <spanspec namest="b27" nameend="b20" spanname="b2"/>
        <spanspec namest="b37" nameend="b30" spanname="b3"/>
        <thead>
          <row>
            <entry>Identifier</entry>
            <entry>Code</entry>
            <entry> </entry>
            <entry spanname="b0">Byte 0</entry>
          </row>
          <row>
            <entry> </entry>
            <entry> </entry>
            <entry>Bit</entry>
            <entry>7</entry>
            <entry>6</entry>
            <entry>5</entry>
            <entry>4</entry>
            <entry>3</entry>
            <entry>2</entry>
            <entry>1</entry>
            <entry>0</entry>
          </row>
        </thead>
        <tbody valign="top">
          <row id="V4L2-PIX-FMT-PAL8">
            <entry><constant>V4L2_PIX_FMT_PAL8</constant></entry>
            <entry>'PAL8'</entry>
            <entry/>
            <entry>i<subscript>7</subscript></entry>
            <entry>i<subscript>6</subscript></entry>
            <entry>i<subscript>5</subscript></entry>
            <entry>i<subscript>4</subscript></entry>
            <entry>i<subscript>3</subscript></entry>
            <entry>i<subscript>2</subscript></entry>
            <entry>i<subscript>1</subscript></entry>
            <entry>i<subscript>0</subscript></entry>
          </row>
        </tbody>
          </tgroup>
        </table>
      </section>




.. _pixfmt-rgb:

RGB Formats
===========


.. toctree::
    :maxdepth: 1

    pixfmt-packed-rgb
    pixfmt-sbggr8
    pixfmt-sgbrg8
    pixfmt-sgrbg8
    pixfmt-srggb8
    pixfmt-sbggr16
    pixfmt-srggb10
    pixfmt-srggb10p
    pixfmt-srggb10alaw8
    pixfmt-srggb10dpcm8
    pixfmt-srggb12

.. _yuv-formats:

YUV Formats
===========

YUV is the format native to TV broadcast and composite video signals. It separates the brightness information (Y) from the color information (U and V or Cb and Cr). The color
information consists of red and blue *color difference* signals, this way the green component can be reconstructed by subtracting from the brightness component. See
:ref:`colorspaces` for conversion examples. YUV was chosen because early television would only transmit brightness information. To add color in a way compatible with existing
receivers a new signal carrier was added to transmit the color difference signals. Secondary in the YUV format the U and V components usually have lower resolution than the Y
component. This is an analog video compression technique taking advantage of a property of the human visual system, being more sensitive to brightness information.


.. toctree::
    :maxdepth: 1

    pixfmt-packed-yuv
    pixfmt-grey
    pixfmt-y10
    pixfmt-y12
    pixfmt-y10b
    pixfmt-y16
    pixfmt-y16-be
    pixfmt-y8i
    pixfmt-y12i
    pixfmt-uv8
    pixfmt-yuyv
    pixfmt-uyvy
    pixfmt-yvyu
    pixfmt-vyuy
    pixfmt-y41p
    pixfmt-yuv420
    pixfmt-yuv420m
    pixfmt-yuv422m
    pixfmt-yuv444m
    pixfmt-yuv410
    pixfmt-yuv422p
    pixfmt-yuv411p
    pixfmt-nv12
    pixfmt-nv12m
    pixfmt-nv12mt
    pixfmt-nv16
    pixfmt-nv16m
    pixfmt-nv24
    pixfmt-m420

.. _depth-formats:

Depth Formats
=============

Depth data provides distance to points, mapped onto the image plane


.. toctree::
    :maxdepth: 1

    pixfmt-z16

Compressed Formats
==================


.. _compressed-formats:

.. table:: Compressed Image Formats

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | Identifier                                                          | Code                   | Details                                                                                    |
    +=====================================================================+========================+============================================================================================+
    | ``V4L2_PIX_FMT_JPEG``                                               | 'JPEG'                 | TBD. See also :ref:`VIDIOC_G_JPEGCOMP    <vidioc-g-jpegcomp>`,                             |
    |                                                                     |                        | :ref:`VIDIOC_S_JPEGCOMP    <vidioc-g-jpegcomp>`.                                           |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_MPEG``                                               | 'MPEG'                 | MPEG multiplexed stream. The actual format is determined by extended control               |
    |                                                                     |                        | ``V4L2_CID_MPEG_STREAM_TYPE``, see :ref:`mpeg-control-id`.                                 |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_H264``                                               | 'H264'                 | H264 video elementary stream with start codes.                                             |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_H264_NO_SC``                                         | 'AVC1'                 | H264 video elementary stream without start codes.                                          |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_H264_MVC``                                           | 'M264'                 | H264 MVC video elementary stream.                                                          |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_H263``                                               | 'H263'                 | H263 video elementary stream.                                                              |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_MPEG1``                                              | 'MPG1'                 | MPEG1 video elementary stream.                                                             |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_MPEG2``                                              | 'MPG2'                 | MPEG2 video elementary stream.                                                             |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_MPEG4``                                              | 'MPG4'                 | MPEG4 video elementary stream.                                                             |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_XVID``                                               | 'XVID'                 | Xvid video elementary stream.                                                              |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_VC1_ANNEX_G``                                        | 'VC1G'                 | VC1, SMPTE 421M Annex G compliant stream.                                                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_VC1_ANNEX_L``                                        | 'VC1L'                 | VC1, SMPTE 421M Annex L compliant stream.                                                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_VP8``                                                | 'VP80'                 | VP8 video elementary stream.                                                               |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



.. _sdr-formats:

SDR Formats
===========

These formats are used for :ref:`SDR <sdr>` interface only.


.. toctree::
    :maxdepth: 1

    pixfmt-sdr-cu08
    pixfmt-sdr-cu16le
    pixfmt-sdr-cs08
    pixfmt-sdr-cs14le
    pixfmt-sdr-ru12le

.. _pixfmt-reserved:

Reserved Format Identifiers
===========================

These formats are not defined by this specification, they are just listed for reference and to avoid naming conflicts. If you want to register your own format, send an e-mail to
the linux-media mailing list https://linuxtv.org/lists.php for inclusion in the ``videodev2.h`` file. If you want to share your format with other developers add a link to your
documentation and send a copy to the linux-media mailing list for inclusion in this section. If you think your format should be listed in a standard format section please make a
proposal on the linux-media mailing list.


.. _reserved-formats:

.. table:: Reserved Image Formats

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | Identifier                                                          | Code                   | Details                                                                                    |
    +=====================================================================+========================+============================================================================================+
    | ``V4L2_PIX_FMT_DV``                                                 | 'dvsd'                 | unknown                                                                                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_ET61X251``                                           | 'E625'                 | Compressed format of the ET61X251 driver.                                                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_HI240``                                              | 'HI24'                 | 8 bit RGB format used by the BTTV driver.                                                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_HM12``                                               | 'HM12'                 | YUV 4:2:0 format used by the IVTV driver, http://www.ivtvdriver.org/                       |
    |                                                                     |                        |                                                                                            |
    |                                                                     |                        | The format is documented in the kernel sources in the file                                 |
    |                                                                     |                        | ``Documentation/video4linux/cx2341x/README.hm12``                                          |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_CPIA1``                                              | 'CPIA'                 | YUV format used by the gspca cpia1 driver.                                                 |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_JPGL``                                               | 'JPGL'                 | JPEG-Light format (Pegasus Lossless JPEG) used in Divio webcams NW 80x.                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_SPCA501``                                            | 'S501'                 | YUYV per line used by the gspca driver.                                                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_SPCA505``                                            | 'S505'                 | YYUV per line used by the gspca driver.                                                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_SPCA508``                                            | 'S508'                 | YUVY per line used by the gspca driver.                                                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_SPCA561``                                            | 'S561'                 | Compressed GBRG Bayer format used by the gspca driver.                                     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_PAC207``                                             | 'P207'                 | Compressed BGGR Bayer format used by the gspca driver.                                     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_MR97310A``                                           | 'M310'                 | Compressed BGGR Bayer format used by the gspca driver.                                     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_JL2005BCD``                                          | 'JL20'                 | JPEG compressed RGGB Bayer format used by the gspca driver.                                |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_OV511``                                              | 'O511'                 | OV511 JPEG format used by the gspca driver.                                                |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_OV518``                                              | 'O518'                 | OV518 JPEG format used by the gspca driver.                                                |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_PJPG``                                               | 'PJPG'                 | Pixart 73xx JPEG format used by the gspca driver.                                          |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_SE401``                                              | 'S401'                 | Compressed RGB format used by the gspca se401 driver                                       |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_SQ905C``                                             | '905C'                 | Compressed RGGB bayer format used by the gspca driver.                                     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_MJPEG``                                              | 'MJPG'                 | Compressed format used by the Zoran driver                                                 |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_PWC1``                                               | 'PWC1'                 | Compressed format of the PWC driver.                                                       |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_PWC2``                                               | 'PWC2'                 | Compressed format of the PWC driver.                                                       |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_SN9C10X``                                            | 'S910'                 | Compressed format of the SN9C102 driver.                                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_SN9C20X_I420``                                       | 'S920'                 | YUV 4:2:0 format of the gspca sn9c20x driver.                                              |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_SN9C2028``                                           | 'SONX'                 | Compressed GBRG bayer format of the gspca sn9c2028 driver.                                 |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_STV0680``                                            | 'S680'                 | Bayer format of the gspca stv0680 driver.                                                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_WNVA``                                               | 'WNVA'                 | Used by the Winnov Videum driver, http://www.thedirks.org/winnov/                          |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_TM6000``                                             | 'TM60'                 | Used by Trident tm6000                                                                     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_CIT_YYVYUY``                                         | 'CITV'                 | Used by xirlink CIT, found at IBM webcams.                                                 |
    |                                                                     |                        |                                                                                            |
    |                                                                     |                        | Uses one line of Y then 1 line of VYUY                                                     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_KONICA420``                                          | 'KONI'                 | Used by Konica webcams.                                                                    |
    |                                                                     |                        |                                                                                            |
    |                                                                     |                        | YUV420 planar in blocks of 256 pixels.                                                     |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_YYUV``                                               | 'YYUV'                 | unknown                                                                                    |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_Y4``                                                 | 'Y04 '                 | Old 4-bit greyscale format. Only the most significant 4 bits of each byte are used, the    |
    |                                                                     |                        | other bits are set to 0.                                                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_Y6``                                                 | 'Y06 '                 | Old 6-bit greyscale format. Only the most significant 6 bits of each byte are used, the    |
    |                                                                     |                        | other bits are set to 0.                                                                   |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_S5C_UYVY_JPG``                                       | 'S5CI'                 | Two-planar format used by Samsung S5C73MX cameras. The first plane contains interleaved    |
    |                                                                     |                        | JPEG and UYVY image data, followed by meta data in form of an array of offsets to the UYVY |
    |                                                                     |                        | data blocks. The actual pointer array follows immediately the interleaved JPEG/UYVY data,  |
    |                                                                     |                        | the number of entries in this array equals the height of the UYVY image. Each entry is a   |
    |                                                                     |                        | 4-byte unsigned integer in big endian order and it's an offset to a single pixel line of   |
    |                                                                     |                        | the UYVY image. The first plane can start either with JPEG or UYVY data chunk. The size of |
    |                                                                     |                        | a single UYVY block equals the UYVY image's width multiplied by 2. The size of a JPEG      |
    |                                                                     |                        | chunk depends on the image and can vary with each line.                                    |
    |                                                                     |                        | The second plane, at an offset of 4084 bytes, contains a 4-byte offset to the pointer      |
    |                                                                     |                        | array in the first plane. This offset is followed by a 4-byte value indicating size of the |
    |                                                                     |                        | pointer array. All numbers in the second plane are also in big endian order. Remaining     |
    |                                                                     |                        | data in the second plane is undefined. The information in the second plane allows to       |
    |                                                                     |                        | easily find location of the pointer array, which can be different for each frame. The size |
    |                                                                     |                        | of the pointer array is constant for given UYVY image height.                              |
    |                                                                     |                        |                                                                                            |
    |                                                                     |                        | In order to extract UYVY and JPEG frames an application can initially set a data pointer   |
    |                                                                     |                        | to the start of first plane and then add an offset from the first entry of the pointers    |
    |                                                                     |                        | table. Such a pointer indicates start of an UYVY image pixel line. Whole UYVY line can be  |
    |                                                                     |                        | copied to a separate buffer. These steps should be repeated for each line, i.e. the number |
    |                                                                     |                        | of entries in the pointer array. Anything what's in between the UYVY lines is JPEG data    |
    |                                                                     |                        | and should be concatenated to form the JPEG stream.                                        |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



.. _format-flags:

.. table:: Format Flags

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``V4L2_PIX_FMT_FLAG_PREMUL_ALPHA``                                  | 0x00000001             | The color values are premultiplied by the alpha channel value. For example, if a light     |
    |                                                                     |                        | blue pixel with 50% transparency was described by RGBA values (128, 192, 255, 128), the    |
    |                                                                     |                        | same pixel described with premultiplied colors would be described by RGBA values (64, 96,  |
    |                                                                     |                        | 128, 128)                                                                                  |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+



.. _CIE 1931 colorspace: http://en.wikipedia.org/wiki/CIE_1931_color_space#CIE_xy_chromaticity_diagram_and_the_CIE_xyY_color_space
