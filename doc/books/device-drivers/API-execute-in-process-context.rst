
.. _API-execute-in-process-context:

==========================
execute_in_process_context
==========================

*man execute_in_process_context(9)*

*4.6.0-rc1*

reliably execute the routine with user context


Synopsis
========

.. c:function:: int execute_in_process_context( work_func_t fn, struct execute_work * ew )

Arguments
=========

``fn``
    the function to execute

``ew``
    guaranteed storage for the execute work structure (must be available when the work executes)


Description
===========

Executes the function immediately if process context is available, otherwise schedules the function for delayed execution.


Return
======

0 - function was executed 1 - function was scheduled for execution
