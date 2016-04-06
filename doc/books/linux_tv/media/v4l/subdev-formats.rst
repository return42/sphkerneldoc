
.. _v4l2-mbus-format:

Media Bus Formats
=================


.. _v4l2-mbus-framefmt:

.. table:: struct v4l2_mbus_framefmt

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``width``                                     | Image width, in pixels.                                                                    |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``height``                                    | Image height, in pixels.                                                                   |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``code``                                      | Format code, from enum :ref:`v4l2_mbus_pixelcode    <v4l2-mbus-pixelcode>`.                |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``field``                                     | Field order, from enum :ref:`v4l2_field   <v4l2-field>`.  See :ref:`field-order`   for     |
    |                                               |                                               | details.                                                                                   |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | __u32                                         | ``colorspace``                                | Image colorspace, from enum :ref:`v4l2_colorspace   <v4l2-colorspace>`.  See               |
    |                                               |                                               | :ref:`colorspaces`   for details.                                                          |
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
    | __u16                                         | ``reserved``  [11]                            | Reserved for future extensions. Applications and drivers must set the array to zero.       |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-mbus-pixelcode:

Media Bus Pixel Codes
=====================

The media bus pixel codes describe image formats as flowing over physical busses (both between separate physical components and inside SoC devices). This should not be confused
with the V4L2 pixel formats that describe, using four character codes, image formats as stored in memory.

While there is a relationship between image formats on busses and image formats in memory (a raw Bayer image won't be magically converted to JPEG just by storing it to memory),
there is no one-to-one correspondance between them.


Packed RGB Formats
==================

Those formats transfer pixel data as red, green and blue components. The format code is made of the following information.

-  The red, green and blue components order code, as encoded in a pixel sample. Possible values are RGB and BGR.

-  The number of bits per component, for each component. The values can be different for all components. Common values are 555 and 565.

-  The number of bus samples per pixel. Pixels that are wider than the bus width must be transferred in multiple samples. Common values are 1 and 2.

-  The bus width.

-  For formats where the total number of bits per pixel is smaller than the number of bus samples per pixel times the bus width, a padding value stating if the bytes are padded in
   their most high order bits (PADHI) or low order bits (PADLO). A "C" prefix is used for component-wise padding in the most high order bits (CPADHI) or low order bits (CPADLO) of
   each separate component.

-  For formats where the number of bus samples per pixel is larger than 1, an endianness value stating if the pixel is transferred MSB first (BE) or LSB first (LE).

For instance, a format where pixels are encoded as 5-bits red, 5-bits green and 5-bit blue values padded on the high bit, transferred as 2 8-bit samples per pixel with the most
significant bits (padding, red and half of the green value) transferred first will be named ``MEDIA_BUS_FMT_RGB555_2X8_PADHI_BE``.

The following tables list existing packed RGB formats.


.. _v4l2-mbus-pixelcode-rgb:

RGB formats
===========

::

    TODO ... 


    <table pgwide="0" frame="none" id="v4l2-mbus-pixelcode-rgb">
        <title>RGB formats</title>
        <tgroup cols="27">
          <colspec colname="id" align="left"/>
          <colspec colname="code" align="center"/>
          <colspec colname="bit"/>
          <colspec colnum="4" colname="b31" align="center"/>
          <colspec colnum="5" colname="b20" align="center"/>
          <colspec colnum="6" colname="b29" align="center"/>
          <colspec colnum="7" colname="b28" align="center"/>
          <colspec colnum="8" colname="b27" align="center"/>
          <colspec colnum="9" colname="b26" align="center"/>
          <colspec colnum="10" colname="b25" align="center"/>
          <colspec colnum="11" colname="b24" align="center"/>
          <colspec colnum="12" colname="b23" align="center"/>
          <colspec colnum="13" colname="b22" align="center"/>
          <colspec colnum="14" colname="b21" align="center"/>
          <colspec colnum="15" colname="b20" align="center"/>
          <colspec colnum="16" colname="b19" align="center"/>
          <colspec colnum="17" colname="b18" align="center"/>
          <colspec colnum="18" colname="b17" align="center"/>
          <colspec colnum="19" colname="b16" align="center"/>
          <colspec colnum="20" colname="b15" align="center"/>
          <colspec colnum="21" colname="b14" align="center"/>
          <colspec colnum="22" colname="b13" align="center"/>
          <colspec colnum="23" colname="b12" align="center"/>
          <colspec colnum="24" colname="b11" align="center"/>
          <colspec colnum="25" colname="b10" align="center"/>
          <colspec colnum="26" colname="b09" align="center"/>
          <colspec colnum="27" colname="b08" align="center"/>
          <colspec colnum="28" colname="b07" align="center"/>
          <colspec colnum="29" colname="b06" align="center"/>
          <colspec colnum="30" colname="b05" align="center"/>
          <colspec colnum="31" colname="b04" align="center"/>
          <colspec colnum="32" colname="b03" align="center"/>
          <colspec colnum="33" colname="b02" align="center"/>
          <colspec colnum="34" colname="b01" align="center"/>
          <colspec colnum="35" colname="b00" align="center"/>
          <spanspec namest="b31" nameend="b00" spanname="b0"/>
          <thead>
            <row>
              <entry>Identifier</entry>
              <entry>Code</entry>
              <entry/>
              <entry spanname="b0">Data organization</entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry>Bit</entry>
              <entry>31</entry>
              <entry>30</entry>
              <entry>29</entry>
              <entry>28</entry>
              <entry>27</entry>
              <entry>26</entry>
              <entry>25</entry>
              <entry>24</entry>
              <entry>23</entry>
              <entry>22</entry>
              <entry>21</entry>
              <entry>20</entry>
              <entry>19</entry>
              <entry>18</entry>
              <entry>17</entry>
              <entry>16</entry>
              <entry>15</entry>
              <entry>14</entry>
              <entry>13</entry>
              <entry>12</entry>
              <entry>11</entry>
              <entry>10</entry>
              <entry>9</entry>
              <entry>8</entry>
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
            <row id="MEDIA-BUS-FMT-RGB444-1X12">
              <entry>MEDIA_BUS_FMT_RGB444_1X12</entry>
              <entry>0x1016</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RGB444-2X8-PADHI-BE">
              <entry>MEDIA_BUS_FMT_RGB444_2X8_PADHI_BE</entry>
              <entry>0x1001</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RGB444-2X8-PADHI-LE">
              <entry>MEDIA_BUS_FMT_RGB444_2X8_PADHI_LE</entry>
              <entry>0x1002</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RGB555-2X8-PADHI-BE">
              <entry>MEDIA_BUS_FMT_RGB555_2X8_PADHI_BE</entry>
              <entry>0x1003</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>0</entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RGB555-2X8-PADHI-LE">
              <entry>MEDIA_BUS_FMT_RGB555_2X8_PADHI_LE</entry>
              <entry>0x1004</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>0</entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RGB565-1X16">
              <entry>MEDIA_BUS_FMT_RGB565_1X16</entry>
              <entry>0x1017</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-BGR565-2X8-BE">
              <entry>MEDIA_BUS_FMT_BGR565_2X8_BE</entry>
              <entry>0x1005</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-BGR565-2X8-LE">
              <entry>MEDIA_BUS_FMT_BGR565_2X8_LE</entry>
              <entry>0x1006</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RGB565-2X8-BE">
              <entry>MEDIA_BUS_FMT_RGB565_2X8_BE</entry>
              <entry>0x1007</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RGB565-2X8-LE">
              <entry>MEDIA_BUS_FMT_RGB565_2X8_LE</entry>
              <entry>0x1008</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RGB666-1X18">
              <entry>MEDIA_BUS_FMT_RGB666_1X18</entry>
              <entry>0x1009</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RBG888-1X24">
              <entry>MEDIA_BUS_FMT_RBG888_1X24</entry>
              <entry>0x100e</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>r<subscript>7</subscript></entry>
              <entry>r<subscript>6</subscript></entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RGB666-1X24_CPADHI">
              <entry>MEDIA_BUS_FMT_RGB666_1X24_CPADHI</entry>
              <entry>0x1015</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-BGR888-1X24">
              <entry>MEDIA_BUS_FMT_BGR888_1X24</entry>
              <entry>0x1013</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>r<subscript>7</subscript></entry>
              <entry>r<subscript>6</subscript></entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-GBR888-1X24">
              <entry>MEDIA_BUS_FMT_GBR888_1X24</entry>
              <entry>0x1014</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
              <entry>r<subscript>7</subscript></entry>
              <entry>r<subscript>6</subscript></entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RGB888-1X24">
              <entry>MEDIA_BUS_FMT_RGB888_1X24</entry>
              <entry>0x100a</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>r<subscript>7</subscript></entry>
              <entry>r<subscript>6</subscript></entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RGB888-2X12-BE">
              <entry>MEDIA_BUS_FMT_RGB888_2X12_BE</entry>
              <entry>0x100b</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>r<subscript>7</subscript></entry>
              <entry>r<subscript>6</subscript></entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RGB888-2X12-LE">
              <entry>MEDIA_BUS_FMT_RGB888_2X12_LE</entry>
              <entry>0x100c</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>r<subscript>7</subscript></entry>
              <entry>r<subscript>6</subscript></entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-ARGB888-1X32">
              <entry>MEDIA_BUS_FMT_ARGB888_1X32</entry>
              <entry>0x100d</entry>
              <entry/>
              <entry>a<subscript>7</subscript></entry>
              <entry>a<subscript>6</subscript></entry>
              <entry>a<subscript>5</subscript></entry>
              <entry>a<subscript>4</subscript></entry>
              <entry>a<subscript>3</subscript></entry>
              <entry>a<subscript>2</subscript></entry>
              <entry>a<subscript>1</subscript></entry>
              <entry>a<subscript>0</subscript></entry>
              <entry>r<subscript>7</subscript></entry>
              <entry>r<subscript>6</subscript></entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-RGB888-1X32-PADHI">
              <entry>MEDIA_BUS_FMT_RGB888_1X32_PADHI</entry>
              <entry>0x100f</entry>
              <entry/>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>r<subscript>7</subscript></entry>
              <entry>r<subscript>6</subscript></entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
          </tbody>
        </tgroup>
          </table>



On LVDS buses, usually each sample is transferred serialized in seven time slots per pixel clock, on three (18-bit) or four (24-bit) differential data pairs at the same time. The
remaining bits are used for control signals as defined by SPWG/PSWG/VESA or JEIDA standards. The 24-bit RGB format serialized in seven time slots on four lanes using JEIDA defined
bit mapping will be named ``MEDIA_BUS_FMT_RGB888_1X7X4_JEIDA``, for example.


.. _v4l2-mbus-pixelcode-rgb-lvds:

.. table:: LVDS RGB formats

    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    | Identifier           | Code                 |                      |                      | Data organization    |                      |                      |                                          |
    +======================+======================+======================+======================+======================+======================+======================+==========================================+
    | MEDIA_BUS_FMT_RGB    | 0x1010               | 0                    |                      | -                    | d                    | b  :sub:`1`          | g  :sub:`0`                              |
    | 666_1X7X3_SPWG       |                      |                      |                      |                      |                      |                      |                                          |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 1                    |                      | -                    | d                    | b\ :sub:`0`          | r\ :sub:`5`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 2                    |                      | -                    | d                    | g\ :sub:`5`          | r\ :sub:`4`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 3                    |                      | -                    | b\ :sub:`5`          | g\ :sub:`4`          | r\ :sub:`3`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 4                    |                      | -                    | b\ :sub:`4`          | g\ :sub:`3`          | r\ :sub:`2`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 5                    |                      | -                    | b\ :sub:`3`          | g\ :sub:`2`          | r\ :sub:`1`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 6                    |                      | -                    | b\ :sub:`2`          | g\ :sub:`1`          | r\ :sub:`0`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    | MEDIA_BUS_FMT_RGB    | 0x1011               | 0                    |                      | d                    | d                    | b  :sub:`1`          | g  :sub:`0`                              |
    | 888_1X7X4_SPWG       |                      |                      |                      |                      |                      |                      |                                          |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 1                    |                      | b\ :sub:`7`          | d                    | b\ :sub:`0`          | r\ :sub:`5`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 2                    |                      | b\ :sub:`6`          | d                    | g\ :sub:`5`          | r\ :sub:`4`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 3                    |                      | g\ :sub:`7`          | b\ :sub:`5`          | g\ :sub:`4`          | r\ :sub:`3`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 4                    |                      | g\ :sub:`6`          | b\ :sub:`4`          | g\ :sub:`3`          | r\ :sub:`2`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 5                    |                      | r\ :sub:`7`          | b\ :sub:`3`          | g\ :sub:`2`          | r\ :sub:`1`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 6                    |                      | r\ :sub:`6`          | b\ :sub:`2`          | g\ :sub:`1`          | r\ :sub:`0`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    | MEDIA_BUS_FMT_RGB    | 0x1012               | 0                    |                      | d                    | d                    | b  :sub:`3`          | g  :sub:`2`                              |
    | 888_1X7X4_JEIDA      |                      |                      |                      |                      |                      |                      |                                          |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 1                    |                      | b\ :sub:`1`          | d                    | b\ :sub:`2`          | r\ :sub:`7`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 2                    |                      | b\ :sub:`0`          | d                    | g\ :sub:`7`          | r\ :sub:`6`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 3                    |                      | g\ :sub:`1`          | b\ :sub:`7`          | g\ :sub:`6`          | r\ :sub:`5`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 4                    |                      | g\ :sub:`0`          | b\ :sub:`6`          | g\ :sub:`5`          | r\ :sub:`4`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 5                    |                      | r\ :sub:`1`          | b\ :sub:`5`          | g\ :sub:`4`          | r\ :sub:`3`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+
    |                      |                      | 6                    |                      | r\ :sub:`0`          | b\ :sub:`4`          | g\ :sub:`3`          | r\ :sub:`2`                              |
    +----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+------------------------------------------+



Bayer Formats
=============

Those formats transfer pixel data as red, green and blue components. The format code is made of the following information.

-  The red, green and blue components order code, as encoded in a pixel sample. The possible values are shown in :ref:`bayer-patterns`.

-  The number of bits per pixel component. All components are transferred on the same number of bits. Common values are 8, 10 and 12.

-  The compression (optional). If the pixel components are ALAW- or DPCM-compressed, a mention of the compression scheme and the number of bits per compressed pixel component.

-  The number of bus samples per pixel. Pixels that are wider than the bus width must be transferred in multiple samples. Common values are 1 and 2.

-  The bus width.

-  For formats where the total number of bits per pixel is smaller than the number of bus samples per pixel times the bus width, a padding value stating if the bytes are padded in
   their most high order bits (PADHI) or low order bits (PADLO).

-  For formats where the number of bus samples per pixel is larger than 1, an endianness value stating if the pixel is transferred MSB first (BE) or LSB first (LE).

For instance, a format with uncompressed 10-bit Bayer components arranged in a red, green, green, blue pattern transferred as 2 8-bit samples per pixel with the least significant
bits transferred first will be named ``MEDIA_BUS_FMT_SRGGB10_2X8_PADHI_LE``.


.. _bayer-patterns:

.. figure::  subdev-formats_files/bayer.*
    :alt:    bayer.png
    :align:  center

    Bayer Patterns

    Bayer filter color patterns



The following table lists existing packed Bayer formats. The data organization is given as an example for the first pixel only.


.. _v4l2-mbus-pixelcode-bayer:

Bayer Formats
=============

::

    TODO ... 


    <table pgwide="0" frame="none" id="v4l2-mbus-pixelcode-bayer">
        <title>Bayer Formats</title>
        <tgroup cols="15">
          <colspec colname="id" align="left"/>
          <colspec colname="code" align="center"/>
          <colspec colname="bit"/>
          <colspec colnum="4" colname="b11" align="center"/>
          <colspec colnum="5" colname="b10" align="center"/>
          <colspec colnum="6" colname="b09" align="center"/>
          <colspec colnum="7" colname="b08" align="center"/>
          <colspec colnum="8" colname="b07" align="center"/>
          <colspec colnum="9" colname="b06" align="center"/>
          <colspec colnum="10" colname="b05" align="center"/>
          <colspec colnum="11" colname="b04" align="center"/>
          <colspec colnum="12" colname="b03" align="center"/>
          <colspec colnum="13" colname="b02" align="center"/>
          <colspec colnum="14" colname="b01" align="center"/>
          <colspec colnum="15" colname="b00" align="center"/>
          <spanspec namest="b11" nameend="b00" spanname="b0"/>
          <thead>
            <row>
              <entry>Identifier</entry>
              <entry>Code</entry>
              <entry/>
              <entry spanname="b0">Data organization</entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry>Bit</entry>
              <entry>11</entry>
              <entry>10</entry>
              <entry>9</entry>
              <entry>8</entry>
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
            <row id="MEDIA-BUS-FMT-SBGGR8-1X8">
              <entry>MEDIA_BUS_FMT_SBGGR8_1X8</entry>
              <entry>0x3001</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SGBRG8-1X8">
              <entry>MEDIA_BUS_FMT_SGBRG8_1X8</entry>
              <entry>0x3013</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SGRBG8-1X8">
              <entry>MEDIA_BUS_FMT_SGRBG8_1X8</entry>
              <entry>0x3002</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SRGGB8-1X8">
              <entry>MEDIA_BUS_FMT_SRGGB8_1X8</entry>
              <entry>0x3014</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>r<subscript>7</subscript></entry>
              <entry>r<subscript>6</subscript></entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SBGGR10-ALAW8-1X8">
              <entry>MEDIA_BUS_FMT_SBGGR10_ALAW8_1X8</entry>
              <entry>0x3015</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SGBRG10-ALAW8-1X8">
              <entry>MEDIA_BUS_FMT_SGBRG10_ALAW8_1X8</entry>
              <entry>0x3016</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SGRBG10-ALAW8-1X8">
              <entry>MEDIA_BUS_FMT_SGRBG10_ALAW8_1X8</entry>
              <entry>0x3017</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SRGGB10-ALAW8-1X8">
              <entry>MEDIA_BUS_FMT_SRGGB10_ALAW8_1X8</entry>
              <entry>0x3018</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>r<subscript>7</subscript></entry>
              <entry>r<subscript>6</subscript></entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SBGGR10-DPCM8-1X8">
              <entry>MEDIA_BUS_FMT_SBGGR10_DPCM8_1X8</entry>
              <entry>0x300b</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SGBRG10-DPCM8-1X8">
              <entry>MEDIA_BUS_FMT_SGBRG10_DPCM8_1X8</entry>
              <entry>0x300c</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SGRBG10-DPCM8-1X8">
              <entry>MEDIA_BUS_FMT_SGRBG10_DPCM8_1X8</entry>
              <entry>0x3009</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SRGGB10-DPCM8-1X8">
              <entry>MEDIA_BUS_FMT_SRGGB10_DPCM8_1X8</entry>
              <entry>0x300d</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>r<subscript>7</subscript></entry>
              <entry>r<subscript>6</subscript></entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SBGGR10-2X8-PADHI-BE">
              <entry>MEDIA_BUS_FMT_SBGGR10_2X8_PADHI_BE</entry>
              <entry>0x3003</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>b<subscript>9</subscript></entry>
              <entry>b<subscript>8</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SBGGR10-2X8-PADHI-LE">
              <entry>MEDIA_BUS_FMT_SBGGR10_2X8_PADHI_LE</entry>
              <entry>0x3004</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>b<subscript>9</subscript></entry>
              <entry>b<subscript>8</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SBGGR10-2X8-PADLO-BE">
              <entry>MEDIA_BUS_FMT_SBGGR10_2X8_PADLO_BE</entry>
              <entry>0x3005</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>b<subscript>9</subscript></entry>
              <entry>b<subscript>8</subscript></entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
            </row>
            <row id="MEDIA-BUS-FMT-SBGGR10-2X8-PADLO-LE">
              <entry>MEDIA_BUS_FMT_SBGGR10_2X8_PADLO_LE</entry>
              <entry>0x3006</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
              <entry>0</entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>b<subscript>9</subscript></entry>
              <entry>b<subscript>8</subscript></entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SBGGR10-1X10">
              <entry>MEDIA_BUS_FMT_SBGGR10_1X10</entry>
              <entry>0x3007</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>b<subscript>9</subscript></entry>
              <entry>b<subscript>8</subscript></entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SGBRG10-1X10">
              <entry>MEDIA_BUS_FMT_SGBRG10_1X10</entry>
              <entry>0x300e</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>g<subscript>9</subscript></entry>
              <entry>g<subscript>8</subscript></entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SGRBG10-1X10">
              <entry>MEDIA_BUS_FMT_SGRBG10_1X10</entry>
              <entry>0x300a</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>g<subscript>9</subscript></entry>
              <entry>g<subscript>8</subscript></entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SRGGB10-1X10">
              <entry>MEDIA_BUS_FMT_SRGGB10_1X10</entry>
              <entry>0x300f</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>r<subscript>9</subscript></entry>
              <entry>r<subscript>8</subscript></entry>
              <entry>r<subscript>7</subscript></entry>
              <entry>r<subscript>6</subscript></entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SBGGR12-1X12">
              <entry>MEDIA_BUS_FMT_SBGGR12_1X12</entry>
              <entry>0x3008</entry>
              <entry/>
              <entry>b<subscript>11</subscript></entry>
              <entry>b<subscript>10</subscript></entry>
              <entry>b<subscript>9</subscript></entry>
              <entry>b<subscript>8</subscript></entry>
              <entry>b<subscript>7</subscript></entry>
              <entry>b<subscript>6</subscript></entry>
              <entry>b<subscript>5</subscript></entry>
              <entry>b<subscript>4</subscript></entry>
              <entry>b<subscript>3</subscript></entry>
              <entry>b<subscript>2</subscript></entry>
              <entry>b<subscript>1</subscript></entry>
              <entry>b<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SGBRG12-1X12">
              <entry>MEDIA_BUS_FMT_SGBRG12_1X12</entry>
              <entry>0x3010</entry>
              <entry/>
              <entry>g<subscript>11</subscript></entry>
              <entry>g<subscript>10</subscript></entry>
              <entry>g<subscript>9</subscript></entry>
              <entry>g<subscript>8</subscript></entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SGRBG12-1X12">
              <entry>MEDIA_BUS_FMT_SGRBG12_1X12</entry>
              <entry>0x3011</entry>
              <entry/>
              <entry>g<subscript>11</subscript></entry>
              <entry>g<subscript>10</subscript></entry>
              <entry>g<subscript>9</subscript></entry>
              <entry>g<subscript>8</subscript></entry>
              <entry>g<subscript>7</subscript></entry>
              <entry>g<subscript>6</subscript></entry>
              <entry>g<subscript>5</subscript></entry>
              <entry>g<subscript>4</subscript></entry>
              <entry>g<subscript>3</subscript></entry>
              <entry>g<subscript>2</subscript></entry>
              <entry>g<subscript>1</subscript></entry>
              <entry>g<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-SRGGB12-1X12">
              <entry>MEDIA_BUS_FMT_SRGGB12_1X12</entry>
              <entry>0x3012</entry>
              <entry/>
              <entry>r<subscript>11</subscript></entry>
              <entry>r<subscript>10</subscript></entry>
              <entry>r<subscript>9</subscript></entry>
              <entry>r<subscript>8</subscript></entry>
              <entry>r<subscript>7</subscript></entry>
              <entry>r<subscript>6</subscript></entry>
              <entry>r<subscript>5</subscript></entry>
              <entry>r<subscript>4</subscript></entry>
              <entry>r<subscript>3</subscript></entry>
              <entry>r<subscript>2</subscript></entry>
              <entry>r<subscript>1</subscript></entry>
              <entry>r<subscript>0</subscript></entry>
            </row>
          </tbody>
        </tgroup>
          </table>



Packed YUV Formats
==================

Those data formats transfer pixel data as (possibly downsampled) Y, U and V components. Some formats include dummy bits in some of their samples and are collectively referred to as
"YDYC" (Y-Dummy-Y-Chroma) formats. One cannot rely on the values of these dummy bits as those are undefined.

The format code is made of the following information.

-  The Y, U and V components order code, as transferred on the bus. Possible values are YUYV, UYVY, YVYU and VYUY for formats with no dummy bit, and YDYUYDYV, YDYVYDYU, YUYDYVYD
   and YVYDYUYD for YDYC formats.

-  The number of bits per pixel component. All components are transferred on the same number of bits. Common values are 8, 10 and 12.

-  The number of bus samples per pixel. Pixels that are wider than the bus width must be transferred in multiple samples. Common values are 1, 1.5 (encoded as 1_5) and 2.

-  The bus width. When the bus width is larger than the number of bits per pixel component, several components are packed in a single bus sample. The components are ordered as
   specified by the order code, with components on the left of the code transferred in the high order bits. Common values are 8 and 16.

For instance, a format where pixels are encoded as 8-bit YUV values downsampled to 4:2:2 and transferred as 2 8-bit bus samples per pixel in the U, Y, V, Y order will be named
``MEDIA_BUS_FMT_UYVY8_2X8``.

:ref:`v4l2-mbus-pixelcode-yuv8` lists existing packed YUV formats and describes the organization of each pixel data in each sample. When a format pattern is split across multiple
samples each of the samples in the pattern is described.

The role of each bit transferred over the bus is identified by one of the following codes.

-  y\ :sub:`x` for luma component bit number x

-  u\ :sub:`x` for blue chroma component bit number x

-  v\ :sub:`x` for red chroma component bit number x

-  a\ :sub:`x` for alpha component bit number x

-  - for non-available bits (for positions higher than the bus width)

-  d for dummy bits


.. _v4l2-mbus-pixelcode-yuv8:

YUV Formats
===========

::

    TODO ... 


    <table pgwide="0" frame="none" id="v4l2-mbus-pixelcode-yuv8">
        <title>YUV Formats</title>
        <tgroup cols="23">
          <colspec colname="id" align="left"/>
          <colspec colname="code" align="center"/>
          <colspec colname="bit"/>
          <colspec colnum="4" colname="b31" align="center"/>
          <colspec colnum="5" colname="b20" align="center"/>
          <colspec colnum="6" colname="b29" align="center"/>
          <colspec colnum="7" colname="b28" align="center"/>
          <colspec colnum="8" colname="b27" align="center"/>
          <colspec colnum="9" colname="b26" align="center"/>
          <colspec colnum="10" colname="b25" align="center"/>
          <colspec colnum="11" colname="b24" align="center"/>
          <colspec colnum="12" colname="b23" align="center"/>
          <colspec colnum="13" colname="b22" align="center"/>
          <colspec colnum="14" colname="b21" align="center"/>
          <colspec colnum="15" colname="b20" align="center"/>
          <colspec colnum="16" colname="b19" align="center"/>
          <colspec colnum="17" colname="b18" align="center"/>
          <colspec colnum="18" colname="b17" align="center"/>
          <colspec colnum="19" colname="b16" align="center"/>
          <colspec colnum="20" colname="b15" align="center"/>
          <colspec colnum="21" colname="b14" align="center"/>
          <colspec colnum="22" colname="b13" align="center"/>
          <colspec colnum="23" colname="b12" align="center"/>
          <colspec colnum="24" colname="b11" align="center"/>
          <colspec colnum="25" colname="b10" align="center"/>
          <colspec colnum="26" colname="b09" align="center"/>
          <colspec colnum="27" colname="b08" align="center"/>
          <colspec colnum="28" colname="b07" align="center"/>
          <colspec colnum="29" colname="b06" align="center"/>
          <colspec colnum="30" colname="b05" align="center"/>
          <colspec colnum="31" colname="b04" align="center"/>
          <colspec colnum="32" colname="b03" align="center"/>
          <colspec colnum="33" colname="b02" align="center"/>
          <colspec colnum="34" colname="b01" align="center"/>
          <colspec colnum="35" colname="b00" align="center"/>
          <spanspec namest="b31" nameend="b00" spanname="b0"/>
          <thead>
            <row>
              <entry>Identifier</entry>
              <entry>Code</entry>
              <entry/>
              <entry spanname="b0">Data organization</entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry>Bit</entry>
              <entry>31</entry>
              <entry>30</entry>
              <entry>29</entry>
              <entry>28</entry>
              <entry>27</entry>
              <entry>26</entry>
              <entry>25</entry>
              <entry>24</entry>
              <entry>23</entry>
              <entry>22</entry>
              <entry>21</entry>
              <entry>10</entry>
              <entry>19</entry>
              <entry>18</entry>
              <entry>17</entry>
              <entry>16</entry>
              <entry>15</entry>
              <entry>14</entry>
              <entry>13</entry>
              <entry>12</entry>
              <entry>11</entry>
              <entry>10</entry>
              <entry>9</entry>
              <entry>8</entry>
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
            <row id="MEDIA-BUS-FMT-Y8-1X8">
              <entry>MEDIA_BUS_FMT_Y8_1X8</entry>
              <entry>0x2001</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-UV8-1X8">
              <entry>MEDIA_BUS_FMT_UV8_1X8</entry>
              <entry>0x2015</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-UYVY8-1_5X8">
              <entry>MEDIA_BUS_FMT_UYVY8_1_5X8</entry>
              <entry>0x2002</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-VYUY8-1_5X8">
              <entry>MEDIA_BUS_FMT_VYUY8_1_5X8</entry>
              <entry>0x2003</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YUYV8-1_5X8">
              <entry>MEDIA_BUS_FMT_YUYV8_1_5X8</entry>
              <entry>0x2004</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YVYU8-1_5X8">
              <entry>MEDIA_BUS_FMT_YVYU8_1_5X8</entry>
              <entry>0x2005</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-UYVY8-2X8">
              <entry>MEDIA_BUS_FMT_UYVY8_2X8</entry>
              <entry>0x2006</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-VYUY8-2X8">
              <entry>MEDIA_BUS_FMT_VYUY8_2X8</entry>
              <entry>0x2007</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YUYV8-2X8">
              <entry>MEDIA_BUS_FMT_YUYV8_2X8</entry>
              <entry>0x2008</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YVYU8-2X8">
              <entry>MEDIA_BUS_FMT_YVYU8_2X8</entry>
              <entry>0x2009</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-Y10-1X10">
              <entry>MEDIA_BUS_FMT_Y10_1X10</entry>
              <entry>0x200a</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-UYVY10-2X10">
              <entry>MEDIA_BUS_FMT_UYVY10_2X10</entry>
              <entry>0x2018</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-VYUY10-2X10">
              <entry>MEDIA_BUS_FMT_VYUY10_2X10</entry>
              <entry>0x2019</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YUYV10-2X10">
              <entry>MEDIA_BUS_FMT_YUYV10_2X10</entry>
              <entry>0x200b</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YVYU10-2X10">
              <entry>MEDIA_BUS_FMT_YVYU10_2X10</entry>
              <entry>0x200c</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-Y12-1X12">
              <entry>MEDIA_BUS_FMT_Y12_1X12</entry>
              <entry>0x2013</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-UYVY12-2X12">
              <entry>MEDIA_BUS_FMT_UYVY12_2X12</entry>
              <entry>0x201c</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>11</subscript></entry>
              <entry>u<subscript>10</subscript></entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>11</subscript></entry>
              <entry>v<subscript>10</subscript></entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-VYUY12-2X12">
              <entry>MEDIA_BUS_FMT_VYUY12_2X12</entry>
              <entry>0x201d</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>11</subscript></entry>
              <entry>v<subscript>10</subscript></entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>11</subscript></entry>
              <entry>u<subscript>10</subscript></entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YUYV12-2X12">
              <entry>MEDIA_BUS_FMT_YUYV12_2X12</entry>
              <entry>0x201e</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>11</subscript></entry>
              <entry>u<subscript>10</subscript></entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>11</subscript></entry>
              <entry>v<subscript>10</subscript></entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YVYU12-2X12">
              <entry>MEDIA_BUS_FMT_YVYU12_2X12</entry>
              <entry>0x201f</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>11</subscript></entry>
              <entry>v<subscript>10</subscript></entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>11</subscript></entry>
              <entry>u<subscript>10</subscript></entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-UYVY8-1X16">
              <entry>MEDIA_BUS_FMT_UYVY8_1X16</entry>
              <entry>0x200f</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-VYUY8-1X16">
              <entry>MEDIA_BUS_FMT_VYUY8_1X16</entry>
              <entry>0x2010</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YUYV8-1X16">
              <entry>MEDIA_BUS_FMT_YUYV8_1X16</entry>
              <entry>0x2011</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YVYU8-1X16">
              <entry>MEDIA_BUS_FMT_YVYU8_1X16</entry>
              <entry>0x2012</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YDYUYDYV8-1X16">
              <entry>MEDIA_BUS_FMT_YDYUYDYV8_1X16</entry>
              <entry>0x2014</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>d</entry>
              <entry>d</entry>
              <entry>d</entry>
              <entry>d</entry>
              <entry>d</entry>
              <entry>d</entry>
              <entry>d</entry>
              <entry>d</entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>d</entry>
              <entry>d</entry>
              <entry>d</entry>
              <entry>d</entry>
              <entry>d</entry>
              <entry>d</entry>
              <entry>d</entry>
              <entry>d</entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-UYVY10-1X20">
              <entry>MEDIA_BUS_FMT_UYVY10_1X20</entry>
              <entry>0x201a</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-VYUY10-1X20">
              <entry>MEDIA_BUS_FMT_VYUY10_1X20</entry>
              <entry>0x201b</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YUYV10-1X20">
              <entry>MEDIA_BUS_FMT_YUYV10_1X20</entry>
              <entry>0x200d</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YVYU10-1X20">
              <entry>MEDIA_BUS_FMT_YVYU10_1X20</entry>
              <entry>0x200e</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-VUY8-1X24">
              <entry>MEDIA_BUS_FMT_VUY8_1X24</entry>
              <entry>0x201a</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YUV8-1X24">
              <entry>MEDIA_BUS_FMT_YUV8_1X24</entry>
              <entry>0x2025</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>-</entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-UYVY12-1X24">
              <entry>MEDIA_BUS_FMT_UYVY12_1X24</entry>
              <entry>0x2020</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>11</subscript></entry>
              <entry>u<subscript>10</subscript></entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>11</subscript></entry>
              <entry>v<subscript>10</subscript></entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-VYUY12-1X24">
              <entry>MEDIA_BUS_FMT_VYUY12_1X24</entry>
              <entry>0x2021</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>v<subscript>11</subscript></entry>
              <entry>v<subscript>10</subscript></entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>u<subscript>11</subscript></entry>
              <entry>u<subscript>10</subscript></entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YUYV12-1X24">
              <entry>MEDIA_BUS_FMT_YUYV12_1X24</entry>
              <entry>0x2022</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>u<subscript>11</subscript></entry>
              <entry>u<subscript>10</subscript></entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>v<subscript>11</subscript></entry>
              <entry>v<subscript>10</subscript></entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YVYU12-1X24">
              <entry>MEDIA_BUS_FMT_YVYU12_1X24</entry>
              <entry>0x2023</entry>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>v<subscript>11</subscript></entry>
              <entry>v<subscript>10</subscript></entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry/>
              <entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry><entry>-</entry>
              <entry>y<subscript>11</subscript></entry>
              <entry>y<subscript>10</subscript></entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>u<subscript>11</subscript></entry>
              <entry>u<subscript>10</subscript></entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-YUV10-1X30">
              <entry>MEDIA_BUS_FMT_YUV10_1X30</entry>
              <entry>0x2016</entry>
              <entry/>
              <entry>-</entry>
              <entry>-</entry>
              <entry>y<subscript>9</subscript></entry>
              <entry>y<subscript>8</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>u<subscript>9</subscript></entry>
              <entry>u<subscript>8</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
              <entry>v<subscript>9</subscript></entry>
              <entry>v<subscript>8</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
            <row id="MEDIA-BUS-FMT-AYUV8-1X32">
              <entry>MEDIA_BUS_FMT_AYUV8_1X32</entry>
              <entry>0x2017</entry>
              <entry/>
              <entry>a<subscript>7</subscript></entry>
              <entry>a<subscript>6</subscript></entry>
              <entry>a<subscript>5</subscript></entry>
              <entry>a<subscript>4</subscript></entry>
              <entry>a<subscript>3</subscript></entry>
              <entry>a<subscript>2</subscript></entry>
              <entry>a<subscript>1</subscript></entry>
              <entry>a<subscript>0</subscript></entry>
              <entry>y<subscript>7</subscript></entry>
              <entry>y<subscript>6</subscript></entry>
              <entry>y<subscript>5</subscript></entry>
              <entry>y<subscript>4</subscript></entry>
              <entry>y<subscript>3</subscript></entry>
              <entry>y<subscript>2</subscript></entry>
              <entry>y<subscript>1</subscript></entry>
              <entry>y<subscript>0</subscript></entry>
              <entry>u<subscript>7</subscript></entry>
              <entry>u<subscript>6</subscript></entry>
              <entry>u<subscript>5</subscript></entry>
              <entry>u<subscript>4</subscript></entry>
              <entry>u<subscript>3</subscript></entry>
              <entry>u<subscript>2</subscript></entry>
              <entry>u<subscript>1</subscript></entry>
              <entry>u<subscript>0</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
          </tbody>
        </tgroup>
          </table>



HSV/HSL Formats
===============

Those formats transfer pixel data as RGB values in a cylindrical-coordinate system using Hue-Saturation-Value or Hue-Saturation-Lightness components. The format code is made of the
following information.

-  The hue, saturation, value or lightness and optional alpha components order code, as encoded in a pixel sample. The only currently supported value is AHSV.

-  The number of bits per component, for each component. The values can be different for all components. The only currently supported value is 8888.

-  The number of bus samples per pixel. Pixels that are wider than the bus width must be transferred in multiple samples. The only currently supported value is 1.

-  The bus width.

-  For formats where the total number of bits per pixel is smaller than the number of bus samples per pixel times the bus width, a padding value stating if the bytes are padded in
   their most high order bits (PADHI) or low order bits (PADLO).

-  For formats where the number of bus samples per pixel is larger than 1, an endianness value stating if the pixel is transferred MSB first (BE) or LSB first (LE).

The following table lists existing HSV/HSL formats.


.. _v4l2-mbus-pixelcode-hsv:

HSV/HSL formats
===============

::

    TODO ... 


    <table pgwide="0" frame="none" id="v4l2-mbus-pixelcode-hsv">
        <title>HSV/HSL formats</title>
        <tgroup cols="27">
          <colspec colname="id" align="left"/>
          <colspec colname="code" align="center"/>
          <colspec colname="bit"/>
          <colspec colnum="4" colname="b31" align="center"/>
          <colspec colnum="5" colname="b20" align="center"/>
          <colspec colnum="6" colname="b29" align="center"/>
          <colspec colnum="7" colname="b28" align="center"/>
          <colspec colnum="8" colname="b27" align="center"/>
          <colspec colnum="9" colname="b26" align="center"/>
          <colspec colnum="10" colname="b25" align="center"/>
          <colspec colnum="11" colname="b24" align="center"/>
          <colspec colnum="12" colname="b23" align="center"/>
          <colspec colnum="13" colname="b22" align="center"/>
          <colspec colnum="14" colname="b21" align="center"/>
          <colspec colnum="15" colname="b20" align="center"/>
          <colspec colnum="16" colname="b19" align="center"/>
          <colspec colnum="17" colname="b18" align="center"/>
          <colspec colnum="18" colname="b17" align="center"/>
          <colspec colnum="19" colname="b16" align="center"/>
          <colspec colnum="20" colname="b15" align="center"/>
          <colspec colnum="21" colname="b14" align="center"/>
          <colspec colnum="22" colname="b13" align="center"/>
          <colspec colnum="23" colname="b12" align="center"/>
          <colspec colnum="24" colname="b11" align="center"/>
          <colspec colnum="25" colname="b10" align="center"/>
          <colspec colnum="26" colname="b09" align="center"/>
          <colspec colnum="27" colname="b08" align="center"/>
          <colspec colnum="28" colname="b07" align="center"/>
          <colspec colnum="29" colname="b06" align="center"/>
          <colspec colnum="30" colname="b05" align="center"/>
          <colspec colnum="31" colname="b04" align="center"/>
          <colspec colnum="32" colname="b03" align="center"/>
          <colspec colnum="33" colname="b02" align="center"/>
          <colspec colnum="34" colname="b01" align="center"/>
          <colspec colnum="35" colname="b00" align="center"/>
          <spanspec namest="b31" nameend="b00" spanname="b0"/>
          <thead>
            <row>
              <entry>Identifier</entry>
              <entry>Code</entry>
              <entry/>
              <entry spanname="b0">Data organization</entry>
            </row>
            <row>
              <entry/>
              <entry/>
              <entry>Bit</entry>
              <entry>31</entry>
              <entry>30</entry>
              <entry>29</entry>
              <entry>28</entry>
              <entry>27</entry>
              <entry>26</entry>
              <entry>25</entry>
              <entry>24</entry>
              <entry>23</entry>
              <entry>22</entry>
              <entry>21</entry>
              <entry>20</entry>
              <entry>19</entry>
              <entry>18</entry>
              <entry>17</entry>
              <entry>16</entry>
              <entry>15</entry>
              <entry>14</entry>
              <entry>13</entry>
              <entry>12</entry>
              <entry>11</entry>
              <entry>10</entry>
              <entry>9</entry>
              <entry>8</entry>
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
            <row id="MEDIA-BUS-FMT-AHSV8888-1X32">
              <entry>MEDIA_BUS_FMT_AHSV8888_1X32</entry>
              <entry>0x6001</entry>
              <entry/>
              <entry>a<subscript>7</subscript></entry>
              <entry>a<subscript>6</subscript></entry>
              <entry>a<subscript>5</subscript></entry>
              <entry>a<subscript>4</subscript></entry>
              <entry>a<subscript>3</subscript></entry>
              <entry>a<subscript>2</subscript></entry>
              <entry>a<subscript>1</subscript></entry>
              <entry>a<subscript>0</subscript></entry>
              <entry>h<subscript>7</subscript></entry>
              <entry>h<subscript>6</subscript></entry>
              <entry>h<subscript>5</subscript></entry>
              <entry>h<subscript>4</subscript></entry>
              <entry>h<subscript>3</subscript></entry>
              <entry>h<subscript>2</subscript></entry>
              <entry>h<subscript>1</subscript></entry>
              <entry>h<subscript>0</subscript></entry>
              <entry>s<subscript>7</subscript></entry>
              <entry>s<subscript>6</subscript></entry>
              <entry>s<subscript>5</subscript></entry>
              <entry>s<subscript>4</subscript></entry>
              <entry>s<subscript>3</subscript></entry>
              <entry>s<subscript>2</subscript></entry>
              <entry>s<subscript>1</subscript></entry>
              <entry>s<subscript>0</subscript></entry>
              <entry>v<subscript>7</subscript></entry>
              <entry>v<subscript>6</subscript></entry>
              <entry>v<subscript>5</subscript></entry>
              <entry>v<subscript>4</subscript></entry>
              <entry>v<subscript>3</subscript></entry>
              <entry>v<subscript>2</subscript></entry>
              <entry>v<subscript>1</subscript></entry>
              <entry>v<subscript>0</subscript></entry>
            </row>
          </tbody>
        </tgroup>
          </table>



JPEG Compressed Formats
=======================

Those data formats consist of an ordered sequence of 8-bit bytes obtained from JPEG compression process. Additionally to the ``_JPEG`` postfix the format code is made of the
following information.

-  The number of bus samples per entropy encoded byte.

-  The bus width.

For instance, for a JPEG baseline process and an 8-bit bus width the format will be named ``MEDIA_BUS_FMT_JPEG_1X8``.

The following table lists existing JPEG compressed formats.


.. _v4l2-mbus-pixelcode-jpeg:

.. table:: JPEG Formats

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Identifier                                    | Code                                          | Remarks                                                                                    |
    +===============================================+===============================================+============================================================================================+
    | MEDIA_BUS_FMT_JPEG_1X8                        | 0x4001                                        | Besides of its usage for the parallel bus this format is recommended for transmission of   |
    |                                               |                                               | JPEG data over MIPI CSI bus using the User Defined 8-bit Data types.                       |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+



.. _v4l2-mbus-vendor-spec-fmts:

Vendor and Device Specific Formats
==================================

    **Note**

    This is an :ref:`experimental <experimental>` interface and may change in the future.

This section lists complex data formats that are either vendor or device specific.

The following table lists the existing vendor and device specific formats.


.. _v4l2-mbus-pixelcode-vendor-specific:

.. table:: Vendor and device specific formats

    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+
    | Identifier                                    | Code                                          | Comments                                                                                   |
    +===============================================+===============================================+============================================================================================+
    | MEDIA_BUS_FMT_S5C_UYVY_JPEG_1X8               | 0x5001                                        | Interleaved raw UYVY and JPEG image format with embedded meta-data used by Samsung S3C73MX |
    |                                               |                                               | camera sensors.                                                                            |
    +-----------------------------------------------+-----------------------------------------------+--------------------------------------------------------------------------------------------+


