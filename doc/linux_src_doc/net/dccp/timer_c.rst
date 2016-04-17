.. -*- coding: utf-8; mode: rst -*-

=======
timer.c
=======


.. _`dccp_write_xmitlet`:

dccp_write_xmitlet
==================

.. c:function:: void dccp_write_xmitlet (unsigned long data)

    Workhorse for CCID packet dequeueing interface See the comments above %ccid_dequeueing_decision for supported modes.

    :param unsigned long data:

        *undescribed*



.. _`dccp_timestamp`:

dccp_timestamp
==============

.. c:function:: u32 dccp_timestamp ( void)

    10s of microseconds time source Returns the number of 10s of microseconds since loading DCCP. This is native DCCP time difference format (RFC 4340, sec. 13).

    :param void:
        no arguments



.. _`dccp_timestamp.please-note`:

Please note
-----------

This will wrap around about circa every 11.9 hours.

