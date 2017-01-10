.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/sdio_uart.c

.. _`uart_dtr_rts`:

uart_dtr_rts
============

.. c:function:: void uart_dtr_rts(struct tty_port *tport, int onoff)

    port helper to set uart signals

    :param struct tty_port \*tport:
        tty port to be updated

    :param int onoff:
        set to turn on DTR/RTS

.. _`uart_dtr_rts.description`:

Description
-----------

Called by the tty port helpers when the modem signals need to be
adjusted during an open, close and hangup.

.. _`sdio_uart_activate`:

sdio_uart_activate
==================

.. c:function:: int sdio_uart_activate(struct tty_port *tport, struct tty_struct *tty)

    start up hardware

    :param struct tty_port \*tport:
        tty port to activate

    :param struct tty_struct \*tty:
        tty bound to this port

.. _`sdio_uart_activate.description`:

Description
-----------

Activate a tty port. The port locking guarantees us this will be
run exactly once per set of opens, and if successful will see the
shutdown method run exactly once to match. Start up and shutdown are
protected from each other by the internal locking and will not run
at the same time even during a hangup event.

If we successfully start up the port we take an extra kref as we
will keep it around until shutdown when the kref is dropped.

.. _`sdio_uart_shutdown`:

sdio_uart_shutdown
==================

.. c:function:: void sdio_uart_shutdown(struct tty_port *tport)

    stop hardware

    :param struct tty_port \*tport:
        tty port to shut down

.. _`sdio_uart_shutdown.description`:

Description
-----------

Deactivate a tty port. The port locking guarantees us this will be
run only if a successful matching activate already ran. The two are
protected from each other by the internal locking and will not run
at the same time even during a hangup event.

.. _`sdio_uart_install`:

sdio_uart_install
=================

.. c:function:: int sdio_uart_install(struct tty_driver *driver, struct tty_struct *tty)

    install method

    :param struct tty_driver \*driver:
        the driver in use (sdio_uart in our case)

    :param struct tty_struct \*tty:
        the tty being bound

.. _`sdio_uart_install.description`:

Description
-----------

Look up and bind the tty and the driver together. Initialize
any needed private data (in our case the termios)

.. _`sdio_uart_cleanup`:

sdio_uart_cleanup
=================

.. c:function:: void sdio_uart_cleanup(struct tty_struct *tty)

    called on the last tty kref drop

    :param struct tty_struct \*tty:
        the tty being destroyed

.. _`sdio_uart_cleanup.description`:

Description
-----------

Called asynchronously when the last reference to the tty is dropped.
We cannot destroy the tty->driver_data port kref until this point

.. This file was automatic generated / don't edit.

