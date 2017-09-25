.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/initvals.c

.. _`ath5k_ini`:

struct ath5k_ini
================

.. c:type:: struct ath5k_ini

    Mode-independent initial register writes

.. _`ath5k_ini.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_ini {
        u16 ini_register;
        u32 ini_value;
        enum {
            AR5K_INI_WRITE = 0, AR5K_INI_READ = 1, } ini_mode;
    }

.. _`ath5k_ini.members`:

Members
-------

ini_register
    Register address

ini_value
    Default value

ini_mode
    0 to write 1 to read (and clear)

.. _`ath5k_ini_mode`:

struct ath5k_ini_mode
=====================

.. c:type:: struct ath5k_ini_mode

    Mode specific initial register values

.. _`ath5k_ini_mode.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_ini_mode {
        u16 mode_register;
        u32 mode_value[3];
    }

.. _`ath5k_ini_mode.members`:

Members
-------

mode_register
    Register address

mode_value
    Set of values for each enum ath5k_driver_mode

.. _`ath5k_hw_ini_registers`:

ath5k_hw_ini_registers
======================

.. c:function:: void ath5k_hw_ini_registers(struct ath5k_hw *ah, unsigned int size, const struct ath5k_ini *ini_regs, bool skip_pcu)

    Write initial register dump common for all modes

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param unsigned int size:
        Dump size

    :param const struct ath5k_ini \*ini_regs:
        The array of \ :c:type:`struct ath5k_ini <ath5k_ini>`\ 

    :param bool skip_pcu:
        Skip PCU registers

.. _`ath5k_hw_ini_mode_registers`:

ath5k_hw_ini_mode_registers
===========================

.. c:function:: void ath5k_hw_ini_mode_registers(struct ath5k_hw *ah, unsigned int size, const struct ath5k_ini_mode *ini_mode, u8 mode)

    Write initial mode-specific register dump

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param unsigned int size:
        Dump size

    :param const struct ath5k_ini_mode \*ini_mode:
        The array of \ :c:type:`struct ath5k_ini_mode <ath5k_ini_mode>`\ 

    :param u8 mode:
        One of enum ath5k_driver_mode

.. _`ath5k_hw_write_initvals`:

ath5k_hw_write_initvals
=======================

.. c:function:: int ath5k_hw_write_initvals(struct ath5k_hw *ah, u8 mode, bool skip_pcu)

    Write initial chip-specific register dump

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u8 mode:
        One of enum ath5k_driver_mode

    :param bool skip_pcu:
        Skip PCU registers

.. _`ath5k_hw_write_initvals.description`:

Description
-----------

Write initial chip-specific register dump, to get the chipset on a
clean and ready-to-work state after warm reset.

.. This file was automatic generated / don't edit.

