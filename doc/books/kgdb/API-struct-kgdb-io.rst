.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-kgdb-io:

==============
struct kgdb_io
==============

*man struct kgdb_io(9)*

*4.6.0-rc5*

Describe the interface for an I/O driver to talk with KGDB.


Synopsis
========

.. code-block:: c

    struct kgdb_io {
      const char * name;
      int (* read_char) (void);
      void (* write_char) (u8);
      void (* flush) (void);
      int (* init) (void);
      void (* pre_exception) (void);
      void (* post_exception) (void);
      int is_console;
    };


Members
=======

name
    Name of the I/O driver.

read_char
    Pointer to a function that will return one char.

write_char
    Pointer to a function that will write one char.

flush
    Pointer to a function that will flush any pending writes.

init
    Pointer to a function that will initialize the device.

pre_exception
    Pointer to a function that will do any prep work for the I/O driver.

post_exception
    Pointer to a function that will do any cleanup work for the I/O
    driver.

is_console
    1 if the end device is a console 0 if the I/O device is not a
    console


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
