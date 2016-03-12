.. -*- coding: utf-8; mode: rst -*-

============
img-ir-raw.h
============



.. _xref_struct_img_ir_priv_raw:

struct img_ir_priv_raw
======================

.. c:type:: struct img_ir_priv_raw

    Private driver data for raw decoder.



Definition
----------

.. code-block:: c

  struct img_ir_priv_raw {
    struct rc_dev * rdev;
    struct timer_list timer;
    u32 last_status;
  };



Members
-------

:``struct rc_dev * rdev``:
    Raw remote control device

:``struct timer_list timer``:
    Timer to echo samples to keep soft decoders happy.

:``u32 last_status``:
    Last raw status bits.



