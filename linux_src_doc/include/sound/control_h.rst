.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/control.h

.. _`snd_ctl_add_slave`:

snd_ctl_add_slave
=================

.. c:function:: int snd_ctl_add_slave(struct snd_kcontrol *master, struct snd_kcontrol *slave)

    Add a virtual slave control

    :param master:
        vmaster element
    :type master: struct snd_kcontrol \*

    :param slave:
        slave element to add
    :type slave: struct snd_kcontrol \*

.. _`snd_ctl_add_slave.description`:

Description
-----------

Add a virtual slave control to the given master element created via
\ :c:func:`snd_ctl_create_virtual_master`\  beforehand.

All slaves must be the same type (returning the same information
via info callback).  The function doesn't check it, so it's your
responsibility.

Also, some additional limitations:
at most two channels,
logarithmic volume control (dB level) thus no linear volume,
master can only attenuate the volume without gain

.. _`snd_ctl_add_slave.return`:

Return
------

Zero if successful or a negative error code.

.. _`snd_ctl_add_slave_uncached`:

snd_ctl_add_slave_uncached
==========================

.. c:function:: int snd_ctl_add_slave_uncached(struct snd_kcontrol *master, struct snd_kcontrol *slave)

    Add a virtual slave control

    :param master:
        vmaster element
    :type master: struct snd_kcontrol \*

    :param slave:
        slave element to add
    :type slave: struct snd_kcontrol \*

.. _`snd_ctl_add_slave_uncached.description`:

Description
-----------

Add a virtual slave control to the given master.
Unlike \ :c:func:`snd_ctl_add_slave`\ , the element added via this function
is supposed to have volatile values, and get callback is called
at each time queried from the master.

When the control peeks the hardware values directly and the value
can be changed by other means than the put callback of the element,
this function should be used to keep the value always up-to-date.

.. _`snd_ctl_add_slave_uncached.return`:

Return
------

Zero if successful or a negative error code.

.. This file was automatic generated / don't edit.

