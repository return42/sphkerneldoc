.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/iavf/iavf_trace.h

.. _`_iavf_trace_name`:

\_IAVF_TRACE_NAME
=================

.. c:function::  _IAVF_TRACE_NAME( trace_name)

    :param trace_name:
        *undescribed*
    :type trace_name: 

.. _`_iavf_trace_name.like`:

like
----


trace_iavf{,vf}_example(args...)

... as:

iavf_trace(example, args...)

... to resolve to the PF or VF version of the tracepoint without
ifdefs, and to allow tracepoints to be disabled entirely at build
time.

Trace point should always be referred to in the driver via this
macro.

Similarly, iavf_trace_enabled(trace_name) wraps references to
trace_iavf{,vf}_<trace_name>_enabled() functions.

.. This file was automatic generated / don't edit.

