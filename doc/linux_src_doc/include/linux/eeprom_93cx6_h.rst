.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/eeprom_93cx6.h

.. _`eeprom_93cx6`:

struct eeprom_93cx6
===================

.. c:type:: struct eeprom_93cx6

    control structure for setting the commands for reading the eeprom data.

.. _`eeprom_93cx6.definition`:

Definition
----------

.. code-block:: c

    struct eeprom_93cx6 {
        void *data;
        void (* register_read) (struct eeprom_93cx6 *eeprom);
        void (* register_write) (struct eeprom_93cx6 *eeprom);
        int width;
        char drive_data;
        char reg_data_in;
        char reg_data_out;
        char reg_data_clock;
        char reg_chip_select;
    }

.. _`eeprom_93cx6.members`:

Members
-------

data
    private pointer for the driver.

register_read
    handler to
    read the eeprom register, this function should set all reg\_\* fields.

register_write
    handler to
    write to the eeprom register by using all reg\_\* fields.

width
    eeprom width, should be one of the PCI_EEPROM_WIDTH\_\* defines

drive_data
    Set if we're driving the data line.

reg_data_in
    register field to indicate data input

reg_data_out
    register field to indicate data output

reg_data_clock
    register field to set the data clock

reg_chip_select
    register field to set the chip select

.. _`eeprom_93cx6.description`:

Description
-----------

This structure is used for the communication between the driver
and the eeprom_93cx6 handlers for reading the eeprom.

.. This file was automatic generated / don't edit.

