.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/parisc/pdc_stable.c

.. _`pdcspath_fetch`:

pdcspath_fetch
==============

.. c:function:: int pdcspath_fetch(struct pdcspath_entry *entry)

    This function populates the path entry structs.

    :param entry:
        A pointer to an allocated pdcspath_entry.
    :type entry: struct pdcspath_entry \*

.. _`pdcspath_fetch.description`:

Description
-----------

The general idea is that you don't read from the Stable Storage every time
you access the files provided by the facilities. We store a copy of the
content of the stable storage WRT various paths in these structs. We read
these structs when reading the files, and we will write to these structs when
writing to the files, and only then write them back to the Stable Storage.

This function expects to be called with \ ``entry->rw_lock``\  write-hold.

.. _`pdcspath_store`:

pdcspath_store
==============

.. c:function:: void pdcspath_store(struct pdcspath_entry *entry)

    This function writes a path to stable storage.

    :param entry:
        A pointer to an allocated pdcspath_entry.
    :type entry: struct pdcspath_entry \*

.. _`pdcspath_store.it-can-be-used-in-two-ways`:

It can be used in two ways
--------------------------

either by passing it a preset devpath struct
containing an already computed hardware path, or by passing it a device
pointer, from which it'll find out the corresponding hardware path.
For now we do not handle the case where there's an error in writing to the
Stable Storage area, so you'd better not mess up the data :P

This function expects to be called with \ ``entry->rw_lock``\  write-hold.

.. _`pdcspath_hwpath_read`:

pdcspath_hwpath_read
====================

.. c:function:: ssize_t pdcspath_hwpath_read(struct pdcspath_entry *entry, char *buf)

    This function handles hardware path pretty printing.

    :param entry:
        An allocated and populated pdscpath_entry struct.
    :type entry: struct pdcspath_entry \*

    :param buf:
        The output buffer to write to.
    :type buf: char \*

.. _`pdcspath_hwpath_read.description`:

Description
-----------

We will call this function to format the output of the hwpath attribute file.

.. _`pdcspath_hwpath_write`:

pdcspath_hwpath_write
=====================

.. c:function:: ssize_t pdcspath_hwpath_write(struct pdcspath_entry *entry, const char *buf, size_t count)

    This function handles hardware path modifying.

    :param entry:
        An allocated and populated pdscpath_entry struct.
    :type entry: struct pdcspath_entry \*

    :param buf:
        The input buffer to read from.
    :type buf: const char \*

    :param count:
        The number of bytes to be read.
    :type count: size_t

.. _`pdcspath_hwpath_write.description`:

Description
-----------

We will call this function to change the current hardware path.
Hardware paths are to be given '/'-delimited, without brackets.
We make sure that the provided path actually maps to an existing
device, BUT nothing would prevent some foolish user to set the path to some
PCI bridge or even a CPU...
A better work around would be to make sure we are at the end of a device tree
for instance, but it would be IMHO beyond the simple scope of that driver.
The aim is to provide a facility. Data correctness is left to userland.

.. _`pdcspath_layer_read`:

pdcspath_layer_read
===================

.. c:function:: ssize_t pdcspath_layer_read(struct pdcspath_entry *entry, char *buf)

    Extended layer (eg. SCSI ids) pretty printing.

    :param entry:
        An allocated and populated pdscpath_entry struct.
    :type entry: struct pdcspath_entry \*

    :param buf:
        The output buffer to write to.
    :type buf: char \*

.. _`pdcspath_layer_read.description`:

Description
-----------

We will call this function to format the output of the layer attribute file.

.. _`pdcspath_layer_write`:

pdcspath_layer_write
====================

.. c:function:: ssize_t pdcspath_layer_write(struct pdcspath_entry *entry, const char *buf, size_t count)

    This function handles extended layer modifying.

    :param entry:
        An allocated and populated pdscpath_entry struct.
    :type entry: struct pdcspath_entry \*

    :param buf:
        The input buffer to read from.
    :type buf: const char \*

    :param count:
        The number of bytes to be read.
    :type count: size_t

.. _`pdcspath_layer_write.description`:

Description
-----------

We will call this function to change the current layer value.
Layers are to be given '.'-delimited, without brackets.
XXX beware we are far less checky WRT input data provided than for hwpath.
Potential harm can be done, since there's no way to check the validity of
the layer fields.

.. _`pdcspath_attr_show`:

pdcspath_attr_show
==================

.. c:function:: ssize_t pdcspath_attr_show(struct kobject *kobj, struct attribute *attr, char *buf)

    Generic read function call wrapper.

    :param kobj:
        The kobject to get info from.
    :type kobj: struct kobject \*

    :param attr:
        The attribute looked upon.
    :type attr: struct attribute \*

    :param buf:
        The output buffer.
    :type buf: char \*

.. _`pdcspath_attr_store`:

pdcspath_attr_store
===================

.. c:function:: ssize_t pdcspath_attr_store(struct kobject *kobj, struct attribute *attr, const char *buf, size_t count)

    Generic write function call wrapper.

    :param kobj:
        The kobject to write info to.
    :type kobj: struct kobject \*

    :param attr:
        The attribute to be modified.
    :type attr: struct attribute \*

    :param buf:
        The input buffer.
    :type buf: const char \*

    :param count:
        The size of the buffer.
    :type count: size_t

.. _`pdcs_size_read`:

pdcs_size_read
==============

.. c:function:: ssize_t pdcs_size_read(struct kobject *kobj, struct kobj_attribute *attr, char *buf)

    Stable Storage size output.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The output buffer to write to.
    :type buf: char \*

.. _`pdcs_auto_read`:

pdcs_auto_read
==============

.. c:function:: ssize_t pdcs_auto_read(struct kobject *kobj, struct kobj_attribute *attr, char *buf, int knob)

    Stable Storage autoboot/search flag output.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The output buffer to write to.
    :type buf: char \*

    :param knob:
        The PF_AUTOBOOT or PF_AUTOSEARCH flag
    :type knob: int

.. _`pdcs_autoboot_read`:

pdcs_autoboot_read
==================

.. c:function:: ssize_t pdcs_autoboot_read(struct kobject *kobj, struct kobj_attribute *attr, char *buf)

    Stable Storage autoboot flag output.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The output buffer to write to.
    :type buf: char \*

.. _`pdcs_autosearch_read`:

pdcs_autosearch_read
====================

.. c:function:: ssize_t pdcs_autosearch_read(struct kobject *kobj, struct kobj_attribute *attr, char *buf)

    Stable Storage autoboot flag output.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The output buffer to write to.
    :type buf: char \*

.. _`pdcs_timer_read`:

pdcs_timer_read
===============

.. c:function:: ssize_t pdcs_timer_read(struct kobject *kobj, struct kobj_attribute *attr, char *buf)

    Stable Storage timer count output (in seconds).

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The output buffer to write to.
    :type buf: char \*

.. _`pdcs_timer_read.description`:

Description
-----------

The value of the timer field correponds to a number of seconds in powers of 2.

.. _`pdcs_osid_read`:

pdcs_osid_read
==============

.. c:function:: ssize_t pdcs_osid_read(struct kobject *kobj, struct kobj_attribute *attr, char *buf)

    Stable Storage OS ID register output.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The output buffer to write to.
    :type buf: char \*

.. _`pdcs_osdep1_read`:

pdcs_osdep1_read
================

.. c:function:: ssize_t pdcs_osdep1_read(struct kobject *kobj, struct kobj_attribute *attr, char *buf)

    Stable Storage OS-Dependent data area 1 output.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The output buffer to write to.
    :type buf: char \*

.. _`pdcs_osdep1_read.description`:

Description
-----------

This can hold 16 bytes of OS-Dependent data.

.. _`pdcs_diagnostic_read`:

pdcs_diagnostic_read
====================

.. c:function:: ssize_t pdcs_diagnostic_read(struct kobject *kobj, struct kobj_attribute *attr, char *buf)

    Stable Storage Diagnostic register output.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The output buffer to write to.
    :type buf: char \*

.. _`pdcs_diagnostic_read.description`:

Description
-----------

I have NFC how to interpret the content of that register ;-).

.. _`pdcs_fastsize_read`:

pdcs_fastsize_read
==================

.. c:function:: ssize_t pdcs_fastsize_read(struct kobject *kobj, struct kobj_attribute *attr, char *buf)

    Stable Storage FastSize register output.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The output buffer to write to.
    :type buf: char \*

.. _`pdcs_fastsize_read.description`:

Description
-----------

This register holds the amount of system RAM to be tested during boot sequence.

.. _`pdcs_osdep2_read`:

pdcs_osdep2_read
================

.. c:function:: ssize_t pdcs_osdep2_read(struct kobject *kobj, struct kobj_attribute *attr, char *buf)

    Stable Storage OS-Dependent data area 2 output.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The output buffer to write to.
    :type buf: char \*

.. _`pdcs_osdep2_read.description`:

Description
-----------

This can hold pdcs_size - 224 bytes of OS-Dependent data, when available.

.. _`pdcs_auto_write`:

pdcs_auto_write
===============

.. c:function:: ssize_t pdcs_auto_write(struct kobject *kobj, struct kobj_attribute *attr, const char *buf, size_t count, int knob)

    This function handles autoboot/search flag modifying.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The input buffer to read from.
    :type buf: const char \*

    :param count:
        The number of bytes to be read.
    :type count: size_t

    :param knob:
        The PF_AUTOBOOT or PF_AUTOSEARCH flag
    :type knob: int

.. _`pdcs_auto_write.description`:

Description
-----------

We will call this function to change the current autoboot flag.

.. _`pdcs_auto_write.we-expect-a-precise-syntax`:

We expect a precise syntax
--------------------------

\"n\" (n == 0 or 1) to toggle AutoBoot Off or On

.. _`pdcs_autoboot_write`:

pdcs_autoboot_write
===================

.. c:function:: ssize_t pdcs_autoboot_write(struct kobject *kobj, struct kobj_attribute *attr, const char *buf, size_t count)

    This function handles autoboot flag modifying.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The input buffer to read from.
    :type buf: const char \*

    :param count:
        The number of bytes to be read.
    :type count: size_t

.. _`pdcs_autoboot_write.description`:

Description
-----------

We will call this function to change the current boot flags.

.. _`pdcs_autoboot_write.we-expect-a-precise-syntax`:

We expect a precise syntax
--------------------------

\"n\" (n == 0 or 1) to toggle AutoSearch Off or On

.. _`pdcs_autosearch_write`:

pdcs_autosearch_write
=====================

.. c:function:: ssize_t pdcs_autosearch_write(struct kobject *kobj, struct kobj_attribute *attr, const char *buf, size_t count)

    This function handles autosearch flag modifying.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The input buffer to read from.
    :type buf: const char \*

    :param count:
        The number of bytes to be read.
    :type count: size_t

.. _`pdcs_autosearch_write.description`:

Description
-----------

We will call this function to change the current boot flags.

.. _`pdcs_autosearch_write.we-expect-a-precise-syntax`:

We expect a precise syntax
--------------------------

\"n\" (n == 0 or 1) to toggle AutoSearch Off or On

.. _`pdcs_osdep1_write`:

pdcs_osdep1_write
=================

.. c:function:: ssize_t pdcs_osdep1_write(struct kobject *kobj, struct kobj_attribute *attr, const char *buf, size_t count)

    Stable Storage OS-Dependent data area 1 input.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The input buffer to read from.
    :type buf: const char \*

    :param count:
        The number of bytes to be read.
    :type count: size_t

.. _`pdcs_osdep1_write.description`:

Description
-----------

This can store 16 bytes of OS-Dependent data. We use a byte-by-byte
write approach. It's up to userspace to deal with it when constructing
its input buffer.

.. _`pdcs_osdep2_write`:

pdcs_osdep2_write
=================

.. c:function:: ssize_t pdcs_osdep2_write(struct kobject *kobj, struct kobj_attribute *attr, const char *buf, size_t count)

    Stable Storage OS-Dependent data area 2 input.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        The input buffer to read from.
    :type buf: const char \*

    :param count:
        The number of bytes to be read.
    :type count: size_t

.. _`pdcs_osdep2_write.description`:

Description
-----------

This can store pdcs_size - 224 bytes of OS-Dependent data. We use a
byte-by-byte write approach. It's up to userspace to deal with it when
constructing its input buffer.

.. _`pdcs_register_pathentries`:

pdcs_register_pathentries
=========================

.. c:function:: int pdcs_register_pathentries( void)

    Prepares path entries kobjects for sysfs usage.

    :param void:
        no arguments
    :type void: 

.. _`pdcs_register_pathentries.description`:

Description
-----------

It creates kobjects corresponding to each path entry with nice sysfs
links to the real device. This is where the magic takes place: when
registering the subsystem attributes during module init, each kobject hereby
created will show in the sysfs tree as a folder containing files as defined
by path_subsys_attr[].

.. _`pdcs_unregister_pathentries`:

pdcs_unregister_pathentries
===========================

.. c:function:: void pdcs_unregister_pathentries( void)

    Routine called when unregistering the module.

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

