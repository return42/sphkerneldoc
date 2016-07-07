.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/m68k/include/asm/mcfqspi.h

.. _`mcfqspi_cs_control`:

struct mcfqspi_cs_control
=========================

.. c:type:: struct mcfqspi_cs_control

    chip select control for the coldfire qspi driver

.. _`mcfqspi_cs_control.definition`:

Definition
----------

.. code-block:: c

    struct mcfqspi_cs_control {
        int (* setup) (struct mcfqspi_cs_control *);
        void (* teardown) (struct mcfqspi_cs_control *);
        void (* select) (struct mcfqspi_cs_control *, u8, bool);
        void (* deselect) (struct mcfqspi_cs_control *, u8, bool);
    }

.. _`mcfqspi_cs_control.members`:

Members
-------

setup
    setup the control; allocate gpio's, etc. May be NULL.

teardown
    finish with the control; free gpio's, etc. May be NULL.

select
    output the signals to select the device.  Can not be NULL.

deselect
    output the signals to deselect the device. Can not be NULL.

.. _`mcfqspi_cs_control.description`:

Description
-----------

The QSPI module has 4 hardware chip selects.  We don't use them.  Instead
platforms are required to supply a mcfqspi_cs_control as a part of the
platform data for each QSPI master controller.  Only the select and
deselect functions are required.

.. _`mcfqspi_platform_data`:

struct mcfqspi_platform_data
============================

.. c:type:: struct mcfqspi_platform_data

    platform data for the coldfire qspi driver

.. _`mcfqspi_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct mcfqspi_platform_data {
        s16 bus_num;
        u16 num_chipselect;
        struct mcfqspi_cs_control *cs_control;
    }

.. _`mcfqspi_platform_data.members`:

Members
-------

bus_num
    board specific identifier for this qspi driver.

num_chipselect
    *undescribed*

cs_control
    platform dependent chip select control.

.. This file was automatic generated / don't edit.

