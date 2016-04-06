
.. _API-struct-v4l2-ctrl-handler:

========================
struct v4l2_ctrl_handler
========================

*man struct v4l2_ctrl_handler(9)*

*4.6.0-rc1*

The control handler keeps track of all the


Synopsis
========

.. code-block:: c

    struct v4l2_ctrl_handler {
      struct mutex _lock;
      struct mutex * lock;
      struct list_head ctrls;
      struct list_head ctrl_refs;
      struct v4l2_ctrl_ref * cached;
      struct v4l2_ctrl_ref ** buckets;
      v4l2_ctrl_notify_fnc notify;
      void * notify_priv;
      u16 nr_of_buckets;
      int error;
    };


Members
=======

_lock
    Default for “lock”.

lock
    Lock to control access to this handler and its controls. May be replaced by the user right after init.

ctrls
    The list of controls owned by this handler.

ctrl_refs
    The list of control references.

cached
    The last found control reference. It is common that the same control is needed multiple times, so this is a simple optimization.

buckets
    Buckets for the hashing. Allows for quick control lookup.

notify
    A notify callback that is called whenever the control changes value. Note that the handler's lock is held when the notify function is called!

notify_priv
    Passed as argument to the v4l2_ctrl notify callback.

nr_of_buckets
    Total number of buckets in the array.

error
    The error code of the first failed control addition.


controls
========

both the controls owned by the handler and those inherited from other handlers.
