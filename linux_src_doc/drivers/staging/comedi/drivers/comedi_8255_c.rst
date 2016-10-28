.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/drivers/comedi_8255.c

.. _`subdev_8255_init`:

subdev_8255_init
================

.. c:function:: int subdev_8255_init(struct comedi_device *dev, struct comedi_subdevice *s, int (*io)(struct comedi_device *dev, int dir, int port, int data, unsigned long regbase), unsigned long regbase)

    initialize DIO subdevice for driving I/O mapped 8255

    :param struct comedi_device \*dev:
        comedi device owning subdevice

    :param struct comedi_subdevice \*s:
        comedi subdevice to initialize

    :param int (\*io)(struct comedi_device \*dev, int dir, int port, int data, unsigned long regbase):
        (optional) register I/O call-back function

    :param unsigned long regbase:
        offset of 8255 registers from dev->iobase, or call-back context

.. _`subdev_8255_init.description`:

Description
-----------

Initializes a comedi subdevice as a DIO subdevice driving an 8255 chip.

If the optional I/O call-back function is provided, its prototype is of

.. _`subdev_8255_init.the-following-form`:

the following form
------------------


int my_8255_callback(struct comedi_device \*dev, int dir, int port,
int data, unsigned long regbase);

where 'dev', and 'regbase' match the values passed to this function,
'port' is the 8255 port number 0 to 3 (including the control port), 'dir'
is the direction (0 for read, 1 for write) and 'data' is the value to be
written.  It should return 0 if writing or the value read if reading.

If the optional I/O call-back function is not provided, an internal
call-back function is used which uses consecutive I/O port addresses
starting at dev->iobase + regbase.

.. _`subdev_8255_init.return`:

Return
------

-ENOMEM if failed to allocate memory, zero on success.

.. _`subdev_8255_mm_init`:

subdev_8255_mm_init
===================

.. c:function:: int subdev_8255_mm_init(struct comedi_device *dev, struct comedi_subdevice *s, int (*io)(struct comedi_device *dev, int dir, int port, int data, unsigned long regbase), unsigned long regbase)

    initialize DIO subdevice for driving mmio-mapped 8255

    :param struct comedi_device \*dev:
        comedi device owning subdevice

    :param struct comedi_subdevice \*s:
        comedi subdevice to initialize

    :param int (\*io)(struct comedi_device \*dev, int dir, int port, int data, unsigned long regbase):
        (optional) register I/O call-back function

    :param unsigned long regbase:
        offset of 8255 registers from dev->mmio, or call-back context

.. _`subdev_8255_mm_init.description`:

Description
-----------

Initializes a comedi subdevice as a DIO subdevice driving an 8255 chip.

If the optional I/O call-back function is provided, its prototype is of

.. _`subdev_8255_mm_init.the-following-form`:

the following form
------------------


int my_8255_callback(struct comedi_device \*dev, int dir, int port,
int data, unsigned long regbase);

where 'dev', and 'regbase' match the values passed to this function,
'port' is the 8255 port number 0 to 3 (including the control port), 'dir'
is the direction (0 for read, 1 for write) and 'data' is the value to be
written.  It should return 0 if writing or the value read if reading.

If the optional I/O call-back function is not provided, an internal
call-back function is used which uses consecutive MMIO virtual addresses
starting at dev->mmio + regbase.

.. _`subdev_8255_mm_init.return`:

Return
------

-ENOMEM if failed to allocate memory, zero on success.

.. _`subdev_8255_regbase`:

subdev_8255_regbase
===================

.. c:function:: unsigned long subdev_8255_regbase(struct comedi_subdevice *s)

    get offset of 8255 registers or call-back context

    :param struct comedi_subdevice \*s:
        comedi subdevice

.. _`subdev_8255_regbase.description`:

Description
-----------

Returns the 'regbase' parameter that was previously passed to to
\ :c:func:`subdev_8255_init`\  or \ :c:func:`subdev_8255_mm_init`\  to set up the subdevice.
Only valid if the subdevice was set up successfully.

.. This file was automatic generated / don't edit.

