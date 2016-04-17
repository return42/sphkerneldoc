
.. _packed-rgb:

==================
Packed RGB formats
==================

*man Packed RGB formats(2)*

Packed RGB formats


Description
===========

These formats are designed to match the pixel formats of typical PC graphics frame buffers. They occupy 8, 16, 24 or 32 bits per pixel. These are all packed-pixel formats, meaning
all the data for a pixel lie next to each other in memory.


.. _rgb-formats:

Packed RGB Image Formats
========================

::

    TODO ... 


    <table pgwide="1" frame="none" id="rgb-formats">
          <title>Packed RGB Image Formats</title>
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

        <colspec colnum="13" colname="b17" align="center"/>
        <colspec colnum="14" colname="b16" align="center"/>
        <colspec colnum="15" colname="b15" align="center"/>
        <colspec colnum="16" colname="b14" align="center"/>
        <colspec colnum="17" colname="b13" align="center"/>
        <colspec colnum="18" colname="b12" align="center"/>
        <colspec colnum="19" colname="b11" align="center"/>
        <colspec colnum="20" colname="b10" align="center"/>

        <colspec colnum="22" colname="b27" align="center"/>
        <colspec colnum="23" colname="b26" align="center"/>
        <colspec colnum="24" colname="b25" align="center"/>
        <colspec colnum="25" colname="b24" align="center"/>
        <colspec colnum="26" colname="b23" align="center"/>
        <colspec colnum="27" colname="b22" align="center"/>
        <colspec colnum="28" colname="b21" align="center"/>
        <colspec colnum="29" colname="b20" align="center"/>

        <colspec colnum="31" colname="b37" align="center"/>
        <colspec colnum="32" colname="b36" align="center"/>
        <colspec colnum="33" colname="b35" align="center"/>
        <colspec colnum="34" colname="b34" align="center"/>
        <colspec colnum="35" colname="b33" align="center"/>
        <colspec colnum="36" colname="b32" align="center"/>
        <colspec colnum="37" colname="b31" align="center"/>
        <colspec colnum="38" colname="b30" align="center"/>

        <spanspec namest="b07" nameend="b00" spanname="b0"/>
        <spanspec namest="b17" nameend="b10" spanname="b1"/>
        <spanspec namest="b27" nameend="b20" spanname="b2"/>
        <spanspec namest="b37" nameend="b30" spanname="b3"/>
        <thead>
          <row>
            <entry>Identifier</entry>
            <entry>Code</entry>
            <entry> </entry>
            <entry spanname="b0">Byte 0 in memory</entry>
            <entry spanname="b1">Byte 1</entry>
            <entry spanname="b2">Byte 2</entry>
            <entry spanname="b3">Byte 3</entry>
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
            <entry> </entry>
            <entry>7</entry>
            <entry>6</entry>
            <entry>5</entry>
            <entry>4</entry>
            <entry>3</entry>
            <entry>2</entry>
            <entry>1</entry>
            <entry>0</entry>
            <entry> </entry>
            <entry>7</entry>
            <entry>6</entry>
            <entry>5</entry>
            <entry>4</entry>
            <entry>3</entry>
            <entry>2</entry>
            <entry>1</entry>
            <entry>0</entry>
            <entry> </entry>
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
          <row id="V4L2-PIX-FMT-RGB332">
            <entry><constant>V4L2_PIX_FMT_RGB332</constant></entry>
            <entry>'RGB1'</entry>
            <entry/>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-ARGB444">
            <entry><constant>V4L2_PIX_FMT_ARGB444</constant></entry>
            <entry>'AR12'</entry>
            <entry/>
            <entry>g<subscript>3</subscript></entry>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
            <entry/>
            <entry>a<subscript>3</subscript></entry>
            <entry>a<subscript>2</subscript></entry>
            <entry>a<subscript>1</subscript></entry>
            <entry>a<subscript>0</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-XRGB444">
            <entry><constant>V4L2_PIX_FMT_XRGB444</constant></entry>
            <entry>'XR12'</entry>
            <entry/>
            <entry>g<subscript>3</subscript></entry>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
            <entry/>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-ARGB555">
            <entry><constant>V4L2_PIX_FMT_ARGB555</constant></entry>
            <entry>'AR15'</entry>
            <entry/>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
            <entry/>
            <entry>a</entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-XRGB555">
            <entry><constant>V4L2_PIX_FMT_XRGB555</constant></entry>
            <entry>'XR15'</entry>
            <entry/>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
            <entry/>
            <entry>-</entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-RGB565">
            <entry><constant>V4L2_PIX_FMT_RGB565</constant></entry>
            <entry>'RGBP'</entry>
            <entry/>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
            <entry/>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry>g<subscript>5</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-ARGB555X">
            <entry><constant>V4L2_PIX_FMT_ARGB555X</constant></entry>
            <entry>'AR15' | (1 &lt;&lt; 31)</entry>
            <entry/>
            <entry>a</entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
            <entry/>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-XRGB555X">
            <entry><constant>V4L2_PIX_FMT_XRGB555X</constant></entry>
            <entry>'XR15' | (1 &lt;&lt; 31)</entry>
            <entry/>
            <entry>-</entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
            <entry/>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-RGB565X">
            <entry><constant>V4L2_PIX_FMT_RGB565X</constant></entry>
            <entry>'RGBR'</entry>
            <entry/>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry>g<subscript>5</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
            <entry/>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-BGR24">
            <entry><constant>V4L2_PIX_FMT_BGR24</constant></entry>
            <entry>'BGR3'</entry>
            <entry/>
            <entry>b<subscript>7</subscript></entry>
            <entry>b<subscript>6</subscript></entry>
            <entry>b<subscript>5</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
            <entry/>
            <entry>g<subscript>7</subscript></entry>
            <entry>g<subscript>6</subscript></entry>
            <entry>g<subscript>5</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry/>
            <entry>r<subscript>7</subscript></entry>
            <entry>r<subscript>6</subscript></entry>
            <entry>r<subscript>5</subscript></entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-RGB24">
            <entry><constant>V4L2_PIX_FMT_RGB24</constant></entry>
            <entry>'RGB3'</entry>
            <entry/>
            <entry>r<subscript>7</subscript></entry>
            <entry>r<subscript>6</subscript></entry>
            <entry>r<subscript>5</subscript></entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry/>
            <entry>g<subscript>7</subscript></entry>
            <entry>g<subscript>6</subscript></entry>
            <entry>g<subscript>5</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry/>
            <entry>b<subscript>7</subscript></entry>
            <entry>b<subscript>6</subscript></entry>
            <entry>b<subscript>5</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-BGR666">
            <entry><constant>V4L2_PIX_FMT_BGR666</constant></entry>
            <entry>'BGRH'</entry>
            <entry/>
            <entry>b<subscript>5</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
            <entry>g<subscript>5</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry/>
            <entry>g<subscript>3</subscript></entry>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry>r<subscript>5</subscript></entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry/>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry/>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
          </row>
          <row id="V4L2-PIX-FMT-ABGR32">
            <entry><constant>V4L2_PIX_FMT_ABGR32</constant></entry>
            <entry>'AR24'</entry>
            <entry/>
            <entry>b<subscript>7</subscript></entry>
            <entry>b<subscript>6</subscript></entry>
            <entry>b<subscript>5</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
            <entry/>
            <entry>g<subscript>7</subscript></entry>
            <entry>g<subscript>6</subscript></entry>
            <entry>g<subscript>5</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry/>
            <entry>r<subscript>7</subscript></entry>
            <entry>r<subscript>6</subscript></entry>
            <entry>r<subscript>5</subscript></entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry/>
            <entry>a<subscript>7</subscript></entry>
            <entry>a<subscript>6</subscript></entry>
            <entry>a<subscript>5</subscript></entry>
            <entry>a<subscript>4</subscript></entry>
            <entry>a<subscript>3</subscript></entry>
            <entry>a<subscript>2</subscript></entry>
            <entry>a<subscript>1</subscript></entry>
            <entry>a<subscript>0</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-XBGR32">
            <entry><constant>V4L2_PIX_FMT_XBGR32</constant></entry>
            <entry>'XR24'</entry>
            <entry/>
            <entry>b<subscript>7</subscript></entry>
            <entry>b<subscript>6</subscript></entry>
            <entry>b<subscript>5</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
            <entry/>
            <entry>g<subscript>7</subscript></entry>
            <entry>g<subscript>6</subscript></entry>
            <entry>g<subscript>5</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry/>
            <entry>r<subscript>7</subscript></entry>
            <entry>r<subscript>6</subscript></entry>
            <entry>r<subscript>5</subscript></entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry/>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
          </row>
          <row id="V4L2-PIX-FMT-ARGB32">
            <entry><constant>V4L2_PIX_FMT_ARGB32</constant></entry>
            <entry>'BA24'</entry>
            <entry/>
            <entry>a<subscript>7</subscript></entry>
            <entry>a<subscript>6</subscript></entry>
            <entry>a<subscript>5</subscript></entry>
            <entry>a<subscript>4</subscript></entry>
            <entry>a<subscript>3</subscript></entry>
            <entry>a<subscript>2</subscript></entry>
            <entry>a<subscript>1</subscript></entry>
            <entry>a<subscript>0</subscript></entry>
            <entry/>
            <entry>r<subscript>7</subscript></entry>
            <entry>r<subscript>6</subscript></entry>
            <entry>r<subscript>5</subscript></entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry/>
            <entry>g<subscript>7</subscript></entry>
            <entry>g<subscript>6</subscript></entry>
            <entry>g<subscript>5</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry/>
            <entry>b<subscript>7</subscript></entry>
            <entry>b<subscript>6</subscript></entry>
            <entry>b<subscript>5</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-XRGB32">
            <entry><constant>V4L2_PIX_FMT_XRGB32</constant></entry>
            <entry>'BX24'</entry>
            <entry/>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry>-</entry>
            <entry/>
            <entry>r<subscript>7</subscript></entry>
            <entry>r<subscript>6</subscript></entry>
            <entry>r<subscript>5</subscript></entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry/>
            <entry>g<subscript>7</subscript></entry>
            <entry>g<subscript>6</subscript></entry>
            <entry>g<subscript>5</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry/>
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



Bit 7 is the most significant bit.

The usage and value of the alpha bits (a) in the ARGB and ABGR formats (collectively referred to as alpha formats) depend on the device type and hardware operation.
:ref:`Capture <capture>` devices (including capture queues of mem-to-mem devices) fill the alpha component in memory. When the device outputs an alpha channel the alpha component
will have a meaningful value. Otherwise, when the device doesn't output an alpha channel but can set the alpha bit to a user-configurable value, the
:ref:`V4L2_CID_ALPHA_COMPONENT <v4l2-alpha-component>` control is used to specify that alpha value, and the alpha component of all pixels will be set to the value specified by
that control. Otherwise a corresponding format without an alpha component (XRGB or XBGR) must be used instead of an alpha format.

:ref:`Output <output>` devices (including output queues of mem-to-mem devices and :ref:`video output overlay <osd>` devices) read the alpha component from memory. When the
device processes the alpha channel the alpha component must be filled with meaningful values by applications. Otherwise a corresponding format without an alpha component (XRGB or
XBGR) must be used instead of an alpha format.

The XRGB and XBGR formats contain undefined bits (-). Applications, devices and drivers must ignore those bits, for both :ref:`capture <capture>` and :ref:`output <output>`
devices.

**Byte Order..**

Each cell is one byte.



.. table::

    +---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
    | start + 0:    | B\ :sub:`00`  | G\ :sub:`00`  | R\ :sub:`00`  | B\ :sub:`01`  | G\ :sub:`01`  | R\ :sub:`01`  | B\ :sub:`02`  | G\ :sub:`02`  | R\ :sub:`02`  | B\ :sub:`03`  | G\ :sub:`03`  | R\ :sub:`03`  |
    +---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
    | start + 12:   | B\ :sub:`10`  | G\ :sub:`10`  | R\ :sub:`10`  | B\ :sub:`11`  | G\ :sub:`11`  | R\ :sub:`11`  | B\ :sub:`12`  | G\ :sub:`12`  | R\ :sub:`12`  | B\ :sub:`13`  | G\ :sub:`13`  | R\ :sub:`13`  |
    +---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
    | start + 24:   | B\ :sub:`20`  | G\ :sub:`20`  | R\ :sub:`20`  | B\ :sub:`21`  | G\ :sub:`21`  | R\ :sub:`21`  | B\ :sub:`22`  | G\ :sub:`22`  | R\ :sub:`22`  | B\ :sub:`23`  | G\ :sub:`23`  | R\ :sub:`23`  |
    +---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
    | start + 36:   | B\ :sub:`30`  | G\ :sub:`30`  | R\ :sub:`30`  | B\ :sub:`31`  | G\ :sub:`31`  | R\ :sub:`31`  | B\ :sub:`32`  | G\ :sub:`32`  | R\ :sub:`32`  | B\ :sub:`33`  | G\ :sub:`33`  | R\ :sub:`33`  |
    +---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+


Formats defined in :ref:`rgb-formats-deprecated` are deprecated and must not be used by new drivers. They are documented here for reference. The meaning of their alpha bits (a)
is ill-defined and interpreted as in either the corresponding ARGB or XRGB format, depending on the driver.


.. _rgb-formats-deprecated:

Deprecated Packed RGB Image Formats
===================================

::

    TODO ... 


    <table pgwide="1" frame="none" id="rgb-formats-deprecated">
          <title>Deprecated Packed RGB Image Formats</title>
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

        <colspec colnum="13" colname="b17" align="center"/>
        <colspec colnum="14" colname="b16" align="center"/>
        <colspec colnum="15" colname="b15" align="center"/>
        <colspec colnum="16" colname="b14" align="center"/>
        <colspec colnum="17" colname="b13" align="center"/>
        <colspec colnum="18" colname="b12" align="center"/>
        <colspec colnum="19" colname="b11" align="center"/>
        <colspec colnum="20" colname="b10" align="center"/>

        <colspec colnum="22" colname="b27" align="center"/>
        <colspec colnum="23" colname="b26" align="center"/>
        <colspec colnum="24" colname="b25" align="center"/>
        <colspec colnum="25" colname="b24" align="center"/>
        <colspec colnum="26" colname="b23" align="center"/>
        <colspec colnum="27" colname="b22" align="center"/>
        <colspec colnum="28" colname="b21" align="center"/>
        <colspec colnum="29" colname="b20" align="center"/>

        <colspec colnum="31" colname="b37" align="center"/>
        <colspec colnum="32" colname="b36" align="center"/>
        <colspec colnum="33" colname="b35" align="center"/>
        <colspec colnum="34" colname="b34" align="center"/>
        <colspec colnum="35" colname="b33" align="center"/>
        <colspec colnum="36" colname="b32" align="center"/>
        <colspec colnum="37" colname="b31" align="center"/>
        <colspec colnum="38" colname="b30" align="center"/>

        <spanspec namest="b07" nameend="b00" spanname="b0"/>
        <spanspec namest="b17" nameend="b10" spanname="b1"/>
        <spanspec namest="b27" nameend="b20" spanname="b2"/>
        <spanspec namest="b37" nameend="b30" spanname="b3"/>
        <thead>
          <row>
            <entry>Identifier</entry>
            <entry>Code</entry>
            <entry> </entry>
            <entry spanname="b0">Byte 0 in memory</entry>
            <entry spanname="b1">Byte 1</entry>
            <entry spanname="b2">Byte 2</entry>
            <entry spanname="b3">Byte 3</entry>
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
            <entry> </entry>
            <entry>7</entry>
            <entry>6</entry>
            <entry>5</entry>
            <entry>4</entry>
            <entry>3</entry>
            <entry>2</entry>
            <entry>1</entry>
            <entry>0</entry>
            <entry> </entry>
            <entry>7</entry>
            <entry>6</entry>
            <entry>5</entry>
            <entry>4</entry>
            <entry>3</entry>
            <entry>2</entry>
            <entry>1</entry>
            <entry>0</entry>
            <entry> </entry>
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
        <tbody>
          <row id="V4L2-PIX-FMT-RGB444">
            <entry><constant>V4L2_PIX_FMT_RGB444</constant></entry>
            <entry>'R444'</entry>
            <entry/>
            <entry>g<subscript>3</subscript></entry>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
            <entry/>
            <entry>a<subscript>3</subscript></entry>
            <entry>a<subscript>2</subscript></entry>
            <entry>a<subscript>1</subscript></entry>
            <entry>a<subscript>0</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-RGB555">
            <entry><constant>V4L2_PIX_FMT_RGB555</constant></entry>
            <entry>'RGBO'</entry>
            <entry/>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
            <entry/>
            <entry>a</entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-RGB555X">
            <entry><constant>V4L2_PIX_FMT_RGB555X</constant></entry>
            <entry>'RGBQ'</entry>
            <entry/>
            <entry>a</entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
            <entry/>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-BGR32">
            <entry><constant>V4L2_PIX_FMT_BGR32</constant></entry>
            <entry>'BGR4'</entry>
            <entry/>
            <entry>b<subscript>7</subscript></entry>
            <entry>b<subscript>6</subscript></entry>
            <entry>b<subscript>5</subscript></entry>
            <entry>b<subscript>4</subscript></entry>
            <entry>b<subscript>3</subscript></entry>
            <entry>b<subscript>2</subscript></entry>
            <entry>b<subscript>1</subscript></entry>
            <entry>b<subscript>0</subscript></entry>
            <entry/>
            <entry>g<subscript>7</subscript></entry>
            <entry>g<subscript>6</subscript></entry>
            <entry>g<subscript>5</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry/>
            <entry>r<subscript>7</subscript></entry>
            <entry>r<subscript>6</subscript></entry>
            <entry>r<subscript>5</subscript></entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry/>
            <entry>a<subscript>7</subscript></entry>
            <entry>a<subscript>6</subscript></entry>
            <entry>a<subscript>5</subscript></entry>
            <entry>a<subscript>4</subscript></entry>
            <entry>a<subscript>3</subscript></entry>
            <entry>a<subscript>2</subscript></entry>
            <entry>a<subscript>1</subscript></entry>
            <entry>a<subscript>0</subscript></entry>
          </row>
          <row id="V4L2-PIX-FMT-RGB32">
            <entry><constant>V4L2_PIX_FMT_RGB32</constant></entry>
            <entry>'RGB4'</entry>
            <entry/>
            <entry>a<subscript>7</subscript></entry>
            <entry>a<subscript>6</subscript></entry>
            <entry>a<subscript>5</subscript></entry>
            <entry>a<subscript>4</subscript></entry>
            <entry>a<subscript>3</subscript></entry>
            <entry>a<subscript>2</subscript></entry>
            <entry>a<subscript>1</subscript></entry>
            <entry>a<subscript>0</subscript></entry>
            <entry/>
            <entry>r<subscript>7</subscript></entry>
            <entry>r<subscript>6</subscript></entry>
            <entry>r<subscript>5</subscript></entry>
            <entry>r<subscript>4</subscript></entry>
            <entry>r<subscript>3</subscript></entry>
            <entry>r<subscript>2</subscript></entry>
            <entry>r<subscript>1</subscript></entry>
            <entry>r<subscript>0</subscript></entry>
            <entry/>
            <entry>g<subscript>7</subscript></entry>
            <entry>g<subscript>6</subscript></entry>
            <entry>g<subscript>5</subscript></entry>
            <entry>g<subscript>4</subscript></entry>
            <entry>g<subscript>3</subscript></entry>
            <entry>g<subscript>2</subscript></entry>
            <entry>g<subscript>1</subscript></entry>
            <entry>g<subscript>0</subscript></entry>
            <entry/>
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



A test utility to determine which RGB formats a driver actually supports is available from the LinuxTV v4l-dvb repository. See
`https://linuxtv.org/repo/ <https://linuxtv.org/repo/>`__ for access instructions.
