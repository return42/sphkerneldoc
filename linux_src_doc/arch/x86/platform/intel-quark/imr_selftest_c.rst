.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/platform/intel-quark/imr_selftest.c

.. _`selftest`:

SELFTEST
========

.. c:function::  SELFTEST()

    - Intel Isolated Memory Region self-test driver

.. _`selftest.description`:

Description
-----------

Copyright(c) 2013 Intel Corporation.
Copyright(c) 2015 Bryan O'Donoghue <pure.logic@nexus-software.ie>

IMR self test. The purpose of this module is to run a set of tests on the
IMR API to validate it's sanity. We check for overlapping, reserved
addresses and setup/teardown sanity.

.. _`__printf`:

\__printf
=========

.. c:function::  __printf( 2,  3)

    Print result string for self test.

    :param 2:
        *undescribed*
    :type 2: 

    :param 3:
        *undescribed*
    :type 3: 

.. _`imr_self_test`:

imr_self_test
=============

.. c:function:: void imr_self_test( void)

    :param void:
        no arguments
    :type void: 

.. _`imr_self_test.description`:

Description
-----------

Verify IMR self_test with some simple tests to verify overlap,
zero sized allocations and 1 KiB sized areas.

.. _`imr_self_test_init`:

imr_self_test_init
==================

.. c:function:: int imr_self_test_init( void)

    entry point for IMR driver.

    :param void:
        no arguments
    :type void: 

.. _`imr_self_test_init.return`:

Return
------

-ENODEV for no IMR support 0 if good to go.

.. _`device_initcall`:

device_initcall
===============

.. c:function::  device_initcall( imr_self_test_init)

    exit point for IMR code.

    :param imr_self_test_init:
        *undescribed*
    :type imr_self_test_init: 

.. This file was automatic generated / don't edit.

