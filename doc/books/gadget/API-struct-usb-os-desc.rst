
.. _API-struct-usb-os-desc:

==================
struct usb_os_desc
==================

*man struct usb_os_desc(9)*

*4.6.0-rc1*

describes OS descriptors associated with one interface


Synopsis
========

.. code-block:: c

    struct usb_os_desc {
      char * ext_compat_id;
      struct list_head ext_prop;
      int ext_prop_len;
      int ext_prop_count;
      struct mutex * opts_mutex;
      struct config_group group;
      struct module * owner;
    };


Members
=======

ext_compat_id
    16 bytes of “Compatible ID” and “Subcompatible ID”

ext_prop
    Extended Properties list

ext_prop_len
    Total length of Extended Properties blobs

ext_prop_count
    Number of Extended Properties

opts_mutex
    Optional mutex protecting config data of a usb_function_instance

group
    Represents OS descriptors associated with an interface in configfs

owner
    Module associated with this OS descriptor
