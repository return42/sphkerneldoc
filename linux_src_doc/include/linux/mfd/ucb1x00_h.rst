.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/ucb1x00.h

.. _`ucb1x00_clkrate`:

ucb1x00_clkrate
===============

.. c:function:: unsigned int ucb1x00_clkrate(struct ucb1x00 *ucb)

    return the UCB1x00 SIB clock rate

    :param ucb:
        UCB1x00 structure describing chip
    :type ucb: struct ucb1x00 \*

.. _`ucb1x00_clkrate.description`:

Description
-----------

Return the SIB clock rate in Hz.

.. _`ucb1x00_enable`:

ucb1x00_enable
==============

.. c:function:: void ucb1x00_enable(struct ucb1x00 *ucb)

    enable the UCB1x00 SIB clock

    :param ucb:
        UCB1x00 structure describing chip
    :type ucb: struct ucb1x00 \*

.. _`ucb1x00_enable.description`:

Description
-----------

Enable the SIB clock.  This can be called multiple times.

.. _`ucb1x00_disable`:

ucb1x00_disable
===============

.. c:function:: void ucb1x00_disable(struct ucb1x00 *ucb)

    disable the UCB1x00 SIB clock

    :param ucb:
        UCB1x00 structure describing chip
    :type ucb: struct ucb1x00 \*

.. _`ucb1x00_disable.description`:

Description
-----------

Disable the SIB clock.  The SIB clock will only be disabled
when the number of ucb1x00_enable calls match the number of
ucb1x00_disable calls.

.. _`ucb1x00_reg_write`:

ucb1x00_reg_write
=================

.. c:function:: void ucb1x00_reg_write(struct ucb1x00 *ucb, unsigned int reg, unsigned int val)

    write a UCB1x00 register

    :param ucb:
        UCB1x00 structure describing chip
    :type ucb: struct ucb1x00 \*

    :param reg:
        UCB1x00 4-bit register index to write
    :type reg: unsigned int

    :param val:
        UCB1x00 16-bit value to write
    :type val: unsigned int

.. _`ucb1x00_reg_write.description`:

Description
-----------

Write the UCB1x00 register \ ``reg``\  with value \ ``val``\ .  The SIB
clock must be running for this function to return.

.. _`ucb1x00_reg_read`:

ucb1x00_reg_read
================

.. c:function:: unsigned int ucb1x00_reg_read(struct ucb1x00 *ucb, unsigned int reg)

    read a UCB1x00 register

    :param ucb:
        UCB1x00 structure describing chip
    :type ucb: struct ucb1x00 \*

    :param reg:
        UCB1x00 4-bit register index to write
    :type reg: unsigned int

.. _`ucb1x00_reg_read.description`:

Description
-----------

Read the UCB1x00 register \ ``reg``\  and return its value.  The SIB
clock must be running for this function to return.

.. _`ucb1x00_set_audio_divisor`:

ucb1x00_set_audio_divisor
=========================

.. c:function:: void ucb1x00_set_audio_divisor(struct ucb1x00 *ucb, unsigned int div)

    :param ucb:
        UCB1x00 structure describing chip
    :type ucb: struct ucb1x00 \*

    :param div:
        SIB clock divisor
    :type div: unsigned int

.. _`ucb1x00_set_telecom_divisor`:

ucb1x00_set_telecom_divisor
===========================

.. c:function:: void ucb1x00_set_telecom_divisor(struct ucb1x00 *ucb, unsigned int div)

    :param ucb:
        UCB1x00 structure describing chip
    :type ucb: struct ucb1x00 \*

    :param div:
        SIB clock divisor
    :type div: unsigned int

.. This file was automatic generated / don't edit.

