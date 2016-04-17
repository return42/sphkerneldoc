.. -*- coding: utf-8; mode: rst -*-

===========
ti-msgmgr.h
===========


.. _`ti_msgmgr_message`:

struct ti_msgmgr_message
========================

.. c:type:: ti_msgmgr_message

    Message Manager structure


.. _`ti_msgmgr_message.definition`:

Definition
----------

.. code-block:: c

  struct ti_msgmgr_message {
    size_t len;
    u8 * buf;
  };


.. _`ti_msgmgr_message.members`:

Members
-------

:``len``:
    Length of data in the Buffer

:``buf``:
    Buffer pointer




.. _`ti_msgmgr_message.description`:

Description
-----------

This is the structure for data used in mbox_send_message
the length of data buffer used depends on the SoC integration
parameters - each message may be 64, 128 bytes long depending
on SoC. Client is supposed to be aware of this.

