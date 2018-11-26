.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_trace.h

.. _`_i40e_trace_name`:

\_I40E_TRACE_NAME
=================

.. c:function::  _I40E_TRACE_NAME( trace_name)

    :param trace_name:
        *undescribed*
    :type trace_name: 

.. _`_i40e_trace_name.like`:

like
----


trace_i40e{,vf}_example(args...)

... as:

i40e_trace(example, args...)

... to resolve to the PF or VF version of the tracepoint without
ifdefs, and to allow tracepoints to be disabled entirely at build
time.

Trace point should always be referred to in the driver via this
macro.

Similarly, i40e_trace_enabled(trace_name) wraps references to
trace_i40e{,vf}_<trace_name>_enabled() functions.

.. This file was automatic generated / don't edit.

