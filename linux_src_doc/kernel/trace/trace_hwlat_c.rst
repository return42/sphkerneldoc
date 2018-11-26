.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/trace_hwlat.c

.. _`get_sample`:

get_sample
==========

.. c:function:: int get_sample( void)

    sample the CPU TSC and look for likely hardware latencies

    :param void:
        no arguments
    :type void: 

.. _`get_sample.description`:

Description
-----------

Used to repeatedly capture the CPU TSC (or similar), looking for potential
hardware-induced latency. Called with interrupts disabled and with
hwlat_data.lock held.

.. _`start_kthread`:

start_kthread
=============

.. c:function:: int start_kthread(struct trace_array *tr)

    Kick off the hardware latency sampling/detector kthread

    :param tr:
        *undescribed*
    :type tr: struct trace_array \*

.. _`start_kthread.description`:

Description
-----------

This starts the kernel thread that will sit and sample the CPU timestamp
counter (TSC or similar) and look for potential hardware latencies.

.. _`stop_kthread`:

stop_kthread
============

.. c:function:: void stop_kthread( void)

    Inform the hardware latency samping/detector kthread to stop

    :param void:
        no arguments
    :type void: 

.. _`stop_kthread.description`:

Description
-----------

This kicks the running hardware latency sampling/detector kernel thread and
tells it to stop sampling now. Use this on unload and at system shutdown.

.. _`hwlat_width_write`:

hwlat_width_write
=================

.. c:function:: ssize_t hwlat_width_write(struct file *filp, const char __user *ubuf, size_t cnt, loff_t *ppos)

    Write function for "width" entry

    :param filp:
        The active open file structure
    :type filp: struct file \*

    :param ubuf:
        The user buffer that contains the value to write
    :type ubuf: const char __user \*

    :param cnt:
        The maximum number of bytes to write to "file"
    :type cnt: size_t

    :param ppos:
        The current position in \ ``file``\ 
    :type ppos: loff_t \*

.. _`hwlat_width_write.description`:

Description
-----------

This function provides a write implementation for the "width" interface
to the hardware latency detector. It can be used to configure
for how many us of the total window us we will actively sample for any
hardware-induced latency periods. Obviously, it is not possible to
sample constantly and have the system respond to a sample reader, or,
worse, without having the system appear to have gone out to lunch. It
is enforced that width is less that the total window size.

.. _`hwlat_window_write`:

hwlat_window_write
==================

.. c:function:: ssize_t hwlat_window_write(struct file *filp, const char __user *ubuf, size_t cnt, loff_t *ppos)

    Write function for "window" entry

    :param filp:
        The active open file structure
    :type filp: struct file \*

    :param ubuf:
        The user buffer that contains the value to write
    :type ubuf: const char __user \*

    :param cnt:
        The maximum number of bytes to write to "file"
    :type cnt: size_t

    :param ppos:
        The current position in \ ``file``\ 
    :type ppos: loff_t \*

.. _`hwlat_window_write.description`:

Description
-----------

This function provides a write implementation for the "window" interface
to the hardware latency detetector. The window is the total time
in us that will be considered one sample period. Conceptually, windows
occur back-to-back and contain a sample width period during which
actual sampling occurs. Can be used to write a new total window size. It
is enfoced that any value written must be greater than the sample width
size, or an error results.

.. _`init_tracefs`:

init_tracefs
============

.. c:function:: int init_tracefs( void)

    A function to initialize the tracefs interface files

    :param void:
        no arguments
    :type void: 

.. _`init_tracefs.description`:

Description
-----------

This function creates entries in tracefs for "hwlat_detector".
It creates the hwlat_detector directory in the tracing directory,
and within that directory is the count, width and window files to
change and view those values.

.. This file was automatic generated / don't edit.

