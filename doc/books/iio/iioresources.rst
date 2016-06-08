.. -*- coding: utf-8; mode: rst -*-

.. _iioresources:

*********
Resources
*********

-  drivers/iio/
   , contains the IIO core plus and directories for each sensor type
   (e.g. accel, magnetometer, etc.)
-  include/linux/iio/
   , contains the header files, nice to read for the internal kernel
   interfaces.
-  include/uapi/linux/iio/
   , contains files to be used by user space applications.
-  tools/iio/
   , contains tools for rapidly testing buffers, events and device
   creation.
-  drivers/staging/iio/
   , contains code for some drivers or experimental features that are
   not yet mature enough to be moved out.

Besides the code, there are some good online documentation sources:

-  !ri!`Industrial I/O mailing list
   <http://marc.info/?l=linux-iio>`__
-  !ri!`Analog Device IIO wiki page
   <http://wiki.analog.com/software/linux/docs/iio/iio>`__
-  !ri!`Using the Linux IIO framework for SDR, Lars-Peter Clausen's
   presentation at FOSDEM
   <https://fosdem.org/2015/schedule/event/iiosdr/>`__


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
