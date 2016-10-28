.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/img-ir/img-ir-raw.h

.. _`img_ir_priv_raw`:

struct img_ir_priv_raw
======================

.. c:type:: struct img_ir_priv_raw

    Private driver data for raw decoder.

.. _`img_ir_priv_raw.definition`:

Definition
----------

.. code-block:: c

    struct img_ir_priv_raw {
        struct rc_dev *rdev;
        struct timer_list timer;
        u32 last_status;
    }

.. _`img_ir_priv_raw.members`:

Members
-------

rdev
    Raw remote control device

timer
    Timer to echo samples to keep soft decoders happy.

last_status
    Last raw status bits.

.. This file was automatic generated / don't edit.

