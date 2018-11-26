.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/testing/selftests/futex/include/logging.h

.. _`log_color`:

log_color
=========

.. c:function:: void log_color(int use_color)

    Use colored output for PASS, ERROR, and FAIL strings

    :param use_color:
        use color (1) or not (0)
    :type use_color: int

.. _`log_verbosity`:

log_verbosity
=============

.. c:function:: void log_verbosity(int level)

    Set verbosity of test output

    :param level:
        *undescribed*
    :type level: int

.. _`log_verbosity.description`:

Description
-----------

Currently setting verbose=1 will enable INFO messages and 0 will disable
them. FAIL and ERROR messages are always displayed.

.. _`print_result`:

print_result
============

.. c:function:: void print_result(const char *test_name, int ret)

    Print standard PASS \| ERROR \| FAIL results

    :param test_name:
        *undescribed*
    :type test_name: const char \*

    :param ret:
        the return value to be considered: 0 \| RET_ERROR \| RET_FAIL
    :type ret: int

.. _`print_result.description`:

Description
-----------

\ :c:func:`print_result`\  is primarily intended for functional tests.

.. This file was automatic generated / don't edit.

