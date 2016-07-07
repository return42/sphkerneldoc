.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/e1000e/manage.c

.. _`e1000_calculate_checksum`:

e1000_calculate_checksum
========================

.. c:function:: u8 e1000_calculate_checksum(u8 *buffer, u32 length)

    Calculate checksum for buffer

    :param u8 \*buffer:
        pointer to EEPROM

    :param u32 length:
        size of EEPROM to calculate a checksum for

.. _`e1000_calculate_checksum.description`:

Description
-----------

Calculates the checksum for some buffer on a specified length.  The
checksum calculated is returned.

.. _`e1000_mng_enable_host_if`:

e1000_mng_enable_host_if
========================

.. c:function:: s32 e1000_mng_enable_host_if(struct e1000_hw *hw)

    Checks host interface is enabled

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_mng_enable_host_if.description`:

Description
-----------

Returns 0 upon success, else -E1000_ERR_HOST_INTERFACE_COMMAND

This function checks whether the HOST IF is enabled for command operation
and also checks whether the previous command is completed.  It busy waits
in case of previous command is not completed.

.. _`e1000e_check_mng_mode_generic`:

e1000e_check_mng_mode_generic
=============================

.. c:function:: bool e1000e_check_mng_mode_generic(struct e1000_hw *hw)

    Generic check management mode

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_check_mng_mode_generic.description`:

Description
-----------

Reads the firmware semaphore register and returns true (>0) if
manageability is enabled, else false (0).

.. _`e1000e_enable_tx_pkt_filtering`:

e1000e_enable_tx_pkt_filtering
==============================

.. c:function:: bool e1000e_enable_tx_pkt_filtering(struct e1000_hw *hw)

    Enable packet filtering on Tx

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_enable_tx_pkt_filtering.description`:

Description
-----------

Enables packet filtering on transmit packets if manageability is enabled
and host interface is enabled.

.. _`e1000_mng_write_cmd_header`:

e1000_mng_write_cmd_header
==========================

.. c:function:: s32 e1000_mng_write_cmd_header(struct e1000_hw *hw, struct e1000_host_mng_command_header *hdr)

    Writes manageability command header

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param struct e1000_host_mng_command_header \*hdr:
        pointer to the host interface command header

.. _`e1000_mng_write_cmd_header.description`:

Description
-----------

Writes the command header after does the checksum calculation.

.. _`e1000_mng_host_if_write`:

e1000_mng_host_if_write
=======================

.. c:function:: s32 e1000_mng_host_if_write(struct e1000_hw *hw, u8 *buffer, u16 length, u16 offset, u8 *sum)

    Write to the manageability host interface

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u8 \*buffer:
        pointer to the host interface buffer

    :param u16 length:
        size of the buffer

    :param u16 offset:
        location in the buffer to write to

    :param u8 \*sum:
        sum of the data (not checksum)

.. _`e1000_mng_host_if_write.description`:

Description
-----------

This function writes the buffer content at the offset given on the host if.
It also does alignment considerations to do the writes in most efficient
way.  Also fills up the sum of the buffer in \*buffer parameter.

.. _`e1000e_mng_write_dhcp_info`:

e1000e_mng_write_dhcp_info
==========================

.. c:function:: s32 e1000e_mng_write_dhcp_info(struct e1000_hw *hw, u8 *buffer, u16 length)

    Writes DHCP info to host interface

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u8 \*buffer:
        pointer to the host interface

    :param u16 length:
        size of the buffer

.. _`e1000e_mng_write_dhcp_info.description`:

Description
-----------

Writes the DHCP information to the host interface.

.. _`e1000e_enable_mng_pass_thru`:

e1000e_enable_mng_pass_thru
===========================

.. c:function:: bool e1000e_enable_mng_pass_thru(struct e1000_hw *hw)

    Check if management passthrough is needed

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_enable_mng_pass_thru.description`:

Description
-----------

Verifies the hardware needs to leave interface enabled so that frames can
be directed to and from the management interface.

.. This file was automatic generated / don't edit.

