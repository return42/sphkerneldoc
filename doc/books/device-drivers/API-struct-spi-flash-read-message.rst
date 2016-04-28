.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-spi-flash-read-message:

=============================
struct spi_flash_read_message
=============================

*man struct spi_flash_read_message(9)*

*4.6.0-rc5*

flash specific information for spi-masters that provide accelerated
flash read interfaces


Synopsis
========

.. code-block:: c

    struct spi_flash_read_message {
      void * buf;
      loff_t from;
      size_t len;
      size_t retlen;
      u8 read_opcode;
      u8 addr_width;
      u8 dummy_bytes;
      u8 opcode_nbits;
      u8 addr_nbits;
      u8 data_nbits;
    };


Members
=======

buf
    buffer to read data

from
    offset within the flash from where data is to be read

len
    length of data to be read

retlen
    actual length of data read

read_opcode
    read_opcode to be used to communicate with flash

addr_width
    number of address bytes

dummy_bytes
    number of dummy bytes

opcode_nbits
    number of lines to send opcode

addr_nbits
    number of lines to send address

data_nbits
    number of lines for data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
