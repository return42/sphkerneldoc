.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/8250/8250_exar.c

.. _`exar8250_board`:

struct exar8250_board
=====================

.. c:type:: struct exar8250_board

    board information

.. _`exar8250_board.definition`:

Definition
----------

.. code-block:: c

    struct exar8250_board {
        unsigned int num_ports;
        unsigned int reg_shift;
        bool has_slave;
        int (*setup)(struct exar8250 *, struct pci_dev *,struct uart_8250_port *, int);
        void (*exit)(struct pci_dev *pcidev);
    }

.. _`exar8250_board.members`:

Members
-------

num_ports
    number of serial ports

reg_shift
    describes UART register mapping in PCI memory

has_slave
    *undescribed*

setup
    *undescribed*

exit
    *undescribed*

.. This file was automatic generated / don't edit.

