.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/kgdb_nmi.c

.. _`kgdb_nmi_poll_knock`:

kgdb_nmi_poll_knock
===================

.. c:function:: bool kgdb_nmi_poll_knock( void)

    Check if it is time to enter the debugger

    :param  void:
        no arguments

.. _`kgdb_nmi_poll_knock.description`:

Description
-----------

"Serial ports are often noisy, especially when muxed over another port (we
often use serial over the headset connector). Noise on the async command
line just causes characters that are ignored, on a command line that blocked
execution noise would be catastrophic." -- Colin Cross

So, this function implements KGDB/KDB knocking on the serial line: we won't
enter the debugger until we receive a known magic phrase (which is actually
"$3#33", known as "escape to KDB" command. There is also a relaxed variant
of knocking, i.e. just pressing the return key is enough to enter the
debugger. And if knocking is disabled, the function always returns 1.

.. This file was automatic generated / don't edit.

