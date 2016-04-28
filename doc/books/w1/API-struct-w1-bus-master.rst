.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-w1-bus-master:

====================
struct w1_bus_master
====================

*man struct w1_bus_master(9)*

*4.6.0-rc5*

operations available on a bus master


Synopsis
========

.. code-block:: c

    struct w1_bus_master {
      void * data;
      u8 (* read_bit) (void *);
      void (* write_bit) (void *, u8);
      u8 (* touch_bit) (void *, u8);
      u8 (* read_byte) (void *);
      void (* write_byte) (void *, u8);
      u8 (* read_block) (void *, u8 *, int);
      void (* write_block) (void *, const u8 *, int);
      u8 (* triplet) (void *, u8);
      u8 (* reset_bus) (void *);
      u8 (* set_pullup) (void *, int);
      void (* search) (void *, struct w1_master *,u8, w1_slave_found_callback);
    };


Members
=======

data
    the first parameter in all the functions below

read_bit
    Sample the line level ``return`` the level read (0 or 1)

write_bit
    Sets the line level

touch_bit
    the lowest-level function for devices that really support the 1-wire
    protocol. touch_bit(0) = write-0 cycle touch_bit(1) = write-1 /
    read cycle ``return`` the bit read (0 or 1)

read_byte
    Reads a bytes. Same as 8 touch_bit(1) calls. ``return`` the byte
    read

write_byte
    Writes a byte. Same as 8 touch_bit(x) calls.

read_block
    Same as a series of ``read_byte`` calls ``return`` the number of
    bytes read

write_block
    Same as a series of ``write_byte`` calls

triplet
    Combines two reads and a smart write for ROM searches ``return``
    bit0=Id bit1=comp_id bit2=dir_taken

reset_bus
    long write-0 with a read for the presence pulse detection ``return``
    -1=Error, 0=Device present, 1=No device present

set_pullup
    Put out a strong pull-up pulse of the specified duration. ``return``
    -1=Error, 0=completed

search
    Really nice hardware can handles the different types of ROM search
    w1_master* is passed to the slave found callback. u8 is
    search_type, W1_SEARCH or W1_ALARM_SEARCH


Note
====

read_bit and write_bit are very low level functions and should only be
used with hardware that doesn't really support 1-wire operations, like a
parallel/serial port. Either define read_bit and write_bit OR define,
at minimum, touch_bit and reset_bus.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
