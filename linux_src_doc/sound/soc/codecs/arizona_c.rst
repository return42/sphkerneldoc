.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/codecs/arizona.c

.. _`arizona_set_output_mode`:

arizona_set_output_mode
=======================

.. c:function:: int arizona_set_output_mode(struct snd_soc_component *component, int output, bool diff)

    Set the mode of the specified output

    :param component:
        Device to configure
    :type component: struct snd_soc_component \*

    :param output:
        Output number
    :type output: int

    :param diff:
        True to set the output to differential mode
    :type diff: bool

.. _`arizona_set_output_mode.description`:

Description
-----------

Some systems use external analogue switches to connect more
analogue devices to the CODEC than are supported by the device.  In
some systems this requires changing the switched output from single
ended to differential mode dynamically at runtime, an operation
supported using this function.

Most systems have a single static configuration and should use
platform data instead.

.. This file was automatic generated / don't edit.

