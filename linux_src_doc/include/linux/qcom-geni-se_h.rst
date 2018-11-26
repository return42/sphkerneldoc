.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/qcom-geni-se.h

.. _`geni_se`:

struct geni_se
==============

.. c:type:: struct geni_se

    GENI Serial Engine

.. _`geni_se.definition`:

Definition
----------

.. code-block:: c

    struct geni_se {
        void __iomem *base;
        struct device *dev;
        struct geni_wrapper *wrapper;
        struct clk *clk;
        unsigned int num_clk_levels;
        unsigned long *clk_perf_tbl;
    }

.. _`geni_se.members`:

Members
-------

base
    Base Address of the Serial Engine's register block

dev
    Pointer to the Serial Engine device

wrapper
    Pointer to the parent QUP Wrapper core

clk
    Handle to the core serial engine clock

num_clk_levels
    Number of valid clock levels in clk_perf_tbl

clk_perf_tbl
    Table of clock frequency input to serial engine clock

.. _`geni_se_read_proto`:

geni_se_read_proto
==================

.. c:function:: u32 geni_se_read_proto(struct geni_se *se)

    Read the protocol configured for a serial engine

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

.. _`geni_se_read_proto.return`:

Return
------

Protocol value as configured in the serial engine.

.. _`geni_se_setup_m_cmd`:

geni_se_setup_m_cmd
===================

.. c:function:: void geni_se_setup_m_cmd(struct geni_se *se, u32 cmd, u32 params)

    Setup the primary sequencer

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

    :param cmd:
        Command/Operation to setup in the primary sequencer.
    :type cmd: u32

    :param params:
        Parameter for the sequencer command.
    :type params: u32

.. _`geni_se_setup_m_cmd.description`:

Description
-----------

This function is used to configure the primary sequencer with the
command and its associated parameters.

.. _`geni_se_setup_s_cmd`:

geni_se_setup_s_cmd
===================

.. c:function:: void geni_se_setup_s_cmd(struct geni_se *se, u32 cmd, u32 params)

    Setup the secondary sequencer

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

    :param cmd:
        Command/Operation to setup in the secondary sequencer.
    :type cmd: u32

    :param params:
        Parameter for the sequencer command.
    :type params: u32

.. _`geni_se_setup_s_cmd.description`:

Description
-----------

This function is used to configure the secondary sequencer with the
command and its associated parameters.

.. _`geni_se_cancel_m_cmd`:

geni_se_cancel_m_cmd
====================

.. c:function:: void geni_se_cancel_m_cmd(struct geni_se *se)

    Cancel the command configured in the primary sequencer

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

.. _`geni_se_cancel_m_cmd.description`:

Description
-----------

This function is used to cancel the currently configured command in the
primary sequencer.

.. _`geni_se_cancel_s_cmd`:

geni_se_cancel_s_cmd
====================

.. c:function:: void geni_se_cancel_s_cmd(struct geni_se *se)

    Cancel the command configured in the secondary sequencer

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

.. _`geni_se_cancel_s_cmd.description`:

Description
-----------

This function is used to cancel the currently configured command in the
secondary sequencer.

.. _`geni_se_abort_m_cmd`:

geni_se_abort_m_cmd
===================

.. c:function:: void geni_se_abort_m_cmd(struct geni_se *se)

    Abort the command configured in the primary sequencer

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

.. _`geni_se_abort_m_cmd.description`:

Description
-----------

This function is used to force abort the currently configured command in the
primary sequencer.

.. _`geni_se_abort_s_cmd`:

geni_se_abort_s_cmd
===================

.. c:function:: void geni_se_abort_s_cmd(struct geni_se *se)

    Abort the command configured in the secondary sequencer

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

.. _`geni_se_abort_s_cmd.description`:

Description
-----------

This function is used to force abort the currently configured command in the
secondary sequencer.

.. _`geni_se_get_tx_fifo_depth`:

geni_se_get_tx_fifo_depth
=========================

.. c:function:: u32 geni_se_get_tx_fifo_depth(struct geni_se *se)

    Get the TX fifo depth of the serial engine

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

.. _`geni_se_get_tx_fifo_depth.description`:

Description
-----------

This function is used to get the depth i.e. number of elements in the
TX fifo of the serial engine.

.. _`geni_se_get_tx_fifo_depth.return`:

Return
------

TX fifo depth in units of FIFO words.

.. _`geni_se_get_tx_fifo_width`:

geni_se_get_tx_fifo_width
=========================

.. c:function:: u32 geni_se_get_tx_fifo_width(struct geni_se *se)

    Get the TX fifo width of the serial engine

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

.. _`geni_se_get_tx_fifo_width.description`:

Description
-----------

This function is used to get the width i.e. word size per element in the
TX fifo of the serial engine.

.. _`geni_se_get_tx_fifo_width.return`:

Return
------

TX fifo width in bits

.. _`geni_se_get_rx_fifo_depth`:

geni_se_get_rx_fifo_depth
=========================

.. c:function:: u32 geni_se_get_rx_fifo_depth(struct geni_se *se)

    Get the RX fifo depth of the serial engine

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

.. _`geni_se_get_rx_fifo_depth.description`:

Description
-----------

This function is used to get the depth i.e. number of elements in the
RX fifo of the serial engine.

.. _`geni_se_get_rx_fifo_depth.return`:

Return
------

RX fifo depth in units of FIFO words

.. This file was automatic generated / don't edit.

