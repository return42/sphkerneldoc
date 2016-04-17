
.. _pixfmt-indexed:

Indexed Format
==============

::

    TODO ... 


    <chapter id="pixfmt-indexed" chunkNode="1">
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
      </chapter>




