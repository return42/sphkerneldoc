.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_devinfo.c

.. _`scsi_dev_info_list_add`:

scsi_dev_info_list_add
======================

.. c:function:: int scsi_dev_info_list_add(int compatible, char *vendor, char *model, char *strflags, blist_flags_t flags)

    add one dev_info list entry.

    :param compatible:
        if true, null terminate short strings.  Otherwise space pad.
    :type compatible: int

    :param vendor:
        vendor string
    :type vendor: char \*

    :param model:
        model (product) string
    :type model: char \*

    :param strflags:
        integer string
    :type strflags: char \*

    :param flags:
        if strflags NULL, use this flag value
    :type flags: blist_flags_t

.. _`scsi_dev_info_list_add.description`:

Description
-----------

     Create and add one dev_info entry for \ ``vendor``\ , \ ``model``\ , \ ``strflags``\  or
     \ ``flag``\ . If \ ``compatible``\ , add to the tail of the list, do not space
     pad, and set devinfo->compatible. The scsi_static_device_list entries
     are added with \ ``compatible``\  1 and \ ``clfags``\  NULL.

.. _`scsi_dev_info_list_add.return`:

Return
------

0 OK, -error on failure.

.. _`scsi_dev_info_list_add_keyed`:

scsi_dev_info_list_add_keyed
============================

.. c:function:: int scsi_dev_info_list_add_keyed(int compatible, char *vendor, char *model, char *strflags, blist_flags_t flags, enum scsi_devinfo_key key)

    add one dev_info list entry.

    :param compatible:
        if true, null terminate short strings.  Otherwise space pad.
    :type compatible: int

    :param vendor:
        vendor string
    :type vendor: char \*

    :param model:
        model (product) string
    :type model: char \*

    :param strflags:
        integer string
    :type strflags: char \*

    :param flags:
        if strflags NULL, use this flag value
    :type flags: blist_flags_t

    :param key:
        specify list to use
    :type key: enum scsi_devinfo_key

.. _`scsi_dev_info_list_add_keyed.description`:

Description
-----------

     Create and add one dev_info entry for \ ``vendor``\ , \ ``model``\ ,
     \ ``strflags``\  or \ ``flag``\  in list specified by \ ``key``\ . If \ ``compatible``\ ,
     add to the tail of the list, do not space pad, and set
     devinfo->compatible. The scsi_static_device_list entries are
     added with \ ``compatible``\  1 and \ ``clfags``\  NULL.

.. _`scsi_dev_info_list_add_keyed.return`:

Return
------

0 OK, -error on failure.

.. _`scsi_dev_info_list_find`:

scsi_dev_info_list_find
=======================

.. c:function:: struct scsi_dev_info_list *scsi_dev_info_list_find(const char *vendor, const char *model, enum scsi_devinfo_key key)

    find a matching dev_info list entry.

    :param vendor:
        full vendor string
    :type vendor: const char \*

    :param model:
        full model (product) string
    :type model: const char \*

    :param key:
        specify list to use
    :type key: enum scsi_devinfo_key

.. _`scsi_dev_info_list_find.description`:

Description
-----------

     Finds the first dev_info entry matching \ ``vendor``\ , \ ``model``\ 
     in list specified by \ ``key``\ .

.. _`scsi_dev_info_list_find.return`:

Return
------

pointer to matching entry, or ERR_PTR on failure.

.. _`scsi_dev_info_list_del_keyed`:

scsi_dev_info_list_del_keyed
============================

.. c:function:: int scsi_dev_info_list_del_keyed(char *vendor, char *model, enum scsi_devinfo_key key)

    remove one dev_info list entry.

    :param vendor:
        vendor string
    :type vendor: char \*

    :param model:
        model (product) string
    :type model: char \*

    :param key:
        specify list to use
    :type key: enum scsi_devinfo_key

.. _`scsi_dev_info_list_del_keyed.description`:

Description
-----------

     Remove and destroy one dev_info entry for \ ``vendor``\ , \ ``model``\ 
     in list specified by \ ``key``\ .

.. _`scsi_dev_info_list_del_keyed.return`:

Return
------

0 OK, -error on failure.

.. _`scsi_dev_info_list_add_str`:

scsi_dev_info_list_add_str
==========================

.. c:function:: int scsi_dev_info_list_add_str(char *dev_list)

    parse dev_list and add to the scsi_dev_info_list.

    :param dev_list:
        string of device flags to add
    :type dev_list: char \*

.. _`scsi_dev_info_list_add_str.description`:

Description
-----------

     Parse dev_list, and add entries to the scsi_dev_info_list.
     dev_list is of the form "vendor:product:flag,vendor:product:flag".
     dev_list is modified via strsep. Can be called for command line
     addition, for proc or mabye a sysfs interface.

.. _`scsi_dev_info_list_add_str.return`:

Return
------

0 if OK, -error on failure.

.. _`scsi_get_device_flags`:

scsi_get_device_flags
=====================

.. c:function:: blist_flags_t scsi_get_device_flags(struct scsi_device *sdev, const unsigned char *vendor, const unsigned char *model)

    get device specific flags from the dynamic device list.

    :param sdev:
        \ :c:type:`struct scsi_device <scsi_device>`\  to get flags for
    :type sdev: struct scsi_device \*

    :param vendor:
        vendor name
    :type vendor: const unsigned char \*

    :param model:
        model name
    :type model: const unsigned char \*

.. _`scsi_get_device_flags.description`:

Description
-----------

    Search the global scsi_dev_info_list (specified by list zero)
    for an entry matching \ ``vendor``\  and \ ``model``\ , if found, return the
    matching flags value, else return the host or global default
    settings.  Called during scan time.

.. _`scsi_get_device_flags_keyed`:

scsi_get_device_flags_keyed
===========================

.. c:function:: blist_flags_t scsi_get_device_flags_keyed(struct scsi_device *sdev, const unsigned char *vendor, const unsigned char *model, enum scsi_devinfo_key key)

    get device specific flags from the dynamic device list

    :param sdev:
        \ :c:type:`struct scsi_device <scsi_device>`\  to get flags for
    :type sdev: struct scsi_device \*

    :param vendor:
        vendor name
    :type vendor: const unsigned char \*

    :param model:
        model name
    :type model: const unsigned char \*

    :param key:
        list to look up
    :type key: enum scsi_devinfo_key

.. _`scsi_get_device_flags_keyed.description`:

Description
-----------

    Search the scsi_dev_info_list specified by \ ``key``\  for an entry
    matching \ ``vendor``\  and \ ``model``\ , if found, return the matching
    flags value, else return the host or global default settings.
    Called during scan time.

.. _`scsi_exit_devinfo`:

scsi_exit_devinfo
=================

.. c:function:: void scsi_exit_devinfo( void)

    remove /proc/scsi/device_info & the scsi_dev_info_list

    :param void:
        no arguments
    :type void: 

.. _`scsi_dev_info_add_list`:

scsi_dev_info_add_list
======================

.. c:function:: int scsi_dev_info_add_list(enum scsi_devinfo_key key, const char *name)

    add a new devinfo list

    :param key:
        key of the list to add
    :type key: enum scsi_devinfo_key

    :param name:
        Name of the list to add (for /proc/scsi/device_info)
    :type name: const char \*

.. _`scsi_dev_info_add_list.description`:

Description
-----------

Adds the requested list, returns zero on success, -EEXIST if the
key is already registered to a list, or other error on failure.

.. _`scsi_dev_info_remove_list`:

scsi_dev_info_remove_list
=========================

.. c:function:: int scsi_dev_info_remove_list(enum scsi_devinfo_key key)

    destroy an added devinfo list

    :param key:
        key of the list to destroy
    :type key: enum scsi_devinfo_key

.. _`scsi_dev_info_remove_list.description`:

Description
-----------

Iterates over the entire list first, freeing all the values, then
frees the list itself.  Returns 0 on success or -EINVAL if the key
can't be found.

.. _`scsi_init_devinfo`:

scsi_init_devinfo
=================

.. c:function:: int scsi_init_devinfo( void)

    set up the dynamic device list.

    :param void:
        no arguments
    :type void: 

.. _`scsi_init_devinfo.description`:

Description
-----------

     Add command line entries from scsi_dev_flags, then add
     scsi_static_device_list entries to the scsi device info list.

.. This file was automatic generated / don't edit.

