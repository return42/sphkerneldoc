
.. _API-struct-fence-ops:

================
struct fence_ops
================

*man struct fence_ops(9)*

*4.6.0-rc1*

operations implemented for fence


Synopsis
========

.. code-block:: c

    struct fence_ops {
      const char * (* get_driver_name) (struct fence *fence);
      const char * (* get_timeline_name) (struct fence *fence);
      bool (* enable_signaling) (struct fence *fence);
      bool (* signaled) (struct fence *fence);
      signed long (* wait) (struct fence *fence, bool intr, signed long timeout);
      void (* release) (struct fence *fence);
      int (* fill_driver_data) (struct fence *fence, void *data, int size);
      void (* fence_value_str) (struct fence *fence, char *str, int size);
      void (* timeline_value_str) (struct fence *fence, char *str, int size);
    };


Members
=======

get_driver_name
    returns the driver name.

get_timeline_name
    return the name of the context this fence belongs to.

enable_signaling
    enable software signaling of fence.

signaled
    [optional] peek whether the fence is signaled, can be null.

wait
    custom wait implementation, or fence_default_wait.

release
    [optional] called on destruction of fence, can be null

fill_driver_data
    [optional] callback to fill in free-form debug info Returns amount of bytes filled, or -errno.

fence_value_str
    [optional] fills in the value of the fence as a string

timeline_value_str
    [optional] fills in the current value of the timeline as a string


Notes on enable_signaling
=========================

For fence implementations that have the capability for hw->hw signaling, they can implement this op to enable the necessary irqs, or insert commands into cmdstream, etc. This is
called in the first ``wait`` or ``add_callback`` path to let the fence implementation know that there is another driver waiting on the signal (ie. hw->sw case).

This function can be called called from atomic context, but not from irq context, so normal spinlocks can be used.

A return value of false indicates the fence already passed, or some failure occurred that made it impossible to enable signaling. True indicates successful enabling.

fence->status may be set in enable_signaling, but only when false is returned.

Calling fence_signal before enable_signaling is called allows for a tiny race window in which enable_signaling is called during, before, or after fence_signal. To fight this,
it is recommended that before enable_signaling returns true an extra reference is taken on the fence, to be released when the fence is signaled. This will mean fence_signal will
still be called twice, but the second time will be a noop since it was already signaled.


Notes on signaled
=================

May set fence->status if returning true.


Notes on wait
=============

Must not be NULL, set to fence_default_wait for default implementation. the fence_default_wait implementation should work for any fence, as long as enable_signaling works
correctly.

Must return -ERESTARTSYS if the wait is intr = true and the wait was interrupted, and remaining jiffies if fence has signaled, or 0 if wait timed out. Can also return other error
values on custom implementations, which should be treated as if the fence is signaled. For example a hardware lockup could be reported like that.


Notes on release
================

Can be NULL, this function allows additional commands to run on destruction of the fence. Can be called from irq context. If pointer is set to NULL, kfree will get called instead.
