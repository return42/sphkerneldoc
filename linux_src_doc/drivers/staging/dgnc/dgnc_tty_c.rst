.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/dgnc/dgnc_tty.c

.. _`dgnc_tty_register`:

dgnc_tty_register
=================

.. c:function:: int dgnc_tty_register(struct dgnc_board *brd)

    Init the tty subsystem for this board.

    :param struct dgnc_board \*brd:
        *undescribed*

.. _`dgnc_tty_init`:

dgnc_tty_init
=============

.. c:function:: int dgnc_tty_init(struct dgnc_board *brd)

    Initialize the tty subsystem.

    :param struct dgnc_board \*brd:
        *undescribed*

.. _`dgnc_tty_init.description`:

Description
-----------

Called once per board after board has been downloaded and initialized.

.. _`dgnc_cleanup_tty`:

dgnc_cleanup_tty
================

.. c:function:: void dgnc_cleanup_tty(struct dgnc_board *brd)

    Cleanup driver.

    :param struct dgnc_board \*brd:
        *undescribed*

.. _`dgnc_cleanup_tty.description`:

Description
-----------

Uninitialize the TTY portion of this driver.  Free all memory and
resources.

.. _`dgnc_wmove`:

dgnc_wmove
==========

.. c:function:: void dgnc_wmove(struct channel_t *ch, char *buf, uint n)

    Write data to transmit queue.

    :param struct channel_t \*ch:
        Pointer to channel structure.

    :param char \*buf:
        Pointer to characters to be moved.

    :param uint n:
        Number of characters to move.

.. _`dgnc_input`:

dgnc_input
==========

.. c:function:: void dgnc_input(struct channel_t *ch)

    Process received data.

    :param struct channel_t \*ch:
        Pointer to channel structure.

.. _`dgnc_carrier`:

dgnc_carrier
============

.. c:function:: void dgnc_carrier(struct channel_t *ch)

    :param struct channel_t \*ch:
        *undescribed*

.. _`dgnc_carrier.description`:

Description
-----------

Determines when CARRIER changes state and takes appropriate
action.

.. This file was automatic generated / don't edit.

