.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/most/mostcore/core.c

.. _`list_pop_mbo`:

list_pop_mbo
============

.. c:function::  list_pop_mbo( ptr)

    retrieves the first MBO of the list and removes it

    :param  ptr:
        the list head to grab the MBO from.

.. _`most_c_attr`:

struct most_c_attr
==================

.. c:type:: struct most_c_attr

    to access the attributes of a channel object

.. _`most_c_attr.definition`:

Definition
----------

.. code-block:: c

    struct most_c_attr {
        struct attribute attr;
        ssize_t (* show) (struct most_c_obj *d,struct most_c_attr *attr,char *buf);
        ssize_t (* store) (struct most_c_obj *d,struct most_c_attr *attr,const char *buf,size_t count);
    }

.. _`most_c_attr.members`:

Members
-------

attr
    attributes of a channel

show
    pointer to the show function

store
    pointer to the store function

.. _`channel_attr_show`:

channel_attr_show
=================

.. c:function:: ssize_t channel_attr_show(struct kobject *kobj, struct attribute *attr, char *buf)

    show function of channel object

    :param struct kobject \*kobj:
        pointer to its kobject

    :param struct attribute \*attr:
        pointer to its attributes

    :param char \*buf:
        buffer

.. _`channel_attr_store`:

channel_attr_store
==================

.. c:function:: ssize_t channel_attr_store(struct kobject *kobj, struct attribute *attr, const char *buf, size_t len)

    store function of channel object

    :param struct kobject \*kobj:
        pointer to its kobject

    :param struct attribute \*attr:
        pointer to its attributes

    :param const char \*buf:
        buffer

    :param size_t len:
        length of buffer

.. _`most_free_mbo_coherent`:

most_free_mbo_coherent
======================

.. c:function:: void most_free_mbo_coherent(struct mbo *mbo)

    free an MBO and its coherent buffer

    :param struct mbo \*mbo:
        buffer to be released

.. _`flush_channel_fifos`:

flush_channel_fifos
===================

.. c:function:: void flush_channel_fifos(struct most_c_obj *c)

    clear the channel fifos

    :param struct most_c_obj \*c:
        pointer to channel object

.. _`flush_trash_fifo`:

flush_trash_fifo
================

.. c:function:: int flush_trash_fifo(struct most_c_obj *c)

    clear the trash fifo

    :param struct most_c_obj \*c:
        pointer to channel object

.. _`most_channel_release`:

most_channel_release
====================

.. c:function:: void most_channel_release(struct kobject *kobj)

    release function of channel object

    :param struct kobject \*kobj:
        pointer to channel's kobject

.. _`create_most_c_obj`:

create_most_c_obj
=================

.. c:function:: struct most_c_obj *create_most_c_obj(const char *name, struct kobject *parent)

    allocates a channel object

    :param const char \*name:
        name of the channel object

    :param struct kobject \*parent:
        parent kobject

.. _`create_most_c_obj.description`:

Description
-----------

This create a channel object and registers it with sysfs.
Returns a pointer to the object or NULL when something went wrong.

.. _`most_inst_attribute`:

struct most_inst_attribute
==========================

.. c:type:: struct most_inst_attribute

    to access the attributes of instance object

.. _`most_inst_attribute.definition`:

Definition
----------

.. code-block:: c

    struct most_inst_attribute {
        struct attribute attr;
        ssize_t (* show) (struct most_inst_obj *d,struct most_inst_attribute *attr,char *buf);
        ssize_t (* store) (struct most_inst_obj *d,struct most_inst_attribute *attr,const char *buf,size_t count);
    }

.. _`most_inst_attribute.members`:

Members
-------

attr
    attributes of an instance

show
    pointer to the show function

store
    pointer to the store function

.. _`instance_attr_show`:

instance_attr_show
==================

.. c:function:: ssize_t instance_attr_show(struct kobject *kobj, struct attribute *attr, char *buf)

    show function for an instance object

    :param struct kobject \*kobj:
        pointer to kobject

    :param struct attribute \*attr:
        pointer to attribute struct

    :param char \*buf:
        buffer

.. _`instance_attr_store`:

instance_attr_store
===================

.. c:function:: ssize_t instance_attr_store(struct kobject *kobj, struct attribute *attr, const char *buf, size_t len)

    store function for an instance object

    :param struct kobject \*kobj:
        pointer to kobject

    :param struct attribute \*attr:
        pointer to attribute struct

    :param const char \*buf:
        buffer

    :param size_t len:
        length of buffer

.. _`most_inst_release`:

most_inst_release
=================

.. c:function:: void most_inst_release(struct kobject *kobj)

    release function for instance object

    :param struct kobject \*kobj:
        pointer to instance's kobject

.. _`most_inst_release.description`:

Description
-----------

This frees the allocated memory for the instance object

.. _`create_most_inst_obj`:

create_most_inst_obj
====================

.. c:function:: struct most_inst_obj *create_most_inst_obj(const char *name)

    creates an instance object

    :param const char \*name:
        name of the object to be created

.. _`create_most_inst_obj.description`:

Description
-----------

This allocates memory for an instance structure, assigns the proper kset
and registers it with sysfs.

Returns a pointer to the instance object or NULL when something went wrong.

.. _`destroy_most_inst_obj`:

destroy_most_inst_obj
=====================

.. c:function:: void destroy_most_inst_obj(struct most_inst_obj *inst)

    MOST instance release function

    :param struct most_inst_obj \*inst:
        pointer to the instance object

.. _`destroy_most_inst_obj.description`:

Description
-----------

This decrements the reference counter of the instance object.
If the reference count turns zero, its release function is called

.. _`most_aim_attribute`:

struct most_aim_attribute
=========================

.. c:type:: struct most_aim_attribute

    to access the attributes of AIM object

.. _`most_aim_attribute.definition`:

Definition
----------

.. code-block:: c

    struct most_aim_attribute {
        struct attribute attr;
        ssize_t (* show) (struct most_aim_obj *d,struct most_aim_attribute *attr,char *buf);
        ssize_t (* store) (struct most_aim_obj *d,struct most_aim_attribute *attr,const char *buf,size_t count);
    }

.. _`most_aim_attribute.members`:

Members
-------

attr
    attributes of an AIM

show
    pointer to the show function

store
    pointer to the store function

.. _`aim_attr_show`:

aim_attr_show
=============

.. c:function:: ssize_t aim_attr_show(struct kobject *kobj, struct attribute *attr, char *buf)

    show function of an AIM object

    :param struct kobject \*kobj:
        pointer to kobject

    :param struct attribute \*attr:
        pointer to attribute struct

    :param char \*buf:
        buffer

.. _`aim_attr_store`:

aim_attr_store
==============

.. c:function:: ssize_t aim_attr_store(struct kobject *kobj, struct attribute *attr, const char *buf, size_t len)

    store function of an AIM object

    :param struct kobject \*kobj:
        pointer to kobject

    :param struct attribute \*attr:
        pointer to attribute struct

    :param const char \*buf:
        buffer

    :param size_t len:
        length of buffer

.. _`most_aim_release`:

most_aim_release
================

.. c:function:: void most_aim_release(struct kobject *kobj)

    AIM release function

    :param struct kobject \*kobj:
        pointer to AIM's kobject

.. _`split_string`:

split_string
============

.. c:function:: int split_string(char *buf, char **a, char **b, char **c)

    parses and changes string in the buffer buf and splits it into two mandatory and one optional substrings.

    :param char \*buf:
        complete string from attribute 'add_channel'

    :param char \*\*a:
        address of pointer to 1st substring (=instance name)

    :param char \*\*b:
        address of pointer to 2nd substring (=channel name)

    :param char \*\*c:
        optional address of pointer to 3rd substring (=user defined name)

.. _`split_string.examples`:

Examples
--------


Input: "mdev0:ch0\ ``ep_81``\ :my_channel\n" or
"mdev0:ch0\ ``ep_81``\ :my_channel"

.. _`split_string.output`:

Output
------

\*a -> "mdev0", \*b -> "ch0\ ``ep_81``\ ", \*c -> "my_channel"

Input: "mdev0:ch0\ ``ep_81``\ \n"

\*a -> "mdev0", \*b -> "ch0\ ``ep_81``\ ", \*c -> ""

Input: "mdev0:ch0\ ``ep_81``\ "

\*a -> "mdev0", \*b -> "ch0\ ``ep_81``\ ", \*c == NULL

.. _`get_channel_by_name`:

get_channel_by_name
===================

.. c:function:: struct most_c_obj *get_channel_by_name(char *mdev, char *mdev_ch)

    get pointer to channel object

    :param char \*mdev:
        name of the device instance

    :param char \*mdev_ch:
        name of the respective channel

.. _`get_channel_by_name.description`:

Description
-----------

This retrieves the pointer to a channel object.

.. _`store_add_link`:

store_add_link
==============

.. c:function:: ssize_t store_add_link(struct most_aim_obj *aim_obj, struct most_aim_attribute *attr, const char *buf, size_t len)

    \ :c:func:`store`\  function for add_link attribute

    :param struct most_aim_obj \*aim_obj:
        pointer to AIM object

    :param struct most_aim_attribute \*attr:
        its attributes

    :param const char \*buf:
        buffer

    :param size_t len:
        buffer length

.. _`store_add_link.description`:

Description
-----------

This parses the string given by buf and splits it into
three substrings. Note: third substring is optional. In case a cdev
AIM is loaded the optional 3rd substring will make up the name of
device node in the /dev directory. If omitted, the device node will
inherit the channel's name within sysfs.

Searches for a pair of device and channel and probes the AIM

.. _`store_add_link.example`:

Example
-------

.. code-block:: c

    (1) echo -n -e "mdev0:ch0@ep_81:my_rxchannel\n" >add_link
    (2) echo -n -e "mdev0:ch0@ep_81\n" >add_link

    (1) would create the device node /dev/my_rxchannel
    (2) would create the device node /dev/mdev0-ch0@ep_81


.. _`store_remove_link`:

store_remove_link
=================

.. c:function:: ssize_t store_remove_link(struct most_aim_obj *aim_obj, struct most_aim_attribute *attr, const char *buf, size_t len)

    store function for remove_link attribute

    :param struct most_aim_obj \*aim_obj:
        pointer to AIM object

    :param struct most_aim_attribute \*attr:
        its attributes

    :param const char \*buf:
        buffer

    :param size_t len:
        buffer length

.. _`store_remove_link.example`:

Example
-------

.. code-block:: c

    echo -n -e "mdev0:ch0@ep_81\n" >remove_link


.. _`create_most_aim_obj`:

create_most_aim_obj
===================

.. c:function:: struct most_aim_obj *create_most_aim_obj(const char *name)

    creates an AIM object

    :param const char \*name:
        name of the AIM

.. _`create_most_aim_obj.description`:

Description
-----------

This creates an AIM object assigns the proper kset and registers
it with sysfs.
Returns a pointer to the object or NULL if something went wrong.

.. _`destroy_most_aim_obj`:

destroy_most_aim_obj
====================

.. c:function:: void destroy_most_aim_obj(struct most_aim_obj *p)

    AIM release function

    :param struct most_aim_obj \*p:
        pointer to AIM object

.. _`destroy_most_aim_obj.description`:

Description
-----------

This decrements the reference counter of the AIM object. If the
reference count turns zero, its release function will be called.

.. _`arm_mbo`:

arm_mbo
=======

.. c:function:: void arm_mbo(struct mbo *mbo)

    recycle MBO for further usage

    :param struct mbo \*mbo:
        buffer object

.. _`arm_mbo.description`:

Description
-----------

This puts an MBO back to the list to have it ready for up coming
tx transactions.

In case the MBO belongs to a channel that recently has been
poisoned, the MBO is scheduled to be trashed.
Calls the completion handler of an attached AIM.

.. _`arm_mbo_chain`:

arm_mbo_chain
=============

.. c:function:: int arm_mbo_chain(struct most_c_obj *c, int dir, void (*) compl (struct mbo *)

    helper function that arms an MBO chain for the HDM

    :param struct most_c_obj \*c:
        pointer to interface channel

    :param int dir:
        direction of the channel

    :param (void (\*) compl (struct mbo \*):
        pointer to completion function

.. _`arm_mbo_chain.description`:

Description
-----------

This allocates buffer objects including the containing DMA coherent
buffer and puts them in the fifo.
Buffers of Rx channels are put in the kthread fifo, hence immediately
submitted to the HDM.

Returns the number of allocated and enqueued MBOs.

.. _`most_submit_mbo`:

most_submit_mbo
===============

.. c:function:: int most_submit_mbo(struct mbo *mbo)

    submits an MBO to fifo

    :param struct mbo \*mbo:
        pointer to the MBO

.. _`most_write_completion`:

most_write_completion
=====================

.. c:function:: void most_write_completion(struct mbo *mbo)

    write completion handler

    :param struct mbo \*mbo:
        pointer to MBO

.. _`most_write_completion.description`:

Description
-----------

This recycles the MBO for further usage. In case the channel has been
poisoned, the MBO is scheduled to be trashed.

.. _`get_channel_by_iface`:

get_channel_by_iface
====================

.. c:function:: struct most_c_obj *get_channel_by_iface(struct most_interface *iface, int id)

    get pointer to channel object

    :param struct most_interface \*iface:
        pointer to interface instance

    :param int id:
        channel ID

.. _`get_channel_by_iface.description`:

Description
-----------

This retrieves a pointer to a channel of the given interface and channel ID.

.. _`most_get_mbo`:

most_get_mbo
============

.. c:function:: struct mbo *most_get_mbo(struct most_interface *iface, int id, struct most_aim *aim)

    get pointer to an MBO of pool

    :param struct most_interface \*iface:
        pointer to interface instance

    :param int id:
        channel ID

    :param struct most_aim \*aim:
        *undescribed*

.. _`most_get_mbo.description`:

Description
-----------

This attempts to get a free buffer out of the channel fifo.
Returns a pointer to MBO on success or NULL otherwise.

.. _`most_put_mbo`:

most_put_mbo
============

.. c:function:: void most_put_mbo(struct mbo *mbo)

    return buffer to pool

    :param struct mbo \*mbo:
        buffer object

.. _`most_read_completion`:

most_read_completion
====================

.. c:function:: void most_read_completion(struct mbo *mbo)

    read completion handler

    :param struct mbo \*mbo:
        pointer to MBO

.. _`most_read_completion.description`:

Description
-----------

This function is called by the HDM when data has been received from the
hardware and copied to the buffer of the MBO.

In case the channel has been poisoned it puts the buffer in the trash queue.
Otherwise, it passes the buffer to an AIM for further processing.

.. _`most_start_channel`:

most_start_channel
==================

.. c:function:: int most_start_channel(struct most_interface *iface, int id, struct most_aim *aim)

    prepares a channel for communication

    :param struct most_interface \*iface:
        pointer to interface instance

    :param int id:
        channel ID

    :param struct most_aim \*aim:
        *undescribed*

.. _`most_start_channel.description`:

Description
-----------

This prepares the channel for usage. Cross-checks whether the
channel's been properly configured.

Returns 0 on success or error code otherwise.

.. _`most_stop_channel`:

most_stop_channel
=================

.. c:function:: int most_stop_channel(struct most_interface *iface, int id, struct most_aim *aim)

    stops a running channel

    :param struct most_interface \*iface:
        pointer to interface instance

    :param int id:
        channel ID

    :param struct most_aim \*aim:
        *undescribed*

.. _`most_register_aim`:

most_register_aim
=================

.. c:function:: int most_register_aim(struct most_aim *aim)

    registers an AIM (driver) with the core

    :param struct most_aim \*aim:
        instance of AIM to be registered

.. _`most_deregister_aim`:

most_deregister_aim
===================

.. c:function:: int most_deregister_aim(struct most_aim *aim)

    deregisters an AIM (driver) with the core

    :param struct most_aim \*aim:
        AIM to be removed

.. _`most_register_interface`:

most_register_interface
=======================

.. c:function:: struct kobject *most_register_interface(struct most_interface *iface)

    registers an interface with core

    :param struct most_interface \*iface:
        pointer to the instance of the interface description.

.. _`most_register_interface.description`:

Description
-----------

Allocates and initializes a new interface instance and all of its channels.
Returns a pointer to kobject or an error pointer.

.. _`most_deregister_interface`:

most_deregister_interface
=========================

.. c:function:: void most_deregister_interface(struct most_interface *iface)

    deregisters an interface with core

    :param struct most_interface \*iface:
        pointer to the interface instance description.

.. _`most_deregister_interface.description`:

Description
-----------

Before removing an interface instance from the list, all running
channels are stopped and poisoned.

.. _`most_stop_enqueue`:

most_stop_enqueue
=================

.. c:function:: void most_stop_enqueue(struct most_interface *iface, int id)

    prevents core from enqueueing MBOs

    :param struct most_interface \*iface:
        pointer to interface

    :param int id:
        channel id

.. _`most_stop_enqueue.description`:

Description
-----------

This is called by an HDM that \_cannot\_ attend to its duties and
is imminent to get run over by the core. The core is not going to
enqueue any further packets unless the flagging HDM calls
most_resume \ :c:func:`enqueue`\ .

.. _`most_resume_enqueue`:

most_resume_enqueue
===================

.. c:function:: void most_resume_enqueue(struct most_interface *iface, int id)

    allow core to enqueue MBOs again

    :param struct most_interface \*iface:
        pointer to interface

    :param int id:
        channel id

.. _`most_resume_enqueue.description`:

Description
-----------

This clears the enqueue halt flag and enqueues all MBOs currently
sitting in the wait fifo.

.. This file was automatic generated / don't edit.

