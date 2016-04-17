.. -*- coding: utf-8; mode: rst -*-

=========
kobject.h
=========


.. _`kset`:

struct kset
===========

.. c:type:: kset

    a set of kobjects of a specific type, belonging to a specific subsystem.


.. _`kset.definition`:

Definition
----------

.. code-block:: c

  struct kset {
    struct list_head list;
    spinlock_t list_lock;
    struct kobject kobj;
    const struct kset_uevent_ops * uevent_ops;
  };


.. _`kset.members`:

Members
-------

:``list``:
    the list of all kobjects for this kset

:``list_lock``:
    a lock for iterating over the kobjects

:``kobj``:
    the embedded kobject for this kset (recursion, isn't it fun...)

:``uevent_ops``:
    the set of uevent operations for this kset.  These are
    called whenever a kobject has something happen to it so that the kset
    can add new environment variables, or filter out the uevents if so
    desired.




.. _`kset.description`:

Description
-----------


A kset defines a group of kobjects.  They can be individually
different "types" but overall these kobjects all want to be grouped
together and operated on in the same manner.  ksets are used to
define the attribute callbacks and other common events that happen to
a kobject.

