.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/pciehp_ctrl.c

.. _`board_added`:

board_added
===========

.. c:function:: int board_added(struct controller *ctrl)

    Called after a board has been added to the system.

    :param ctrl:
        PCIe hotplug controller where board is added
    :type ctrl: struct controller \*

.. _`board_added.description`:

Description
-----------

Turns power on for the board.
Configures board.

.. _`remove_board`:

remove_board
============

.. c:function:: void remove_board(struct controller *ctrl, bool safe_removal)

    Turns off slot and LEDs

    :param ctrl:
        PCIe hotplug controller where board is being removed
    :type ctrl: struct controller \*

    :param safe_removal:
        whether the board is safely removed (versus surprise removed)
    :type safe_removal: bool

.. This file was automatic generated / don't edit.

