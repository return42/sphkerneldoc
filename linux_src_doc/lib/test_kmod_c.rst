.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/test_kmod.c

.. _`kmod_test_case`:

enum kmod_test_case
===================

.. c:type:: enum kmod_test_case

    linker table test case

.. _`kmod_test_case.definition`:

Definition
----------

.. code-block:: c

    enum kmod_test_case {
        __TEST_KMOD_INVALID,
        TEST_KMOD_DRIVER,
        TEST_KMOD_FS_TYPE,
        __TEST_KMOD_MAX
    };

.. _`kmod_test_case.constants`:

Constants
---------

__TEST_KMOD_INVALID
    *undescribed*

TEST_KMOD_DRIVER
    stress tests \ :c:func:`request_module`\ 

TEST_KMOD_FS_TYPE
    stress tests \ :c:func:`get_fs_type`\ 

__TEST_KMOD_MAX
    *undescribed*

.. _`kmod_test_case.description`:

Description
-----------

If you add a  test case, please be sure to review if you need to se
\ ``need_mod_put``\  for your tests case.

.. This file was automatic generated / don't edit.

