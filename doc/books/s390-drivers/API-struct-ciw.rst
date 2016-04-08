
.. _API-struct-ciw:

==========
struct ciw
==========

*man struct ciw(9)*

*4.6.0-rc1*

command information word (CIW) layout


Synopsis
========

.. code-block:: c

    struct ciw {
      __u32 et:2;
      __u32 reserved:2;
      __u32 ct:4;
      __u32 cmd:8;
      __u32 count:16;
    };


Members
=======

et
    entry type

reserved
    reserved bits

ct
    command type

cmd
    command code

count
    command count
