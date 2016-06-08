.. -*- coding: utf-8; mode: rst -*-

.. _api:

*************
API reference
*************

Due to limitations of the kernel documentation framework and the
existing layout of the source code the entire regulator API is
documented here.


.. kernel-doc:: include/linux/regulator/consumer.h
    :internal:

.. kernel-doc:: include/linux/regulator/machine.h
    :internal:

.. kernel-doc:: include/linux/regulator/driver.h
    :internal:

.. kernel-doc:: drivers/regulator/core.c
    :export:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
