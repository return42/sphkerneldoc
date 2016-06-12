.. -*- coding: utf-8; mode: rst -*-

.. _misc-devices:

*********************
Miscellaneous Devices
*********************


.. _misc-devices-opl3:

FM OPL3
=======

The FM OPL3 is still used in many chips (mainly for backward
compatibility). ALSA has a nice OPL3 FM control layer, too. The OPL3 API
is defined in ``<sound/opl3.h>``.

FM registers can be directly accessed through the direct-FM API, defined
in ``<sound/asound_fm.h>``. In ALSA native mode, FM registers are
accessed through the Hardware-Dependent Device direct-FM extension API,
whereas in OSS compatible mode, FM registers can be accessed with the
OSS direct-FM compatible API in ``/dev/dmfmX`` device.

To create the OPL3 component, you have two functions to call. The first
one is a constructor for the ``opl3_t`` instance.


.. code-block:: c

      struct snd_opl3 *opl3;
      snd_opl3_create(card, lport, rport, OPL3_HW_OPL3_XXX,
                      integrated, &opl3);

The first argument is the card pointer, the second one is the left port
address, and the third is the right port address. In most cases, the
right port is placed at the left port + 2.

The fourth argument is the hardware type.

When the left and right ports have been already allocated by the card
driver, pass non-zero to the fifth argument (``integrated``). Otherwise,
the opl3 module will allocate the specified ports by itself.

When the accessing the hardware requires special method instead of the
standard I/O access, you can create opl3 instance separately with
:c:func:`snd_opl3_new()`.


.. code-block:: c

      struct snd_opl3 *opl3;
      snd_opl3_new(card, OPL3_HW_OPL3_XXX, &opl3);

Then set ``command``, ``private_data`` and ``private_free`` for the
private access function, the private data and the destructor. The
l_port and r_port are not necessarily set. Only the command must be
set properly. You can retrieve the data from the opl3->private_data
field.

After creating the opl3 instance via :c:func:`snd_opl3_new()`, call
:c:func:`snd_opl3_init()` to initialize the chip to the proper
state. Note that :c:func:`snd_opl3_create()` always calls it
internally.

If the opl3 instance is created successfully, then create a hwdep device
for this opl3.


.. code-block:: c

      struct snd_hwdep *opl3hwdep;
      snd_opl3_hwdep_new(opl3, 0, 1, &opl3hwdep);

The first argument is the ``opl3_t`` instance you created, and the
second is the index number, usually 0.

The third argument is the index-offset for the sequencer client assigned
to the OPL3 port. When there is an MPU401-UART, give 1 for here (UART
always takes 0).


.. _misc-devices-hardware-dependent:

Hardware-Dependent Devices
==========================

Some chips need user-space access for special controls or for loading
the micro code. In such a case, you can create a hwdep
(hardware-dependent) device. The hwdep API is defined in
``<sound/hwdep.h>``. You can find examples in opl3 driver or
``isa/sb/sb16_csp.c``.

The creation of the ``hwdep`` instance is done via
:c:func:`snd_hwdep_new()`.


.. code-block:: c

      struct snd_hwdep *hw;
      snd_hwdep_new(card, "My HWDEP", 0, &hw);

where the third argument is the index number.

You can then pass any pointer value to the ``private_data``. If you
assign a private data, you should define the destructor, too. The
destructor function is set in the ``private_free`` field.


.. code-block:: c

      struct mydata *p = kmalloc(sizeof(*p), GFP_KERNEL);
      hw->private_data = p;
      hw->private_free = mydata_free;

and the implementation of the destructor would be:


.. code-block:: c

      static void mydata_free(struct snd_hwdep *hw)
      {
              struct mydata *p = hw->private_data;
              kfree(p);
      }

The arbitrary file operations can be defined for this instance. The file
operators are defined in the ``ops`` table. For example, assume that
this chip needs an ioctl.


.. code-block:: c

      hw->ops.open = mydata_open;
      hw->ops.ioctl = mydata_ioctl;
      hw->ops.release = mydata_release;

And implement the callback functions as you like.


.. _misc-devices-IEC958:

IEC958 (S/PDIF)
===============

Usually the controls for IEC958 devices are implemented via the control
interface. There is a macro to compose a name string for IEC958
controls, :c:func:`SNDRV_CTL_NAME_IEC958()` defined in
``<include/asound.h>``.

There are some standard controls for IEC958 status bits. These controls
use the type ``SNDRV_CTL_ELEM_TYPE_IEC958``, and the size of element is
fixed as 4 bytes array (value.iec958.status[x]). For the ``info``
callback, you don't specify the value field for this type (the count
field must be set, though).

“IEC958 Playback Con Mask” is used to return the bit-mask for the IEC958
status bits of consumer mode. Similarly, “IEC958 Playback Pro Mask”
returns the bitmask for professional mode. They are read-only controls,
and are defined as MIXER controls (iface =
``SNDRV_CTL_ELEM_IFACE_MIXER``).

Meanwhile, “IEC958 Playback Default” control is defined for getting and
setting the current default IEC958 bits. Note that this one is usually
defined as a PCM control (iface = ``SNDRV_CTL_ELEM_IFACE_PCM``),
although in some places it's defined as a MIXER control.

In addition, you can define the control switches to enable/disable or to
set the raw bit mode. The implementation will depend on the chip, but
the control should be named as “IEC958 xxx”, preferably using the
:c:func:`SNDRV_CTL_NAME_IEC958()` macro.

You can find several cases, for example, ``pci/emu10k1``,
``pci/ice1712``, or ``pci/cmipci.c``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
