.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-davinci/board-dm646x-evm.c

.. _`setup_vpif_input_path`:

setup_vpif_input_path
=====================

.. c:function:: int setup_vpif_input_path(int channel, const char *sub_dev_name)

    :param int channel:
        channel id (0 - CH0, 1 - CH1)

    :param const char \*sub_dev_name:
        ptr sub device name

.. _`setup_vpif_input_path.description`:

Description
-----------

This will set vpif input to capture data from tvp514x or
tvp7002.

.. _`setup_vpif_input_channel_mode`:

setup_vpif_input_channel_mode
=============================

.. c:function:: int setup_vpif_input_channel_mode(int mux_mode)

    :param int mux_mode:
        mux mode. 0 - 1 channel or (1) - 2 channel

.. _`setup_vpif_input_channel_mode.description`:

Description
-----------

This will setup input mode to one channel (TVP7002) or 2 channel (TVP5147)

.. This file was automatic generated / don't edit.

