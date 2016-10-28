.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/shpchp_ctrl.c

.. _`board_added`:

board_added
===========

.. c:function:: int board_added(struct slot *p_slot)

    Called after a board has been added to the system.

    :param struct slot \*p_slot:
        target \ :c:type:`struct slot <slot>`

.. _`board_added.description`:

Description
-----------

Turns power on for the board.
Configures board.

.. _`remove_board`:

remove_board
============

.. c:function:: int remove_board(struct slot *p_slot)

    Turns off slot and LEDs

    :param struct slot \*p_slot:
        target \ :c:type:`struct slot <slot>`

.. _`shpchp_pushbutton_thread`:

shpchp_pushbutton_thread
========================

.. c:function:: void shpchp_pushbutton_thread(struct work_struct *work)

    handle pushbutton events

    :param struct work_struct \*work:
        \ :c:type:`struct work_struct <work_struct>`\  to be handled

.. _`shpchp_pushbutton_thread.description`:

Description
-----------

Scheduled procedure to handle blocking stuff for the pushbuttons.
Handles all pending events and exits.

.. This file was automatic generated / don't edit.

