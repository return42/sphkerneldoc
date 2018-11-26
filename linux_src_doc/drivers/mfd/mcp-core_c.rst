.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/mcp-core.c

.. _`mcp_set_telecom_divisor`:

mcp_set_telecom_divisor
=======================

.. c:function:: void mcp_set_telecom_divisor(struct mcp *mcp, unsigned int div)

    set the telecom divisor

    :param mcp:
        MCP interface structure
    :type mcp: struct mcp \*

    :param div:
        SIB clock divisor
    :type div: unsigned int

.. _`mcp_set_telecom_divisor.description`:

Description
-----------

Set the telecom divisor on the MCP interface.  The resulting
sample rate is SIBCLOCK/div.

.. _`mcp_set_audio_divisor`:

mcp_set_audio_divisor
=====================

.. c:function:: void mcp_set_audio_divisor(struct mcp *mcp, unsigned int div)

    set the audio divisor

    :param mcp:
        MCP interface structure
    :type mcp: struct mcp \*

    :param div:
        SIB clock divisor
    :type div: unsigned int

.. _`mcp_set_audio_divisor.description`:

Description
-----------

Set the audio divisor on the MCP interface.

.. _`mcp_reg_write`:

mcp_reg_write
=============

.. c:function:: void mcp_reg_write(struct mcp *mcp, unsigned int reg, unsigned int val)

    write a device register

    :param mcp:
        MCP interface structure
    :type mcp: struct mcp \*

    :param reg:
        4-bit register index
    :type reg: unsigned int

    :param val:
        16-bit data value
    :type val: unsigned int

.. _`mcp_reg_write.description`:

Description
-----------

Write a device register.  The MCP interface must be enabled
to prevent this function hanging.

.. _`mcp_reg_read`:

mcp_reg_read
============

.. c:function:: unsigned int mcp_reg_read(struct mcp *mcp, unsigned int reg)

    read a device register

    :param mcp:
        MCP interface structure
    :type mcp: struct mcp \*

    :param reg:
        4-bit register index
    :type reg: unsigned int

.. _`mcp_reg_read.description`:

Description
-----------

Read a device register and return its value.  The MCP interface
must be enabled to prevent this function hanging.

.. _`mcp_enable`:

mcp_enable
==========

.. c:function:: void mcp_enable(struct mcp *mcp)

    enable the MCP interface

    :param mcp:
        MCP interface to enable
    :type mcp: struct mcp \*

.. _`mcp_enable.description`:

Description
-----------

Enable the MCP interface.  Each call to mcp_enable will need
a corresponding call to mcp_disable to disable the interface.

.. _`mcp_disable`:

mcp_disable
===========

.. c:function:: void mcp_disable(struct mcp *mcp)

    disable the MCP interface

    :param mcp:
        MCP interface to disable
    :type mcp: struct mcp \*

.. _`mcp_disable.description`:

Description
-----------

Disable the MCP interface.  The MCP interface will only be
disabled once the number of calls to mcp_enable matches the
number of calls to mcp_disable.

.. This file was automatic generated / don't edit.

