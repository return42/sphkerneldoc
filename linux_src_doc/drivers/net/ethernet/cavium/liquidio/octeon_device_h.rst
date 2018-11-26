.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/cavium/liquidio/octeon_device.h

.. _`octeon_mem_access_ok`:

octeon_mem_access_ok
====================

.. c:function:: int octeon_mem_access_ok(struct octeon_device *oct)

    :param oct:
        *undescribed*
    :type oct: struct octeon_device \*

.. _`octeon_mem_access_ok.description`:

Description
-----------

\ ``param``\  oct which octeon to send to
\ ``return``\  Zero on success, negative on failure.

.. _`octeon_wait_for_ddr_init`:

octeon_wait_for_ddr_init
========================

.. c:function:: int octeon_wait_for_ddr_init(struct octeon_device *oct, u32 *timeout_in_ms)

    :param oct:
        *undescribed*
    :type oct: struct octeon_device \*

    :param timeout_in_ms:
        *undescribed*
    :type timeout_in_ms: u32 \*

.. _`octeon_wait_for_ddr_init.description`:

Description
-----------

\ ``param``\  oct which octeon to send to
\ ``param``\  timeout_in_ms pointer to how long to wait until DDR is initialized
in ms.
If contents are 0, it waits until contents are non-zero
before starting to check.
\ ``return``\  Zero on success, negative on failure.

.. _`octeon_wait_for_bootloader`:

octeon_wait_for_bootloader
==========================

.. c:function:: int octeon_wait_for_bootloader(struct octeon_device *oct, u32 wait_time_hundredths)

    boot to boot and be waiting for a command.

    :param oct:
        *undescribed*
    :type oct: struct octeon_device \*

    :param wait_time_hundredths:
        *undescribed*
    :type wait_time_hundredths: u32

.. _`octeon_wait_for_bootloader.description`:

Description
-----------

\ ``param``\  wait_time_hundredths
Maximum time to wait

\ ``return``\  Zero on success, negative on failure.

.. _`octeon_init_consoles`:

octeon_init_consoles
====================

.. c:function:: int octeon_init_consoles(struct octeon_device *oct)

    :param oct:
        *undescribed*
    :type oct: struct octeon_device \*

.. _`octeon_init_consoles.description`:

Description
-----------

\ ``param``\  oct which octeon initialize
\ ``return``\  Zero on success, negative on failure.

.. _`octeon_add_console`:

octeon_add_console
==================

.. c:function:: int octeon_add_console(struct octeon_device *oct, u32 console_num, char *dbg_enb)

    :param oct:
        *undescribed*
    :type oct: struct octeon_device \*

    :param console_num:
        *undescribed*
    :type console_num: u32

    :param dbg_enb:
        *undescribed*
    :type dbg_enb: char \*

.. _`octeon_add_console.description`:

Description
-----------

\ ``return``\  Zero on success, negative on failure.

.. _`octeon_console_send_cmd`:

octeon_console_send_cmd
=======================

.. c:function:: int octeon_console_send_cmd(struct octeon_device *oct, char *cmd_str, u32 wait_hundredths)

    boot on console 0 as a command.

    :param oct:
        *undescribed*
    :type oct: struct octeon_device \*

    :param cmd_str:
        *undescribed*
    :type cmd_str: char \*

    :param wait_hundredths:
        *undescribed*
    :type wait_hundredths: u32

.. _`octeon_console_send_cmd.description`:

Description
-----------

\ ``param``\  oct which octeon to send to
\ ``param``\  cmd_str String to send
\ ``param``\  wait_hundredths Time to wait for u-boot to accept the command.

\ ``return``\  Zero on success, negative on failure.

.. This file was automatic generated / don't edit.

