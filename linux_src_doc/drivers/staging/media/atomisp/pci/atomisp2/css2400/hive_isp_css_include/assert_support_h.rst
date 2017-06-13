.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/media/atomisp/pci/atomisp2/css2400/hive_isp_css_include/assert_support.h

.. _`compilation_error_if`:

COMPILATION_ERROR_IF
====================

.. c:function::  COMPILATION_ERROR_IF( condition)

    time rather than at run-time. It does not work for all compilers; see below.

    :param  condition:
        *undescribed*

.. _`compilation_error_if.description`:

Description
-----------

Depending on the value of 'condition', the following macro is expanded to:
- condition==true:
an expression containing an array declaration with negative size,
usually resulting in a compilation error
- condition==false:
(void) 1; // C statement with no effect

.. _`compilation_error_if.example`:

example
-------

.. code-block:: c

    COMPILATION_ERROR_IF( sizeof(struct host_sp_queues) != SIZE_OF_HOST_SP_QUEUES_STRUCT);


.. _`compilation_error_if.verify-that-the-macro-indeed-triggers-a-compilation-error-with-your-compiler`:

verify that the macro indeed triggers a compilation error with your compiler
----------------------------------------------------------------------------

COMPILATION_ERROR_IF( sizeof(struct host_sp_queues) != (sizeof(struct host_sp_queues)+1) );

Not all compilers will trigger an error with this macro; use a search engine to search for
BUILD_BUG_ON to find other methods.

.. This file was automatic generated / don't edit.

